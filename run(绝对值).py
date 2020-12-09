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
k_uok = 10000000
k_mok = 25
# 多重限制
k_umok = (10000000, 1000000)

result = []
jd = 0
for it in to_predict:
    uid = it[0]
    mid = it[1]
    u_rest = uid_only[uid]
    m_rest = mid_only[uid]
    u_res = []
    m_res = []
    u_res2 = []
    m_res2 = []
    # 单独uid方式
    for u_re in u_rest.items():
        if u_re[1] > k_uok:
            u_res.append(u_re[0])
        else:
            break
    if mid in u_res:
        result.append(1)
        continue

    # 单独mid方式
    for m_re in m_rest.items():
        if m_re[1] > k_mok:
            m_res.append(m_re[0])
        else:
            break
    if mid in m_res:
        result.append(1)
        continue

    # 混合方式
    for u_re in u_rest.items():
        if u_re[1] > k_umok[0]:
            u_res2.append(u_re[0])
        else:
            break
    for m_re in m_rest.items():
        if m_re[1] > k_umok[1]:
            m_res2.append(m_re[0])
        else:
            break
    if mid in m_res2 and mid in u_res2:
        result.append(1)
        continue

    result.append(0)

t = pd.DataFrame({
    'tt': result
})

t.to_excel('result/3融合(绝对值).xlsx')
print('已写入到3融合(绝对值).xlsx')
