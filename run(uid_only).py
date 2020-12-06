# %%
import shelve
import pandas as pd

data = shelve.open('data/srcData')
data2 = shelve.open('data/recommend')

to_predict = data['to_predict']
recommends_map = data2['uid_only']

k = 240
result = []
for it in to_predict:
    uid = it[0]
    mid = it[1]
    recommends = list(recommends_map[uid])[:k]
    if mid in recommends:
        result.append(1)
    else:
        result.append(0)

# %%
t = pd.DataFrame({
    'Pre': result
})

t.to_excel('result/2u.xlsx')

print("已写入到2u.xlsx！")
