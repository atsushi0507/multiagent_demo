import re
import requests
from config.settings import GMAP_API_KEY

def search_hotels(destination):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=hotels+in+{destination}&language=ja&key={GMAP_API_KEY}"
    response = requests.get(url)
    data = response.json()

    results = data.get("results", [])
    hotels = []
    for r in results[:3]:
        hotels.append({
            "name": r["name"],
            "rating": r.get("rating", "N/A"),
            "address": r["formatted_address"]
        })
    return hotels

def generate_hotel_recommendations(destination):
    hotels = search_hotels(destination)

    recommendations = []
    recommendation_text = f"【ホテルの提案】（{destination}）\n"
    for i, r in enumerate(hotels, 1):
        recommendation_text += f"{i}. {r['name']}（評価: {r['rating']}）\n   {r['address']} \n"
    recommendations.append(recommendation_text)

    return "".join(recommendations)
