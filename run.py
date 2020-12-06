# %%
import shelve
import pandas as pd

data = shelve.open('../data/recommend')
data2 = shelve.open('../data/srcData')
uid_only = data['uid_only']
mid_only = data['mid_only']

to_predict = data2['to_predict']

k_uok = 240
k_mok = 240
k_umok = (300, 300)

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
print('写入到3融合.xlsx')
