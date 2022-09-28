What does this tool do? (<br>)
Helps you provision users to the Snyk platform at scale

How does this tool work? (<br>)
Utilizes the [Snyk API](https://snyk.docs.apiary.io/#reference/organizations/provision-user/provision-a-user-to-the-organization) to provision users declared in a membership file

How do I use it? (<br>)
1. Generate a [membership file](https://github.com/snyk-labs/snyk-user-sync-tool#membership-file-format)(option 1, User-based), ATM this tool does not include a utility to generate this file so you will have to create it yourself

2. Set an environment variable for your Snyk token (<br>)
`export SNYK_TOKEN=YOUR_TOKEN_HERE`

3. Call the app and declare the path to your membership file (<br>)
`python3 app/app.py --file=PATH_TO_YOUR_FILE` 