from random import randint
import time,sys
import time
import os
# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification)

#延时10s
for Timerange in range(1,11):                                       #测试完记得改回11
    time.sleep(1)   
print("time is over")

#两种清屏方法
for Backrange in range(1,40):
    print("\b")
os.system('cls')


#判断是否为数字的方法
def ifcount(num):
    try:
        num=int(num)
    except:
        renum=input("非法输入，请重新输入正确数字：")
        ifcount(renum)
    else:
        return num


#确定战士种类方法
def typedef(Warriortype):
    Warriortype=ifcount(Warriortype)
    if Warriortype ==1:
        player.warriors[newwarriorname]=Archer(newwarriorname)
        player.stoneNumber-=Archer.price
        print("购买成功，剩余灵石："+str(player.stoneNumber))
    if Warriortype ==2:
        player.warriors[newwarriorname]=Axeman(newwarriorname)
        player.stoneNumber-=Axeman.price
        print("购买成功，剩余灵石："+str(player.stoneNumber))
    if Warriortype != 1 and Warriortype != 2:
        print("输入错误，请重新输入.")
        reint=int(input("弓箭手请输入1，斧头并请输入2:"))
        typedef(reint)



#命名方法
def rename():
    warriorname=input("请为该战士命名：")
    if warriorname in player.warriors:
        print('该名字已存在,请重新命名')
        rename()
    if warriorname=="":
        print("名字不能为空，请重新输入：")
        rename()
    else:
        return warriorname




#初始化
player=Player(1000)
Warriornumber=int(input("\n你要购买的士兵的总数为："))

for Warrioraddress in range(1,Warriornumber+1):
    #为士兵命名并记录
    newwarriorname=rename()
    player.warriors[newwarriorname]=newwarriorname

    #确定士兵种类
    WarriorType=input("弓箭手请输入1，斧头并请输入2:")
    typedef(WarriorType)

#os.system('cls')










print('''
***************************************
****           战斗开始            ****
***************************************

'''
)

List=list(player.warriors.keys())
print("您的战士有：")
print(List)




#判断战士名是否正确
def ifkey(key):
    if key in player.warriors:
        return key
    else:
        rekey=input("您没有该战士，请重新输入")
        ifkey(rekey)




#每个森林战斗过程
for x in range(0,forest_num):
    fightwarrior=input("这是第"+str(x+1)+"个森林,请输入你要派出士兵的名字：")
    fightwarrior=ifkey(fightwarrior)
    player.warriors[fightwarrior].fightWithMonster(forestList[x].monster)
    print("该士兵剩余生命值为：")
    print(player.warriors[fightwarrior].strength)
    countname=input("您是否需要治疗士兵，需要请输入士兵姓名，不需要请勿输入：")
    if countname == "":
        print("您选择了不需要治疗。")
    else:
        #治疗过程
        countname=ifkey(countname)
        losestone=input("你选择为该士兵花费多少灵石治疗？")
        losestone=ifcount(losestone)
        player.warriors[countname].healing(losestone)
        player.stoneNumber-=losestone
        print("经过您的治疗，该士兵剩余生命值为"+str(player.warriors[countname].strength)+"\n")
        print("您剩余灵石："+str(player.stoneNumber))


print("\n您最终剩余的灵石为：\n"+str(player.stoneNumber))
