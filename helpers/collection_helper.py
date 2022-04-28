from discord import Member
from discord.ext import pages

from managers import mongo_manager
from helpers import general_helper
from config import USER_COL_NAME, COL_COL_NAME

async def register_collection(user:Member, pokemon:str) -> str:

    pokemon = pokemon.lower()

    # Update the users collections
    query = {"user" : str(user.id)}

    cursor = mongo_manager.manager.get_all_data(USER_COL_NAME, query)

    data = cursor[0]

    """
    {
        "user" : "734754644286504991",
        "col" : [
            "scizor",
            "aron"
        ]
    }
    """

    collection = data["col"]

    if pokemon not in collection:
        collection.append(pokemon)
    else:
        return "Pokemon is already in your collection list"

    updated_data = {"col" : collection}

    mongo_manager.manager.update_all_data(USER_COL_NAME, query, updated_data)

    # Update the cols collections

    """
    {
        "col" : "pokemon",
        "users" : [
            "user_id_1",
            "user_id_2"
        ]
    }
    """

    query = {"col" : pokemon}

    cursor = mongo_manager.manager.get_all_data(COL_COL_NAME, query)

    try:
        data = cursor[0]

        users = data["users"]

        if str(user.id) not in users:
            users.append(str(user.id))
        else:
            return "You are already collecting this pokemon"

        updated_data = {"users" : users}

        mongo_manager.manager.update_all_data(COL_COL_NAME, query, updated_data)

    except:
        if mongo_manager.manager.get_documents_length(COL_COL_NAME, query) <= 0:

            entry = {
                "col" : pokemon,
                "users" : [
                    str(user.id)
                ]
            }

            mongo_manager.manager.add_data(COL_COL_NAME, entry)

    return f"**{pokemon.capitalize()}** was added to your collection"

async def get_collection(user:Member) -> pages.Paginator:

    MAX_COLLECTION_PER_PAGE = 15

    query = {"user" : str(user.id)}

    cursor = mongo_manager.manager.get_all_data(USER_COL_NAME, query)

    try:
        data = cursor[0]

        collection = data["col"]

        paginator = await general_helper.get_paginator_from_list(collection, 6, f"{user.name.capitalize()}'s Collection")

        return paginator
    except:
        if mongo_manager.manager.get_documents_length(USER_COL_NAME, query) <= 0:
            return None





