import shelve

srcData = shelve.open('../data/srcData')
result = shelve.open('../data/result')
recommend = shelve.open('../data/recommend')
t = recommend['uid_only']
