import os
import json
import requests
import time

#this function will take in a membershipfile containing orgs and and usernames in plain text and convert them to ID's
def convertMembershipFile(membershipFile):
    #convert json and get orgMapping
    orgMapping = {}
    for page in range(10):
        orgMapping.update(getOrgMapping(page))
        print("Getting orgs")
        time.sleep(1)
    

    membershipFile = json.loads(membershipFile)
    #replace each org in member to org ID
    for member in membershipFile:
        member["org"] = orgMapping[member["org"]]

    return membershipFile



#returns object that maps org names to org ids
def getOrgMapping(page):
    #snyk token
    snykToken = os.getenv('SNYK_TOKEN')
    groupId = os.getenv('GROUP_ID')
    counter = 0

    #request data
    headers = {
        "Content-type" : "application/json; charset=utf-8",
        "Authorization" : "token {}".format(snykToken)
    }
    #request logged as response
    response = requests.get(
        url='https://api.snyk.io/api/v1/group/{}/orgs?page={}'.format(groupId, page),
        headers=headers,
        )

    orgs = response.json()["orgs"]
    orgMapping = {}


    for org in orgs:
        orgMapping[org["name"]] = org["id"]

    return orgMapping


