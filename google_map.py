"""
import os
import googlemaps
import google.generativeai as genai
import requests
import urllib.parse
from dotenv import load_dotenv
load_dotenv()

# 讀取金鑰
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API")
GEMINI_API_KEY = os.getenv("GEMINI_API")

# 初始化 Google Maps
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# 初始化 Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def get_static_map_url(origin_latlng, dest_latlng, polyline):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    
    params = {
        "size": "640x400",
        "maptype": "roadmap",
        "markers": [
            f"color:red|label:S|{origin_latlng[0]},{origin_latlng[1]}",
            f"color:blue|label:E|{dest_latlng[0]},{dest_latlng[1]}"
        ],
        "path": f"enc:{polyline}",
        "key": os.getenv("GOOGLE_MAPS_API")
    }

    # 把 markers 轉成多個參數格式
    marker_params = "&".join([f"markers={urllib.parse.quote(m)}" for m in params["markers"]])

    # 組合整個 URL
    url = f"{base_url}size={params['size']}&maptype={params['maptype']}&{marker_params}&path={params['path']}&key={params['key']}"
    return url

# 步驟一：取得步行路線

def get_nearby_landmark(lat, lng):
    api_key = os.getenv("GOOGLE_MAPS_API")  # 讀取你的 API 金鑰
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    params = {
        "location": f"{lat},{lng}",
        "radius": 20,
        "key": api_key,
        "type": "point_of_interest"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or not data["results"]:
        return None
    
    name = data["results"][0]["name"]
    if len(name) > 25 or "Unnamed" in name:
        return None
    return name

def get_route(origin, destination):
    directions = gmaps.directions(origin, destination, mode="walking")
    if not directions:
        return None
    print(f"google map提供的資料:{directions}\n")

    steps = directions[0]['legs'][0]['steps']
    route_text = []

    for step in steps:
        html = step['html_instructions']
        text = html.replace("<b>", "").replace("</b>", "").replace("<div style=\"font-size:0.9em\">", " ").replace("</div>", "")
        distance = step['distance']['value']
        direction = step.get("maneuver", "")

        # 根據方向和距離建立說法
        if direction == "turn-right":
            sentence = f"接著往前走大約 {distance} 公尺，看到路口右轉。"
        elif direction == "turn-left":
            sentence = f"然後走大概 {distance} 公尺後左轉，快到囉！"
        elif direction == "turn-slight-left":
            sentence = f"稍微往左前方走約 {distance} 公尺。"
        elif direction == "turn-slight-right":
            sentence = f"稍微往右前方走約 {distance} 公尺。"
        else:
            sentence = f"{text}，大約走 {distance} 公尺。"

        # 檢查是否是最後一段，並有目的地提示
        if "Destination will be on the left" in html:
            sentence += " 你的目的地會出現在左手邊喔！"
        elif "Destination will be on the right" in html:
            sentence += " 你的目的地會在右手邊，注意看！"

        # 加入 landmark 地標提示
        lat = step['start_location']['lat']
        lng = step['start_location']['lng']
        landmark = get_nearby_landmark(lat, lng)
        if landmark:
            sentence += f" 你會經過「{landmark}」，可以注意一下喔～"

        route_text.append(sentence)
    origin = directions[0]['legs'][0]['start_location']
    dest = directions[0]['legs'][0]['end_location']
    polyline = directions[0]['overview_polyline']['points']
    
    static_map_url = get_static_map_url((origin['lat'], origin['lng']), (dest['lat'], dest['lng']), polyline)
    
    return "\n".join(route_text), static_map_url
    

# 步驟二：用 Gemini 生成導覽語句
def generate_guide(route_text, destination_name):
    prompt = f你是一位親切的校園導覽員。
根據下列步行路線，請為使用者生成一段清楚易懂的中文語音導覽，目的地是「{destination_name}」。

請讓說明有點口語化，像在實際講解路線，不需要重複原本文字內容。

步行路線如下：
{route_text}
    print(f"清理過後:{route_text}\n")
    response = model.generate_content(prompt)
    return response.text

# 主程式：對外提供功能
def get_guide(origin, destination):
    route_data = get_route(origin, destination)
    if not route_data:
        return "❌ 找不到路線，請確認地點拼寫或座標是否正確。"
    
    route_text, map_url = route_data
    guide = generate_guide(route_text, destination)
    
    return f"{guide}\n\n  導覽地圖：{map_url}"

def get_lat_and_lon(adress):
    lat_and_lon =gmaps.geocode(adress)
    if not lat_and_lon :
        return "錯誤"
    return lat_and_lon

result =get_guide("附中體育館","附中西樓")
print(f"{result}")

import os
import json
import googlemaps
import google.generativeai as genai
import requests
import urllib.parse
from dotenv import load_dotenv
load_dotenv()

# 讀取金鑰
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API")
GEMINI_API_KEY = os.getenv("GEMINI_API")

# 初始化 Google Maps
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# 初始化 Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# 載入建築區域資料
with open("location.json", "r", encoding="utf-8") as f:
    CAMPUS_ZONES = json.load(f)["zones"]

def get_static_map_url(origin_latlng, dest_latlng, polyline):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"

    params = {
        "size": "640x400",
        "maptype": "roadmap",
        "markers": [
            f"color:red|label:S|{origin_latlng[0]},{origin_latlng[1]}",
            f"color:blue|label:E|{dest_latlng[0]},{dest_latlng[1]}"
        ],
        "path": f"enc:{polyline}",
        "key": GOOGLE_MAPS_API_KEY
    }

    marker_params = "&".join([f"markers={urllib.parse.quote(m)}" for m in params["markers"]])
    url = f"{base_url}size={params['size']}&maptype={params['maptype']}&{marker_params}&path={params['path']}&key={params['key']}"
    return url

def get_nearby_landmark(lat, lng):
    api_key = GOOGLE_MAPS_API_KEY
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lng}",
        "radius": 20,
        "key": api_key,
        "type": "point_of_interest"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    name = data["results"][0]["name"]
    if len(name) > 25 or "Unnamed" in name:
        return None
    return name

def match_building_by_name(name):
    for zone in CAMPUS_ZONES:
        if zone.get("name") == name or zone.get("nickname") == name:
            entries = zone.get("entry")
            if entries:
                return entries[0]  # 回傳第一個入口座標
    return None

def get_route(origin_name, destination_name):
    origin = match_building_by_name(origin_name)
    destination = match_building_by_name(destination_name)
    if not origin or not destination:
        return None

    directions = gmaps.directions(origin, destination, mode="walking")
    if not directions:
        return None

    print(f"google map提供的資料:{directions}\n")
    steps = directions[0]['legs'][0]['steps']
    route_text = []

    for step in steps:
        html = step['html_instructions']
        text = html.replace("<b>", "").replace("</b>", "").replace("<div style=\"font-size:0.9em\">", " ").replace("</div>", "")
        distance = step['distance']['value']
        direction = step.get("maneuver", "")

        if direction == "turn-right":
            sentence = f"接著往前走大約 {distance} 公尺，看到路口右轉。"
        elif direction == "turn-left":
            sentence = f"然後走大概 {distance} 公尺後左轉，快到囉！"
        elif direction == "turn-slight-left":
            sentence = f"稍微往左前方走約 {distance} 公尺。"
        elif direction == "turn-slight-right":
            sentence = f"稍微往右前方走約 {distance} 公尺。"
        else:
            sentence = f"{text}，大約走 {distance} 公尺。"

        if "Destination will be on the left" in html:
            sentence += " 你的目的地會出現在左手邊喔！"
        elif "Destination will be on the right" in html:
            sentence += " 你的目的地會在右手邊，注意看！"

        lat = step['start_location']['lat']
        lng = step['start_location']['lng']
        landmark = get_nearby_landmark(lat, lng)
        if landmark:
            sentence += f" 你會經過「{landmark}」，可以注意一下喔～"

        route_text.append(sentence)

    origin_loc = directions[0]['legs'][0]['start_location']
    dest_loc = directions[0]['legs'][0]['end_location']
    polyline = directions[0]['overview_polyline']['points']

    static_map_url = get_static_map_url((origin_loc['lat'], origin_loc['lng']), (dest_loc['lat'], dest_loc['lng']), polyline)

    return "\n".join(route_text), static_map_url

def generate_guide(route_text, destination_name):
    prompt = f你是一位親切的校園導覽員。
根據下列步行路線，請為使用者生成一段清楚易懂的中文語音導覽，目的地是「{destination_name}」。

請讓說明有點口語化，像在實際講解路線，不需要重複原本文字內容。

步行路線如下：
{route_text}

    print(f"清理過後:{route_text}\n")
    response = model.generate_content(prompt)
    return response.text

def get_guide(origin_name, destination_name):
    route_data = get_route(origin_name, destination_name)
    if not route_data:
        return "❌ 找不到路線，請確認地點名稱是否正確，或該地點是否有標記入口。"

    route_text, map_url = route_data
    guide = generate_guide(route_text, destination_name)
    return f"{guide}\n\n🗺️ 導覽地圖：{map_url}"


result = get_guide("附中游泳池", "附中技藝館")
print(result)

import os
import json
import googlemaps
import google.generativeai as genai
import requests
import urllib.parse
from dotenv import load_dotenv
load_dotenv()

# 讀取金鑰
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API")
GEMINI_API_KEY = os.getenv("GEMINI_API")

# 初始化 Google Maps
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# 初始化 Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# 載入建築區域資料
with open("location.json", "r", encoding="utf-8") as f:
    CAMPUS_ZONES = json.load(f)["zones"]

def get_static_map_url(origin_latlng, dest_latlng, polyline):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"

    params = {
        "size": "640x400",
        "maptype": "roadmap",
        "markers": [
            f"color:red|label:S|{origin_latlng[0]},{origin_latlng[1]}",
            f"color:blue|label:E|{dest_latlng[0]},{dest_latlng[1]}"
        ],
        "path": f"enc:{polyline}",
        "key": GOOGLE_MAPS_API_KEY
    }

    marker_params = "&".join([f"markers={urllib.parse.quote(m)}" for m in params["markers"]])
    url = f"{base_url}size={params['size']}&maptype={params['maptype']}&{marker_params}&path={params['path']}&key={params['key']}"
    return url

def get_nearby_landmark(lat, lng):
    api_key = GOOGLE_MAPS_API_KEY
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lng}",
        "radius": 20,
        "key": api_key,
        "type": "point_of_interest"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    name = data["results"][0]["name"]
    if len(name) > 25 or "Unnamed" in name:
        return None
    return name

def calculate_distance(lat1, lng1, lat2, lng2):
    
    計算兩點間的直線距離（使用簡化的歐幾里得距離）
    對於小範圍內的距離比較已經足夠精確
    
    import math
    
    # 將經緯度轉換為弧度
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)
    
    # 使用 Haversine 公式計算距離
    dlat = lat2_rad - lat1_rad
    dlng = lng2_rad - lng1_rad
    
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlng/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # 地球半徑（公里）
    r = 6371
    
    return c * r * 1000  # 轉換為公尺

def find_destination_location(destination_name, origin_coords):
    
    根據目的地名稱和起點座標查找最適合的目的地座標
    如果有多個 entry，選擇距離起點最近的入口
    如果沒有 entry（戶外空間），返回多邊形的中心點
   
    for zone in CAMPUS_ZONES:
        if zone.get("name") == destination_name or zone.get("nickname") == destination_name:
            # 如果有入口座標，選擇距離最近的入口
            if zone.get("entry") and len(zone["entry"]) > 0:
                entries = zone["entry"]
                
                if len(entries) == 1:
                    return entries[0], "入口"
                
                # 計算每個入口到起點的距離
                distances = []
                for entry in entries:
                    distance = calculate_distance(
                        origin_coords[0], origin_coords[1],
                        entry[0], entry[1]
                    )
                    distances.append((distance, entry))
                
                # 選擇距離最近的入口
                closest_entry = min(distances, key=lambda x: x[0])[1]
                return closest_entry, f"最近入口（共{len(entries)}個入口）"
            
            # 如果沒有入口（戶外空間），計算多邊形中心點
            elif zone.get("polygon"):
                polygon = zone["polygon"]
                # 計算多邊形中心點（簡單平均）
                lat_sum = sum(point[0] for point in polygon)
                lng_sum = sum(point[1] for point in polygon)
                center_lat = lat_sum / len(polygon)
                center_lng = lng_sum / len(polygon)
                return [center_lat, center_lng], "區域中心"
    
    return None, None

def validate_coordinates(lat, lng):
    驗證經緯度格式是否正確
    try:
        lat = float(lat)
        lng = float(lng)
        
        # 基本範圍檢查（台灣地區大致範圍）
        if not (22.0 <= lat <= 26.0 and 120.0 <= lng <= 122.5):
            return False, "經緯度超出台灣地區範圍"
        
        return True, (lat, lng)
    except ValueError:
        return False, "經緯度格式錯誤，請輸入數字"

def get_route(origin_coords, destination_name):
   
    獲取路線資訊
    origin_coords: (lat, lng) 起點經緯度元組
    destination_name: 目的地名稱字串
  
    # 查找目的地座標（會自動選擇最近的入口）
    destination_result = find_destination_location(destination_name, origin_coords)
    if not destination_result[0]:
        return None, f"找不到目的地「{destination_name}」"
    
    destination_coords, entry_info = destination_result

    # 轉換格式為 Google Maps API 需要的格式
    origin = f"{origin_coords[0]},{origin_coords[1]}"
    destination = f"{destination_coords[0]},{destination_coords[1]}"

    try:
        directions = gmaps.directions(origin, destination, mode="walking")
        if not directions:
            return None, "無法規劃路線"

        print(f"目的地資訊: 使用{entry_info}")
        print(f"Google Maps 提供的資料: {directions}\n")
        
        steps = directions[0]['legs'][0]['steps']
        route_text = []

        for step in steps:
            html = step['html_instructions']
            text = html.replace("<b>", "").replace("</b>", "").replace("<div style=\"font-size:0.9em\">", " ").replace("</div>", "")
            distance = step['distance']['value']
            direction = step.get("maneuver", "")

            if direction == "turn-right":
                sentence = f"接著往前走大約 {distance} 公尺，看到路口右轉。"
            elif direction == "turn-left":
                sentence = f"然後走大概 {distance} 公尺後左轉，快到囉！"
            elif direction == "turn-slight-left":
                sentence = f"稍微往左前方走約 {distance} 公尺。"
            elif direction == "turn-slight-right":
                sentence = f"稍微往右前方走約 {distance} 公尺。"
            else:
                sentence = f"{text}，大約走 {distance} 公尺。"

            if "Destination will be on the left" in html:
                sentence += " 你的目的地會出現在左手邊喔！"
            elif "Destination will be on the right" in html:
                sentence += " 你的目的地會在右手邊，注意看！"

            lat = step['start_location']['lat']
            lng = step['start_location']['lng']
            landmark = get_nearby_landmark(lat, lng)
            if landmark:
                sentence += f" 你會經過「{landmark}」，可以注意一下喔～"

            route_text.append(sentence)

        origin_loc = directions[0]['legs'][0]['start_location']
        dest_loc = directions[0]['legs'][0]['end_location']
        polyline = directions[0]['overview_polyline']['points']

        static_map_url = get_static_map_url(
            (origin_loc['lat'], origin_loc['lng']), 
            (dest_loc['lat'], dest_loc['lng']), 
            polyline
        )

        return ("\n".join(route_text), static_map_url, entry_info), None

    except Exception as e:
        return None, f"路線規劃發生錯誤: {str(e)}"

def generate_guide(route_text, destination_name):
    prompt = f你是一位親切的校園導覽員。
根據下列步行路線，請為使用者生成一段清楚易懂的中文語音導覽，目的地是「{destination_name}」。

請讓說明有點口語化，像在實際講解路線，不需要重複原本文字內容。

步行路線如下：
{route_text}

    print(f"清理過後: {route_text}\n")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"導覽生成失敗: {str(e)}"

def get_guide(origin_lat, origin_lng, destination_name):
  
    主要功能函數
    origin_lat, origin_lng: 起點經緯度
    destination_name: 目的地名稱
   
    # 驗證起點座標
    is_valid, result = validate_coordinates(origin_lat, origin_lng)
    if not is_valid:
        return f"❌ 起點座標錯誤: {result}"
    
    origin_coords = result
    
    # 獲取路線
    route_result, error = get_route(origin_coords, destination_name)
    if error:
        return f"❌ {error}"
    
    route_text, map_url, entry_info = route_result
    
    # 生成導覽
    guide = generate_guide(route_text, destination_name)
    
    return f"📍 導航至「{destination_name}」（{entry_info}）\n\n{guide}\n\n🗺️ 導覽地圖：{map_url}"


def list_available_destinations():
    destinations = []
    for zone in CAMPUS_ZONES:
        name = zone.get("name", "")
        nickname = zone.get("nickname", "")
        zone_type = zone.get("type", "")
        
        if nickname:
            destinations.append(f"{name}（{nickname}）- {zone_type}")
        else:
            destinations.append(f"{name} - {zone_type}")
    
    return destinations


result = get_guide(25.03378698051789, 121.54018077196909, "游泳池")
print("範例導覽結果：")
print(result)
"""
import os
import json
import googlemaps
import google.generativeai as genai
import requests
import urllib.parse
from dotenv import load_dotenv
from rag_for_location import build_prompt_location
load_dotenv()

