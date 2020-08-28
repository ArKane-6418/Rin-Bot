import discord
import time
import asyncio
import random
import os
from discord.ext import commands

# id = 601938885525635073
messages = joined = 0

# client = discord.Client()
print(os.listdir())

bot = commands.Bot(command_prefix = "?")


@bot.event
async def on_ready():
    print(f"お帰りに野菜 {bot.user.name}!")


@bot.command(name='nyahelp')
async def nyahelp(ctx):
    embedded = discord.Embed(title="Help:", description="Commands:")
    embedded.set_image(url = "https://cdn.discordapp.com/attachments/403078270356029451/600479309194461192/ykRfE4lF.jpeg")
    embedded.add_field(name="?rinsay", value="Rin's dialogue lines", inline = True)
    embedded.add_field(name="?say", value="Type messages for bot", inline = True)
    await ctx.send(content=None, embed=embedded)


@bot.command(name="say")
async def say(ctx, msg):
    content = ctx.message.content.replace("?say ", "")
    await ctx.message.delete()
    await ctx.send(content)


@bot.event
async def on_member_join(member):
    """Bot Test Server: logs channel ID, message
       Soda's Server: logs channel ID, message
       Casual Server: testing channel ID, message
    """
    guild_dict = {583864496964108288: [602295175003504682, f"""Welcome to the Test Server, {member.mention}!"""],
                  593963541858353162: [593970916141039639, f"""Welcome to the server, {member.mention}!"""],
                  532048598888742924: [603809782742384652, f"""Welcome to the Casual Server, {member.mention}!"""]}

    for guild_id in guild_dict:
        if guild_id == member.guild.id:
            await bot.get_channel(guild_dict[guild_id][0]).send(guild_dict[guild_id][1])
            print(str(bot.get_guild(guild_id)))


@bot.event
async def on_member_remove(member):
    """Bot Test Server: logs channel ID, message
       Soda's Server: logs channel ID, message
       Casual Server: testing channel ID, message
    """
    guild_dict = {583864496964108288: [602295175003504682, f"""Sorry to see you go, {member.name}, nya~."""],
                  593963541858353162: [593970916141039639, f"""Sorry to see you go, {member.name}, nya~."""],
                  532048598888742924: [603809782742384652, f"""Sorry to see you go, {member.name}, nya~."""]}

    for guild_id in guild_dict:
        if guild_id == member.guild.id:
            await bot.get_channel(guild_dict[guild_id][0]).send(guild_dict[guild_id][1])
            print(str(bot.get_guild(guild_id)))


