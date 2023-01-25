import pygame.image #导入pygame图片模块
class Card: #定义卡片类
    def __init__(self,img,x,y): #设置工具
        self.img=img
        self.x=x
        self.y=y
    def write(self,img,x,y): #构建显示卡片的方法
        screen.blit(pygame.image.load(img),(x,y)) #在(x,y)的地方显示卡片
@Card#对Card函数使用装饰器
class Card_Package: #定义卡片仓库
    global card_list #声明全局变量card_list，即玩家所拥有的卡片
    def __init__(self,x,y): #构建工具
        self.x=x
        self.y=y
    def write(self,x,y): #构建显示卡片的方法
        for i in card_list: #循环遍历card_list并将每一项的值赋值给变量i
            img=pygame.image.load(i) #将显示卡片i的构造方法赋值给变量img
            if(x> ):#卡牌换行显示
                x=#卡牌显示在下一行第一个
                y+=#卡牌距离(上下)+卡牌的y长度
            screen.blit(img,(x,y)) #显示卡片在(x,y)
            x+=#卡牌的距离(左右)+卡牌的x长度
@Card_Package#对Card_Package函数使用装饰器