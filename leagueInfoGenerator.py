import requests
import re
import pyquery
import urllib
import praw
import random
import pudb
import json

PyQuery = pyquery.PyQuery

listOfChampions = []
listOfAbilities = []
listOfLore = []
listOfSkinsv1 = []
listOfSkins = []
listOfItems = []
TaricQuotes = []

p2 = PyQuery("http://leagueoflegends.wikia.com/wiki/Champion")

with open ("championList.txt","w") as f:
    for i in p2.items("li[style='display:inline-block;width:10em;'] > div[class='character_icon']"):
        print(i.attr("data-character"))
        listOfChampions.append(i.attr("data-character"))
        f.write(i.attr("data-character") + "#####")

#pu.db
with open("Skinlist.txt","w") as f:
    for x in listOfChampions:
            ptemp = PyQuery("http://leagueoflegends.wikia.com/wiki/" \
                            + x + "/Skins")
            tempSkinsArray = []
            for j in ptemp.items("div[class='wikia-gallery-item']"):
                shottest = j("div[class='wikia-gallery-item'] > div >" \
                             " div[class='gallery-image-wrapper accent']" \
                             ).attr("id")
                if "Screenshot" not in shottest and shottest != "Jpg" and \
                   "_-" not in shottest:
                    SkinArrayx2 = []
                    interim = j("div[class='wikia-gallery-item'] > " \
                                "div[class='lightbox-caption']").contents()
                    skinStr=""
                    for k in interim:
                        if "<" not in str(k):
                            skinStr = str(k).replace("\n","")
                            break
                    if skinStr=="":
                        print("blank str")
                        skinStr = j("div[class='wikia-gallery-item'] > " \
                                "div[class='lightbox-caption'] >"
                                "a[rel='nofollow']").text()
                    print("skinstr = " + skinStr)

                    restInfo = j("div[class='wikia-gallery-item'] > "
                                "div[class='lightbox-caption']").text()
                    restInfo = restInfo.replace(skinStr,"")
                    print("restinfo =" + restInfo)

                    SkinArrayx2.append(skinStr.strip())
                    newurl = "http://leagueoflegends.wikia.com"
                    newurl += j("div[class='wikia-gallery-item'] > div >" \
                                " div[class='gallery-image-wrapper accent']" \
                                " > a").attr("href")
                    ptemp2 = PyQuery(newurl)
                    skinlink = ptemp2("div[class='fullImageLink'] > a").attr("h" \
                                                                             "ref")
                    SkinArrayx2.append(skinlink)
                    skinfo = re.split("/",restInfo)
                    print("skinfo = " + str(skinfo))
                    for i in skinfo:
                        SkinArrayx2.append(i.strip())
                    for i in SkinArrayx2:
                        print(i)
                        f.write(i + "xxDELIM1xx")
                    tempSkinsArray.append(SkinArrayx2)
                    f.write("xxDELIM2xx")
            listOfSkinsv1.append(tempSkinsArray)
            f.write("xxDELIM3xx")

