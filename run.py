# %%
import shelve
import pandas as pd

data = shelve.open('data/recommend')
data2 = shelve.open('data/srcData')
uid_only = data['uid_only']
mid_only = data['mid_only']
_mid_only = data['_mid_only']

to_predict = data2['to_predict']


# %%
def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


def sort_by_keys(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[0], reverse=False)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


def ss(mmap):
    nm = {}
    for it in mmap.items():
        u = it[0]
        rec = sort_by_values(it[1])
        nm.update({u: rec})
    return nm


def value_(map1, map2):
    newm = {}

    jd = tt = 0
    for item in map1.items():
        uid = item[0]
        dic = item[1]
        _dic = map2[item[0]]
        ndic = {}
        for mid in dic.keys():
            ndic.update({mid: dic[mid] - _dic[mid]})
        newm.update({uid: ndic})

        # 进度条相关
        print('\r--progressing...\t' + str(jd) + "%", end='')
        tt += 1
        if tt == int(len(map1.items()) / 100 + 1):
            jd += 1
            tt = 0

    return newm


mid_only = sort_by_keys(mid_only)
_mid_only = sort_by_keys(_mid_only)

mid_only = value_(mid_only, _mid_only)
mid_only = ss(mid_only)

import shelve

rec = shelve.open('data/recommend')
rec['fff'] = mid_only
# %%
# 59.35
# 单独限制
k_uok = 0
k_mok = 240
# 多重限制
k_umok = (240, 350)

result = []
for it in to_predict:
    uid = it[0]
    u_re = list(uid_only[uid])
    m_re = list(mid_only[uid])

    mid = it[1]
    if mid in u_re[:k_uok]:
        result.append(1)
        continue
    if mid in m_re[:k_mok]:
        result.append(1)
        continue
    if mid in u_re[:k_umok[0]] and mid in m_re[:k_umok[1]]:
        result.append(1)
        continue
    result.append(0)

t = pd.DataFrame({
    'tt': result
})

t.to_excel('result/3融合.xlsx')
print('已写入到3融合.xlsx')
