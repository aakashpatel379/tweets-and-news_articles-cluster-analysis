import os

def extractor(content):
    mainsplit = content.split("<TEXT>")
    for i in range(len(mainsplit)):
        if "</TEXT>" in str(mainsplit[i]):
            secondsplit = mainsplit[i].split("</TEXT>")
            for j in range(len(secondsplit)):
                if "<BODY>" in str(secondsplit[j]):
                    results.append(secondsplit[j])


results = []
file1 = open("reut2-020.sgm", "r")
content = (file1.read())
extractor(content)
file2 = open("reut2-021.sgm", "r")
content = (file2.read())
extractor(content)
print("Count: " + str(len(results)))
directory_name = "Articles_Export"
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

path = os.getcwd()
path = path + "\\" + directory_name
for i in range((len(results))):
    f = open(path + "\\article" + str(i + 1) + ".txt", "w+")
    f.write(results[i])
print("Article data exported!")
