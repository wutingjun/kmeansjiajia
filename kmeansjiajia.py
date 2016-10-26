#coding=utf-8
from numpy import *
import matplotlib.pyplot as plt

# 计算两个向量之间的距离
def euclDistance(vector1, vector2):
    # vector1,vector2是向量才能相加减,python中一维向量用矩阵表示
    return sqrt(sum(power(vector2 - vector1, 2)))

# k-means cluster
def kmeans(dataSet, k):			#dataSet=[[1 2][3 4][5 6]...]
    import centroids
    numSamples = dataSet.shape[0]
    # clusterAssment第一列存储对应样本点属于哪一个簇,第二列是该点到簇中心的距离平方和
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    # step 1:找出初始点
    centroids = centroids.initCentroids(dataSet, k)
    while clusterChanged:
        # clusterChanged标记簇中心是否改变
        clusterChanged = False

        # step 2:对于每个样本点,计算它与每个簇之间的距离,距离最小划分为它归属的簇
        for i in xrange(numSamples):
            minDist=inf #inf是numpy中的一个常量,表示无穷大
            minIndex =0

            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist  = distance
                    minIndex =j

            # step 3:判断该样本点所属的簇是否改变,若改变记下它与簇中心之间的距离
            if clusterAssment[i, 0]!=minIndex:    #clusterAssment[i, 0]是原先该样本所属的簇中心,minIndex是新样本点所属的簇中心
                clusterChanged = True   #簇中心已发生改变
                clusterAssment[i, :] = minIndex, minDist**2

        # step 4:更新簇中心
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]  #clusterAssment[:,0].A将clusterAssment[:,0]矩阵转换成数组
            # nonzero(a)函数将对矩阵a的所有非零元素,分别从两个维度(行和列)看,非0元素对应的行坐标放在一个列表中,对应的列坐标放在一个列表中,然后一起返回!
            # clusterAssment[:, 0].A ==j将对应的元素编程True和False了,所以nonzero(clusterAssment[:, 0].A == j)[0]最终将该簇的点
            centroids[j, :] = mean(pointsInCluster, axis = 0) #选项axis=0表示沿矩阵的列方向进行均值计算

    print 'Congratulations, cluster complete!'
    return centroids, clusterAssment

# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large!"
        return 1

    # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

    plt.show()