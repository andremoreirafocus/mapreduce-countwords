#!/usr/bin/env python
import mincemeat
import glob
import csv
import stopwords 

text_files = glob.glob('textos\\*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))for file_name in text_files)
for key, value in source.items() :
    print (key)

def mapfn(k, v):
    print `map  ` + k
    from stopwords import allstopwords
    for line in v.splitlines():
        for word in line.split():
            if (word not in allstopwords):
                yield word, 1

def reducefn(k, v):
    print `reduce ` + k
    return sum(v)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("textos/RESULT.csv", "w"))
for k, v in results.items():
    w.writerow([k, v])
    