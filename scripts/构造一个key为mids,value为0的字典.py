import shelve

data = shelve.open('../data/srcData')
MIDs = data['MIDs']

tm = {}
for mid in MIDs:
    tm.update({mid: 0})

data['mid_map'] = tm
