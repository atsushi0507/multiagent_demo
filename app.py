import streamlit as st
from datetime import date
from sightseeing_agent import sightseeing_agent
from meal_agent import generate_meal_recommendations
from agent import app

if "plan" not in st.session_state:
    st.session_state.plan = ""
if "api_key" not in st.session_state:
    st.session_state.api_key = None

st.title("✈️LLMトラベル")

with st.sidebar:
    st.session_state.api_key = st.text_input(
        "OpenAIのAPIキー",
        value=None,
        placeholder="OpenAIのAPIキーを入力してください"
    )

departure = st.text_input("出発駅", placeholder="例: 東京駅")
destination = st.text_input("目的地", placeholder="例: 京都")
budget = st.number_input(
    "予算(¥)",
    min_value=0,
    step=1000,
)
start_date = date.today()
end_date = start_date.replace(day=start_date.day)
trip_dates = tuple(st.date_input(
    "日程",
    value=(start_date, end_date)
))
stay = True if trip_dates[0] != trip_dates[1] else False

if not isinstance(trip_dates, tuple):
    st.warning("旅行の日程を選択してください")

disable = True if st.session_state.api_key == None else False
if st.button("提案を受ける", disabled=disable):
    if not departure or not destination:
        st.warning("出発地と目的地を入力してください")
    else:
        state = {
            "departure": departure,
            "destination": destination,
            "budget": budget,
            "trip_dates": trip_dates,
            "stay": stay,
            "api_key": st.session_state.api_key
        }
        with st.spinner("プラン作成中..."):
            res = app.invoke(state)
            st.session_state.plan = res.get("itinerary_plan", "作成に失敗しました")

        st.subheader("📖旅のしおり")
        st.write(st.session_state.plan)
