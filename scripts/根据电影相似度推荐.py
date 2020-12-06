import shelve

data = shelve.open('../data/srcData')
uid_records = data['uid_records']
xsd_2map = data['mid_xsd_sorted']

result_li = []


def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


jd = tt = 0
for record in uid_records.items():
    uid = record[0]
    mids = record[1]

    lit = []
    for mid in mids:
        lit.append(xsd_2map[mid])

    map_mid = {}
    for key in lit[0].keys():
        map_mid.update({key: 0})

    for m in lit:
        for item in map_mid.items():
            key = item[0]
            value = item[1] + m[key]
            map_mid.update({key: value})

    # 相似度排序后的列表
    map_mid_rank = sort_by_values(map_mid)

    result_li.append(map_mid_rank)

    # 进度条相关
    print('\r--progressing...\t' + str(jd) + "%", end='')
    tt += 1
    if tt == int(len(uid_records.items()) / 100 + 1):
        jd += 1
        tt = 0
# %%
result_m = {}
i = 0
for uid in data['UIDs']:
    result_m.update({uid: result_li[i]})
    i += 1

# %%
data = shelve.open('../data/recommend')
data['mid_only'] = result_m
data.close()
print('\r--progressing...\t100%\tok')