# 讀取金鑰
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API")
GEMINI_API_KEY = os.getenv("GEMINI_API")

# 初始化 Google Maps
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# 初始化 Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# 載入建築區域資料
with open("location.json", "r", encoding="utf-8") as f:
    CAMPUS_ZONES = json.load(f)["zones"]

def get_static_map_url(origin_latlng, dest_latlng, polyline):
    """
    生成靜態地圖 URL，同時返回包含 API 金鑰的完整 URL 和不含金鑰的分享 URL
    """
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"

    params = {
        "size": "640x400",
        "maptype": "roadmap",
        "markers": [
            f"color:red|label:S|{origin_latlng[0]},{origin_latlng[1]}",
            f"color:blue|label:E|{dest_latlng[0]},{dest_latlng[1]}"
        ],
        "path": f"enc:{polyline}",
        "key": GOOGLE_MAPS_API_KEY
    }

    marker_params = "&".join([f"markers={urllib.parse.quote(m)}" for m in params["markers"]])
    full_url = f"{base_url}size={params['size']}&maptype={params['maptype']}&{marker_params}&path={params['path']}&key={params['key']}"
    
    # 生成 Google Maps 分享連結（不含 API 金鑰）
    share_url = f"https://www.google.com/maps/dir/{origin_latlng[0]},{origin_latlng[1]}/{dest_latlng[0]},{dest_latlng[1]}/data=!3m1!4b1!4m2!4m1!3e2"
    
    return  share_url




