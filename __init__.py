import sys
import pygame.image #导入pygame图片模块
import json
from main import *
class Card(): #定义卡片类
    def __init__(self,img,x,y): #设置工具
        self.img=img
        self.x=x
        self.y=y
    def write(self): #构建显示卡片的方法
        screen.blit(pygame.image.load(self.img),(self.x,self.y)) #在(x,y)的地方显示卡片
@Card#对Card函数使用装饰器

class Users():#创建玩家操作的类
    global login_bool#声明全局变量login_bool
    global register_bool#声明全局变量与register_bool
    def __init__(self,user_name,password):#创建构造方法
        self.user_name=user_name#玩家姓名
        self.password=password#登录密码
    def login(self):#构建登录函数
        json_path = r'User.json'#获取所有玩家登录信息
        num=open(r'UserCount.','w+',encoding="UTF-8")#获取登录的总玩家数
        json_file = open('User.json', 'a+', encoding="UTF-8")#打开玩家信息，用a+模式，UTF-8编码
        json_lib = dict(json.load(json_file))#将json文件转换为字典类型
        for i in range(0,num):#从下表0开始一直到最后一个玩家逐个遍历
            if self.user_name==json_lib["user_"+str(num)]["name"] and \
                self.password == json_lib["user_"+str(num)]["password"]:#如果输入的玩家姓名与登录密码相匹配
                login_bool=True#则允许登录
                return
        login_bool=False#拒绝登录
    def register(self):#构建注册函数
        global re_bg
        pygame.image.load(re_bg,(0,0))#加载注册界面的背景图片
        num = open(r'UserCount.', 'w+', encoding="UTF-8")#将玩家总人数的文件以w+模式，UTF-8编码打开
        json_path=r'User.json'#存储玩家信息的文件的路径
        json_file=open('User.json','a+',encoding="UTF-8")#以a+模式，UTF-8编码打开存储玩家信息的json文件
        json_lib = dict(json.load(json_file))  # 将json文件转换为字典类型
        for i in range(0, num):#从下表0开始逐个遍历玩家信息的字典
            if self.user_name == json_lib["user_" + str(num)]["name"] and \
                    self.password == json_lib["user_" + str(num)]["password"]:#如果有玩家注册信息、注册密码与玩家信息库相匹配
                register_bool=False#拒绝注册
                return#返回
            register_bool = True#允许注册
        if register_bool:#如果允许注册
            json_file.write(#将新玩家信息填入json文件中，使用复式字符串，并与使用占位符，最后将玩家总人数+1
                """
                "user_%d"{
                "name":%s,
                "password":%s,
                }    
                """%(int(num.read())+1,self.user_name,self.password)
            )
            num.write(num.read()+1)#将存储玩家总人数的文件中的整数+1

