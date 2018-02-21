import requests
import re
import pyquery
import urllib
import praw
import random
import pudb
import sys
import time
import discord
import logging
import asyncio
import json

client = discord.Client()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-' \
                              '8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%' \
                                       '(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

redditregex = re.compile(r"\[\[(.+?)\]\]")

with open("discord_keys.txt") as f:
    token_arr = json.load(f)
    token = token_arr["token"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

with open("MasterCatalog.txt") as f:
    champDict = json.load(f)

with open("AliasJson.txt") as f:
    aliasDict = json.load(f)

with open("TaricQuoteJson.txt") as f:
    TaricDict = json.load(f)
    TaricQuotes = TaricDict["Quotes"]

testStr1 = "Gnar/Skins"
testStr2 = "Jayce/Lore"
testStr3 = "Bastion"
testStr4 = "PAX Jax"
testStr5 = "Classic Akali"
testStr6 = "Urf the Manatee"
testStr8 = "Winter's Bite"
testStr9 = "waiFu"
testStr10 = "GNAR!"
testStr11 = "Xayah"
testStrings = [testStr1, testStr2, testStr3, testStr4, testStr5,
               testStr6, testStr8, testStr9, testStr10, testStr11]

def giveResults(i):
    testResults = []
    print(i)

    for champ, details in champDict.items():
        if i.strip().lower() == champ.lower() or i.strip().lower() in (nick.lower() for nick in aliasDict[champ]):
            if champ.lower() == "Taric":
                testResults.append(True)
            else:
                testResults.append(False)
            testResults.append("Overview")
            testResults.append(champ)
            testResults.append(details["Lore"])
            
            abilNames = []
            for abilKey, abil in details["Abilities"].items():
                abilNames.append(abil["Name"])
            testResults.append(abilNames)

            skinNames = []
            for skin in details["Skins"]:
                skinNames.append(skin)
            testResults.append(skinNames)
            return testResults
        elif i.strip().lower() == champ.lower() + "/lore":
            if champ.lower() == "Taric":
                testResults.append(True)
            else:
                testResults.append(False)
            testResults.append("/Lore")
            testResults.append(details["Lore"])
            return testResults
        elif i.strip().lower() == champ.lower() + "/abilities":
            if champ.lower() == "Taric":
                testResults.append(True)
            else:
                testResults.append(False)
            testResults.append("/Abilities")
            abilNames = []
            for abilKey, abil in details["Abilities"].items():
                abilNames.append(abil["Name"])
            testResults.append(abilNames)
            return testResults
        elif i.strip().lower() == champ.lower() + "/skins":
            if champ.lower() == "Taric":
                testResults.append(True)
            else:
                testResults.append(False)
            skinNames = []
            for skin in details["Skins"]:
                skinNames.append(skin)
            testResults.append(skinNames)
            return testResults
        for abilKey, abil in details["Abilities"].items():
            if i.strip().lower() == abil["Name"].lower():
                if champ.lower() == "Taric":
                    testResults.append(True)
                else:
                    testResults.append(False)
                testResults.append("Ability")
                testResults.append(abilKey)
                testResults.append(abil)
                return testResults
        for skin, skinDeets in details["Skins"].items():
            if i.strip().lower() == skin.lower():
                if champ.lower() == "Taric":
                    testResults.append(True)
                else:
                    testResults.append(False)
                testResults.append("Skin")
                testResults.append(skin)
                testResults.append(skinDeets)
                return testResults
    return testResults

for test in testStrings:
    print(giveResults(test))

@client.event
async def on_message(message):
    body = message.content
    matches = redditregex.findall(body)
    if matches != []:
        if len(matches) > 3: #Caps at 3 responses
            a = 3
        else:
            a = len(matches)
        finalstr = ""
        for i in range(a):
            noMatch = False
            basis = giveResults(matches[i])
            if basis != []:
                if basis[0] == True: #If Taric is involved
                    finalstr += "Hey, it's me!\n\n"
                else:
                    pass
                
                if basis[1] == "Overview":
                    finalstr += basis[2] + ":\n\n" #Champion name

                    finalstr += basis[3] + "\n\n" #Lore

                    #List ability names
                    finalstr += "Passive: " + basis[4][0] + "\n"
                    finalstr += "Q: " + basis[4][1] + "\n"
                    finalstr += "W: " + basis[4][2] + "\n"
                    finalstr += "E: " + basis[4][3] + "\n"
                    finalstr += "R: " + basis[4][4] + "\n\n"

                    #List skin names
                    finalstr += "Skins: \n"
                    for skin in basis[5]:
                        finalstr += skin + "\n"
                elif basis[1] == "Ability":
                    finalstr += basis[3]["Description"] + "\n\n" #Description has name
                elif basis[1] == "Skin":
                    finalstr += basis[2] + "\n" #Skin name
                    for deetN, deet in basis[3].items():
                        finalstr += deetN + ": " + deet + "\n" #Skin attributes
                elif basis[1] == "/Lore":
                    finalstr += basis[2] + "\n\n" #Lore
                elif basis[1] == "/Abilities":
                    #List ability names
                    finalstr += "Passive: " + basis[2][0] + "\n"
                    finalstr += "Q: " + basis[2][1] + "\n"
                    finalstr += "W: " + basis[2][2] + "\n"
                    finalstr += "E: " + basis[2][3] + "\n"
                    finalstr += "R: " + basis[2][4] + "\n\n"
                elif basis[1] == "/Skins":
                    for skin in basis[2]:
                        finalstr += skin + "\n"                   
            else:
                noMatch = True
            print(noMatch)
            if not noMatch:
                finalstr += "------------------------------------\n\n"
        if finalstr not in "":
            finalstr += "I'm a bot-in-training! If you have questions or bugs," \
                        " PM me at https://www.reddit.com/message/compose/?to=Tarics" \
                        "KnowledgeBot  \n  \n"
            quote = TaricQuotes[random.randint(0, len(TaricQuotes)-1)]
            finalstr += ("_"+quote+"_")
            print(finalstr)
            await client.send_message(message.channel, finalstr)

while True:
    try:
        client.run(token)
    except Exception as e:
        print(e)
        print("Sleepy time")
        time.sleep(60)
