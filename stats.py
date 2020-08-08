import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
sns.set_palette('pastel')
PATH = '/Users/Privat/Documents/*.csv'
files = glob.glob(PATH)

dfs = list()
for f in files:
    sheet = pd.read_csv(f)
    sheet.columns = ['band', 'song']
    dfs.append(sheet)

df = pd.concat(dfs, ignore_index=True)
df['band'] = df.band.str.lower()
df['band'] = df.band.str.replace('chill', 'chili')
df['band'].str.replace('the ', '')

df['song'] = df.song.str.replace("'", '')

plt.figure(figsize=(10,7))
sns.countplot(data=df, x=df.song, order=df.song.value_counts().index, orient='vertical')
plt.xticks(rotation=90)