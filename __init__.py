import sys
import pygame.image #导入pygame图片模块
import json
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
class Person:
    def __init__(self,img,x,y):
        self.img=img
        self.x=x
        self.y=y
    def write(self,img,x,y):
        screen.blit(pygame.image.load(img),(x,y))
def Menu():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if
                elif
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                return
            elif event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
def image_loads():
    bg1 = pygame.image.load(r'.\image\background1.jpg')
class Users:
    global login_bool
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
    def login(self,user_name,password):
        json_path = r'User.json'
        num=open(r'UserCount.','w+',encoding="UTF-8")
        assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
        json_file = open('User.json', 'a+', encoding="UTF-8")
        json_lib = dict(json.load(json_file))#将json文件转换为字典类型
        for i in range(0,num,1):
            if user_name==json_lib["user_"+str(num)]["name"] and \
                password == json_lib["user_"+str(num)]["password"]:
                login_bool=True
            else:
                login_bool=False
    def register(self,user_name,password):
        num = open(r'UserCount.', 'w+', encoding="UTF-8")
        json_path=r'User.json'
        json_file=open('User.json','a+',encoding="UTF-8")
        for i in range(0, num, 1):
            if user_name == json_lib["user_" + str(num)]["name"] and \
                    password == json_lib["user_" + str(num)]["password"]:
                register_bool=False
            else:
                register_bool = True
        if register_bool:
            json_file.write(
                """
                "user_%d"{
                "name":%s,
                "password":%s,
                }
                """%(int(num.read())+1,user_name,password)
            )
            num.write(num.read()+1)
        else:
            return
