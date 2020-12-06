# %%
import shelve

data = shelve.open('data/srcData')
MIDs = data['MIDs']
uid_records = data['uid_records']

# %%
tm = {}
for mid in MIDs:
    tli = []
    for record in uid_records.items():
        uid = record[0]
        mids = record[1]
        # 如果看过，则把该用户添加到tli中
        if mid in mids:
            tli.append(uid)
    tm.update({mid: tli})

# %%
data['mid_records'] = tm
data.close()
