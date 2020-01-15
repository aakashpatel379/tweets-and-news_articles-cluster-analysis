import tweepy
from tweepy import StreamListener
import sys
import re
import csv
import json

consumerkey="opv5wVwdc8Q1Z65gAmqKWxsGu"
consumersecret="EsWgtxJlK08VgN4TNrZFpx9h4LACZG2YrkLZuCl4UDUQWYpa1Z"
accesstoken="1140653455763214337-711SafjU05GEzbwtcrJzsqPelHDMeL"
accesstokensecret="RMYM5wIjccSOpzpAUFGHSeiR96VuZSxI8c6HCdqczZfsQ"

#Authentication
auth=tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken,accesstokensecret)
api=tweepy.API(auth)


count=1
limit=1000

clean_csv = open("clean_stream.csv", "w+",newline='',encoding="utf-8")
clean_csv = csv.writer(clean_csv, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
clean_csv.writerow(['Sr_No', 'Name', 'Username', 'Follower_Count','Friends_Count','Tweet' ,'Time', 'Retweet_Count', 'Likes', 'Location'])

raw_csv = open("raw_stream.csv", "w+", newline='',encoding="utf-8")
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

class CustomListener(StreamListener):

    def on_data(self, status):
        global count
        if count <= limit:
            json_str = json.loads(status)
            try:
                content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['extended_tweet']['full_text'], flags=re.MULTILINE)
                content = content.encode('ascii', 'ignore').decode(
                    'ascii')
                content = re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
                content.replace("\\u", "")
                count = processRecord(json_str, content)

            except KeyboardInterrupt:
                print("Stopped")
                streamObject.disconnect()
                sys.exit()

            except:
                try:
                    content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['retweeted_status']['extended_tweet']['full_text'], flags=re.MULTILINE)
                    content = content.encode('ascii', 'ignore').decode(
                        'ascii')

                    content = re.sub(r"[^.,'a-zA-Z0-9]+", " ", content)
                    content.replace("\\u", "")
                    count = processRecord(json_str, content)

                except KeyboardInterrupt:
                    print("Stopped")
                    streamObject.disconnect()
                    sys.exit()

                except:
                    try:
                        content = re.sub(r' https?:\/\/.*[\r\n]*', '', json_str['quoted_status']['extended_tweet']['full_text'],
                                         flags=re.MULTILINE)
                        content= content.encode('ascii', 'ignore').decode('ascii')
                        content =re.sub(r"[^.,'A-Za-z0-9]+", ' ', content)
                        count= processRecord(json_str, content)

                    except Exception as e:
                        pass
        else:
            print("\nDone")
            streamObject.disconnect()
            sys.exit()


customListener = CustomListener()
streamObject = tweepy.Stream(auth=api.auth, listener=customListener)
streamObject.filter(track=["Canada","Canada vehicle sales", "Canadian Education", "Canadian Export", "Canadian import" ])

