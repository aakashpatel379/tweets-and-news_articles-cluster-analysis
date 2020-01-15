import csv
import os
import json
import glob
import sys
from pyspark import SparkContext, SparkConf

twitter_dir = "Tweet_JSON"
article_dir = "Articles_Export"
all_data = []
# words list
words = ["oil", "vehicle", "university", "dalhousie", "expensive", "good school",
         "dalhousie", "expensive", "good school", "good schools", "bad school", "bad schools", "poor school",
         "poor schools", "population", "bus", "buses", "agriculture", "economy"]
data_dict = {"oil": 0, "vehicle": 0, "university": 0, "dalhousie": 0, "expensive": 0, "good school": 0, "dalhousie": 0,
                 "expensive": 0, "good school": 0, "good schools": 0, "bad school": 0, "bad schools": 0, "poor school": 0,
                 "poor schools": 0, "population": 0, "bus": 0, "buses": 0, "agriculture": 0, "economy": 0}


def processTwitterData(path):
    searchfilepath = path + "\\" + "clean_search.json"
    streamfilepath = path + "\\" + "clean_stream.json"
    for line in open(searchfilepath, "r"):
        searchdata = json.loads(line)
        if searchdata['Sr_No'] == "Sr_No":
            continue
        all_data.append(searchdata["Tweet"])

    for line in open(streamfilepath, "r"):
        streamdata = json.loads(line)
        if streamdata['Sr_No'] == "Sr_No":
            continue
        all_data.append(streamdata["Tweet"])
    print("Twitter data extracted!")
    print(len(all_data))


def processArticleData(path):
    filelist = os.listdir(path)
    for filename in filelist:
        subpath = path + "\\" + filename
        article_file = open(subpath, "r")
        text = article_file.read()
        all_data.append(text)
        article_file.close()

    print("Articles extracted!")
    print(len(all_data))


if os.path.exists(twitter_dir) & os.path.exists(article_dir):
    path = os.getcwd()
    path = path + "\\" + twitter_dir
    processTwitterData(path)
    path = os.getcwd()
    path = path + "\\" + article_dir
    processArticleData(path)
    outfile = open("all_data.csv", "w+", newline='', encoding="utf-8")
    outfile = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for record in all_data:
        outfile.writerow([record])


else:
    print("Export Directory missing")
    print("Ensure files have been executed in sequence:")
    print("1. Twitter Search")
    print("2. Twitter Stream")
    print("3. Article Extractor")
    print("4. JSON Utility")
