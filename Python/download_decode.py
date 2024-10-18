import sqlite3 # import library
import json # import library
import datetime # import library

def state(data): # function to extract state from JSON data and convert it to a readable status
    convertState={0:"In Progress",1:"Complete",3:"Stopped",4:"Paused"} # dictionary
    return convertState[json.loads(data)['state']] # extracts the value associated to the name "state" in the JSON data, and uses that as a key to access the dictionary

def convertTime(t): # converts Firefox PRTime to human readable time
    return datetime.datetime.fromtimestamp(int(t)/1000).strftime('%Y-%m-%d %H:%M:%S')+' UTC'
    
def endTime(data): # function to extract the endTime from JSON data
    return convertTime(json.loads(data)['endTime']) # calls converTime using the JSON value extracted to get human readable date/time

def fileSize(data): # function to extract fileSize from JSON data.
    return "{:.2f} MB".format(json.loads(data)['fileSize']/1024/1024) # converts to MB and rounds to 2nd place after decimal

connection=sqlite3.connect("places.sqlite") # connect to the sqlite file
connection.create_function("state",1,state) # create SQLite function called state that takes 1 parameter, and calls Python function called state
connection.create_function("endTime",1,endTime) # create SQLite function called endTime that takes 1 parameter, and calls Python function called endTime
connection.create_function("fileSize",1,fileSize)# create SQLite function called fileSize that takes 1 parameter, and calls Python function called fileSize
cursor=connection.cursor() # create a cursor

recordsJSON=cursor.execute('select id, place_id, state(content), endTime(content), fileSize(content) from moz_annos where id=20 or id=23') # get record 20, field content - contains JSON
for record in recordsJSON: # loops through the hits
    print ("id: {}, place_id: {}, state: {}, end time: {}, file size: {}".format(record[0],record[1],record[2],record[3],record[4])) # format output

connection.close()
