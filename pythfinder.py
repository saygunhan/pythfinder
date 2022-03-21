import requests
import argparse

domain=''
wordlist=''
subdomain=''
flen = ''
fres = ''
words = []

parser= argparse.ArgumentParser(description='directory buster')
parser.add_argument('-u','--url'   , required=False, type=str, metavar='' , help='url "example.com"')
parser.add_argument('-w','--wordlist' , type=str, metavar='', help='wordlist absolute path "/usr/share/wordlists/directory_list.txt"')
parser.add_argument('-s','--subdomain',required=False, type=str,  metavar='', help='type "enable"')
parser.add_argument('-fl','--flen',required=False, type=str,  metavar='', help='filter the response by content length"')
#parser.add_argument('-fr','--fres',required=False, type=str,  metavar='', help='filter the response by response code"')
args = parser.parse_args()
def appender(wordlist):
  file1 = open('{}'.format(wordlist), 'r')
  Lines = file1.readlines()
  for line in Lines:
   words.append(line.strip())


def dir_buster(url):
  for payload in words:
   try:
    response = requests.get("http://{}/{}".format(url,payload))
    if response.status_code in range (200,300):
     print("/{}".format(payload),response.status_code,)

   except:
    response = requests.get("https://{}/{}".format(url,payload))
 
    if response.status_code == 200:
     print("/{}".format(payload),response.status_code)
  

def sub_finder(url):
 for payload in words:
  sub_response = requests.get("https://{}.{}".format(payload,url))
  if args.flen is not None:  
    if len(sub_response.content) != int(args.flen):
     print(sub_response.status_code,payload,len(sub_response.content))
  else:
    print(sub_response.status_code,payload,len(sub_response.content)) 
   











if args.wordlist:
  appender(args.wordlist)
if args.subdomain is None:
  dir_buster(args.url)
if args.subdomain:
  sub_finder(args.url)



  
 
  

  
  
