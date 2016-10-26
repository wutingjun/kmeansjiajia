#coding=utf-8
from numpy import *

# kmeans++的初始点选择，输入数据dataSet是列表
# 如果输入数据dataSet是矩阵的话，可以根据这个代码能改出代码来即可
def initCentroids1(dataSet, k):
    numSamples=len(dataSet)
    centroids =[] #centroids存储每个簇心的坐标

    firstCenterIndex= int(random.uniform(0, numSamples))
    centroids.append(dataSet[firstCenterIndex]) #首先随机选择一个样本点作为第一个簇中心

    for i in xrange(1,k):
        distances=[]
        sums=0

        # 遍历数据集中每一个点，
        for x in xrange(0,numSamples):
            dist=minDist(dataSet[x],centroids)
            distances.append(dist)
            sums+=dist

        random_gen=random.uniform(0,sums)
        for x in xrange(0,numSamples):
            random_gen -=distances[x]
            if random_gen>0:
                continue
            centroids.append(dataSet[x])
            break

    return centroids

def minDist(point,centroids):
    mindist=float('inf')

    for index in xrange(0,len(centroids)):
        dist=euclDistance(mat(point),mat(centroids[index]))
        if dist<mindist:
            mindist=dist
    return mindist

def euclDistance(vector1, vector2):
    # vector1,vector2是向量才能相加减,python中一维向量用矩阵表示
    return sqrt(sum(power(vector2 - vector1, 2)))