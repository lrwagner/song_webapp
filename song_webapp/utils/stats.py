import pandas as pd
import glob
import os


def format_date(datestr):
    
    year = datestr[-4:]
    day = datestr[:2]
    month = datestr[2:4]
    return f'{year}-{month}-{day}'


def get_sheets():
    PATH = 'data/*.csv'
    files = glob.glob(PATH)
    dfs = list()
    for f in files:
        sheet = pd.read_csv(f)
        sheet.columns = ['band', 'song']
        sheet['date'] = format_date(os.path.basename(f)[:-4])
        dfs.append(sheet)

    df = pd.concat(dfs, ignore_index=True)
    df['band'] = df.band.str.lower()
    df['band'] = df.band.str.replace('chill', 'chili')
    df['band'] = df['band'].str.replace('the ', '')
    df['song'] = df.song.str.strip()
    df['song'] = df.song.str.replace("'", '')

    return df