import shelve

data = shelve.open('data/srcData')
records = data['uid_records']

# %%
def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


tm = {}

for record in records.items():
    tm.update({record[0]: len(record[1])})

m = sort_by_values(tm)