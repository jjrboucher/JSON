import sqlite3 # import library

connection=sqlite3.connect("places.sqlite") # connect to the sqlite file
cursor=connection.cursor() # create a cursor
records=cursor.execute("select * from moz_annos") # execute sqlite statement

print ("Here are all the downloads")
print ("--------------------------")
for record in records:
    print (record)
    
print ("\nHere is the field 'content' from record 20")
print ("------------------------------------------")
record20=cursor.execute("select content from moz_annos where id=20")
for field in record20:
    print (field)

connection.close()
