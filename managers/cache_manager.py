import json

cached_type_data = {}

async def cache_data() -> str:
    try:
        global cached_type_data

        cached_type_data = get_type_data()

        return "Data Cached"
    except:
        return "Data not cached"

def get_type_data() -> dict:

    with open("data/type_data.json", "r") as f_out:
        data = json.loads(f_out.read())

    return data
