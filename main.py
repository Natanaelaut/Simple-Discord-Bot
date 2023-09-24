import discord
from discord.ext import commands
import datetime
import json

class Colors:
    Red = "\033[0;31m"
    Green = "\033[0;32m"
    LightGreen = "\033[1;32m"
    White = "\033[0m"
    Yellow = "\033[1;33m"
    DarkGray = "\033[1;30m"
    LightBlue = "\033[1;34m"
    LightRed = "\033[1;31m"

class Prefix:
    event = f"{Colors.Green}[Event] {Colors.White}"
    error = f"{Colors.Red}[Erreur] {Colors.White}"
    info = f"{Colors.LightRed}[Info] {Colors.White}"
    success = f"{Colors.Green}[Succès] {Colors.White}"
    attention = f"{Colors.Red}[Attention] {Colors.White}"
    logs = f"{Colors.LightRed}[Logs] {Colors.White}"

class Bot:
    Footer_text ="Footer text"
    Footer_img = "link.com/img.png"

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.presences = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"{Colors.Green}[Succès] {Colors.White} Commandes slash synchronisé pour {self.user}")

    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="⚠️ Permission", description="Vous n'avez pas la permission d'utiliser cette commande", color=0xFFFFFF)
            embed.set_footer(text=Bot.Footer_text, icon_url=Bot.Footer_img)
            embed.timestamp = datetime.now()
            await ctx.reply(embed=embed, ephemeral=True)
        else:
            await ctx.reply(error, ephemeral=True)    

bot = Bot()

# TOKEN
bot.run(json.loads(open('credentials.json', 'r', encoding='utf-8').read())["token"])
