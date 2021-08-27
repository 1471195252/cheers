#cook厨师  basket 篮子  consumer消费者  bread面包


from  threading import Thread
import time
mianbao = 0

class cook(Thread):
   cname = "" #用户名
   gouname = ""
   money = float(0)
   mianbao = 0
   c = 0
   def run(self) -> None:
        global miaobao  # global 全局变量
        while True:
            if self.cname:
                 if mianbao < 500:
                     mianbao = mianbao + 1
                     self.c += 1
                     print(self.c,"个")
                 elif mianbao >= 500:
                    print("篮子已满，傻狗！")
                 elif mianbao == 0:
                     time.sleep(2)
                     print("稍等，傻狗！")
                     if mianbao == 500:
                         break

            elif self.gouname:
                 if self.money >= 2.5:

                    self.money -= 2.5
                    print(self.gouname,"还剩",self.money)

                 elif self.money < 2.5:
                     print("没钱了，滚吧")
                     break
cook1 = cook()
cook1.cname = "mc"
cook2 = cook()
cook2.cname = "mm"
cook3 = cook()
cook3.cname = "sc"
dook4 = cook()
dook4.money  = 3000
dook4.gouname  = "小"
dook5 = cook()
dook5.money  = 3000
dook5.gouname  = "马"
dook6 = cook()
dook6.money  = 3000
dook6.gouname  = "蹄"
dook7 = cook()
dook7.money  = 3000
dook7.gouname  = "小小"
dook8 = cook()
dook8.money  = 3000
dook8.gouname  = "马马"
dook9 = cook()
dook9.money  = 3000
dook9.gouname  = "蹄铁"
cook1.start()
cook2.start()
cook3.start()
dook4.start()
dook5.start()
dook6.start()
dook7.start()
dook8.start()
dook9.start()












