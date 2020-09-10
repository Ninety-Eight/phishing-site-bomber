import requests
import os
import random
import string
import json
import sys
#put the POST request URL here. This can be obtained with the Firefox / Chrome network inspect and viewing the headers of the request you made when you entered something into the boxes and pressed enter

url = 'URL'
firstbox = 'email'
secondbox = 'pass'
#print messages to the user
print('Bomber seems to be working!')
print('Targeting: ' + url)
print('Ensure you have the IDs for the boxes properly set or this attack will be meaningless. Code 200 means successful connection btw :D')


while True:
    firstnames = json.loads(open('firstnames.json').read())
    lastnames = json.loads(open('lastnames.json').read())
    mailservers = json.loads(open('mailservers.json').read())
    breachedpasswords = json.loads(open('breachedpasswords.json').read())
    proxyfile = json.loads(open('proxies.json').read())
    useragents = json.loads(open('useragents.json').read())
    headers = {'User-Agent': random.choice(useragents)}
    proxychoice = random.choice(proxyfile)
    numbersaddon = ''.join(random.choice(string.digits))
    username = random.choice(firstnames) +'.' + random.choice(lastnames) + '@' + random.choice(mailservers)
    password = random.choice(breachedpasswords)
    proxyserver = random.choice(proxyfile)
    s = requests.Session()
    s.proxies = proxychoice
    r = requests.post(url, data={firstbox: username, secondbox: password}, headers=headers)
    print('Sending Fake Login Details: '+username+':'+password+" - HTTP Status code: "+str(r.status_code))
