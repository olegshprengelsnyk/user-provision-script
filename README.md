What does this tool do? <br>
Helps you provision users to the Snyk platform at scale, IMPORTANT!!this tool will only work if inviter and invitees are using SSO!!.

How does this tool work? <br>
Utilizes the [Snyk API](https://snyk.docs.apiary.io/#reference/organizations/provision-user/provision-a-user-to-the-organization) to provision users declared in a membership file

How do I use it? <br>
1. Generate a membership file of the format below. ATM this tool does not include a utility to generate this file so you will have to create it yourself.

```
[
    {
        "userEmail": "user1@email.com",
  	    "role": "roleID",
  	    "org": orgID"
    },
    {
  	    "userEmail": "user1@email.com",
  	    "role": "roleID2",
  	    "org": orgID"
    },
    {
  	    "userEmail": "user1@email.com",
  	    "role": "roleID2",
  	    "org": orgID2"
    },
    {
  	    "userEmail": "user2@email.com",
  	    "role": "roleID",
  	    "org": "orgID
   }
]
```

2. install pip3 dependencies <br>
`pip3 install -r requirements.txt `

3. Set an environment variable for your Snyk token <br>
`export SNYK_TOKEN=YOUR_TOKEN_HERE`

4. Set an enviroment variable for your Group ID <br>
`export GROUP_ID=YOUR_ID_HERE`

4. Call the app and declare the path to your membership file <br>
`python3 app/app.py --file=PATH_TO_YOUR_FILE`
