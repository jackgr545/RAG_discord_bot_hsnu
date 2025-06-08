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
from shapely.geometry import Point, Polygon
import math
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

def get_map_url(origin_latlng, dest_latlng, polyline):
    
    
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



def get_direction(dx, dy):
    if abs(dx) > abs(dy):
        return "東" if dx > 0 else "西"
    else:
        return "北" if dy > 0 else "南"

def distance_m(lat1, lng1, lat2, lng2):
    # 粗略距離估算（經度緯度差約 111000 公尺）
    dx = (lng2 - lng1) * 111000 * math.cos(math.radians((lat1 + lat2) / 2))
    dy = (lat2 - lat1) * 111000
    return math.hypot(dx, dy), dx, dy

def find_relative_position(lat_lng):
    point = Point(lat_lng[0], lat_lng[1])  # (lat, lng)

    # 1. 先檢查是否落在區域內
    for zone in CAMPUS_ZONES:
        polygon = Polygon(zone['polygon'])
        if polygon.contains(point):
            return f"您位於「{zone['name']}」區域內"

    # 2. 不在任何區域內，找最近的建築與方向
    nearest = None
    min_dist = float('inf')
    for zone in CAMPUS_ZONES:
        points = [(lng, lat) for lat, lng in zone['polygon']]
        poly = Polygon(points)
        centroid = poly.centroid
        dist, dx, dy = distance_m(lat_lng[0], lat_lng[1], centroid.y, centroid.x)
        #print(f"{dist},{lat_lng[0]},{lat_lng[1]},{centroid.y},{centroid.x}")
        if dist < min_dist:
            min_dist = dist
            direction = get_direction(dx, dy)
            nearest = (zone['name'], direction, round(dist))

    if nearest:
        return f"距離您最近的建築是「{nearest[0]}」，位於您{nearest[1]}方，距離約 {nearest[2]} 公尺"
    else:
        return "無法判斷位置"

