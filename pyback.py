import requests
print("Strawberry Backend System 0.2 Beta \n")
import sys
r = requests.get("http://" + sys.argv[1])

print(r.text)