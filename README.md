# PokeCol
An easy to use, self-hosted, server specific Collection Bot for Pokémon Players on Discord.

## Commands
* `>col add <pokemon>` : Adds a pokemon in your collection list.
* `>col remove <pokemon>` : Removes a pokemon from your collection list.
* `>col show` : Displays your current collection list.
* `>cp <pokemon>` : Pings users collecting that pokemon.

## How to Run da Bot

This bot is self-hosted. This means, there is no bot that you can invite to your server. To use it in  your server, you have to host the bot on websites like Heroku, Digital Ocean, etc. 

Step 1. **Get the code.**
  Clone the repo into your local machine. Make sure you have python, git installed.
  
Step 2. **Setup a Virtual Environment.**
  Create a Virtual Environment using `python3.8 -m venv venv` command.
  
Step 3. **Install Dependencies.**
  Install the dependencies using pip. 
  `pip install -r requirements.txt`
  
Step 4. **Create a Bot Application.**
  Head over to [Discord Developer Portal](https://discord.com/developers/applications/) and create an Application for this bot. Copy the TOKEN.
  
Step 5. **Create a MongoDB database.**
  Go to [Mongodb Website](mongodb.com) to create a database and note the Database URI. This database will be used to store collection data. [Click for Guide](https://www.mongodb.com/docs/manual/tutorial/getting-started/)
  
Step 6. **Setup the environment variables.**
  Setup the following environment variables :
  * TOKEN = _Copied from **Discord Developer Portal [Step 4]**_
  * MONGO = _Copied from **Database Dashboard [Step 5]**_
  * DB = _Name of the database [Step 5]_
