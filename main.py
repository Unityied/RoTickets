import os

import discord
from discord import message
from discord import channel
from discord import guild
from discord.ext.commands.core import bot_has_role
import discord.ui
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.ui import view
from discord.ui import select
from discord.utils import get
import random
#from keep_alive import keep_alive

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix="!")

bannernmbr = {}
reasonnmbr = {}
setupenabled = False
timer = 60
role = ""


# Accept Button
class ButtonAccept(discord.ui.View):

    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Continue",
                       style=discord.ButtonStyle.grey,
                       emoji="➡️")
    # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, interaction: discord.Interaction,
                              button: discord.ui.Button):
        global setupenabled
        setupenabled = True
        global timer
        timer = 60

        embed2 = discord.Embed(
            title="Choose the best fitting banner!",
            description=
            "Choose one of the banners made by RoTickets✨ bot, or enter your own url!",
            color=discord.Colour.blurple(
            ),  # Pycord provides a class with default colors you can choose from
        )
        embed2.add_field(
            name="Own url...",
            value="Click the Own URL button to use your own banner url!",
            inline=False)

        embed2.add_field(name="Banner-1",
                         value="Used for RP-Games",
                         inline=True)
        embed2.add_field(name="Banner-2", value="Basic one!", inline=True)
        embed2.add_field(name="Custom URL",
                         value="Use a custom URL",
                         inline=True)

        embed2.set_footer(text="Thanks for using RoTickets✨ bot!"
                          )  #footers can have icons too
        embed2.set_author(
            name="RoTickets✨ Team",
            icon_url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237745148746534994/AAAA.png?ex=663cc37f&is=663b71ff&hm=3748e231fb6c6529287c9239a10076bbaef62774766778f64691db190c90f815&=&format=webp&quality=lossless"
        )
        embed2.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237745118543609867/operation.png?ex=663cc378&is=663b71f8&hm=0c54decec87be6a17d8059f56432fd615f2bfad3e5bf07598cd47b9d58c5449f&=&format=webp&quality=lossless"
        )
        embed2.set_image(url="https://example.com/link-to-my-banner.png")

        embedbanners1 = discord.Embed(title="Banner-1", )
        embedbanners1.set_image(
            url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237790632546930789/AAAAAAAAABANNERERLC.png?ex=663ceddb&is=663b9c5b&hm=2aa79360458360c3c16d2c5bd5b4e4c662ffd6fa798faab1fa5e33dd71e80adf&=&format=webp&quality=lossless&width=550&height=229"
        )

        embedbanners2 = discord.Embed(title="Banner-2", )
        embedbanners2.set_image(
            url=
            "https://media.discordapp.net/attachments/1237744893099773962/1238022623212998657/AAAAAAAABANNERGEN.png?ex=663f176a&is=663dc5ea&hm=31066981fb3efba6fcc4aee9419f0da061ed15d447cda89c037f9988ffbf62cb&=&format=webp&quality=lossless&width=550&height=229"
        )
        await interaction.response.send_message(
            "Choose the best fitting banner to continue!",
            embeds=(embed2, embedbanners1, embedbanners2),
            view=DropdownParent())

        await interaction.guild.create_role(name="RoTickets - Setup")


# Choose buttons!
class ButtonsChoose(discord.ui.View):

    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Embed 1",
                       style=discord.ButtonStyle.grey,
                       emoji="1️⃣")
    # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, interaction: discord.Interaction,
                              button: discord.ui.Button):
        await interaction.response.send_message("Click")


# Dropdown (https://www.youtube.com/watch?v=RV9Kfc1KQOA)
class DropdownChoose(discord.ui.Select):

    def __init__(self):
        options = [
            discord.SelectOption(label="Banner 1",
                                 emoji="1️⃣",
                                 description="Choose Banner-1!"),
            discord.SelectOption(label="Banner 2",
                                 emoji="2️⃣",
                                 description="Choose Banner-2!"),
            discord.SelectOption(label="Own Banner",
                                 emoji="🆕",
                                 description="Set your own ID")
        ]

        super().__init__(placeholder="Choose one of the options!",
                         options=options,
                         min_values=1,
                         max_values=1)

    async def callback(self, interaction: discord.Interaction):
        embed23 = discord.Embed(
            title="Choose the best fitting ticket reason!",
            description="Choose one of the reasibs made by RoTickets✨ bot!",
            color=discord.Colour.blurple(
            ),  # Pycord provides a class with default colors you can choose from
        )
        embed23.add_field(
            name="Own url...",
            value="Click the Own URL button to use your own banner url!",
            inline=False)

        embed23.add_field(name="Reason-1",
                          value="General Support",
                          inline=True)
        embed23.add_field(name="Reason-2", value="Report Staff", inline=True)
        embed23.add_field(name="Reason-3", value="Open a Ticket", inline=True)

        embed23.set_footer(text="Thanks for using RoTickets✨ bot!"
                           )  #footers can have icons too
        embed23.set_author(
            name="RoTickets✨ Team",
            icon_url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237745148746534994/AAAA.png?ex=663cc37f&is=663b71ff&hm=3748e231fb6c6529287c9239a10076bbaef62774766778f64691db190c90f815&=&format=webp&quality=lossless"
        )
        embed23.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237745118543609867/operation.png?ex=663cc378&is=663b71f8&hm=0c54decec87be6a17d8059f56432fd615f2bfad3e5bf07598cd47b9d58c5449f&=&format=webp&quality=lossless"
        )
        embed23.set_image(url="https://example.com/link-to-my-banner.png")
        global bannernmbr
        bannernmbr = self.values[0]
        await interaction.response.send_message(
            f"You choosed: `{self.values[0]}` Wait for the next step!",
            embed=embed23,
            view=ReasonParent())


