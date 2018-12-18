'''
This program has several utility functions for retrieving information from Facebook.
usage: ./FacePwn -c [command] -k [keyword file] -h [prints out commands]
Good example: https://github.com/chenjr0719/Facebook-Page-Crawler/blob/master/facebook_page_crawler/facebook_page_crawler.py
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
import requests
import urllib
import bf4 #Beuatifulsoup
'''
Step 1: Search keywords to find a group like:
Step 2: CTRL + U to view source code.
Step 3: CTRL + F, search for entity_id . 
Step 4: We can now query this to find out who likes the crime group. https://www.facebook.com/search/str/[entity_id]/likers
Step 5: We can find individuals within an area specificed and then get their idea to repeat the process.
Step 6: Repeat the process above to find his ID. We now go to https://www.facebook.com/search/str/[entity_id]/groups to see what other groups he is in.
'''
token = ""
query = ""
r = requests.get("https://graph.facebook.com/search?access_token=" + token +  "&q=" + query + "&type=page")
