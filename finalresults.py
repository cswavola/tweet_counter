final results

import sys
import psycopg2

count_input=len(sys.argv)

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if count_input < 3:
    if count_input==1:
        #return all words
        cur.execute("SELECT word, count FROM tweetwordcount ORDER BY word")


    if count_input==2:
        #return this word
        word=sys.argv[1]
        cur.execute("SELECT word, count FROM tweetwordcount WHERE word=%s", (word, ))



Else:
    print("Please enter only one word")
    exit()

conn.commit()
conn.close()
