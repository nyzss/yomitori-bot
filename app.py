from discord.ext import commands
import discord
import requests
# from discord.ext.commands.core import command

client = commands.Bot(command_prefix= "?")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="?manga to search for a manga!"))
    print('yomitori is ready!')

@client.command()
async def manga(ctx, title: str, limit=None):
    if limit is None:
        limit = 7

    elif not limit.isdigit():
        title = f'{title} {limit}'
        limit = 7

    # elif type(limit) is str:

        
    mangaSearch = requests.get(f'https://api.mangadex.org/manga?title={title}&limit={limit}')
    
    mangaSearch = mangaSearch.json()

    manga_title = []

    manga_data = discord.Embed(
        title=f'Search list for {title}',
        description=f"This bot is using the Mangadex API",
        color=0xC538B5
    )

    manga_data.set_footer(text="Made by nyzs")

    manga_link = 'https://yomitori.vercel.app/manga/'


    for x in mangaSearch['results']:
        manga_title = x['data']['attributes']['title']['en']
        manga_id = x['data']['id']
        manga_data.add_field(name="---------", value=f"[{manga_title}]({manga_link}{manga_id})", inline=False)

    await ctx.send(embed=manga_data)

client.run('ODQzODQyMDM1MTc2OTY0MDk2.YKJvIw.RbDn6QOul7OdjlWJcVGD_dXKs5M')