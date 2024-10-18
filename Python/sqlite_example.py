import sqlite3 # import library

connection=sqlite3.connect("places.sqlite") # connect to the sqlite file
cursor=connection.cursor() # create a cursor
records=cursor.execute("select * from moz_places where id<50") # execute sqlite statement

for record in records: # loop through results
    print (record) # print each result
