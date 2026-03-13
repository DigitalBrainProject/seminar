import urllib.request
import re

html = urllib.request.urlopen("https://www.youtube.com/@kennakae2779").read().decode("utf-8")
matches = re.findall(r'<link rel="canonical" href="(.*?)"', html)
if matches:
    print(matches[0])
else:
    print("Not found")
