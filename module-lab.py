#import the modules we need to interact with json and print the results

import json
#import pprint

#Open our json file as object f and then load into object myjson
#using the json module. 

with open('luke.json') as f:
	myjson = json.load(f)

#now print the result using the print() command

print(myjson)

#to print a much prettier version of our data, we can use pretty print
#also called pprint. To use pprint, uncomment the import pprint statement
#at the top of this program.  Then comment out the print line above and
#uncomment the pprint command below:

#pprint.pprint(myjson)
