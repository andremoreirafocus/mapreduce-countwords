Simple map reduce example that demonstrates how to count word occurrences in a a thousand text files

It requires python 2.7 or above

First run:
python .\extract.py

It will map all the words in all texts using the map function

The reduce function will count the occurrences of each word

a CSV is generated as a list of words and number of occurences of each word

stopwords.py is used to remove connection words like articles, advbers and prepositions.

Run as many instances of the client as possible to make it faster
python mincemeat.py -p changeme localhost

In this example, the client and the server runs at the same machine. To change it, replace the "localhost" parameter to the host where the server (name server is running)

This code has been derived from the course from PUC Minas on Big Data Architecture, which is part of a PG in Distributed Systems Architecture


