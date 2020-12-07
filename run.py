# %%
import shelve
import pandas as pd

data = shelve.open('data/recommend')
data2 = shelve.open('data/srcData')
uid_only = data['uid_only']
mid_only = data['mid_only']

to_predict = data2['to_predict']

# k_uok = 150
# k_mok = 180
# k_umok = (200, 240)
# 单独限制
k_uok = 0
k_mok = 0
# 多重限制
k_umok = (240, 240)

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
