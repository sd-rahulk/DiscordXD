#make an economy Discord bot with Python and discord.py
#import necessary libraries
#import discord
from discord.ext import commands
import random
import os
#create a bot with prefix as Yo!
bot = commands.Bot(command_prefix='Yo! ')

def choose():

    # list of word

  words = ("cooking", "dosa", "rice", "egg", "water", "masala", "oil", 
   "noodles",
         "juice", "ice-cream", "idly", "carrot", "curd", "sambar", "pulses",
         "medu-vada", "idly-sambar", "lemon-rice", "coconut", "panipuri")
 

    # choice() method randomly choose

    # any word from the list.
 

  return random.choice(words)
  
def jumble(word):
    random_word = random.sample(word, len(word))
 

    # join() method join the elements

    # of the iterator(e.g. list) with particular character .

    jumbled = ''.join(random_word)

    return jumbled


#create a function hi which shoud print -reply hey dude! What's up when called
@bot.command()
async def hi(ctx):
    await ctx.send('hey dude! What\'s up')


#make a function to create account for a user with a username and password
@bot.command()
async def create_account(ctx, password):
    if (os.path.isfile(ctx.author.name + '.txt')):
        await ctx.send('Account already exists!')

    else:
        #create a file with the username and password
        file = open(ctx.author.name + '.txt', 'w')
        file.write(password)
        file.close()
        #print User photo, user name and "congratulations u have create ur account"
        await ctx.send(ctx.author.avatar_url)
        await ctx.send(ctx.message.author.name +
                       ' congratulations u have created ur account')
        #make a new line in username file and add the bal value as 0
        file = open(ctx.author.name + '.txt', 'a')
        file.write('\n')
        file.write('100')
        file.close()
    #if account already exists, send a message saying so to the user using ctx.send()


#make a function to check the balance of a user in the account
@bot.command()
async def check_balance(ctx):
    #open the username file
    #if no user found
    if (not os.path.isfile(ctx.author.name + '.txt')):
        await ctx.send('No user found!')

    else:
        file = open(ctx.author.name + '.txt', 'r')
        #read the file
        lines = file.readlines()
        #close the file
        file.close()
        #print the balance of the user
        await ctx.send('The balance of ' + ctx.author.name + ' is ' + lines[1])


#make a function named help, if it is called print the following message: Hi dude, This is Vulture a fun currency game bot. U can add a account for u and ur money will be saved in ☆ (Currency name). To earn money u have many options available 1. Choosing ur job (Yo! work list) and work (Yo! work) for 2 times in a day. 2. Playing a battle survival game - Fighters 3. Bet ur frnds
@bot.command()
async def about(ctx):
    await ctx.send(
        '''Hi dude, This is Vulture a fun currency game bot. U can add a account for u and ur money will be saved in ☆ (Currency name). To earn money u have many options available 
    1. Choosing ur job (Yo! work list) and work (Yo! work) for 2 times in a day. 
    2. Playing a battle survival game - Fighters 
    3. Bet ur frnds ''')


#make a share function to share <amount of ☆> to <user name> and when done reduce the ☆ from the sender
@bot.command()
async def share(ctx, amount, username):
    # if the user is not found

    if (not os.path.isfile(ctx.author.name + '.txt')):
        await ctx.send('No user found!')

    elif (not os.path.isfile(username + '.txt')):
        await ctx.send("Username is Invalid")

    else:

        #open the sender file
        file = open(ctx.author.name + '.txt', 'r')
        #read the file
        lines = file.readlines()
        #close the file
        file.close()
        #if the amount of ☆ is greater than the sender's balance
        if (int(lines[1]) < int(amount)):
            await ctx.send('You dont have enough ☆!')
        #if the amount of ☆ is less than the sender's balance
        else:
            #open the receiver file
            file = open(username + '.txt', 'r')
            #read the file
            lines = file.readlines()
            #close the file
            file.close()
            #if the receiver file is not found
            if (not os.path.isfile(username + '.txt')):
                await ctx.send('No user found!')
            #if the receiver file is found
            else:
                #open the sender file
                file = open(ctx.author.name + '.txt', 'r')
                #read the file
                lines = file.readlines()
                #close the file
                file.close()
                #open the receiver file
                file = open(username + '.txt', 'r')
                #read the file
                lines2 = file.readlines()
                #close the file
                file.close()
                #open the sender file
                file = open(ctx.author.name + '.txt', 'w')
                #write the new balance to the sender file
                file.write('\n')
                file.write(str(int(lines[1]) - int(amount)))
                #close the file
                file.close()
                #open the receiver file
                file = open(username + '.txt', 'w')
                #write the new balance to the receiver file
                file.write('\n')
                file.write(str(int(lines2[1]) + int(amount)))
                #close the file
                file.close()
                #send a message to the sender saying that the amount of ☆ has been sent to the receiver
                await ctx.send('The amount of ' + amount +
                               '☆ has been sent to ' + username)


#make a function named worklist
@bot.command()
async def work_list(ctx):
    await ctx.send('''The work list: 
    Hacker - a local hacker [560 ☆]
    Detective - a skilled detective [790 ☆]
    Chef - a fast food chef [900 ☆] 
    Gangster - a right hand of a big mafia don in city [970 ☆] 
    Army soldier - a brave army soldier [1,000 ☆] 
    Superhero - a powerful superhero who works for a secret agency [1,010 ☆] 
    If u choosen a job after 4 months u will be retried for tht job and will continue new job.'''
                   )


@bot.command()
async def work(ctx, work):
    global picked_word
    if (not os.path.isfile(ctx.author.name + '.txt')):
        await ctx.send('No user found!')

    elif (work == "Chef"):
        await ctx.send(
            "Congratulations! U have choosen " + work +
            ". Ur work time is 2 times in a day if u miss to work 100 glints will taken from account"
        )
        await ctx.send("Let's start")
        picked_word = choose()
 

        # jumble() function calling

        qn = jumble(picked_word)

        await ctx.send("jumbled word is :" + qn)
      
@bot.command()
async def check(ctx, ans):
  if(ans == picked_word):
    await ctx.send("Correct")
    file = open(ctx.author.name + '.txt', 'r')
    #read the file
    lines = file.readlines()
    #close the file
    file.close()
    file = open(ctx.author.name + '.txt', 'w')
    file.write('\n')
    #file.write(sum(str(lines[1] + 900))
    file.close()
    await ctx.send("900☆ is added to ur account")
    

  else:
    await ctx.send("incorrect")


bot.run('Token')######## Thambi token maathu#########
############discord token ################
