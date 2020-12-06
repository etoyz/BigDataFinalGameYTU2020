# %%
import shelve

srcData = shelve.open('../data/srcData')

mid_xsd = srcData['mid_xsd']
MIDs = list(mid_xsd.keys())

# %%
srcData['MIDs'] = MIDs
srcData.close()
