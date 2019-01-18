import requests
import json
import pprint

url="https://swapi.co/api/people/1"

#request data from Star Wars API
urlresponse = requests.get(url) 

#uncomment this to view the response status code
print("Status Code:",urlresponse.status_code,"\n")

#parse response as json so we can address individual fields
myjsonresponse=json.loads(urlresponse.content) 

#print formatted JSON response
print("JSON Response:\n")
pprint.pprint(myjsonresponse)

#print a blank line after JSON result
print("\n")

#print name
print("Name:",myjsonresponse['name'],"\n")  

#print gender
print("Gender:",myjsonresponse['gender'],"\n")  

#print question
print("Is the person taller than 175cm?")

#convert height to integer - response is string, before we compare it
#we need to convert it to an integer
intheight=int(myjsonresponse['height'])
print(intheight > 175)
