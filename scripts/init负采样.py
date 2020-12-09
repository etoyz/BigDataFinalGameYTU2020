import os

os.system("python 读电影相似度矩阵(负采样),二维map存到'_mid_xsd'中.py")
os.system("python 将_mid_xsd排序，xsd高的在上面，存到'_mid_xsd_sorted'.py")
os.system("python 根据电影相似度降低推荐(负采样).py")
