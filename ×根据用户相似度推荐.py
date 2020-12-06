# %%
import shelve

data = shelve.open('data/srcData')
uid_records = data['uid_records']
mid_records = data['mid_records']
uid_xsd = data['uid_xsd_sorted']


def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


result_li = []
# %%
jd = 0
ii = 0
for record in mid_records.items():
    ii += 1
    if ii == int(len(mid_records) / 100):
        jd += 1
        ii = 0
        print("processing...\t" + str(jd), end='%\r')

    mid = record[0]
    uids = record[1]

    lit = []
    for uid in uids:
        lit.append(uid_xsd[uid])

    map_uid = {}
    for key in lit[0].keys():
        map_uid.update({key: 0})

    for u in lit:
        for item in map_uid.items():
            key = item[0]
            value = item[1] + u[key]
            map_uid.update({key: value})

    # 相似度排序后的列表
    map_uid_rank = sort_by_values(map_uid)
    # 取最相似的k个UID
    k = 130
    uid_similiest = []
    for t in map_uid_rank.items():
        uid_similiest.append(t[0])
        k -= 1
        if k == 0:
            break

    result_li.append(uid_similiest)
# %%
result_m = {}
i = 0
for mid in data['MIDs']:
    result_m.update({mid: result_li[i]})
    i += 1

# %%
data = shelve.open('data/recommend')
data['uid_only'] = result_m
data.close()
print("processing...\t100%")
print("结果已写入到data/recommend !!")
