# Amazon AWS based Tweet Counter

This pipeline tool is launched through an Amazon EC2 instance to gather and perform live analysis on tweet content. It uses Apache Storm, Amazon EC2, Python, Twitter API, Streamparse, Postgres, PsycoPG, and Tweepy.

The pipeline has the following components, which are built from the files in Table 1:

1. A spout connected to the Twitter streaming API, that pulls tweets and emits them to the parse bolt.
2. A parse-tweet-bolt, that parses the tweets emitted by the spout, and extracts individual words out of the received tweet text.
3. A Postgres database called **tcount**, with a table called **tweetwordcount**.
3. A count-bolt, that counts the number of words emitted by the tweet-parse bolt, and updates the total counts for each word in the Postgres table
<br><br>

| Name of the program | Location | Description |  
|---------------------|----------|-------------|  
| tweets.py | /tweetwordcount/src/spouts/ | tweet-spout |  
| parse.py | /tweetwordcount/src/bolts/ | parse-tweet-bolt |  
| wordcount.py | /tweetwordcount/src/bolts | count-bolt |  
| Twittercredentials.py | [top level] | Twitter API Keys (**excluded**) |  
| tweetwordcount.clj | /tweetwordcount/topologies/ | Topology for the application |  


When credentials are entered, the program finalresults.py can be run from the command line to return the number of occurrences of one word if added as an argument, or of all words in the stream (for 1 minute).

The histogram program- also run from the command line, takes two arguments, a min and max, and returns all words and their counts with total occurrences in the provided limits.