def calculate_distance(lat1, lng1, lat2, lng2):
    """
    計算兩點間的直線距離（使用簡化的歐幾里得距離）
    對於小範圍內的距離比較已經足夠精確
    """
    import math
    
    # 將經緯度轉換為弧度
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)
    
    # 使用 Haversine 公式計算距離
    dlat = lat2_rad - lat1_rad
    dlng = lng2_rad - lng1_rad
    
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlng/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # 地球半徑（公里）
    r = 6371
    
    return c * r * 1000  # 轉換為公尺

def find_destination_location(destination_name, origin_coords):
    """
    根據目的地名稱和起點座標查找最適合的目的地座標
    如果有多個 entry，選擇距離起點最近的入口
    如果沒有 entry（戶外空間），返回多邊形的中心點
    """
    target = destination_name.strip().lower()#防止多餘的\n或是空格影響比對
    for zone in CAMPUS_ZONES:
        name = zone.get("name", "").strip().lower()#防止多餘的\n或是空格影響比對
        nickname = zone.get("nickname", "").strip().lower()#防止多餘的\n或是空格影響比對
        if name == target or nickname == target:
            # 如果有入口座標，選擇距離最近的入口
            if zone.get("entry") and len(zone["entry"]) > 0:
                entries = zone["entry"]
                
                if len(entries) == 1:
                    return entries[0], "入口"
                
                # 計算每個入口到起點的距離
                distances = []
                for entry in entries:
                    distance = calculate_distance(
                        origin_coords[0], origin_coords[1],
                        entry[0], entry[1]
                    )
                    distances.append((distance, entry))
                
                # 選擇距離最近的入口
                closest_entry = min(distances, key=lambda x: x[0])[1]
                return closest_entry, f"最近入口（共{len(entries)}個入口）"
            
            # 如果沒有入口（戶外空間），計算多邊形中心點
            elif zone.get("polygon"):
                polygon = zone["polygon"]
                # 計算多邊形中心點（簡單平均）
                lat_sum = sum(point[0] for point in polygon)
                lng_sum = sum(point[1] for point in polygon)
                center_lat = lat_sum / len(polygon)
                center_lng = lng_sum / len(polygon)
                return [center_lat, center_lng], "區域中心"
    
    return None, None

