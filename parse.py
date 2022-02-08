import pandas as pd
import os
import re

sheets = ["./data/" + w for w in os.listdir("data")]
all_tweets = []
for sheet in sheets:
	df = pd.read_csv(sheet,sep="	")
	data = df['tweet'].to_list()
	data = [re.sub(r'https:\/\/t.co\/[^\s]+','', d.replace("http://", "https://")) + '\n' for d in data if not d.startswith("RT")]
	print(f"{sheet}: {len(data)}")
	all_tweets.extend(data)

print(len(all_tweets))
with open("all_tweets.txt", "w+") as file:
	file.writelines(all_tweets)
print("FINISH")

