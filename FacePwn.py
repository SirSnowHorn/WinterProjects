'''
This program has several utility functions for retrieving information from Facebook.
usage: ./FacePwn -c [command] -k [keyword file] -h [prints out commands]
'''

import sys
args = sys.argv

#Will have an if conditional to run a function based on flags


'''
Command ideas:
- List of groups that match keywords
- List of members of groups that match keywords
- Above but can be locked onto a location like a State
- Most active groups with the keywords and their frequency
- Checks friends of group members to see if they are in any groups that match keywords
- Add additional ones

All of this will generate output. If file1.txt already exists, then file2.txt will be generated. so we need OS lib to search current dir.
'''
