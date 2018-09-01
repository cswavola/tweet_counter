from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        cur = self.con.cursor()

        cur.execute("UPDATE Tweetwordcount SET count=count+1 WHERE word=%s", (word,))

        if cur.rowcount==0:
            cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES (%s,1)", (word,))

        self.conn.commit()

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.


        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
