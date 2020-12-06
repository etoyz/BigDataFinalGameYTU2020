# %%
import shelve

data = shelve.open('../data/srcData')
uid_xsd = data['uid_xsd']


# %%
def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


# %%
tm = {}
for it in uid_xsd.items():
    uid = it[0]
    xsds = it[1]
    xsdss = sort_by_values(xsds)
    tm.update({uid: xsdss})


# %%
data['uid_xsd_sorted'] = tm
data.close()
