import re
import requests
from config.settings import GMAP_API_KEY

def extract_meals(plan_text):
    meal_pattern = re.findall(
        r"<meal>\s*<time>(.*?)</time>\s*<type>(.*?)</type>\s*<location>(.*?)</location>\s*</meal>", 
        plan_text, 
        re.DOTALL
    )
    meals = [{"time": m[0], "type": m[1], "location": m[2]} for m in meal_pattern]
    return meals

def search_restaurants(location):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{location}&language=ja&key={GMAP_API_KEY}"
    response = requests.get(url)
    data = response.json()

    results = data.get("results", [])
    restaurants = []
    for r in results[:3]:
        restaurants.append({
            "name": r["name"],
            "rating": r.get("rating", "N/A"),
            "address": r["formatted_address"]
        })
    return restaurants

def generate_meal_recommendations(plan_text):
    meal_data = extract_meals(plan_text)
    recommendations = []
    for meal in meal_data:
        location = meal["location"]
        restaurants = search_restaurants(location)

        recommendation_text = f"【{meal['type']}の提案】（{location}）\n"
        for i, r in enumerate(restaurants, 1):
            recommendation_text += f"{i}. {r['name']}（評価: {r['rating']}）\n   {r['address']}\n"
        
        recommendations.append(recommendation_text)

    return "\n".join(recommendations)
