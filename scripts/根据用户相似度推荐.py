# %%
import shelve

data = shelve.open('../data/srcData')
uid_xsd = data['uid_xsd_sorted']
UIDs = data['UIDs']
uid_records = data['uid_records']
_mid_map = data['mid_map']


def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


# %%
k = 240

result = {}
jd = tt = 0
for uid in UIDs:
    mid_map = _mid_map.copy()
    uids_sim = uid_xsd[uid]
    for uid_sim in uids_sim.items():
        for mid_watched in uid_records[uid_sim[0]]:
            value = mid_map[mid_watched] + uid_sim[1]
            mid_map.update({mid_watched: value})

    mid_map_ranked = sort_by_values(mid_map)

    result.update({uid: mid_map_ranked})

    # 进度条相关
    print('\r--progressing...\t' + str(jd) + "%", end='')
    tt += 1
    if tt == int(len(UIDs) / 100 + 1):
        jd += 1
        tt = 0

data = shelve.open('../data/recommend')
data['uid_only'] = result
data.close()
print('--progressing...\t100%\tok')
