from numpy import *
import kmeansjiajia

# step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split('\t')
	dataSet.append([float(lineArr[0]), float(lineArr[1])])
dataSet = mat(dataSet)

# step 2: clustering...
print "step 2: clustering..."
k = 4
centroids,clusterAssment =kmeansjiajia.kmeans(dataSet, k)

# step 3: show the result
print "step 3: show the result..."
kmeansjiajia.showCluster(dataSet,k,centroids,clusterAssment)