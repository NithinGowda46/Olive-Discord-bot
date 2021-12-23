#discord bot-Olive 
# -Suhas M L

import discord
#os is imported cos of key of bot
import os
my_secret = os.environ['TOKEN']
import requests
import json
import webbrowser
import random 
from replit import db
from alive import keep_alive
from jokes import get_jokes
from dictionary import dict_api
from hangman import game1
from fortnite import fn

def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

#get_jokes api for returning random jokes:

encouragements = [
  'Cheer up mate!', 'Hang in there buddy', 'You are a great person','Its gonna be okay!','Its gonna get better','Better days are ahead'
  ]

#update encouragements in the database
def update_encouragements(en_msg):
  if "encouagements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(en_msg)
    db['encouragements'] = encouragements
  else:
    db['encouragements'] = [en_msg]

#for deleting an encouraging message;
def delete_encouragements(index):
  encouragements = db['encouragements']
  if len(encouragements)>index:
    del encouragements[index]
    db['encouragements'] = encouragements

#Create an instance for client:
client = discord.Client()
#creating/registering an event 
#async is an asynchronous function that works on callback,i.e.,
#A callback is a functn that is called when something else happens

#now this bot responds with an encouraging message if users message contains any of the sad words
sad_words = ['sad','depressed','unhappy','angry','rage','miserable','depressing','bad week','bad day','miss','Sad','sadd','hopeless','give up']


if "responding" not in db.keys():
  db['responding'] = True

@client.event
async def on_ready():
  #this event is called when the bot s ready to be used:
  print("You have logged in as {0.user}".format(client))
  #{0.user} is replaced with username from client:

#for responding or acting on a message:
#when message is recieved
@client.event
async def on_message(msg):
  #when the message is from the bot or user of the bot itself we dont have to respond
  message = msg.content
  if msg.author == client.user:
    return
  #when there is a bot command:
  #1: *hello command:prints a hello message in the channel
  hi_msg = ['Hello!','Hello there!','Hey',"Heyy",'Hi there!']
  if msg.content.startswith("$hello"):
    await msg.channel.send(random.choice(hi_msg))
    #to return a quote when $juote is passed:
  if msg.content.startswith("$quote"):
    quote = get_quotes()
    await msg.channel.send(quote)
    #this bot noe checks the message for any of the words in sad_words list and if it is present it returns a random message from encouragements list:

  if msg.content.startswith("$pun"):
    joke = get_jokes()
    await msg.channel.send(joke)

  if (msg.content.startswith("Who are you") or msg.content.startswith("Who are you?") or msg.content.startswith("who are you") or msg.content.startswith("who are you?") or msg.content.startswith("Who are you@olive")):
    await msg.channel.send("Hello, I am Olive and I am a bot!")

  #dictionary:
  if msg.content.startswith("$meaning"):
    word = message.split('$meaning ',1)[1]
    mean = dict_api(word)
    mean = mean
    await msg.channel.send(mean)

  #fortnite game:
  if msg.content.startswith("$fortnite"):
    c = fn()
    await msg.channel.send(c)


  #all commands:
  if msg.content.startswith("$commands"):
    await msg.channel.send("1. $hello: Returns a hello message\n2. $quote: Returns a quote\n3. $pun: Returns a pun\n4. $meaning \'word\': Returns the meaning of the given word\n5. $new \'message\': Adds the entered message into the database")

  def w(s):
    if(s==1):
      word = random.choice(["iron man",'hulk','thor','wanda','vision','tonystark','captain america','spiderman','blackwidow','thanos','ultron',"falcon","wintersoldier","scarlett witch","loki",'shang chi',"venom"])
      return word
    elif(s==4):
      word = random.choice(['operating system','network','algorithm','firewall','java','keyboard','linux','motherboard','teminal','windows'])
      return word
    elif(s==3):
      word = random.choice(['athletics','basketball','baseball','badminton','cricket','football','gymnastics','hockey','olympics','rugby','table tennis'])
      return word
    elif(s==2):
      word = random.choice(['afghanistan','australia','brazil','china','canada','denmark','france','india','italy','japan','malaysia','united states of america'])
      return word
    else:
      return

  #hangman

  if msg.content.startswith("$hangman"):
    await msg.channel.send("Guess the word in 10 attempts")
    game1()
  
  if db["responding"]:
    encouragements = [
  'Cheer up mate!', 'Hang in there buddy', 'You are a great person','Its gonna be okay!','Its gonna get better','Better days are ahead'
  ]
    options = encouragements
    if "encouragements" in db.keys():
      options = db["encouragements"]
    if any(word in message for word in sad_words):
      await msg.channel.send(random.choice(options))
    #we can take encourage messages from users and store it in database and use them to return the next time around

    #users acn add new messages using $new command:
  if msg.content.startswith('$new'):
    en_msg = message.split('$new ',1)[1] #this line splits the ip after $new and the rest of the sentence is added to the database
    update_encouragements(en_msg)
    await msg.channel.send("New message has been added")

  if msg.content.startswith('$del'): #for deleting any index encouragement
    encouragements = []
    if "encouragements" in db.keys(): #if the encouragement is already ready itll get deleted
      index = int(message.split('$del',1)[1])
      delete_encouragements(index)
      encouragements = db['encouragements']
    await msg.channel.send(encouragements)

  if msg.content.startswith('$encourage'):
    value = message.split("$encourage ",1)[1]
    if value.lower() == 'true':
      db["responding"] = True
      await msg.channel.send("Encoraging is on")
    else:
      db["responding"] = False
      await msg.channel.send("Encoraging is off")


keep_alive()
#for running the bot:
client.run(my_secret)