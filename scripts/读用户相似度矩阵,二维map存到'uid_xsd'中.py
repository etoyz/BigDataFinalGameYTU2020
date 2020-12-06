# %%
import pandas as pd
import shelve

df_xsd = pd.read_excel('../data/用户相似度矩阵.xlsx')
UIDs = shelve.open('../data/srcData')['UIDs']
# %%
tm1 = {}
x = 0
for uidx in UIDs:
    tm2 = {}
    y = 0
    for uidy in UIDs:
        xsdt = df_xsd[df_xsd.columns[y]][x]
        y += 1
        tm2.update({uidy: xsdt})
    tm1.update({uidx: tm2})
    x += 1

# %%

data = shelve.open('../data/srcData')
data['uid_xsd'] = tm1
data.close()