@bot.command(name="rinsay")
async def nya(ctx):
    phrase_list = ["If you're going to play any sports, please make sure to call me!",
                   "Hah! This smells like ramen! I'm so hungry...", "I love everyone in µ's!",
                   "All right, let's make our voices heard!", "Everything's going swimmingly!",
                   "Great job!", "Good morning! Let's do our best today!", "I'm thirsty from all that practice!",
                   "Ah! Look at the time!", "Oh, you found me! Anyways, you shouldn't stay up too late.",
                   "Such a nice, warm time of year... Makes me sleepy...",
                   "So hot! How about we go to the pool together?", "Fall is for sports! All right, move your body!",
                   "How about coming for a walk with me, since it's so cold?", "I'll support you.", "You called?",
                   "What's up? What happened?", "Hey! That tickles!", "Well that was sudden!", "Hey! Quit it!",
                   "Hey! Knock it off, or I'm going to get angry!",
                   "If you don't tell me that you want to hang out, then I won't know.",
                   "Of course, this is so embarrassing...", "Eeep! Eek! We-well, that was sudden!",
                   "You didn't forget about me, did you?", "Hurry up, I want to see more Story!",
                   "Keep working hard toward your Goal!", "I want to do a Live Show!",
                   "I'm tired too. No surprise there, though.", "I can still Practice.",
                   "We should do a Special Practice and see.", "You have a Present! What is it? What is it?",
                   "Scout someone.", "Check your new information.",
                   "There's an event going on right now! I want to join!", "Can you please wait a moment?",
                   "When we're done, I want to play.", "I love sports!",
                   "I want to play badminton... I should bring a racket.", "All right! Select \"Story\"!",
                   "What are our friends doing?", "You can see all the Members in the group.", "You got this!",
                   "Let's Practice hard!", "Heh.", "It's so comfortable next to you.",
                   "Meow! I'm dressed up as a monster cat for Halloween this year.",
                   "*Snicker* Eating chocolate with you makes me feel like I'm floating on a cloud.",
                   "When you say something looks good on me, it always makes me happy, even if it's just flattery!",
                   "Our next live show is in the style of a musical. You're gonna love it.",
                   "Thanks for everything! I hope you'll keep on cheering for me!",
                   "I set up a big surprise just for you! Hurry up and come over, already!",
                   "We're all so excited to go on this trip to Numazu together! Let's play tag on the seashore later!",
                   "You believed in me!", "Amazing!", "The Live Show was a success!", "All right! Just keep going!",
                   "Please play with me from time to time...", "You can do it!",
                   "Is this what they call \"happiness\"?",
                   "Om nom nom... Om nom nom... You can't talk with a mouthful of ehomaki sushi!",
                   "Fight, fight, fight! Take 'em all down!", "I'm the princess?! *Giggle* Now I'm blushing!",
                   "Nya!", "We're perfect together!", "Hee hee... Together, forever?", "Thank you, thank you!",
                   "It's all thanks to you!",
                   "The stars and sky are extra beautiful tonight. Do you think the sky was like this on the night I was born?",
                   "My favorite thing in the world is to put on a great performance that makes people happy!",
                   "I've got energy to spare! Sing with me, dance with me, party with me!",
                   "I'm a little scared of honeybees because they can sting, but I sure love their sweet, sweet honey!",
                   "I'm always so energetic... But if I can't see you, I get lonely.",
                   "If you work hard, your dreams will come true. You're the one who taught me that.",
                   "Tonight, I will dance most beautifully for you!", "Every time I move, I jingle. It's super cute!",
                   "I've turned into a mouse, squeak squeak! *Groan* Squeaking is too embarrassing!",
                   "What's your favorite animal? I like cats. Big surprise, right? Too bad I'm allergic to them...",
                   "*Glance* Ungh. I'm so embarrassed I just want to put a bucket over my head.", "Nya, nya, nya!",
                   "I love you guys to the moon and back! Let's always stay together!",
                   "Um... I want my crush to have the same interests as me.", "Even I get nervous sometimes... Don't you?",
                   "We're gonna have fun till we drop today! C'mon, c'mon!",
                   "Going out together, just the two of us... It kinda feels like a date!",
                   "Purr... I'm a spoiled kitty. Meow.", "Ta-daa! These are my cat pajamas!",
                   "Huh!? Fish? It's true that cats eat fish, but... fish is the one thing I don't really like...",
                   "Meow~! When you think of cats, you think of Rin! Meow, meow~. I want food, meow~.",
                   "A small miracle? Yeah, of course I've had some happen to me too~!",
                   "Let's go for a run together sometime. I'll blow a whistle to help you out.",
                   "I like dancing, but my favorites would have to be running like \"whoosh\" and jumping like \"pyaa\".",
                   "What kind of ramen do you like? You know~ Hehehe~ I love all kinds of ramen~~!",
                   "Huh? What do I like about ramen? It's so warm... And looking at it is enough to make me happy~ ...Just like you.",
                   "Out of all of us, I'm the best swimmer.",
                   "I want to be able to do well on tests without having to study~ so I can play around as much as I want.",
                   "My feelings for you might bloom as well.",
                   "Morning! I wanted to play with you today so I came to you. You won't refuse just because it's cold out, right?",
                   "Unyaa~!!", "I'm making more of my special ramen. There are customers waiting, you know~",
                   "Unya... When you look at me, I get embarrassed and my chest hurts. It's strange, right?",
                   "I'll keep doing my best! Meow~!!", "Oh? Weren't you going to elope with me?",
                   "Come look at the starry sky with me! *Snicker* Because my last name means starry sky. Get it?"]

    await ctx.send(random.choice(phrase_list))


@bot.event
async def on_message(message):
    channels = ["testing", "bot-commands", "general"]
    restricted = ["music-bot"]

    if (str(message.channel) in channels or str(message.channel) not in restricted) and not message.author.bot:
        if message.content.lower().find("nya") != -1:
            random_nya = random.randint(0,199)
            if random_nya == 0:
                await message.channel.send("Nya~")
        if message.content[-3:].lower() == "nya" or message.content[-4:].lower() == "nya!" or \
                message.content[-4:].lower() == "nya." or message.content[-4:].lower() == "nya~" or \
                message.content[-4:].lower() == "nya?" or message.content[-4:].lower() == "nya,":
            print("Emoji sent.")
            await message.add_reaction("<:rinyay:602299324088451093>")
            # Emoji ID for my server: 602299324088451093
    await bot.process_commands(message)

file_object = open("rinbot_key.txt", "r")
bot.run(file_object.read().strip())