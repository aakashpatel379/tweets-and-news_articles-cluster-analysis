import json
import csv
import os

directory_name = "Tweet_JSON"
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

path = os.getcwd()
path = path + "\\" + directory_name + "\\"

csvsearch = open("clean_search.csv","r",encoding="utf-8")
csvstream = open("clean_stream.csv","r",encoding="utf-8")
jsonsearch = open(path+"clean_search.json", "w",encoding="utf-8")

fields = ['Sr_No', 'Name', 'Username', 'Follower_Count','Friends_Count','Tweet' ,'Time', 'Retweet_Count', 'Likes', 'Location']

readerObj = csv.DictReader(csvsearch, fields)

for record in readerObj:
    json.dump(record, jsonsearch)
    jsonsearch.write("\n")

readerObj = csv.DictReader(csvstream, fields)
jsonstream = open(path+"clean_stream.json", "w",encoding="utf-8")

for record in readerObj:
    json.dump(record, jsonstream)
    jsonstream.write("\n")

print("Cleaned Tweet JSON data exported sucessfully!")