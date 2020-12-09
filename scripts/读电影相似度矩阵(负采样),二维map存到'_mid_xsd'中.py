# %%
import pandas as pd

df_xsd = pd.read_excel('../data/电影相似度矩阵(负采样).xlsx')
df_mids = pd.read_excel('../data/midSort.xlsx')
# %%
tm1 = {}
x = 0
for midx in df_mids['MID']:
    tm2 = {}
    y = 0
    for midy in df_mids['MID']:
        xsdt = df_xsd[df_xsd.columns[y]][x]
        y += 1
        tm2.update({midy: xsdt})
    tm1.update({midx: tm2})
    x += 1

# %%
import shelve

data = shelve.open('../data/srcData')
data['_mid_xsd'] = tm1
data.close()