# Dropdown Parent
class DropdownParent(discord.ui.View):

    # Make sure only on server setups at a time!
    def __init__(self):
        super().__init__()
        self.add_item(DropdownChoose())


class ReasonDropdown(discord.ui.Select):

    def __init__(self):
        options = [
            discord.SelectOption(label="Reason 1",
                                 emoji="1️⃣",
                                 description="Choose Reason-1!"),
            discord.SelectOption(label="Reason 2",
                                 emoji="2️⃣",
                                 description="Choose Reason-2!"),
            discord.SelectOption(label="Reason 3",
                                 emoji="3️⃣",
                                 description="Choose Reason-3!")
        ]

        super().__init__(placeholder="Choose one of the reasons!",
                         options=options,
                         min_values=1,
                         max_values=1)

    async def callback(self, interaction: discord.Interaction):

        # Sets the URL
        if bannernmbr == "Banner 1":
            urlst = "https://media.discordapp.net/attachments/1237744893099773962/1237790632546930789/AAAAAAAAABANNERERLC.png?ex=663ceddb&is=663b9c5b&hm=2aa79360458360c3c16d2c5bd5b4e4c662ffd6fa798faab1fa5e33dd71e80adf&=&format=webp&quality=lossless&width=550&height=229"
        elif bannernmbr == "Banner 2":
            urlst = "https://media.discordapp.net/attachments/1237744893099773962/1238022623212998657/AAAAAAAABANNERGEN.png?ex=663f176a&is=663dc5ea&hm=31066981fb3efba6fcc4aee9419f0da061ed15d447cda89c037f9988ffbf62cb&=&format=webp&quality=lossless&width=550&height=229"
        elif bannernmbr == "Own Banner":
            urlst = ""
        else:
            urlst = "https://www.pragmamx.org/media/pasted_image_0%5B1%5D.png"
        # Sets the title
        if self.values[0] == "Reason 1":
            titlest = "General Support"
        elif self.values[0] == "Reason 2":
            titlest = "Report Staff"
        elif self.values[0] == "Reason 3":
            titlest = "Open a Ticket"
        else:
            titlest = "Unknown Reason"

        mainembed = discord.Embed(
            title=titlest,
            description="Open a ticket to get support!",
            color=discord.Colour.blurple(
            ),  # Pycord provides a class with default colors you can choose from
        )
        mainembed.set_footer(
            text="Made with RoTickets✨ bot!")  #footers can have icons too
        mainembed.set_author(
            name="RoTickets✨ Team",
            icon_url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237745148746534994/AAAA.png?ex=663cc37f&is=663b71ff&hm=3748e231fb6c6529287c9239a10076bbaef62774766778f64691db190c90f815&=&format=webp&quality=lossless"
        )
        mainembed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1237744893099773962/1239191381193523281/tickets.png?ex=6644a968&is=664357e8&hm=990b772ff8bed96c316f918239c5b37c6a8d60d6bd0215cda7b0ba0eeca8a660&=&format=webp&quality=lossless"
        )
        mainembed.set_image(url=urlst)
        global reasonnmbr
        reasonnmbr = {self.values[0]}
        await interaction.response.send_message(embed=mainembed,
                                                view=OpenParent())
        global role
        await role.delete()
        global setupenabled
        setupenabled = False


