import discord
from discord.ext import tasks
from services import env
from mcstatus import MinecraftServer

client = discord.Client()
discord_token = env.get_string("DISCORD_TOKEN")
minecraft_server_ip = env.get_string('MINECRAFT_SERVER_IP')
minecraft_server_port = env.get_string('MINECRAFT_SERVER_PORT')
mc_server = MinecraftServer(minecraft_server_ip, int(minecraft_server_port))


def main() -> None:
    client.run(discord_token)


@client.event
async def on_ready() -> None:
    print("The bot is online !")

    if not loop.is_running():
        loop.start()


@tasks.loop(seconds=10)
async def loop() -> None:
    data = mc_server.status()

    if data:
        activity = discord.Game(name=f"{data.players.online} / {data.players.max}")
        await client.change_presence(activity=activity, status=discord.Status.online)
    else:
        print("Not available status")


if __name__ == "__main__":
    main()