def validate_coordinates(lat, lng):
    """驗證經緯度格式是否正確"""
    try:
        lat = float(lat)
        lng = float(lng)
        
        # 基本範圍檢查（台灣地區大致範圍）
        if not (22.0 <= lat <= 26.0 and 120.0 <= lng <= 122.5):
            return False, "經緯度超出台灣地區範圍"
        
        return True, (lat, lng)
    except ValueError:
        return False, "經緯度格式錯誤，請輸入數字"

def get_route(origin_coords, destination_name):
    """
    獲取路線資訊
    origin_coords: (lat, lng) 起點經緯度元組
    destination_name: 目的地名稱字串
    """
    # 查找目的地座標（會自動選擇最近的入口）
    destination_result = find_destination_location(destination_name, origin_coords)
    if not destination_result[0]:
        return None, f"找不到目的地「{destination_name}」"
    
    destination_coords, entry_info = destination_result

    # 轉換格式為 Google Maps API 需要的格式
    origin = f"{origin_coords[0]},{origin_coords[1]}"
    destination = f"{destination_coords[0]},{destination_coords[1]}"

    try:
        directions = gmaps.directions(origin, destination, mode="walking")
        if not directions:
            return None, "無法規劃路線"
        """"
        print(f"目的地資訊: 使用{entry_info}")
        print(f"Google Maps 提供的資料: {directions}\n")
        """
        steps = directions[0]['legs'][0]['steps']
        total_duration = directions[0]['legs'][0]['duration']['text']
        total_distance = directions[0]['legs'][0]['distance']['text']
        
        # 生成更自然的路線描述
        route_segments = []
        
        for i, step in enumerate(steps):
            html = step['html_instructions']
            text = html.replace("<b>", "").replace("</b>", "").replace("<div style=\"font-size:0.9em\">", " ").replace("</div>", "")
            distance = step['distance']['value']
            duration = step['duration']['text']
            direction = step.get("maneuver", "")
            # 生成更自然的描述
            segment = {
                'step_number': i + 1,
                'total_steps': len(steps),
                'distance': distance,
                'duration': duration,
                'direction': direction,
                'raw_instruction': text,
                'html': html
            }
            
            route_segments.append(segment)

        origin_loc = directions[0]['legs'][0]['start_location']
        dest_loc = directions[0]['legs'][0]['end_location']
        polyline = directions[0]['overview_polyline']['points']

        share_url = get_static_map_url(
            (origin_loc['lat'], origin_loc['lng']), 
            (dest_loc['lat'], dest_loc['lng']), 
            polyline
        )

        route_info = {
            'segments': route_segments,
            'total_duration': total_duration,
            'total_distance': total_distance,
            'share_url': share_url
        }

        return (route_info, entry_info), None

    except Exception as e:
        return None, f"路線規劃發生錯誤: {str(e)}"

