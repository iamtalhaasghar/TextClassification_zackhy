import pandas as pd

df_fake = pd.read_csv("/tmp/fake.csv", sep='}', names=['id', 'content', 'class'])
df_true = pd.read_csv("/tmp/real.csv", sep='}', names=['id', 'content', 'class'])

df_fake["label"] = 0
df_true["label"] = 1

df_merge = pd.concat([df_fake, df_true], axis =0 )
df = df_merge.drop(["id", 'class'], axis = 1)
df.to_csv("./data/tweets.csv", index=False)

