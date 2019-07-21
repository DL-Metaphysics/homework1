import numpy as np
import matplotlib.pyplot as plt
def init():
    #四组数据 两个参数表示武打镜头次数以及亲吻镜头次数
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    #四组数据的标签 类型
    labels = ['爱情片','爱情片','动作片','动作片']
    return group,labels
def draw(X):
    group,label = init()
    #print(group[:,0],group[:,1])
    plt.scatter(group[:,0],group[:,1])
    plt.scatter(X[0],X[1])
    plt.show()
def solve(group,k,labels,input):
    x = group.shape[0]#行数
    new_array = np.tile(input,(x,1))#线性代数矩阵思维
    #  tile函数的作用 重复n行m列
    #  1 2 3
    #  (2,3)
    #   1 2 3 1 2 3 1 2 3
    #   1 2 3 1 2 3 1 2 3
    new_array -= group
    new_array **= 2
    new_array = np.sum(new_array,axis = 1)#每行相加获得的是行向量 axi=0 每列求和
    diatance = new_array**0.5 #距离列表
    #对距离进行排序
    sorted_distance = np.argsort(diatance) #小到大排序返回下标的列表
    map = {}#装k个
    for i in range(k):
        #sorted_distance labels k
        #3 A 0
        #1 A 1
        #0 B 2
        string = labels[sorted_distance[i]]
        map[string] = map.get(string,0)+1#用字典模拟c++中map的作用
    cnt = 0
    for key,value in map.items():#找出出现次数最多的string
        if value > cnt:
            cnt = value
            res_string = key
    return res_string
 
if __name__=='__main__':
    x = int(input())
    y = int(input())
    group,labels = init()
    draw((x,y))
    res = solve(group,2,labels,np.array([x,y]))
    print('经过预测结果是',res)