with open("abilities.txt","w") as f:
    for x in listOfChampions:
            try:
                tempAbilityArray = []
                tempInnate = []
                tempQ = []
                tempW = []
                tempE = []
                tempR = []

                ptemp = PyQuery("http://leagueoflegends.wikia.com/" + x +
                                "/Abilities")

                if not (ptemp("div[class='skill skill_in" \
                            "nate'] > div > div:first-child").attr("id")):
                    tempInnate.append(ptemp("div[class='skill skill_in" \
                                        "nate'] > div > div:first-child" \
                                        "> table:nth-child(2) > tr:first-child" \
                                        "> td:first-child > div > img").attr("" \
                                        "alt").replace(".27", "'").replace(".21", "!"))
                else:
                    tempInnate.append(ptemp("div[class='skill skill_in" \
                                            "nate'] > div > div:first-child"
                                            ).attr("id" \
                                            ).replace("_", " ") \
                                        .replace(".27", "'").replace(".21", "!"))
                tempInnate.append(ptemp("div[class='skill skill_in" \
                                                  "nate']").text())
                tempAbilityArray.append(tempInnate)
                tempQ.append(ptemp("div[class='skill skill_q" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempQ.append(ptemp("div[class='skill skill_q" \
                                                  "']").text())
                tempAbilityArray.append(tempQ)
                tempW.append(ptemp("div[class='skill skill_w" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempW.append(ptemp("div[class='skill skill_w" \
                                                  "']").text())
                tempAbilityArray.append(tempW)
                tempE.append(ptemp("div[class='skill skill_e" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempE.append(ptemp("div[class='skill skill_e" \
                                                  "']").text())
                tempAbilityArray.append(tempE)
                tempR.append(ptemp("div[class='skill skill_r" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempR.append(ptemp("div[class='skill skill_r" \
                                                  "']").text())
                tempAbilityArray.append(tempR)
                listOfAbilities.append(tempAbilityArray)
                for i in listOfAbilities[len(listOfAbilities)-1]:
                        print(i[0])
                        f.write(i[0] + "xxDELIM1xx")
                        print(i[1])
                        f.write(i[1] + "xxDELIM2xx")
                f.write("xxDELIM3xx")
            except urllib.error.HTTPError:
                tempAbilityArray = []
                tempInnate = []
                tempQ = []
                tempW = []
                tempE = []
                tempR = []

                ptemp = PyQuery("http://leagueoflegends.wikia.com/" + x)

                if not (ptemp("div[class='skill skill_in" \
                            "nate'] > div > div:first-child").attr("id")):
                    tempInnate.append(ptemp("div[class='skill skill_in" \
                                        "nate'] > div > div:first-child" \
                                        "> table:nth-child(2) > tr:first-child" \
                                        "> td:first-child > div > img").attr("" \
                                        "alt").replace(".27", "'").replace(".21", "!"))
                else:
                    tempInnate.append(ptemp("div[class='skill skill_in" \
                                            "nate'] > div > div:first-child" \
                                            ).attr("id" \
                                            ).replace("_", " ") \
                                      .replace(".27", "'").replace(".21", "!"))
                tempInnate.append(ptemp("div[class='skill skill_in" \
                                                  "nate']").text())
                tempAbilityArray.append(tempInnate)
                tempQ.append(ptemp("div[class='skill skill_q" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempQ.append(ptemp("div[class='skill skill_q" \
                                                  "']").text())
                tempAbilityArray.append(tempQ)
                tempW.append(ptemp("div[class='skill skill_w" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempW.append(ptemp("div[class='skill skill_w" \
                                                  "']").text())
                tempAbilityArray.append(tempW)
                tempE.append(ptemp("div[class='skill skill_e" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempE.append(ptemp("div[class='skill skill_e" \
                                                  "']").text())
                tempAbilityArray.append(tempE)
                tempR.append(ptemp("div[class='skill skill_r" \
                                   "'] > div > div:first-child").attr("id" \
                                    ).replace("_", " ") \
                             .replace(".27", "'").replace(".21", "!"))
                tempR.append(ptemp("div[class='skill skill_r" \
                                                  "']").text())
                tempAbilityArray.append(tempR)
                listOfAbilities.append(tempAbilityArray)
                for i in listOfAbilities[len(listOfAbilities)-1]:
                        print(i[0])
                        f.write(i[0] + "xxDELIM1xx")
                        print(i[1])
                        f.write(i[1] + "xxDELIM2xx")
                f.write("xxDELIM3xx")
with open("Lore.txt","w") as f:
    for x in listOfChampions:
            ptemp = PyQuery("http://leagueoflegends.wikia.com/wiki/" \
                            + x + "/Background")
            listOfLore.append(ptemp("center").text() + "\n" \
                              + "\n" + ptemp("center + p").text())
            print(listOfLore[len(listOfLore)-1])
            f.write(listOfLore[len(listOfLore)-1] + "#####")
        
with open ("Itemlist.txt", "w") as f:
    p3 = PyQuery("http://leagueoflegends.wikia.com/wiki/Template:Items/Standard")

    for x in p3.items("span[class='item-icon'] > a"):
        tempItems = []
        tempItems.append(x.attr("title").replace(".27", "'"))
        print(tempItems[0])
        tempItems.append("http://leagueoflegends.wikia.com" + x.attr("href"))
        print(tempItems[1])
        ptemp = PyQuery("http://leagueoflegends.wikia.com" + x.attr("href"))
        descStr = ""
        for i in ptemp.items("div[class*='pi-item pi-data']"):
            descStr += i.text()
            descStr += "\n"
        tempItems.append(descStr)
        print(tempItems[2])
        listOfItems.append(tempItems)
        f.write(tempItems[0] + "xxDELIM1xx")
        f.write(tempItems[2] + "xxDELIM2xx")

    p30 = PyQuery("http://leagueoflegends.wikia.com/wiki/Template:Items/Other")

    for x in p30.items("span[class='item-icon'] > a"):
        tempItems = []
        tempItems.append(x.attr("title").replace(".27", "'"))
        print(tempItems[0])
        tempItems.append("http://leagueoflegends.wikia.com" + x.attr("href"))
        print(tempItems[1])
        ptemp = PyQuery("http://leagueoflegends.wikia.com" + x.attr("href"))
        descStr = ""
        for i in ptemp.items("div[class*='pi-item pi-data']"):
            descStr += i.text()
            descStr += "\n"
        tempItems.append(descStr)
        print(tempItems[2])
        listOfItems.append(tempItems)
        f.write(tempItems[0] + "xxDELIM1xx")
        f.write(tempItems[2] + "xxDELIM2xx")
        
p4 = PyQuery("http://leagueoflegends.wikia.com/wiki/Taric/Quotes")

with open ("Taricquotes.txt", "w") as f:
    for x in p4.items("li"):
        if x.children("span a img[alt*='taunt']"):
            pass
        elif x.children("span a img[alt*='laugh']"):
            pass
        elif x.children("span a img[alt*='item']"):
            pass
        elif x.children("i"):
            print(x.text())
            if("Malphite" not in x.text()):
                TaricQuotes.append(x.text())
                f.write(x.text() + "#####")
        else:
            pass
