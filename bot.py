# pip3 install -U discord-py-interactions
# pip3 install -U discord-py-slash-command
# pip3 install discord

from typing_extensions import Required
import discord
import interactions


from bot_token import DISCORD_TOKEN
guild_id = 974059269668343829
bot = interactions.Client(token=DISCORD_TOKEN)

# @bot.command(
#     name="say_something",
#     description="say something!",
#     scope=guild_id,
#     options = [
#         interactions.Option(
#             name="text",
#             description="What you want to say",
#             type=interactions.OptionType.STRING,
#             required=True,
#         ),
#     ],
# )
# async def my_first_command(ctx: interactions.CommandContext, text: str):
#     await ctx.send(f"You said '{text}'!")


button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Get DOH! role",
    custom_id="doh"
)
button1 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Get Dough role",
    custom_id="dough"
)

@bot.command(
    name="role_picker",
    description="This is the first command I made!",
    scope=guild_id,
)
async def role_picker(ctx):
    await ctx.send("Pick a role", components=[button, button1])

@bot.component("doh")
async def button_response(ctx):
    ctx.member.add_role()
    await ctx.send("You clicked the DOH! :O", ephemeral=True)

@bot.component("dough")
async def button_response(ctx):
    # give role
    await ctx.send("You clicked the Dough! :O", ephemeral=True)



bot.start()

# client.run(DISCORD_TOKEN)



# errors and solutions
# 405 Method Not Allowed (error code: 0): 405: Method Not Allowed -- 