class Lo_Re():#创建登录类
    def __init__(self,user_name,password):#创建构造方法
        self.user_name=user_name#形参user_name是将要存储的用户名
        self.password=password#形参password是将要存储的密码
    def LO_PASSWORD(self,password):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        password.join('0')
                    elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        password.join('1')
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        password.join('2')
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        password.join('3')
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        password.join('4')
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        password.join('5')
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        password.join('6')
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        password.join('7')
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        password.join('8')
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        password.join('9')
                    elif event.key == pygame.K_q and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('Q')
                    elif event.key == pygame.K_w and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('W')
                    elif event.key == pygame.K_e and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('E')
                    elif event.key == pygame.K_r and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('R')
                    elif event.key == pygame.K_t and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('T')
                    elif event.key == pygame.K_y and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('Y')
                    elif event.key == pygame.K_u and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('U')
                    elif event.key == pygame.K_i and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('I')
                    elif event.key == pygame.K_o and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('O')
                    elif event.key == pygame.K_p and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('P')
                    elif event.key == pygame.K_a and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('A')
                    elif event.key == pygame.K_s and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('S')
                    elif event.key == pygame.K_d and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('D')
                    elif event.key == pygame.K_f and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('F')
                    elif event.key == pygame.K_g and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('G')
                    elif event.key == pygame.K_h and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('H')
                    elif event.key == pygame.K_j and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('J')
                    elif event.key == pygame.K_k and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('K')
                    elif event.key == pygame.K_l and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('L')
                    elif event.key == pygame.K_z and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('Z')
                    elif event.key == pygame.K_x and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('X')
                    elif event.key == pygame.K_c and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('C')
                    elif event.key == pygame.K_v and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('V')
                    elif event.key == pygame.K_b and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('B')
                    elif event.key == pygame.K_n and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('N')
                    elif event.key == pygame.K_m and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        password.join('M')
                    elif event.key == pygame.K_q:
                        password.join('q')
                    elif event.key == pygame.K_w:
                        password.join('w')
                    elif event.key == pygame.K_e:
                        password.join('e')
                    elif event.key == pygame.K_r:
                        password.join('r')
                    elif event.key == pygame.K_t:
                        password.join('t')
                    elif event.key == pygame.K_y:
                        password.join('y')
                    elif event.key == pygame.K_u:
                        password.join('u')
                    elif event.key == pygame.K_i:
                        password.join('i')
                    elif event.key == pygame.K_o:
                        password.join('o')
                    elif event.key == pygame.K_p:
                        password.join('p')
                    elif event.key == pygame.K_a:
                        password.join('a')
                    elif event.key == pygame.K_s:
                        password.join('s')
                    elif event.key == pygame.K_d:
                        password.join('d')
                    elif event.key == pygame.K_f:
                        password.join('f')
                    elif event.key == pygame.K_g:
                        password.join('g')
                    elif event.key == pygame.K_h:
                        password.join('h')
                    elif event.key == pygame.K_j:
                        password.join('j')
                    elif event.key == pygame.K_k:
                        password.join('k')
                    elif event.key == pygame.K_l:
                        password.join('l')
                    elif event.key == pygame.K_z:
                        password.join('z')
                    elif event.key == pygame.K_x:
                        password.join('x')
                    elif event.key == pygame.K_c:
                        password.join('c')
                    elif event.key == pygame.K_v:
                        password.join('v')
                    elif event.key == pygame.K_b:
                        password.join('b')
                    elif event.key == pygame.K_n:
                        password.join('n')
                    elif event.key == pygame.K_m:
                        password.join('m')
                    elif event.key == pygame.K_UNDERSCORE:
                        password.join('_')
                    elif event.key == pygame.K_BACKSPACE:
                        password[-1]=''
                    elif event.key == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        return

    def Lo_Name(self,user_name):#创建登录的用户名的函数
        while True:#死循环
            for event in pygame.event.get():#获取监听的事件
                if event.type == pygame.KEYDOWN:#如果事件的操作为按下键盘
                    "当按下对应的按键，就在user_name中添加相应的字符，从而达到输入的效果\
                    我觉得我做的貌似有些麻烦"

                    "K_值  是键盘按键"

                    if event.key == pygame.K_q and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        "如果在按下显影按键的同时按下了shift则大写"
                        user_name.join('Q')
                    elif event.key == pygame.K_w and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('W')
                    elif event.key == pygame.K_e and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('E')
                    elif event.key == pygame.K_r and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('R')
                    elif event.key == pygame.K_t and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('T')
                    elif event.key == pygame.K_y and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('Y')
                    elif event.key == pygame.K_u and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('U')
                    elif event.key == pygame.K_i and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('I')
                    elif event.key == pygame.K_o and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('O')
                    elif event.key == pygame.K_p and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('P')
                    elif event.key == pygame.K_a and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('A')
                    elif event.key == pygame.K_s and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('S')
                    elif event.key == pygame.K_d and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('D')
                    elif event.key == pygame.K_f and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('F')
                    elif event.key == pygame.K_g and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('G')
                    elif event.key == pygame.K_h and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('H')
                    elif event.key == pygame.K_j and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('J')
                    elif event.key == pygame.K_k and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('K')
                    elif event.key == pygame.K_l and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('L')
                    elif event.key == pygame.K_z and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('Z')
                    elif event.key == pygame.K_x and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('X')
                    elif event.key == pygame.K_c and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('C')
                    elif event.key == pygame.K_v and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('V')
                    elif event.key == pygame.K_b and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('B')
                    elif event.key == pygame.K_n and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('N')
                    elif event.key == pygame.K_m and event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        user_name.join('M')
                    elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        "K_KP数字  是小键盘，银行输入密码的时候用的那种"
                        "没有KP的是正常电脑键盘"
                        user_name.join('0')
                    elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        user_name.join('1')
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        user_name.join('2')
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        user_name.join('3')
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        user_name.join('4')
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        user_name.join('5')
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        user_name.join('6')
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        user_name.join('7')
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        user_name.join('8')
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        user_name.join('9')
                    elif event.key == pygame.K_q:
                        user_name.join('q')
                    elif event.key == pygame.K_w:
                        user_name.join('w')
                    elif event.key == pygame.K_e:
                        user_name.join('e')
                    elif event.key == pygame.K_r:
                        user_name.join('r')
                    elif event.key == pygame.K_t:
                        user_name.join('t')
                    elif event.key == pygame.K_y:
                        user_name.join('y')
                    elif event.key == pygame.K_u:
                        user_name.join('u')
                    elif event.key == pygame.K_i:
                        user_name.join('i')
                    elif event.key == pygame.K_o:
                        user_name.join('o')
                    elif event.key == pygame.K_p:
                        user_name.join('p')
                    elif event.key == pygame.K_a:
                        user_name.join('a')
                    elif event.key == pygame.K_s:
                        user_name.join('s')
                    elif event.key == pygame.K_d:
                        user_name.join('d')
                    elif event.key == pygame.K_f:
                        user_name.join('f')
                    elif event.key == pygame.K_g:
                        user_name.join('g')
                    elif event.key == pygame.K_h:
                        user_name.join('h')
                    elif event.key == pygame.K_j:
                        user_name.join('j')
                    elif event.key == pygame.K_k:
                        user_name.join('k')
                    elif event.key == pygame.K_l:
                        user_name.join('l')
                    elif event.key == pygame.K_z:
                        user_name.join('z')
                    elif event.key == pygame.K_x:
                        user_name.join('x')
                    elif event.key == pygame.K_c:
                        user_name.join('c')
                    elif event.key == pygame.K_v:
                        user_name.join('v')
                    elif event.key == pygame.K_b:
                        user_name.join('b')
                    elif event.key == pygame.K_n:
                        user_name.join('n')
                    elif event.key == pygame.K_m:
                        user_name.join('m')
                    elif event.key == pygame.K_UNDERSCORE:# 这个是下划线
                        user_name.join('_')
                    elif event.key == pygame.K_BACKSPACE:#删除键Backspace
                        user_name[-1]=''
                    elif event.key == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN or event.key== pygame.K_TAB:#回车键和TAB键
                        L_R_pass=True
                        return