class ReasonParent(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(ReasonDropdown())


class CreateDropdown(discord.ui.Select):

    def __init__(self):
        options = [
            discord.SelectOption(label="Create a ticket!",
                                 emoji="🎟️",
                                 description="Opens a ticket!"),
        ]

        super().__init__(placeholder="Click down below to open a ticket!",
                         options=options,
                         min_values=1,
                         max_values=1)

    async def callback(self, interaction: discord.Interaction):
        global overwritesvar
        overwritesvar = {
            interaction.guild.default_role:
            discord.PermissionOverwrite(read_messages=False),
            interaction.user:
            discord.PermissionOverwrite(read_messages=True),
        }

        channel = await interaction.guild.create_text_channel(
            f"ticket-{random.randint(12345, 99999)}", overwrites=overwritesvar)
        await interaction.response.send_message(
            f"Ticket created in {channel.mention}", ephemeral=True)

        # Sets the title
        mainembed2 = discord.Embed(
            title="Ticket Support",
            description=
            "Welcome to the ticket support! Wait for a staff member to answer you!",
            color=discord.Colour.blurple(
            ),  # Pycord provides a class with default colors you can choose from
        )
        mainembed2.set_footer(
            text="Made with RoTickets✨ bot!")  #footers can have icons too
        mainembed2.set_author(
            name="RoTickets✨",
            icon_url=
            "https://media.discordapp.net/attachments/1237744893099773962/1237745148746534994/AAAA.png?ex=663cc37f&is=663b71ff&hm=3748e231fb6c6529287c9239a10076bbaef62774766778f64691db190c90f815&=&format=webp&quality=lossless"
        )
        mainembed2.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1237744893099773962/1239191381193523281/tickets.png?ex=6644a968&is=664357e8&hm=990b772ff8bed96c316f918239c5b37c6a8d60d6bd0215cda7b0ba0eeca8a660&=&format=webp&quality=lossless"
        )

        await channel.send(f"<@{user.id}>",
                           embed=mainembed2,
                           view=CloseParent())


class OpenParent(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(CreateDropdown())


class CloseDropdown(discord.ui.Select):

    def __init__(self):
        options = [
            discord.SelectOption(label="Close the ticket!",
                                 emoji="🎟️",
                                 description="Closes the ticket!"),
        ]

        super().__init__(placeholder="Click down below to close the ticket!",
                         options=options,
                         min_values=1,
                         max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Ticket is beeing deleted!")
        if isinstance(interaction.channel, discord.TextChannel):
            await interaction.channel.delete()
        else:
            await interaction.response.send_message("Error!")


class CloseParent(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(CloseDropdown())


#----------------------------------------------------------STUFF--------------------------------------------------------


# This runs on start!
@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    # Sets the status!
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="!help - V0.1"))


# MESSAGES
@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if ctx.guild is not None:
        global guildvar
        guildvar = ctx.guild
        global role
        role = discord.utils.get(ctx.guild.roles, name="RoTickets - Setup")
    if message.author.guild_permissions.administrator:
        print("PERMS")
        if message.author == bot.user:
            return

        if message.content.startswith("!setup"):
            global setupenabled
            global user
            user = bot.get_user(1237395618159263764)
            if get(ctx.guild.roles, name="RoTickets - Setup"):
                setupenabled = True
            else:
                setupenabled = False

            if setupenabled:
                await message.channel.send(
                    f"**Wait a minute before you can start the setup!** For questions type: `!help`"
                )
            if not setupenabled:
                await message.channel.send(
                    "**Hey, do you want to start the setup?** The panel is going to be send in here, but first you have to complete some steps!",
                    view=ButtonAccept())

        if message.content.startswith("!invite"):
            await message.channel.send("https://discord.gg/HXBFgsc6Zh")

        # Help command!
        if message.content.startswith("!help"):
            embed = discord.Embed(
                title="Here is some help!",
                description=
                "Here is some help to all commands from the RoTickets✨ bot",
                color=discord.Colour.blurple(
                ),  # Pycord provides a class with default colors you can choose from
            )
            embed.add_field(
                name="There are following commands:",
                value=
                "Down below you can see the commands the RoTickets✨ bot is able to run!",
                inline=False)

            embed.add_field(name="!help",
                            value="Shows this message",
                            inline=True)
            embed.add_field(name="!setup",
                            value="Starts the ticket-system setup",
                            inline=True)
            embed.add_field(name="!invite",
                            value="Get the invite to the support server",
                            inline=True)

            embed.set_footer(text="Thanks for using RoTickets✨ bot!"
                             )  #footers can have icons too
            embed.set_author(
                name="RoTickets✨ Team",
                icon_url=
                "https://media.discordapp.net/attachments/1237744893099773962/1237745148746534994/AAAA.png?ex=663cc37f&is=663b71ff&hm=3748e231fb6c6529287c9239a10076bbaef62774766778f64691db190c90f815&=&format=webp&quality=lossless"
            )
            embed.set_thumbnail(
                url=
                "https://media.discordapp.net/attachments/1237744893099773962/1237745118543609867/operation.png?ex=663cc378&is=663b71f8&hm=0c54decec87be6a17d8059f56432fd615f2bfad3e5bf07598cd47b9d58c5449f&=&format=webp&quality=lossless"
            )
            embed.set_image(url="https://example.com/link-to-my-banner.png")
            await message.channel.send(embed=embed)


# Runs the bot!
#keep_alive()
try:
    bot.run(os.getenv("TOKEN"))
except Exception as err:
    raise err

#https://discord.gg/HXBFgsc6Zh
