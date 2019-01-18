import requests

#request web site
urlresponse = requests.get("https://www.ipchicken.com") 

#print response status code
print(urlresponse.status_code)

#print Headers
#print(urlresponse.headers)

#print Content
#print("Content:",urlresponse.content)

