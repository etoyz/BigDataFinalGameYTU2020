# %%
import shelve
import pandas as pd

data = shelve.open('data/recommend')
data2 = shelve.open('data/srcData')
uid_only = data['uid_only']
mid_only = data['mid_only']

to_predict = data2['to_predict']

k = 0.57

def change_recommended(recs):
    most_rec = None
    new_rec = {}
    for rec in recs.items():
        most_rec = (rec[0], rec[1])
        break
    for rec in recs.items():
        if rec[1] / most_rec[1] > k:
            new_rec.update({rec[0]: rec[1]})
        else:
            break
    return new_rec


# 单独限制
k_uok = 0
k_mok = 240
# 多重限制
k_umok = (230, 300)

result = []
for it in to_predict:
    uid = it[0]
    u_re = uid_only[uid]
    m_re = mid_only[uid]

    u_re = change_recommended(u_re)
    m_re = change_recommended(m_re)
    print(len(m_re))
    u_re = list(u_re)
    m_re = list(m_re)

    mid = it[1]
    # if mid in u_re:
    #     result.append(1)
    #     continue
    if mid in m_re:
        result.append(1)
        continue
    # if mid in u_re and mid in m_re:
    #     result.append(1)
    #     continue
    result.append(0)

t = pd.DataFrame({
    'tt': result
})

t.to_excel('result/3融合(前0.1).xlsx')
print('已写入到3融合(前0.1).xlsx')
