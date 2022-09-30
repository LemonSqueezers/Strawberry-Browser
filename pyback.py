


import urllib.request
print("Strawberry Backend System 1.0 \n")
import sys






infinity = float("inf")
with urllib.request.urlopen("http://" + sys.argv[1]) as f: # TODO: no https!
    body = f.read()
    decoded_body = body.decode("utf-8")
    print(decoded_body[:32849])


