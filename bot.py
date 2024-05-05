#pawloobot.py
import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")
welcome_channel_id = your_welcome_channel_id
@client.event
async def on_member_join(member):
    channel = client.get_channel(welcome_channel_id)
    embed=discord.Embed(title=f"Witamy na serwerze{member.mention}", color=0xffff00)
    await channel.send(embed)
@client.event
async def on_ready():
  print("Bot się zresetował!")
  client.add_view(Verification())

class Verification(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label="Zweryfikuj się",custom_id = "Verify",style = discord.ButtonStyle.success)
  async def verify(self, interaction, button):
    role = 1235630057473441823
    user = interaction.user
    if role not in [y.id for y in user.roles]:
      await user.add_roles(user.guild.get_role(role))
      await user.send("Zweryfikowałeś się!")

@client.command()
async def initialize(ctx):
  embed = discord.Embed(title = "Zweryfikuj się", description = "Kliknij Poniżej aby się zweryfikować.")
  await ctx.send(embed = embed, view = Verification())
@client.command()
async def pomoc(ctx):
    embed=discord.Embed(title="POMOC")
    embed.add_field(name="!pomoc - opis komend", value="", inline=True)
    embed.add_field(name="!event - tworzysz napis z danym przez ciebie opisem", value="(w komendzie event dajesz spacje i piszesz wtedy opis)", inline=False)
    embed.add_field(name="!clear - usuwasz wiadomości z kanału tekstowego", value="(w komendzie clear dajesz spacje a potem piszesz ile wiadomości chcesz usunąć)", inline=False)
    embed.add_field(name="!rybnik - sam sprawdz XD", value="rybnikowa ryba chce cie polizac", inline=False)
    embed.add_field(name="!credits - credity", value="pokazuje kto pracował nad botem", inline=False)
    await ctx.send(embed=embed)
@client.command()
async def regulamin_channel(ctx):
    embed=discord.Embed(title="REGULAMIN", color=0x7aff70)
    embed.add_field(name="Zweryfikować Się Albo Wyrzucenie!", value="", inline=False)
    embed.add_field(name="Zakaz Spamu Albo Ban!", value="", inline=False)
    embed.add_field(name="Zakaz Dodawania Botów Bez Pozwolenia", value="", inline=False)
    embed.add_field(name="Zakaz Oszukiwania", value="", inline=False)
    embed.add_field(name="Zakaz Wyzywania", value="", inline=False)
    embed.add_field(name="Zakaz @Admin Lub @Mod Dodawania Ról Bez Pytania", value="", inline=False)
    embed.add_field(name="Zakaz Śmiania Się Z Innych Lub Z Powitaniach", value="", inline=False)
    await ctx.send(embed=embed)    
@client.command()
async def event(ctx, desc):
    embed=discord.Embed(title="Taka Tam Informacja", description=desc, color=0x7aff70)
    await ctx.send(embed=embed)
@client.command()
async def credits(ctx):
    embed=discord.Embed(title="Bot został zrobiony przez @pawlo", description="", color=0x7aff70)
    await ctx.send(embed=embed)    
@client.command()
async def rybnik(ctx):
    await ctx.send("https://tenor.com/pl/view/crazy-fish-crazy-fish-meme-fish-meme-spanvis-meme-spanvis-gif-5948691788322863963") 
    await ctx.send("rybnikowa ryba chce kogoś polizać")        
@client.command()
async def clear(ctx, limit:int):
		await ctx.channel.purge(limit=limit)
		await ctx.send(f'{limit} wiadomości zostało wyczyszczonych')
client.run("your-bot-token")
