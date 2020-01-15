import tweepy
import sys
import json
import csv
import re

consumerkey="opv5wVwdc8Q1Z65gAmqKWxsGu"
consumersecret="EsWgtxJlK08VgN4TNrZFpx9h4LACZG2YrkLZuCl4UDUQWYpa1Z"
accesstoken="1140653455763214337-711SafjU05GEzbwtcrJzsqPelHDMeL"
accesstokensecret="RMYM5wIjccSOpzpAUFGHSeiR96VuZSxI8c6HCdqczZfsQ"

auth =tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken,accesstokensecret)
api= tweepy.API(auth, wait_on_rate_limit=True)

listCanada=[status._json for status in tweepy.Cursor(api.search,  q="Canada").items(300)]
listCanadaVehicleSales =[status._json for status in tweepy.Cursor(api.search,  q="Canada vehicle sales").items(300)]
listCanadaEducation =[status._json for status in tweepy.Cursor(api.search,  q="Canada Education").items(300)]
listCanadaImport =[status._json for status in tweepy.Cursor(api.search,  q="Canada import").items(300)]
listCanadaExport =[status._json for status in tweepy.Cursor(api.search,  q="Canada export").items(300)]


search_results=[]
search_results = [json.dumps(t) for t in listCanada]

for t in listCanadaVehicleSales:
    search_results.append(json.dumps(t))
for t in listCanadaEducation:
    search_results.append(json.dumps(t))
for t in listCanadaImport:
    search_results.append(json.dumps(t))
for t in listCanadaExport:
    search_results.append(json.dumps(t))

clean_csv = open("clean_search.csv", "w+",newline='',encoding="utf-8")
clean_csv = csv.writer(clean_csv, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
clean_csv.writerow(['Sr_No', 'Name', 'Username', 'Follower_Count','Friends_Count','Tweet' ,'Time', 'Retweet_Count', 'Likes', 'Location'])

raw_csv = open("raw_search.csv", "w+", newline='',encoding="utf-8")
raw_csv = csv.writer(raw_csv, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
raw_csv.writerow(['Sr_No','Raw Tweet Response'])

def addRecord(count, name, screen_name, followers, friends_count, content, created_at, retweet_count, favorite_count,
              location, json_str):
    try:
        clean_csv.writerow(
        [count, name, screen_name, followers, friends_count, content, created_at, retweet_count, favorite_count,
         location])
        raw_csv.writerow([count, json_str])
        print("\nCount = " + str(count))

    except Exception as e:
        print(str(e))
        print("\nCount = " + str(count))
        raw_csv.writerow([count, json_str])

    finally:
        return(count+1)


def processRecord(json_str,content):
    location = json_str['user']['location']
    if (location is None):
        location = ""
    name = json_str['user']['name']
    screen_name = json_str['user']['screen_name']
    followers_count = json_str['user']['followers_count']
    friends_count = json_str['user']['friends_count']
    created_at = json_str['created_at']
    retweet_count = json_str['retweet_count']
    favorite_count = json_str['favorite_count']
    c = addRecord(count, name, screen_name, followers_count, friends_count, content, created_at,
          retweet_count, favorite_count, location, json_str)
    return c

count =1
for json_string in search_results:
    json_str = json.loads(json_string)
    try:
        content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['extended_tweet']['full_text'], flags=re.MULTILINE)
        content = content.encode('ascii', 'ignore').decode(
            'ascii')
        content = re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
        content.replace("\\u", "")
        # content = re.sub('\W+', ' ', content)
        count = processRecord(json_str, content)

    except:
        try:
            content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['retweeted_status']['extended_tweet']['full_text'],
                             flags=re.MULTILINE)
            content = content.encode('ascii', 'ignore').decode(
                'ascii')

            content = re.sub(r"[^.,'a-zA-Z0-9]+", " ", content)
            content.replace("\\u", "")
            count = processRecord(json_str, content)

        except:
            try:
                content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['quoted_status']['extended_tweet']['full_text'],
                                 flags=re.MULTILINE)
                content = content.encode('ascii', 'ignore').decode(
                    'ascii')  # https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
                content = re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
                count = processRecord(json_str, content)

            except:

                try:
                    content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['text'],
                                     flags=re.MULTILINE)
                    content = content.encode('ascii', 'ignore').decode(
                        'ascii')  # https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
                    content = re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
                    # content = re.sub('\W+', ' ', content)
                    count = processRecord(json_str, content)
                except Exception as e:
                    print(str(e))
                    pass

