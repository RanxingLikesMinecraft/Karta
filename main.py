import time

import cv2
import pygame
import sys
from test import *
from __init__ import *

"""
上面导入模块

    整体逻辑：
        __init__.py构建class类
        main.py是主程序
        用循环遍历列表显示卡牌
        本游戏使用pygame框架搭建
    注意事项：
        卡牌要矩形的，可以用截取等方式使图片中不含有“边角料”
        背景图片大小随意，最后将图片发到群里，我再确定大小
        游戏创意可以向bedrock㞗提出
        可向我与bedrock㞗提供音频、视频、图片、插件、开源工具、应用图标(bmp图片格式、ico图片类型)
        (*^▽^*)
"""
pygame.init() #pygame初始化
card_list=[] #创建卡牌列表

pygame.display.set_caption("Karta") #设置标题
screen=pygame.display.set_mode((1840,1000))
login_bool = False
register_bool=False
login_user_name=''
login_password=''

start_bg = pygame.image.load(r'.\image\background_start_menu.jpg').convert_alpha()#创建变量来存储图片，但并不显示图片
re_bg=pygame.image.load(r'.\image\register_background.jpg').convert_alpha()
start_name_img=pygame.image.load(r'.\image\game_name.jpg').convert_alpha()
start_word=pygame.font.Font(r"C:\WINDOWS\Fonts\SIMHEI.TTF",64)
start_word_surface=start_word.render("点击开始游戏", False, (255, 255, 255), (0, 0, 0))
start_word_surface=pygame.transform.scale(start_word_surface,(512,96))
start_name_img=pygame.transform.scale(start_name_img,(1896,516))
lo_re_bg=pygame.image.load(r'.\image\register_background.jpg')
lo_re_bg=pygame.transform.scale(lo_re_bg,(1840,1000))
lo_re_box_1=pygame.image.load(r'.\image\re-lo box_1.jpg').convert_alpha()
lo_re_box_2=pygame.image.load(r'.\image\re-lo box_2.jpg').convert_alpha()
L_R_pass=False
lo_re_box_1=pygame.transform.scale(lo_re_box_1,(366*2,55*2))
lo_re_box_2=pygame.transform.scale(lo_re_box_2,(366*2,55*2))
font_user_name_surface=pygame.font.Font(r'C:\Windows\Fonts\SIMHEI.TTF',64).render("用户名：",False,(255,255,255),None).convert_alpha()
font_password_surface=pygame.font.Font(r"C:\Windows\Fonts\SIMHEI.TTF",64).render("密码：",False,(255,255,255),None).convert_alpha()
login_user_name_font=pygame.font.Font(r"C:\Windows\Fonts\SIMHEI.TTF",32).render("",False,(0,0,0),(255,255,255))
login_user_password_font=None
def Test():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                print(x,y)
            elif event.type==pygame.QUIT:
                pygame.quit()
                exit()
def start_menu():
    global cnt
    while True: #无限次循环并进行事件监听与对玩家操作的处理
        for event in pygame.event.get(): #循环监听事件并将事件写入变量event
            if event.type == pygame.QUIT: #如果玩家想要退出
                pygame.quit() #关闭pygame模块
                sys.exit() #关闭python
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if mouse_x>=633 and mouse_x<=633+512  and mouse_y >= 729 and mouse_y<=729+96  :
                    return
        screen.blit(start_bg,(0,0))
        screen.blit(start_name_img,(10,0))
        screen.blit(start_word_surface,(633,729))
        pygame.display.update()
def settings():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Menu()
            screen.blit(bg1,(0,0))
            pygame.display.update()
def LO_RE():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                print(mouse_x,mouse_y)
                if mouse_x<=589+366*2  and mouse_x >=589  and mouse_y <=146+55*2   and mouse_y >=146  :
                    print(1)
                    global login_user_name_font
                    Lo_Re.Lo_Name(login_user_name)
                    login_user_name_font=pygame.font.Font(r'C:\windows\Fonts\SIMHEI.TTF',32).render(login_user_name,None,(0,0,0),None).convert_alpha()
                #elif


        screen.blit(lo_re_bg,(0,0))
        screen.blit(login_user_name_font,(616,295))
        screen.blit(lo_re_box_1,(589,274))
        screen.blit(lo_re_box_2,(589,537))
        screen.blit(font_user_name_surface,(589,146))
        screen.blit(font_password_surface,(589,408))
        pygame.display.update()

if __name__ == '__main__': #主程序
    start_menu()
    LO_RE()
