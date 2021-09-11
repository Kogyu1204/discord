import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print('█████ █████ █\n    █     █ █\n    █     █ █\n  █       █ █\n█████       █\n실행 완료됨!')
    game = discord.Game('!도움')
    await client.change_presence(status = discord.Status.online, activity = game)

@client.event
async def on_message(message):
    if message.content == "고기":
        await message.channel.send("고기!!")

    if message.content == "!도움":
        embed = discord.Embed(title="명령어 목록", description="고기\n ㄴ무려 '고기!!'로 답합니다!", color=0xffffff)
        embed.set_footer(text="고기#0001")
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
