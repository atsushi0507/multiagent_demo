from openai import OpenAI
from signtseeing_prompt import daytrip_sightseeing_prompt, multiday_sightseeing_prompt

def sightseeing_agent(departure, destination, budget, trip_dates, stay, api_key):
    if stay:
        prompt = multiday_sightseeing_prompt(
            departure,
            destination,
            budget,
            trip_dates
        )
    else:
        prompt = daytrip_sightseeing_prompt(
            departure,
            destination,
            budget,
            trip_dates
        )
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            n=1,
            stop=None,
            temperature=0.1
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"エラーが発生しました: {e}"
