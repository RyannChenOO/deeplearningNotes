import math
import random
import time


class Cylinder(object):
    def __init__(self, height, radius, idx):
        self.id = idx   # 存储对象的属性
        self.height = height
        self.radius = radius

    def PrintInfo(self):
        """打印圆柱体的半径和高"""
        print("圆柱体的半径为:{}, 搞高为:{}".format(self.radius, self.height))

    def GetVolume(self):
        """计算圆柱体的体积"""
        return math.pi * (r ** 2) * h


def create_obj(n=3):
    # 产生10个对象
    object_list = []
    for i in range(3):
        # 获取圆柱体的半径和高
        try:
            height = float(input("请输入圆柱体的高"))
            radius = float(input("请输入圆柱体的半径"))
        except Exception as e:
            print("输入有误")
        while height < 0 or radius < 0:
            print("输入有误")
            try:
                height = float(input("请输入圆柱体的高"))
                radius = float(input("请输入圆柱体的半径"))
            except Exception as e:
                print("输入有误")
        # 创建圆柱体
        obj = Cylinder(height, radius, i)  # 创建时存储对象的唯一编号
        # 对象放入列表中
        object_list.append(obj)
    return object_list


def count_del_time(func):
    print("--------开始删除对象元素-----------------")

    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("---------删除结束------------------------")
        print("删除耗时：{}".format(end-start))
        return res

    return inner


@count_del_time
def del_obj(object_list):
    while len(object_list) > 0:  # 未清空完毕
        idx = random.randint(0, len(object_list)-1)
        # 查找id为idx的对象进行删除
        for i in range(len(object_list)):
            if object_list[i].id == idx:
                del object_list[i]
                break
        print(object_list)


if __name__ == '__main__':
    object_list = create_obj()
    res = del_obj(object_list)
