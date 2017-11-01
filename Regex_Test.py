#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import re
import requests
import pyquery
PyQuery = pyquery.PyQuery
p2 = PyQuery("http://leagueoflegends.wikia.com/wiki/List_of_champions")

listOfChampions = []
listOfSkinsv1 = []
listOfSkins = []

for i in p2.items("tr > td:first-child >" \
    "span[class='sortkey']:first-child"):
    print(i.text())
    if i.text() == "Gnar (Mega)":
        listOfChampions.append("Gnar")
    elif i.text() == "Gnar (Mini)":
        pass
    else:
        listOfChampions.append(i.text())
for x in listOfChampions:
        ptemp = PyQuery("http://leagueoflegends.wikia.com/wiki/" \
                        + x + "/Skins")
        tempSkinsArray = []
        for j in ptemp.items("div[class='wikia-gallery-item']"):
            shottest = j("div[class='wikia-gallery-item'] > div >" \
                         " div[class='gallery-image-wrapper accent']" \
                         ).attr("id")
            if "Screenshot" not in shottest and shottest != "Jpg" and \
               "Chroma" not in shottest:
                SkinArrayx2 = []
                skinStr = j("div[class='wikia-gallery-item'] > "
                            "div[class='lightbox-caption']").text()
                
                SkinArrayx2.append(skinStr)
                newurl = "http://leagueoflegends.wikia.com"
                newurl += j("div[class='wikia-gallery-item'] > div >" \
                            " div[class='gallery-image-wrapper accent']" \
                            " > a").attr("href")
                ptemp2 = PyQuery(newurl)
                skinlink = ptemp2("div[class='fullImageLink'] > a").attr("h" \
                                                                         "ref")
                SkinArrayx2.append(skinlink)
                for i in SkinArrayx2:
                    print(i)
                tempSkinsArray.append(SkinArrayx2)
        listOfSkinsv1.append(tempSkinsArray)
regex1 = re.compile(r"(\w+?\.?\s,?)+?(?=\d{3,4}\s)")
regex2 = re.compile(r"\d{3,4}")
regex3 = re.compile(r"\d{2}-\w{3,4}-\d{4}")
for x in listOfChampions:
    regex4 = re.compile(r".+?"+x)
    regex5 = re.compile(r"" + x + r"\s(.+?)/")
    regex6 = re.compile(r"Classic "+x)
    tempSkinsArray = []
    j = listOfSkinsv1[listOfChampions.index(x)]
    for i in j:
        temptempSkinsArray = []
        strToParse = i[0]
        print(strToParse)
        if strToParse.find("Urf the Manatee") == -1:
            if regex1.search(strToParse):
                temptempSkinsArray.append(regex1.search(strToParse).group(0))
                temptempSkinsArray.append(regex2.search(strToParse).group(0))
                if not regex3.search(strToParse):
                    temptempSkinsArray.append("Upcoming skin")
                else:
                    temptempSkinsArray.append(regex3.search(strToParse).group(0))
                temptempSkinsArray.append(i[1])
            elif regex6.search(strToParse):
                temptempSkinsArray.append(regex6.search(strToParse).group(0))
                temptempSkinsArray.append("Free")
                temptempSkinsArray.append(regex3.search(strToParse).group(0))
                temptempSkinsArray.append(i[1])
            else:
                temptempSkinsArray.append(regex4.search(strToParse).group(0))
                temptempSkinsArray.append(regex5.search(strToParse).group(1) \
                                          .rstrip())
                if not regex3.search(strToParse):
                    temptempSkinsArray.append("Upcoming skin")
                else:
                    temptempSkinsArray.append(regex3.search(strToParse).group(0))
                temptempSkinsArray.append(i[1])
        else:
            regex7 = re.compile(r"Urf the Manatee")
            regex8 = re.compile(r"Urf the Manatee(.+?)/")
            temptempSkinsArray.append(regex7.search(strToParse).group(0))
            temptempSkinsArray.append(regex8.search(strToParse).group(1) \
                                      .rstrip())
            temptempSkinsArray.append(regex3.search(strToParse).group(0))
            temptempSkinsArray.append(i[1])
        tempSkinsArray.append(temptempSkinsArray)
    listOfSkins.append(tempSkinsArray)
print(listOfSkins[listOfChampions.index("Malzahar")][0][0])
print(listOfSkins[listOfChampions.index("Malzahar")][0][1])
print(listOfSkins[listOfChampions.index("Malzahar")][0][2])
print(listOfSkins[listOfChampions.index("Malzahar")][0][3])
                
