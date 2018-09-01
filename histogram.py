#histogram.py

import sys
import psycopg2
min_limit=sys.argv[0]
max_limit=sys.argv[1]

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count FROM tweetwordcount WHERE count>=min_limit AND count<=min_limit ORDER BY word")
collect = cur.fetchall()
for word in collect:
    print word[0],":",word[1]

conn.commit()
conn.close()
