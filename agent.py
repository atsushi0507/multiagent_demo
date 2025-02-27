import langgraph
from langgraph.graph import StateGraph
from typing import TypedDict
from sightseeing_agent import sightseeing_agent
from meal_agent import generate_meal_recommendations
from hotel_agent import generate_hotel_recommendations
from itinerary_agent import generate_itinerary

# 旅行のデータを管理するState
class TravelState(TypedDict):
    departure: str
    destination: str
    budget: int
    trip_dates:tuple
    stay: bool
    sightseeing_plan: str
    meal_reco: str
    hotel_reco: str
    itinerary_plan: str
    api_key: str

# 観光エージェントのノード
def sightseeing_node(state: TravelState):
    res = sightseeing_agent(
        departure=state["departure"],
        destination=state["destination"],
        budget=state["budget"],
        trip_dates=state["trip_dates"],
        stay=state["stay"],
        api_key=state["api_key"]
    )
    return {"sightseeing_plan": res}

# 食事エージェントのノード
def meal_node(state: TravelState):
    meal_reco = generate_meal_recommendations(
        plan_text=state["sightseeing_plan"]
    )
    return {"meal_reco": meal_reco}

# 宿泊エージェントのノード
def hotel_node(state: TravelState):
    hotel_reco = generate_hotel_recommendations(
        destination=state["destination"]
    )
    return {"hotel_reco": hotel_reco}

# 旅のしおりエージェントのノード
def itinerary_node(state: TravelState):
    itinerary = generate_itinerary(
        sightseeing_plan=state["sightseeing_plan"],
        meal_recommendations=state["meal_reco"],
        hotel_recommendations=state.get("hotel_reco", "宿泊なしの日帰り旅行です！"),
        api_key=state["api_key"]
    )
    return {"itinerary_plan": itinerary}

def condition_function(state: TravelState):
    return "hotel" if state["stay"] else "meal"

# LangGraph のグラフ作成
graph = StateGraph(TravelState)

# ノードの登録
graph.add_node("sightseeing", sightseeing_node)
graph.add_node("meal", meal_node)
graph.add_node("hotel", hotel_node)
graph.add_node("itinerary", itinerary_node)

graph.add_conditional_edges("sightseeing", condition_function)
# hotel -> meal (stay = True の場合)
graph.add_edge("hotel", "meal")
graph.add_edge("meal", "itinerary")

# スタート地点から観光ノードへ
graph.set_entry_point("sightseeing")
graph.set_finish_point("itinerary")

# グラフの構築
app = graph.compile()
