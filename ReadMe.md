### Tweet Sentiment Semantics Analysis

#### About

This project first requires to collect tweets from a twitter developer account based on defined keywords. After collecting certain number of tweets using Search and Stream API of twitter, they are cleaned, transformed and stored. We also have News Articles raw data (.sgm files) provided, which is also operated upon for extraction of news articles' text. Entire Corpus composed of tweets and news articles is then clustered on MongoDB on EC2 instance of AWS Cloud services. In the last phase, MapReduce operation is performed on AWS Cloud using pyspark to find the frequency of predefined set of keywords (like oil, vehicle,university etc).

#### File Info

-Articles_Export: Directory containing news articles extracted.

-Tweet_JSON: Processed Tweets from Search and Stream twitter API.

-all_data.csv: Final CSV file to generate corpus from.

-AllDataExporter.py: Python Utility to generate entire text corpus from available data sources.

-ArticleExtractor.py: Python Utility program to extract articles in "Articles_Export" directory.

-clean_search.csv: CSV file to store Cleaned Tweets from Search Twitter API.

-clean_stream.csv: CSV file to store Stream Tweets from Stream Twitter API.

-final_count_file.txt: Output file from MapReduce operation.

-raw_search.csv: CSV file to store raw tweets collected from Search Twitter API.

-raw_stream.csv: CSV file to store raw tweets collected from Stream Twitter API.

-reut2-020.sgm and reut2-021: Input (.sgm) file for news corpus.

-spark.py: Python commands executed on Cloud.

-TwitterSearch.py: Program to collect tweets using Twitter Search API.

-TwitterStream.py: Program to collect tweets using Twitter Stream API.  

#### Cluster Setup

For cluster setup I have created EC2 instance in Amazon AWS as part of lab
curriculum.
Secondly, I installed apache spark on the instance for execution of mapreduce
programs and creating master slave configuration.
For maintaining database in mongo DB, I locally installed MongoDB into my
machine. I have also written a utility file which converts the cleaned data to json to
be imported in MongoDB collection.

#### Twitter Data Extraction and Transformation Procedure:

1. Created Twitter Developer account.

2. Created TwitterSearch python script to extract data from twitter.
- This file will generate clean file for Search data according to provided
keywords.
- I have extracted Name, Screen_Name, Followers Count, Friends count, Tweet,
Created at, Retweet Count, Favorite Count and Location
- I limited the tweets count till 1000.
- This file also generates Raw Response CSV file which can be used to extract
other information later.
-Cleaned file is written after applying regex commands to remove URL, Emojis,
Special characters. I did consider Comma, Apostrophe and Space for not to be
removed. They are not removed since they make sense for tweet interpretation and
have major impact on twitter interpretability on removal.

3. Created TwitterStream python script to extract streaming data from twitter.
- This file will generate cleaned file for streaming data in accordance to the
provided keywords.
- I have extracted all the same attributes from twitter stream responses as did with
Search python script.
-I manually limited the record to nearly 1000 tweets with the help of internal
counter.
- Cleaning approach is same as that used in Search.

#### News Article Data Extraction & Transformation:

1. To extract articles from provided .sgm files I created a python script named
ArticleExtractor.
- This file takes in the provided files from current directory and are cleaning to
derive articles from it one by one.
-It saves all the articles created in a new directory called “Articles_Export”.

2. Than I have created a JSON export utility
-This utility basically operates on the cleaned data extracted for twitter and
generates JSON files to be used for mongo import.
-These files are exported to a newly created “Tweet_JSON” directory.

#### Data Processing (MapReduce)

1. To be able to perform the MapReduce program I firstly created a .py script by name
AllDataExporter.
-This file basically gets data from all the files generated from Twitter and Article
python scripts.
-Its configured to expect data from same directory as created/managed by other
scripts.
-It generates the CSV file as output which basically contains all records generated
for the cluster.

2. This CSV file by name “all_data” is uploaded to configured AWS server using WinSCP
software.

3. Than I processed the all_data file on every record to calculate the word count for given
words/phrases. I have executed commands word processing commands on Ubuntu terminal
inside pyspark. For this I used commands available in spark.py file along with commands
to do mapreduce (specific to pyspark).

#### Screenshots

1. AWS Instance

<img src="/Screenshots/AWS_Instance.JPG" width="700" />

2. Mongo DB cluster

<img src="/Screenshots/Cluster_Mongo.JPG" width="700" />

3. EC2 Dashboard

<img src="/Screenshots/EC2_Dashboard.JPG" width="700" />

4. Spark Master Slave

<img src="/Screenshots/spark_master_slave.JPG" width="700" />

5. Word Count Output

<img src="/Screenshots/Word_Counts.JPG" width="500" />

6. Word Processing 1

<img src="/Screenshots/Word_Processing1.JPG" width="500" />

7. Word Processing 2

<img src="/Screenshots/WordProcessing2.JPG" width="500" />

8. Word Processing 3

<img src="/Screenshots/WordProcessing3.JPG" width="600" />


#### References

1. https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-tomultiline-json
2. https://stackoverflow.com/questions/33404752/removing-emojis-from-astring-in-python
3. https://stackoverflow.com/questions/33404752/removing-emojis-from-astring-in-python
4. https://stackoverflow.com/questions/11331982/how-to-remove-any-urlwithin-a-string-in-python?noredirect=1&lq=1
5. https://stackoverflow.com/questions/24002536/get-tweepy-search-results-asjson/26374664
6. https://pythonprogramming.altervista.org/how-to-get-all-the-file-in-adirectory/?doing_wp_cron=1562083155.3951699733734130859375
7. https://spark.apache.org/examples.html
8. http://docs.tweepy.org/en/v3.5.0/getting_started.html
9. https://www.tutorialkart.com/apache-spark/python-spark-shell-pysparkexample/
