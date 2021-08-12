'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
#随机获得优惠券
import random
shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]



m = random.randint(0,44)
if m in[0,1,2,3,4,5,6,7,8,9]:
    print("恭喜你，获得了一张联想五折优惠券")
    m = 0  #返回购物车角标为4的商品
    chen = 0.5  #打五折
elif m in[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]:
    print("恭喜你，获得了一张老干妈一折优惠券")
    m = 4  #返回购物车角标为5的商品
    chen = 0.1#打一折
elif m in [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]:
    print("恭喜你，获得了一张HUAWEI WATCH PRO 20 八折优惠券")
    m = 2#返回购物车角标为1的商品
    chen = 0.8#打八折



print("------------欢迎来到购物商城-----------")
#  2.初始化您的余额
money = int(input("请输入您本月工资："))
mc = money
# 1.空的购物车
mycart = []


# 3.正常购物

while True:
    for key,value in enumerate(shop):
        print(key,value)
    soso = input("请输入您想要的商品：")
    if soso.isdigit():
        soso = int(soso)
        if soso >=len(shop) or soso < 0: # len
          print("没有该号商品！请重新输入！")
        else:  # 输入的编号在0-6之间
           if soso == m and money >= shop[soso][1] * chen:
             money = money - shop[soso][1] * chen
             mycart.append([shop[soso][0], shop[soso][1]])  # 将打折商品添加到购物车
             print("商品已添加到购物车，您的余额剩余：￥", money)
             m = 10  # 只要不等于451，就不在打折
           elif money >= shop[soso][1]:  # 金额>商品的价格
             money = money - shop[soso][1]
             mycart.append(shop[soso])  # 将商品添加到购物车
             print("商品已添加到购物车，您的余额剩余：￥", money)
           else:
             print("余额不足，请选择其他商品！")
    elif soso == "q" or soso == "Q":
        print("欢迎下次光临！")
        print("-------------购物小票-----------")
        # for key,value in enumerate(mycart):
        #     print(value)

        for m, value in enumerate(mycart):  # 取出第一个数
            count = 0
            flag = True
            for j in range(0, m):
                if mycart[j] == mycart[m]:  # 看看有没有重复的，
                    flag = False
                    break
            if flag == False:
                continue  # 跳出后面的程序 后面的程序不执行
            for i in range(m, len(mycart)):  # 取出第一个数和后面的数作比较，看有没有一样的
                if mycart[m] == mycart[i]:
                    count = count + 1
            print(value, "*", count, "！")

        print("-----------------------------------")
        print("您一共购买了", len(mycart), "件，合计：￥", mc - money)
        break
    else:
        print("输入非法，请重新输入！")