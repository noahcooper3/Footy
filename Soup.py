import urllib2
import requests
from bs4 import BeautifulSoup
import flask
from flask import Flask, render_template



quote_page = 'https://scores.nbcsports.com/epl/scoreboard_daily.asp'
#quote_page = 'https://scores.nbcsports.com/epl/scoreboard_daily.asp?gameday=20181111'
page_response = requests.get(quote_page, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
textContent = []

paragraphs = page_content.find_all('div',attrs={"class":"shsScoreboardCol"})
textContent.append(paragraphs)

print("Today's Soccer Scores")

bigStr = "<script>function getScore() {document.getElementById('id01').innerHTML = document.getElementById(document.getElementById('selector').value).innerHTML;}</script>"

bigStr += "<h2>What game are you watching? "

bigStr += "<select id = 'selector'>"
for strName in textContent[0]:
    bigStr += "<option>"
    count = 0
    tempName = ""
    for i in range(len(str(strName))):
        if(str(strName)[i:i+6] == "title="):
            j = i+6
            count += 1
            while (str(strName)[j] != ">"):
                if(str(strName)[j] != '"'):
                    bigStr += str(strName)[j]
                    tempName += str(strName)[j]
                    print str(strName)[j],
                j += 1 
            print
            if (count == 1):
                bigStr += " vs. "
                tempName += " vs. "
        if (str(strName)[i] == "'"):
            bigStr += "</option>"
            bigStr += "<p style = 'display: none' id = '"+tempName+"'>"+str(strName)[i-2:i+1]+"</p>"
            bigStr += "<br />"
            print(str(strName)[i-2:i+1])

    bigStr += "<br/>--------------<br/><br/>"
    print("------")

bigStr += "</select></h2>"

bigStr += "<div id = 'id01'></div>"

bigStr += "What time are you at? <input id = 'scoreGoal' placeholder = 'minute marker'> <button onclick = 'getScore();'>Enter</button>" 




app = Flask(__name__)
@app.route("/")
def hello():
    return bigStr






