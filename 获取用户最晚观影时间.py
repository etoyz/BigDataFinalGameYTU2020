import pandas as pd

df = pd.read_excel('data/train.xlsx')

UIDs = df['UID']
times = df['TIMESTAMP']

tm = {}
for uid, time in zip(UIDs, times):
    tm.update({uid: time})

df = pd.DataFrame({
    'UID': list(tm.keys()),
    'TIMESTAMP': list(tm.values())
})

df.to_excel('各用户最晚观影时间.xlsx')
