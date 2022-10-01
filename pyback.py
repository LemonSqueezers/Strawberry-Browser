


import urllib.request
print("Strawberry Backend System 0.1 Beta \n")
import sys








with urllib.request.urlopen("http://" + sys.argv[1]) as f: # TODO: no https!
    body = f.read()
    decoded_body = body.decode("utf-8")
    print(decoded_body[:32849])


