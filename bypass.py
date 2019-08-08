#Xractz
#IndoSec

import re
from requests import Session
print("ShortID Bypasser\n")
url = input("Link : ")

s = Session()

r = s.get(url).text
token = re.findall(r'<a href="/visit/(\d+)" rel="nofollow">', r)[0]

ori = s.get(f"https://zanbooredana.com/visit/{token}").text
link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ori)[0]

print(f"Bypassed : {link}")