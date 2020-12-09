import pandas as pd

df = pd.read_excel('data/train.xlsx')

MIDs = df['MID']
times = df['TIMESTAMP']

tm = {}
for uid, time in zip(MIDs, times):
    tm.update({uid: time})

df = pd.DataFrame({
    'MID': list(tm.keys()),
    'TIMESTAMP': list(tm.values())
})

df.to_excel('各电影最早放映时间.xlsx')
