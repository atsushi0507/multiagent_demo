import openai

def generate_itinerary(
        sightseeing_plan,
        meal_recommendations,
        hotel_recommendations,
        api_key
):
    prompt = f"""
    あなたは旅行プランナーです。以下の情報をもとに、旅行者がワクワクするような1日の旅のしおりを作成してください。
    【観光プラン】:
    {sightseeing_plan}

    【飲食店の提案】:
    {meal_recommendations}

    【宿泊の提案】
    {hotel_recommendations}

    💡 期待する出力：
    - 観光、食事、宿泊を **時間順** に並べる
    - ただのリストではなく、**旅行のストーリー** として表現
    - 旅行者が「楽しみ！」と思えるような **魅力的な文体**
    - 「○○を訪れた後、△△でランチ。その後は…」のように **自然な流れ** にする

    では、素晴らしい旅行のしおりを作ってください！
    """
    
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            n=1,
            stop=None
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"エラーが発生しました: {e}"
