import json
import re

strToRe = ""
quoteDict = {}

with open("Taricquotes.txt") as f:
    for line in f:
        strToRe += line;
quotes = strToRe.split("#####")

quoteDict["Quotes"] = quotes

with open("TaricQuoteJson.txt", "w") as f:
    json.dump(quoteDict,f)
