import urllib.request
print("Backend Testing UI for SPiral")
inp = input('URL: ')

with urllib.request.urlopen(inp) as f: # TODO: no https prefix! also no https
    body = f.read()
    decoded_body = body.decode("utf-8")
    print(decoded_body[:50006])
    print("The output has been saved  to disk")
    f = open("output.temp", "a")
    f.write(decoded_body)
    f.close()

