import csv
words = ["oil", "vehicle", "university", "dalhousie", "expensive", "good school",
         "dalhousie", "expensive", "good school", "good schools", "bad school", "bad schools", "poor school",
         "poor schools", "population", "bus", "buses", "agriculture", "economy"]
myfile = open("/home/ubuntu/DataAssignment2/all_data.csv","r",encoding="utf-8")
readCSV = csv.reader(myfile, delimiter=',')
result=[]
for row in readCSV:
    text = (row[0])
    for w in words:
        if w in text:
            count =text.count(w)
            for i in range(count):
                result.append(w)

