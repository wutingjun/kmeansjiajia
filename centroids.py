#coding=utf-8
from numpy import *

# kmeans++与kmeans的区别就在于初始点的选择不同
# 关于kmeans++初始点选择的原理很多，自己可以去查看PPT，接下来讲得是算法实现流程
# 1.首先从数据集中随机选取一个点作为中心点，并介入到中心点集合centroids中
# 2.对与数据集中的每个点i，都和集合centroids中的点(已选簇中心)进行计算，得到最近距离d[i]，计算完之后得到sum(d[i])
# 3.取一个随机值random，使random落在sum(d[i])内，然后循环计算random -=d[i]直到random<0,并把点i作为新的簇中心
# 4.重复b和c过程直到完成所有的中心点的选取

# kmeans++的初始点选择，输入数据dataSet是矩阵
def initCentroids(dataSet,k):
    row,col=dataSet.shape #计算矩阵的行和列
    centroids =zeros((k, col)) #centroids存储每个簇心的坐标

    firstCenterIndex= int(random.uniform(0,row))
    centroids[0,:]=dataSet[firstCenterIndex,:] #首先随机选择一个样本点作为第一个簇中心

    for i in xrange(1,k):
        distances=[] #记录每一个点与每个簇中心的最近距离
        sums=0

        # 遍历数据集中每一个点(即遍历矩阵中的每一个点)，
        for x in xrange(0,row):
            # 计算每一个样本点与选择出来的簇中心距离，并返回与距离最近簇中心的距离。
            dist=minDist(dataSet[x,:],centroids,i)
            distances.append(dist)
            sums+=dist

        random_gen=random.uniform(0,sums)
        for x in xrange(0,row):
            random_gen -=distances[x]
            if random_gen>0:
                continue
            centroids[i,:]=dataSet[x,:] #初始化第i个簇中心
            break

    return centroids

def minDist(point,centroids,cluster_num): #求point与centroids中已初始化簇中心的最近距离
    # point:样本点,centroids:簇中心矩阵,cluster_num:已初始化簇的个数
    mindist=float('inf') #mindist赋值为无穷大

    # 计算point与每个簇中心的距离
    for index in xrange(0,cluster_num):
        dist=euclDistance(point,centroids[index,:])
        if dist<mindist:
            mindist=dist
    return mindist

def euclDistance(vector1, vector2):
    # vector1,vector2是向量才能相加减,python中一维向量用矩阵表示
    return sqrt(sum(power(vector2 - vector1, 2)))
