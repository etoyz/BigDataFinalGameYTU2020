import shelve

data = shelve.open('../data/recommend')
rec = data['mid_only']
UIDs = list(rec.keys())
rec0_first_place = {}

for uid in UIDs:
    recs_m = rec[uid]
    k = -1
    for rec_m in recs_m.items():
        if rec_m[1] > 0:
            k += 1
            continue
        if rec_m[1] <= 0:
            rec0_first_place.update({uid: k})
            break
data['rec0_first_place_m'] = rec0_first_place

rec = data['uid_only']
for uid in UIDs:
    recs_m = rec[uid]
    k = -1
    for rec_m in recs_m.items():
        if rec_m[1] > 0:
            k += 1
            continue
        if rec_m[1] <= 0:
            rec0_first_place.update({uid: k})
            break
data['rec0_first_place_u'] = rec0_first_place
