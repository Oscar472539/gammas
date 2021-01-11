from discord.ext import commands
import time

bot = commands.Bot(command_prefix='!')

@bot.command()
async def forslag(ctx, *, arg):
    channel = bot.get_channel(789125609506340868)
    user = ctx.author
    await channel.send(f"<@&785962831664644116> og <@&785963111281852456> \nDer er ankommet et forslag fra {user.mention}: \n{arg}")
    await ctx.send("Tak for dit forslag!")
    time.sleep(5)
    await ctx.channel.purge(limit=2)


bot.run('Nzc3OTkxOTQxNTkzNzU5NzU2.X7LfdQ.iZ2c5y5q2lLXqG3CHzMD9cbKVEE')