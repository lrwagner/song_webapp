import glob
import os
import re


PATH = '/Users/Privat/Documents/*.txt'
files = glob.glob(PATH)
pattern = r' ?- ?'

def replace_minus(line):
    pass

for idx, f in enumerate(files):
    with open(f, 'r') as txt:
        lines = txt.read()
        lines = re.sub(pattern, ',',lines)
        lines = 'band,song\n' + lines

    with open(f.replace('.txt', '.csv'), 'w') as csv:
        csv.write(lines)
