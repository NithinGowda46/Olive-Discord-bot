import discord
import random
import os
client = discord.Client()
def w(s):
    if(s==1):
        word = random.choice(["iron man",'hulk','thor','wanda','vision','tonystark','captain america','spiderman','blackwidow','thanos','ultron',"falcon","wintersoldier","scarlett witch","loki",'shang chi',"venom"])
        return word
    elif(s==4):
        word = random.choice(['operating system','network','algorithm','firewall','java','keyboard','linux','motherboard','teminal','windows'])
        return
    elif(s==3):
        word = random.choice(['athletics','basketball','baseball','badminton','cricket','football','gymnastics','hockey','olympics','rugby','table tennis'])
        return word
    elif(s==2):
        word = random.choice(['afghanistan','australia','brazil','china','canada','denmark','france','india','italy','japan','malaysia','united states of america'])
        return word
    else:
        print("Invalid choice!")
def game1():
  @client.event
  async def on_message(msg):
    await msg.channel.send("Choose your theme:\n")
    await msg.channel.send("1:Avengers\n2:Country Names\n3:Sports\n4:Computers")
    s = await client.wait_for("message", check=check)
    s = int(s)
    if(s==0 or s>4):
      await msg.channel.send("Invalid choice\nEnter one of the above options")
      s = await client.wait_for("message", check=check)
      s = int(s)
      word = w(s)
    else:
      word = w(s)

    validletters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""
    while(len(word)>0):
      main = ""
      for i in word:
        if i in guessmade:
          main = main + i
        else:
          main = main + "-" + ""
        if(main==word):
          await msg.channel.send(word)
          await msg.channel.send("You Win!!")
          break


        print(main)
        guess = await client.wait_for("message", check=check)
        if guess in guessmade and word:
          await msg.channel.send("Letter already guessed")

        if guess in validletters:
          guessmade = guessmade + guess
        else:
          await msg.channel.send("Invalid input, Re-Enter: ")
          guess = await client.wait_for("message", check=check)
        if guess not in word:
          turns=turns-1
          if turns==9:
            await msg.channel.send("________")
            await msg.channel.send("\n 9 turns left")
            if turns==8:
              await msg.channel.send("________")
              await msg.channel.send("    O   ")
              await msg.channel.send("\n 8 turns left")
            if turns==7:
              await msg.channel.send("________")
              await msg.channel.send("    O   ")
              await msg.channel.send("    |   ")
              await msg.channel.send("\n 7 turns left")
            if turns==6:
              await msg.channel.send("________")
              await msg.channel.send("    O   ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   /    ")
              await msg.channel.send("\n 6 turns left")
            if turns==5:
              await msg.channel.send("________")
              await msg.channel.send("    O   ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   / \  ")
              await msg.channel.send("\n 5 turns left")
            if turns==4:
              await msg.channel.send("________")
              await msg.channel.send("    O /  ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   / \  ")
              await msg.channel.send("\n 4 turns left")
            if turns==3:
              await msg.channel.send("________")
              await msg.channel.send("  \ O /  ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   / \  ")
              await msg.channel.send("\n 3 turns left")
            if turns==2:
              await msg.channel.send("________")
              await msg.channel.send("         ")
              await msg.channel.send("         ")
              await msg.channel.send("    |    ")
              await msg.channel.send("  \ O /  ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   / \  ")
              await msg.channel.send("\n 2 turns left")
            if turns==1:
              await msg.channel.send("________")
              await msg.channel.send("         ")
              await msg.channel.send("    __    ")
              await msg.channel.send("    |    ")
              await msg.channel.send("  \ O /  ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   / \  ")
              await msg.channel.send("\n 1 turns left")
            if turns==0:
              await msg.channel.send("________")
              await msg.channel.send("      |  ")
              await msg.channel.send("    __|    ")
              await msg.channel.send("    |    ")
              await msg.channel.send("  \ O /  ")
              await msg.channel.send("    |   ")
              await msg.channel.send("   / \  ")
              await msg.channel.send("\n GAME OVER !!   Y-O-U-L-O-S-E")
              break