def generate_natural_guide(route_info, destination_name):
    """
    生成更自然、像人類導覽員的語音導覽
    """
    segments = route_info['segments']
    total_duration = route_info['total_duration']
    total_distance = route_info['total_distance']
    
    # 建立詳細的路線描述
    detailed_route = []
    
    for segment in segments:
        step_num = segment['step_number']
        total_steps = segment['total_steps']
        distance = segment['distance']
        duration = segment['duration']
        direction = segment['direction']
        
        
        # 構建這一段的描述
        step_desc = f"第{step_num}段：走{distance}公尺（約{duration}）"
        
        
            
        if direction:
            if direction == "turn-right":
                step_desc += "，然後右轉"
            elif direction == "turn-left":
                step_desc += "，然後左轉"
            elif direction == "turn-slight-left":
                step_desc += "，稍微向左"
            elif direction == "turn-slight-right":
                step_desc += "，稍微向右"
        
        detailed_route.append(step_desc)
    
    route_details = "\n".join(detailed_route)
    
    prompt = f"""你是一位親切又專業的校園導覽員，正在為遊客提供真人語音導覽服務。

目的地：{destination_name}
總行程：{total_distance}，預計需要{total_duration}

詳細路線資訊：
{route_details}

請用自然、口語化的方式為遊客提供導覽解說，就像你在現場陪同他們走路一樣。要求：

1. 用第一人稱"我們"開始，營造陪伴感
2. 適時提到時間估算和經過的地標
3. 語氣要親切自然，就像朋友間的對話
4. 可以加入一些貼心提醒或有趣的觀察
5. 最後要有抵達目的地的確認

範例風格："好的，我們現在要前往{destination_name}，整個路程大約需要{total_duration}。讓我帶著你一起走..."

請生成完整的導覽內容："""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"導覽生成失敗: {str(e)}"

