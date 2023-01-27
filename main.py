import time

import cv2
import pygame
import sys

#from __init__ import *

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
login_str=''
login_password=''


start_bg = pygame.image.load(r'.\image\background_start_menu.jpg').convert_alpha()#创建变量来存储图片，但并不显示图片
re_bg=pygame.image.load(r'.\image\register_background.jpg').convert_alpha()
start_name_img=pygame.image.load(r'.\image\game_name.jpg').convert_alpha()
start_word=pygame.font.Font(r"C:\WINDOWS\Fonts\SIMHEI.TTF",64)
start_word_surface=start_word.render("点击开始游戏", False, (255, 255, 255), (0, 0, 0))
start_word_rect = start_word_surface.get_rect()
start_word_surface=pygame.transform.scale(start_word_surface,(512,96))
start_name_img=pygame.transform.scale(start_name_img,(1896,516))
def start_menu():
    while True: #无限次循环并进行事件监听与对玩家操作的处理
        for event in pygame.event.get(): #循环监听事件并将事件写入变量event
            if event.type == pygame.QUIT: #如果玩家想要退出
                pygame.quit() #关闭pygame模块
                sys.exit() #关闭python
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if mouse_x>=479 and mouse_x<=1272  and mouse_y >= 830 and mouse_y<=918  :
                    break
                    return
        #for i in range():

        #for i in range():
        screen.blit(start_bg,(0,0))
        screen.blit(start_name_img,(10,0))
        screen.blit(start_word_surface,(633,729))
        pygame.display.update()
def ssttings():
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

if __name__ == '__main__': #主程序
    start_menu()
    print(start_name_img.get_size())