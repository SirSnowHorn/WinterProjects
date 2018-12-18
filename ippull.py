#Utility to pull Ips from a text file and order them by network, removing duplicates.
#Usage ./ippull.py [textfile]
import sys
from ipaddress import IPv4Address as ipv4
args = sys.argv
fileName = args[1]

ips = []

#Add regex to check each line for IPs
with open(fileName, 'r') as file:
        for line in file:
                if line[:-1] in ips: #We use [:-1] to get rid of newlines..
                        pass
                else:
                        ips.append(int(ipv4(line[:-1]))) #Creates number representation
        ips.sort() #Sort our completed list.
                        
def printIPS(list):
        for i in list:
                print(str(ipv4(i)))
                
#Add additional utilities later.
printIPS(ips)

#IDEA: Use MindMax database to look up the IP OR use WHOIS to find its location, then sort by location if prompted.
