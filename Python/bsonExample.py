import bson # imports bson library
import json

jsonData={"team":"Ottawa Senators"} #simple JSON data - which in Python we see is a dictionary

bsonData=bson.dumps(jsonData) # convert it to bson

print("{}\nBecomes\n{}".format(jsonData,bsonData)) # print it out

backToJSON=bson.loads(bsonData) # convert from bson back to json

print ("Back to JSON: {}".format(backToJSON)) # print it out
