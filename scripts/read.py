import shelve

srcData = shelve.open('../data/srcData')
result = shelve.open('../data/result')
recommend = shelve.open('../data/recommend')
t = recommend['rec0_first_place_m']

import pandas

tt = pandas.DataFrame({
    '最后一次大于0的位置': t
})
tt.to_excel('zh.xlsx')
