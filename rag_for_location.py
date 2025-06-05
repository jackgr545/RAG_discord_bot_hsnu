from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import json

# 初始化模型(非中文特化)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# 資料庫建立（第一次建好後可以儲存起來）
documents = []
with open("location.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for zone in data["zones"]:
    if zone["type"] == "building" :
        zone_info =f"{zone['name']}是一棟建築"
        documents.append(zone_info)
    else :
        zone_info =f"{zone['name']}是一塊開放空間"
        documents.append(zone_info)
    if "description" in  zone :
        documents.append(zone['description'])
    if "department" in zone :
        for floor, rooms in zone["department"].items():
            room_info = f"{zone['name']} 的 {floor} 包含：" + "、".join(rooms)
            documents.append(room_info)

# 向量化每一段知識
doc_embeddings = embed_model.encode(documents)

# 建立索引（用 FAISS）
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))


def retrieve_top_k(query, k=3):
    """回傳與query最相關的K段文件"""
    query_vec = embed_model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    return [documents[i] for i in indices[0]]


def build_prompt_location(query):
    context = retrieve_top_k(query)
    prompt = "\n3.來自本地資料庫的資料:\n\n"
    for i, para in enumerate(context):
        prompt += f"段落{i+1}：{para}\n"
    
    return prompt
