# %%
import shelve

data = shelve.open('data/srcData')
mid_xsd = data['mid_xsd']


# %%
def sort_by_values(mmap):
    tlist = sorted(mmap.items(), key=lambda x: x[1], reverse=True)
    tmap = {}
    for t in tlist:
        tmap.update({t[0]: t[1]})
    return tmap


# %%
tm = {}
for it in mid_xsd.items():
    mid = it[0]
    xsds = it[1]
    xsdss = sort_by_values(xsds)
    tm.update({mid: xsdss})

# %%
data['mid_xsd_sorted'] = tm
data.close()
