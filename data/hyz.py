import pandas as pd
import random as rd


# -------#-------#-------#-------#-------#-------
def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


# 求出电影的播放次数由高到低列表
df_train = pd.read_excel('train.xlsx')
MIDS = df_train['MID']
UIDS = df_train['UID']
M_cnt = {}
for i in range(len(MIDS)):
    # 如果电影号不存在
    if not MIDS[i] in M_cnt.keys():
        M_cnt.update({MIDS[i]: 1})
    # 存在
    else:
        oldCnt = M_cnt[MIDS[i]]
        M_cnt.update({MIDS[i]: oldCnt + 1})

M_cnt = sort_by_values(M_cnt)
# print("电影的播放次数由低到高",M_cnt)
# -------#-------#-------#-------#-------#-------
# 获取每个用户的播放列表

U_watched_list = {}
for i in range(len(UIDS)):
    if not UIDS[i] in U_watched_list.keys():
        l = []
        l.append(MIDS[i])
        U_watched_list.update({UIDS[i]: l})
    # 已经有这个用户
    else:
        U_watched_list[UIDS[i]].append(MIDS[i])


# print("每个用户的播放列表",U_watched_list)

# -------#-------#-------#-------#-------#-------
# 获取补给的函数
def getBuji(all_mid, person_mid):  # in a ,not in b
    tmp = []
    for a in all_mid:
        if a not in person_mid:
            tmp.append(a)
    return tmp


US_Fu = {}
print(UIDS)
for i in range(1, 944):

    # 再获取用户i观影记录的补集
    Buji = getBuji(MIDS, U_watched_list[i])
    # 得到补集之后，通过M_cnt获取补集中每个电影的播放次数
    Buji_cnt = {}
    for j in Buji:
        Buji_cnt.update({j: M_cnt[j]})
    # 对补集的播放次数排序
    # Buji_cnt =  sort_by_values(Buji_cnt)
    Buji_mids = Buji_cnt.keys()

    # Buji_cnt = sorted(Buji_cnt.items(), key=lambda x: x[1], reverse=True)
    # print(Buji_cnt)
    print("--------------------------------------------------")
    print(len(Buji_cnt), "uid = ", i)

    # -------#-------#-------#-------#-------#-------
    U_watched_len = len(U_watched_list[i])
    U_Fu = []
    print("观影记录数目", U_watched_len, "负采样数:", 4 * U_watched_len)
    # 20是容错
    # 1:4，4不能超过电影的总数
    U_lenn = min(4 * U_watched_len, 1682 - U_watched_len - 20)
    if U_watched_len > 350:
        U_Fu = Buji_mids
    else:
        for j in range(U_lenn):
            selectMid = rd.randint(1, 1683)
            # 如果在已选的里面或者该电影不在key
            while selectMid not in Buji_mids or selectMid in U_Fu:
                print("重复了", selectMid)
                selectMid = rd.randint(1, 1683)
            U_Fu.append(selectMid)
    print(U_Fu)
    US_Fu.update({i: U_Fu})
print(US_Fu)

new_uid = []
new_fu = []
for i in US_Fu.keys():
    for j in US_Fu[i]:
        new_uid.append(i)
        new_fu.append(j)
print("outing")
pd.DataFrame({
    'new_uid': new_uid,
    'new_fu': new_fu
}).to_excel("fu_train_ave.xlsx")
print('outed')
