def daytrip_sightseeing_prompt(departure, destination, budget, trip_dates):
    prompt = f"""
    あなたは優秀な旅行プランナーです。
    次の条件で観光プランを提案してください。

    [条件]
    - 出発地: {departure}
    - 目的地: {destination}
    - 予算: {budget}円
    - 日程: {trip_dates[0]} から {trip_dates[1]} まで

    [提案ルール]
    1. 出発地から目的地までの往復移動時間は現実的な移動時間にしてください。
    2. 目的地では観光スポットと食事の時間を含めたプランを作成。
    3. 食事場所は具体的には提案せず、食事エージェントに任せるため「昼食」「夕食」などのラベルだけ表示。
    4. 食事前後の観光スポットは、周辺に複数の飲食店があるエリアを選定。
    5. 以下のフォーマット例に従って提案してください。

    [提案フォーマット例]
    08:00-09:00 出発 ({departure} → {destination})
    10:00-11:30 観光スポットA (有名な寺院、周囲にカフェ多数)
    <meal>
        <time>11:45~13:00</time>
        <type>昼食</type>
        <location>観光スポットA 周辺</location>
    </meal>
    13:15-15:00 観光スポットB (美術館)
    16:00-17:00 帰路 ({destination} → {departure})

    [注意点]
    - 提案には現実的な移動時間を考慮。
    - 観光スポットの説明を短く添える。
    """
    return prompt

def multiday_sightseeing_prompt(departure, destination, budget, trip_dates):
    prompt = f"""
    あなたは優秀な旅行プランナーです。
    次の条件で観光プランを提案してください。

    [条件]
    - 出発地: {departure}
    - 目的地: {destination}
    - 予算: {budget}円
    - 日程: {trip_dates[0]} から {trip_dates[1]} まで

    [提案ルール]
    1. 出発地から目的地までの往復移動時間は現実的な移動時間にしてください。
    2. 目的地では観光スポットと食事の時間を含めたプランを作成。
    3. 食事場所は具体的には提案せず、食事エージェントに任せるため「昼食」「夕食」などのラベルだけ表示。
    4. 食事前後の観光スポットは、周辺に複数の飲食店があるエリアを選定。
    5. 以下のフォーマット例に従って提案してください。

    [提案フォーマット(1泊2日の場合)例]
    1日目
    08:00-09:00 出発 ({departure} → {destination})
    10:00-11:30 観光スポットA (有名な寺院、周囲にカフェ多数)
    <meal>
        <time>11:45-13:00</time>
        <type>昼食</type>
        <location>観光スポットA 周辺</location>
    </meal>
    13:15-15:00 観光スポットB (美術館)
    15:30-16:30 アクティビティA (陶芸体験)
    17:00-18:00 宿泊先にチェックイン
    <meal>
        <time>19:00-21:00</time>
        <type>夕食</type>
        <location>宿泊先周辺</location>
    </meal>
    2日目
    -10:00 チェックアウト
    10:15-11:30 観光スポットC (有名な神社)
    <meal>
        <time>11:45-13:00</time>
        <type>昼食</type>
        <location>観光スポットA 周辺</location>
    </meal>
    13:00-15:00 アクティビティB (バンジージャンプ)
    15:30-16:00 コーヒーブレーク (人気なカフェ)
    16:10-17:00 観光スポットD (お土産が買える)
    帰路 ({destination} → {departure})

    [注意点]
    - 提案には現実的な移動時間を考慮。
    - 観光スポットの説明を短く添える。
    """
    return prompt
