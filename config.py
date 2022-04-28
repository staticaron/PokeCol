import discord
from os import environ

TOKEN = environ["TOKEN"] # Bot token goes here

MONGO = environ["MONGO"] # MongoDB database URI
DB_NAME = environ["DB"]

USER_COL_NAME = "users"
COL_COL_NAME = "tags"

TIMER=0
PREFIX=">>"

def modify_prefix_and_timer(prefix, timer):
    global TIMER, PREFIX

    TIMER = timer
    PREFIX = prefix

OWNERS = [734754644286504991, 734754644286504991]

NORMAL_COLOR = discord.Color.dark_theme()

NEXT_EMOJI = "<:next:964507779765272648>"
PREV_EMOJI = "<:prev:964508551915634768>"
FIRST_EMOJI = "<:first:964508851166646272>"
LAST_EMOJI = "<:last:964508277809496125>"