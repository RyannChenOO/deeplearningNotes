## 装饰器执行
registry_store = []  # 存储装饰器register所装饰的函数
def register(func):
    print("running register......   (%s)"%func)  # 显示被装饰的函数func
    registry_store.append(func)  # 存储装饰器register所装饰的函数
    return func  # 原封不动的返回原函数

@register
def f1():
    print("running f1")

@register
def f2():
    print("running f2")

def f3():
    print("running f3")

def main():
    print("running main......")
    print("registry_store存储的函数", registry_store)
    f1()
    f2()
    f3()

if __name__=='__main__':
    # __name__是一个全局变量，代表模块的名字，即命名空间。
    # 本模块(py_装饰器.py)被当做脚本直接执行时，__name__变量的值会变为__main__，
    # 从而使该判断语句成立，并执行该语句下的其他代码(main()函数)；
    # 而当Python文件被当做模块 / 包导入时，它的值表示的是模块名，比如module1.test，或者module1.ma1.mb1.test。
    main()

