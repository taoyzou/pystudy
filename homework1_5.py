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




#————————————————————\/————————————————————————————————初始化阶段方法体———————————————————————————————————————————\/————————————————

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
        rere=rename()
        return rere
    if warriorname=="":
        print("名字不能为空，请重新输入：")
        rere1=rename()
        return rere1
    else:
        return warriorname

#————————————————————/\————————————————————————————————————————————————————————————————————————————————/\——————————————————




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

#——————————————————————————————————\/————————————————————战斗过程方法体————————————————————————————————————\/——————————————
#判断战士名是否正确
def ifkey(key):
    if key in player.warriors:
        return key
    else:
        rekey=input("您没有该战士，请重新输入:")
        s=ifkey(rekey)
        return rekey

#对战过程
def  winer(name,a):
    player.warriors[name].fightWithMonster(forestList[a].monster)
    if(player.warriors[name].strength < 0):
        del player.warriors[name]
        if(player.warriors):
            renames=input("该士兵被杀死请重新派出士兵：")
            renames=ifkey(renames)
            newname=winer(renames,a)
            return newname
        else:
        	return 0
    if(player.warriors[name].strength == 0):
    	del player.warriors[name]
    	print("该士兵与妖怪同归于尽。\n")
    	return 1
    else:
    	print("该士兵剩余生命值为：")
    	print(player.warriors[name].strength)
    	return name
#——————————————————————————————————/\————————————————————————————————————————————————————————————————————/\————————————————        




#每个森林战斗过程
for x in range(0,forest_num):
    #战斗开始
    fightwarrior=input("这是第"+str(x+1)+"个森林,请输入你要派出士兵的名字：")
    fightwarrior=ifkey(fightwarrior)
    fightwarrior=winer(fightwarrior,x)
    if (player.warriors):
    	#战斗结束并显示剩余生命值
        countname=input("您是否需要治疗士兵，需要请输入士兵姓名，不需要请勿输入：")
        if countname == "":
            print("您选择了不需要治疗。")
        else:
            #治疗过程
            countname=ifkey(countname)                          #判断是否正确输入战士名

            losestone=input("你选择为该士兵花费多少灵石治疗？")    #读取治疗量

            losestone=ifcount(losestone)                        #判断是否为数字

            player.warriors[countname].healing(losestone)       #治疗过程
            player.stoneNumber-=int(losestone)
            
            print("经过您的治疗，该士兵剩余生命值为"+str(player.warriors[countname].strength)+"\n")
            print("您剩余灵石："+str(player.stoneNumber))
    else:
            print("您的士兵已全部被杀死，游戏结束。由于未能通关，灵石被妖怪剩余妖怪抢走")		#士兵全部阵亡，原石减少，结束游戏
            stonelose=120*x+120
            player.stoneNumber-=stonelose
            if (player.stoneNumber<0):
            	player.stoneNumber=0
            break


print("\n您最终剩余的灵石为：\n"+str(player.stoneNumber))