def get_guide(origin_lat, origin_lng, destination_name):
    """
    主要功能函數
    origin_lat, origin_lng: 起點經緯度
    destination_name: 目的地名稱
    """
    # 驗證起點座標
    is_valid, result = validate_coordinates(origin_lat, origin_lng)
    if not is_valid:
        return f"❌ 起點座標錯誤: {result}"
    
    origin_coords = result
    
    # 獲取路線
    route_result, error = get_route(origin_coords, destination_name)
    if error:
        return f"❌ {error}"
    
    route_info, entry_info = route_result
    
    # 生成自然的導覽
    guide = generate_natural_guide(route_info, destination_name)
    
    # 組合最終結果
    result_text = f"""📍 導航至「{destination_name}」（{entry_info}）
⏱️ 預計時間：{route_info['total_distance']}，約{route_info['total_duration']}

🎙️ 語音導覽：
{guide}

🗺️ 地圖連結：
📱 分享連結：{route_info['share_url']}
"""
    
    return result_text

def list_available_destinations():
    """列出所有可用的目的地"""
    destinations = ""
    for zone in CAMPUS_ZONES:
        name = zone.get("name", "")
        nickname = zone.get("nickname", "")
        type=zone.get("type", "")
        description =zone.get("description", "")
        if nickname:
            destinations+=(f"{name}({nickname}--{type}，地點特色:{description})\n")
        else:
            destinations+=(f"{name}--{type}，地點特色:{description}\n")
    
    return destinations
def clarify_destinations(user_input):
    locatation =list_available_destinations()
    locatation_info = build_prompt_location(user_input)
    prompt = f"""以下為你可以參考的資料:\n{locatation_info}，
    請根據使用者的描述:{user_input}，從中挑選一個最有可能的地點，只需要回復地點的名字，不准回復多餘的解釋，更不要輸出空格或是跳脫字元。"""
    print(f"輸入:\n{prompt}")
    response = model.generate_content(prompt)
    response_text = response.candidates[0].content.parts[0].text
    print(f"{response_text}")
    return response_text
clarify_destinations("我要上音樂課")
    
"""
# 測試範例：從某個經緯度到游泳池
result = get_guide(25.034211880335942, 121.5410756183926, "游泳池")
print("範例導覽結果：")
print(result)
print(str(list_available_destinations()))
"""