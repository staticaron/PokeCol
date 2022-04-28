from discord.ext import pages
from discord import Embed

from config import NORMAL_COLOR
from views.paginators import GeneralPaginator

async def get_paginator_from_list(values:list, max_count_per_page:int=15, heading:str=None) -> pages.Paginator:

    curr_count = 0

    embed_pages = []

    curr_page = Embed(title="{} Page 1".format("" if heading is None else heading + " -"), color=NORMAL_COLOR, description="")

    for i in range(len(values)):
        curr_count = curr_count + 1

        if curr_count%max_count_per_page == 0:
            embed_pages.append(curr_page)
            curr_page = Embed(title="{} Page {}".format("" if heading is None else heading + " -", len(embed_pages) + 1), color=NORMAL_COLOR, description="")
        elif curr_count >= len(values):
            embed_pages.append(curr_page)

        curr_page.description += f"{curr_count}. {values[i].capitalize()}\n"

    return GeneralPaginator(embed_pages)
