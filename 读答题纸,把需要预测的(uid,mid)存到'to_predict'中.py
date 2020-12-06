# %%
import pandas as pd

df = pd.read_excel('data/答题纸.xlsx')
UIDs = df[df.columns[0]]  # 电影相似度
MIDs = df[df.columns[1]]

# %%
# 需要预测的uid与mid
to_predict = []
k = 0
for u in UIDs:
    to_predict.append((u, MIDs[k]))
    k += 1

# %%
import shelve

data = shelve.open('data/srcData')
data['to_predict'] = to_predict
data.close()
