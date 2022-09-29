import json
import requests
import os
import time

#this function will take in a membership file and make the neccesary API calls to provision users
def provision(membershipFile):
    #convert json
    membershipFile = json.loads(str(membershipFile))

    for member in membershipFile:
        print(callProvisionApi(
            userEmail=member['userEmail'],
            role=member['role'],
            orgId=member['org']
            )
        )

        time.sleep(1)


#calls the provision api given a userEmail, role, and org
def callProvisionApi(userEmail: str, role: str, orgId: str):
    
    #snyk token
    snykToken = os.getenv('SNYK_TOKEN')
    
    #request data
    headers = {
        "Content-type" : "application/json; charset=utf-8",
        "Authorization" : "token {}".format(snykToken)
    }

    body = {
        "email" : userEmail,
        "role" : role.capitalize()
    }

    #request logged as response
    response = requests.post(
        url='https://api.snyk.io/api/v1/org/{}/provision'.format(orgId),
        headers=headers,
        json=body
        )
        
    print(orgId)
    

    return response.json()




    

