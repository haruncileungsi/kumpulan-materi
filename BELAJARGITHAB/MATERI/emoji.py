def convert_moot(list_mood):
    mood_map = {
        "senang": "🤣",
        "biasa": "😒",
        "sedih": "😭",
        "semanggat": "😁"
    }

    return list(map(lambda m: mood_map.get(m, "🤷‍♂️"), list_mood))