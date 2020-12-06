# %%
import shelve

srcData = shelve.open('data/srcData')

uid_records = srcData['uid_records']

# %%
UIDs = list(uid_records.keys())

srcData['UIDs'] = UIDs
