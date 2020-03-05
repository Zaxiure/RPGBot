import discord
import time
import asyncio
import asyncio
from threading import Timer
from datetime import datetime

class Command:
    def __init__(self, command, timeout):
        self.command = command
        self.timeout = timeout

commands = [
    Command("test", 1),
    Command("hunt", 60),
    Command("adv", 3600),
    Command("adventure", 3600),
    Command("tr", 900),
    Command("training", 900),
    Command("chop", 300),
    Command("axe", 300),
    Command("bowsaw", 300),
    Command("fish", 300),
    Command("net", 300),
    Command("boat", 300),
    Command("bigboat", 300),
    Command("pickup", 300),
    Command("ladder", 300),
    Command("tractor", 300),
    Command("greenhouse", 300),
    Command("mine", 300),
    Command("pickaxe", 300),
    Command("drill", 300),
    Command("dynamite", 300),
    Command("quest", 21600),
    Command("epic quest", 21600)
]


def newBot(botToken):
    client = discord.Client()
    enabledTimers = []

    def getPrefix():
        return "{0} [RPG]".format(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    @client.event
    async def on_ready():
        print("{0} Bot is now ready!".format(getPrefix()))

    @client.event
    async def on_message(message):
        id = "<@{0}>".format(message.author.id)

        # async def unfuckedMessage(command, id, msg):

        @asyncio.coroutine
        async def postponeMessage(command, id, msg):
            await asyncio.sleep(command.timeout)
            print("{0} rpg {1} -> {2.name}".format(getPrefix(), command.command, message.author))
            await msg.channel.send('You can use **rpg {0}** again! {1}'.format(command.command, id))

        if message.content.lower().startswith("!timer"):
            if message.author.id in enabledTimers:
                enabledTimers.remove(message.author.id)
                print("{0} {1.name} -> disabled timer".format(getPrefix(), message.author))
                await message.channel.send("You have disabled the timer!")
            else:
                enabledTimers.append(message.author.id)
                print("{0} {1.name} -> enabled timer".format(getPrefix(), message.author))
                await message.channel.send("You have enabled the timer!")
        if not message.content.lower().startswith("rpg"):
            return
        if not message.author.id in enabledTimers:
            return
        args = message.content.split()

        try:
            args[1]
        except IndexError:
            return

        for command in commands:
            if args[1] == command.command:
                print("{0} {1.name} -> rpg {2}".format(getPrefix(), message.author, command.command))
                await postponeMessage(command, id, message)
    client.run(botToken)