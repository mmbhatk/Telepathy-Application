import sqlite3
con = sqlite3.connect("Telepathyapp.db")

crsr = con.cursor()

com = """CREATE TABLE answers (    
ID INTEGER,  
ans VARCHAR(1000));"""

# com = """DROP TABLE answers;"""

crsr.execute(com)