"""
end_location = (25.03426314329715, 121.54021701155123)
print(find_relative_position(end_location))
"""
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
        #print(directions)
        """directions example
        [
            {
                "bounds": {  // 整體路線的邊界座標（可用來設定地圖顯示範圍）
                "northeast": { "lat": 25.0359658, "lng": 121.5413522 },
                "southwest": { "lat": 25.034209, "lng": 121.5400334 }
                },
                "copyrights": "Powered by Google, ©2025 Google",

                "legs": [  // 路線分段（通常只有一段，除非有經過點）
                {
                    "distance": { "text": "0.3 km", "value": 318 }, // 總距離
                    "duration": { "text": "4 mins", "value": 258 }, // 預估時間（秒）
                    "start_address": "師大附中東樓",  // 起點地址
                    "end_address": "信義路三段111巷143號",  // 終點地址

                    "start_location": { "lat": 25.034209, "lng": 121.5413522 },  // 起點經緯度
                    "end_location": { "lat": 25.0359658, "lng": 121.5400334 },    // 終點經緯度

                    "steps": [  // 逐步導引指令，每一段步行路線
                    {
                        "distance": { "text": "0.2 km", "value": 230 },   // 本步驟距離
                        "duration": { "text": "3 mins", "value": 184 },   // 本步驟耗時
                        "start_location": { "lat": 25.034209, "lng": 121.5413522 },
                        "end_location": { "lat": 25.0353246, "lng": 121.5402866 },
                        "html_instructions": "Head <b>north</b> toward <b>操場</b>", // 導引提示（含 HTML）
                        "polyline": {
                        "points": "ynxwCmpydViBAmBBADApB?PAv@?N"  // 壓縮的座標編碼（可解碼畫線）
                        },
                        "travel_mode": "WALKING"
                    },
                    {
                        "distance": { "text": "88 m", "value": 88 },
                        "duration": { "text": "1 min", "value": 74 },
                        "start_location": { "lat": 25.0353246, "lng": 121.5402866 },
                        "end_location": { "lat": 25.0359658, "lng": 121.5400334 },
                        "html_instructions": "Turn <b>right</b><div style=\"font-size:0.9em\">Destination will be on the left</div>",
                        "maneuver": "turn-right",  // 動作提示（右轉）
                        "polyline": {
                        "points": "wuxwCyiydVOAi@AA@A??BAD?H?FAFCFCBC@C@C?C?g@@"  // 壓縮路徑
                        },
                        "travel_mode": "WALKING"
                    }
                    ],

                    "traffic_speed_entry": [],   // 交通速度資料（步行時通常空）
                    "via_waypoint": []           // 經過點（無設置時為空）
                }
                ],

                "overview_polyline": {
                "points": "ynxwCmpydVwE@CvBAhA?NOAk@?ABC^GJGBo@@"  // 全路線的壓縮多段路線
                },

                "summary": "",  // 總結文字（步行可能沒有）
                "warnings": [
                "Walking directions are in beta. Use caution – This route may be missing sidewalks or pedestrian paths."
                ],

                "waypoint_order": []  // 經過點順序（若有）
            }
        ]
        """
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
            end_location =step['end_location']['lat'],step['end_location']['lng']
            # 生成更自然的描述
            segment = {
                'step_number': i + 1,
                'total_steps': len(steps),
                'distance': distance,
                'duration': duration,
                'direction': direction,
                'raw_instruction': text,
                'html': html,
                'end_location' : end_location
            }
            
            route_segments.append(segment)

        origin_loc = directions[0]['legs'][0]['start_location']
        dest_loc = directions[0]['legs'][0]['end_location']
        polyline = directions[0]['overview_polyline']['points']

        share_url = get_map_url(
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

def generate_natural_guide(route_info, destination_name,user_input):
    """
    生成更自然、像人類導覽員的語音導覽
    """
    segments = route_info['segments']
    total_duration = route_info['total_duration']
    total_distance = route_info['total_distance']
    indoor_info=get_indoor_info(destination_name)
    # 建立詳細的路線描述
    detailed_route = []
    
    for segment in segments:
        step_num = segment['step_number']
        total_steps = segment['total_steps']
        distance = segment['distance']
        duration = segment['duration']
        direction = segment['direction']
        end_location =segment['end_location']
        
        # 構建這一段的描述
        step_desc = f"第{step_num}段：走{distance}公尺（約{duration}）,到達終點時,,{end_location},{find_relative_position(end_location)}"
        
        
            
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
    
    prompt = f"""

目的地：{destination_name}
總行程：{total_distance}，預計需要{total_duration}

詳細路線資訊：
{route_details}

室內資訊:
{indoor_info}
使用者想去:
{user_input}
範例生成:**Step 1** :走多少公尺，時長多少分鐘，最後會到達校園中的哪裡...**Step 2**...到達目的地後請上幾樓
請根據上述資料生成完整的路線指引內容："""

    try:
        response = model.generate_content(prompt)
        #print(f"{route_details}")
        return response.text
    except Exception as e:
        return f"導覽生成失敗: {str(e)}"

def get_guide(origin_lat, origin_lng, destination_name,t):
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
    print(f"\n--------------------------以下為第{t+1}輪對話--------------------------\n使用者輸入:從{origin_coords}到{destination_name}\n")
    user_input =destination_name
    destination_name=clarify_destinations(destination_name).strip()#清理多餘/n
    print(f"AI翻譯的結果:從{origin_coords}到{destination_name}\n")
    # 獲取路線
    route_result, error = get_route(origin_coords, destination_name)
    if error:
        return f"❌ {error}"
    
    route_info, entry_info = route_result
    
    # 生成自然的導覽
    guide = generate_natural_guide(route_info, destination_name,user_input)
    
    # 組合最終結果
    result_text = f"""
    📍 導航至「{destination_name}」（{entry_info}）
    ⏱️ 預計時間：{route_info['total_distance']}，約{route_info['total_duration']}

    ⭐ 詳細導覽：
    \t{guide}

    🗺️ 地圖連結：\n{route_info['share_url']}
"""
    print(f"AI 生成的導航:{result_text}")
    return result_text

def list_available_destinations():
    """列出所有可用的目的地"""
    destinations = ""
    locations =[]
    for zone in CAMPUS_ZONES:
        name = zone.get("name", "")
        nickname = zone.get("nickname", "")
        zone_type = zone.get("type", "")
        department = zone.get("department", {})
        description = zone.get("description", "")
        locations.append(name)
        # 名稱 + 暱稱
        if nickname:
            destinations += f"地點--{name}（{nickname}）:\n"
        else:
            destinations += f"地點--{name}:\n"

        # 類型與描述
        if zone_type == "building":
            destinations += f"\t{name}是一棟建築，地點特色：{description}\n"
        else:
            destinations += f"\t{name}是一個開放空間，地點特色：{description}\n"

        # 加入樓層資訊（若有）
        if isinstance(department, dict) and department:
            destinations += "\t樓層分佈如下：\n"
            for floor, rooms in department.items():
                room_list = "、".join(rooms)
                destinations += f"\t\t．{floor}：{room_list}\n"

    destinations += "\n"  # 每個地點之間空一行
    
    return destinations,locations

def clarify_destinations(user_input):
    locatation_info,locatations=list_available_destinations()
    prompt = f"""以下為你可以參考的資料:\n{locatation_info}。\n
    請根據使用者的描述:{user_input}，從{locatations}中挑選一個地點，只能挑選一個，只需要回復地點的名字，不准回復多餘的解釋，更不要輸出空格或是跳脫字元。"""
    #print(f"輸入:\n{prompt}")
    response = model.generate_content(prompt)
    response_text = response.candidates[0].content.parts[0].text
    #print(f"{response_text}")
    return response_text

#clarify_destinations("我要上音樂課")
    
def get_indoor_info(location_name):
    indoor_info = ""
    for zone in CAMPUS_ZONES:
        name = zone.get("name", "")
        if name == location_name :
            department = zone.get("department", {})
            if isinstance(department, dict) and department:
                indoor_info+= f"{location_name}的樓層分佈如下：\n"
                for floor, rooms in department.items():
                    room_list = "、".join(rooms)
                    indoor_info += f"\t．{floor}：{room_list}\n"
            break
    return indoor_info or f"{location_name}是開放空間"
#測試
#print(f"{get_indoor_info('至善樓')}")
"""
# 測試範例：從某個經緯度到游泳池
result = get_guide(25.034211880335942, 121.5410756183926, "游泳池")
print("範例導覽結果：")
print(result)
#print(str(list_available_destinations()))"""