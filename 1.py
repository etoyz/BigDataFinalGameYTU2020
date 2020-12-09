# %%
import shelve
import pandas as pd

df = pd.read_excel('data/59.36.xlsx')
data = shelve.open('data/recommend')
_recs = data['_mid_only']

out = list(df['Pred(0/1)'])
uids = list(df['UID'])
mids = list(df['MID'])

k = 250


i = 0
for uid, mid in zip(uids, mids):
    _rect = list(_recs[uid].keys())
    _rec = _rect[:k]
    if mid in _rec:
        out[i] = 0
    i += 1


df = pd.DataFrame({
    'uid': uids,
    'out': out
})

df.to_excel('aaa.xlsx')
