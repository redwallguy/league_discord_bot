import requests
import re
import pyquery
import urllib
import praw
import random
import pudb
import json

PyQuery = pyquery.PyQuery

champDict = {}
listOfAbilities = []
listOfLore = []
listOfSkinsv1 = []
listOfSkins = []
listOfItems = []
TaricQuotes = []

p = PyQuery("http://leagueoflegends.wikia.com/wiki/Champion")

for i in p.items(".champion_roster .champion-icon"):
    print(i.attr("data-champion"))
    champDict[i.attr("data-champion")] = {"Abilities": {"Innate":{"Name": "", "Description": ""},
                                  "Q": {"Name": "", "Description": ""},
                                  "W": {"Name": "", "Description": ""},
                                  "E": {"Name": "", "Description": ""},
                                  "R": {"Name": "", "Description": ""}},
                    "Skins": {}, "Lore": ""}

for champKey, champ in champDict.items():
    p = PyQuery("http://leagueoflegends.wikia.com/wiki/" + champKey + "/Abilities")

    for i in p(".skill_innate > div > div").items():
        champ["Abilities"]["Innate"]["Name"] = i.attr.id.replace("_"," ")
        champ["Abilities"]["Innate"]["Description"] = i.text().replace(".21","!").replace(".27", "'")

    for i in p(".skill_q > div > div").items():
        champ["Abilities"]["Q"]["Name"] = i.attr.id.replace("_"," ")
        champ["Abilities"]["Q"]["Description"] = i.text().replace(".21","!").replace(".27", "'")

    for i in p(".skill_w > div > div").items():
        champ["Abilities"]["W"]["Name"] = i.attr.id.replace("_"," ")
        champ["Abilities"]["W"]["Description"] = i.text().replace(".21","!").replace(".27", "'")

    for i in p(".skill_e > div > div").items():
        champ["Abilities"]["E"]["Name"] = i.attr.id.replace("_"," ")
        champ["Abilities"]["E"]["Description"] = i.text().replace(".21","!").replace(".27", "'")

    for i in p(".skill_r > div > div").items():
        champ["Abilities"]["R"]["Name"] = i.attr.id.replace("_"," ")
        champ["Abilities"]["R"]["Description"] = i.text().replace(".21","!").replace(".27", "'")

    p = PyQuery("http://leagueoflegends.wikia.com/wiki/" + champKey + "/Skins")

    for skin in p(".wikia-gallery-item[style='width:322px; ']").items():
        skinname = str(skin(".lightbox-caption").contents()[0])
        if skinname.startswith("<"):
            pass
        else:
            skinname = skinname.replace(r"\\n","").strip()
            print(skinname)
            skintext = skin(".lightbox-caption > div").text()
            skintextArr = skintext.split("/")
            champ["Skins"][skinname] = {}
            if len(skintextArr) == 1:
                champ["Skins"][skinname]["Date added"] = skintextArr[0].strip()
            else:
                champ["Skins"][skinname]["Cost"] = skintextArr[0].strip()
                champ["Skins"][skinname]["Date added"] = skintextArr[1].strip()
            champ["Skins"][skinname]["Picture link"] = skin(".thumb .image img").attr.src

    p = PyQuery("http://leagueoflegends.wikia.com/wiki/" + champKey + "/Background")

    for i in p("#mw-content-text > center:first-of-type").items():
        print(i.text())
        champ["Lore"] += i.text() + "\n"

    for i in p("#mw-content-text > p:first-of-type").items():
        print(i.text())
        champ["Lore"] += i.text()


with open("MasterCatalog.txt","w") as f:
    json.dump(champDict,f)
