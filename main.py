import discord
import staben
import texts

cmd_prefix = "!"

class BotClient(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content[0] == cmd_prefix:
            message_split = message.content[1:].split(" ")
            command = message_split[0]
            parameters = message_split[1:]
            await self.on_command(message.author, message.channel, command, parameters)

    async def on_command(self, user, channel, command, parameters):
        if command == "staben" and parameters and parameters[0] == "quote":
            embed = discord.Embed(title=staben.get_quote())
            await channel.send(embed=embed)
        elif command == "help":
            embed = discord.Embed(title="Robbe Robot commands", description=texts.help)
            await channel.send(embed=embed)

client = BotClient()
client.run("ODAyMjQzNzA1NzMzMzgyMTU1.YAsZrA.EiHf5HglwCRB1d1ups7VpZCvizQ")
