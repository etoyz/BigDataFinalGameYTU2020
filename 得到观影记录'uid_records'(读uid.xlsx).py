# %%
import pandas as pd

df = pd.read_excel('data/uid.xlsx')
UIDs = df[df.columns[0]]  # 电影相似度
MIDs = df[df.columns[1]]
# %%
id_wrecord = []  # 每个用户的观影记录
j = 0
id_wrecord.append([])
for i in range(len(UIDs) - 1):
    if UIDs[i] == UIDs[i + 1]:
        id_wrecord[j].append(MIDs[i])
    else:
        id_wrecord[j].append(MIDs[i])
        id_wrecord.append([])
        j = j + 1
id_wrecord[j].append(MIDs[i + 1])  # 补最后一个用户的最后一次观看的电影代号
# %%
UIDs = list(UIDs)
UIDs = set(UIDs)

# %%
uid_records = {}
i = 0
for uid in UIDs:
    uid_records.update({uid: id_wrecord[i]})
    i += 1

# %%
import shelve

data = shelve.open('data/srcData')
data['uid_records'] = uid_records
data.close()
