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
k_uok = 40
k_mok = 40
# 多重限制
k_umok = (0, 0)

result = []
for it in to_predict:
    uid = it[0]
    u_rest = uid_only[uid]
    m_rest = mid_only[uid]
    u_res = []
    m_res = []
    for u_re in u_rest.items():
        if u_re[1] > k_uok:
            u_res.append(u_re[0])
        else:
            break
    for m_re in m_rest.items():
        if m_re[1] > k_mok:
            m_res.append(m_re[0])
        else:
            break

    mid = it[1]
    if mid in u_res:
        result.append(1)
        continue
    if mid in m_res:
        result.append(1)
        continue
    if mid in u_res and mid in m_res:
        result.append(1)
        continue
    result.append(0)

t = pd.DataFrame({
    'tt': result
})

t.to_excel('result/3融合.xlsx')
print('已写入到3融合(绝对值).xlsx')
