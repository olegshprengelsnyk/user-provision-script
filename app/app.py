import sys
import getopt
from functions.provision import provision
from functions.convertMembershipFile import convertMembershipFile


#this is the string that is returned if the user asks for help or doesnt pass valid args
helpString = "This script will provision new users according to the roles within a membership file, Supported format is user-based 1 documented here(https://github.com/snyk-labs/snyk-user-sync-tool#membership-file-format)\n "

#allows user to pass in file path, if file is not present then print helpstring
try:
    opts = getopt.getopt(sys.argv[1:], "f", ["file="])
except:
    print(helpString)


# write file path to membershipFile
membershipFile = open(opts[0][0][1], 'r')

#convert membership file to json
membershipFile = convertMembershipFile(membershipFile.read())

#provision
provision(membershipFile)
# membershipFile.close()
