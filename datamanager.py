import os
import json
import re
import shortuuid # instead of uuid for url-safe uuids
from pandas import read_html
from flask import session

def docList(user):
    if os.path.exists('data/_userdocs.json'):
        with open('data/_userdocs.json', 'r') as f:
            userData = json.load(f)
        result = {}
        if user in userData:
            result = userData[user]
        return result
    return {}

def createDoc(content): # param content should already be parsed into html with marko
    contentuuid = shortuuid.uuid()
    fileName = contentuuid + ".html"
    if os.path.exists(f"data/{fileName}"):
        return False
    with open(f"data/{fileName}", "w") as f:
        f.write(content)
    newDocLog(contentuuid)
    return contentuuid

# html tag cleaner. credit c24b. < and > are not concerns in lecture transcript as transcriptions do not have these
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def newDocLog(contentuuid):
    with open('data/_userdocs.json', 'r') as f:
        userData = json.load(f)
    user = session["username"]
    if user not in userData:
        userData[user] = {}
    with open(f"data/{contentuuid}.html", "r") as f:
        firstLine = cleanhtml(f.readline())
    userData[user][contentuuid] = firstLine
    with open(f"data/_userdocs.json", "w") as f:
        json.dump(userData, f)

def getDoc(contentuuid):
    user = session['username']
    with open('data/_userdocs.json', 'r') as f:
        userData = json.load(f)
    userDocList = userData[user]
    if contentuuid not in userDocList:
        return False
    with open(f'data/{contentuuid}.html', 'r', encoding='utf-8') as f:
        doc = f.read()
    return doc
    
def editTitle(newTitle, docID):
    return 200

def deleteDoc(docID):
    user = session['username']
    with open('data/_userdocs.json', 'r') as f:
        userData = json.load(f)
    userDocList = userData[user]
    try:
        userDocList = userDocList.pop(docID)
        with open(f"data/_userdocs.json", "w") as f:
            json.dump(userData, f)
        os.remove(f"data/{docID}.html")
        return True
    except:
        return False