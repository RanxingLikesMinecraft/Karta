import time

import cv2
import pygame
from moviepy.editor import *

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

image_loads()


FPS=60
FramePerSec=pygame.time.Clock()
bg_video_path = cv2.VideoCapture(r".\video\background.mp4")
bg_video=cv2.VideoCapture(bg_video_path)
card_list=[] #创建卡牌列表
pygame.init() #pygame初始化
pygame.display.set_caption("Karta") #设置标题
screen=pygame.display.set_mode((1140,940))
screen.fill([0,0,0])
bg_num=0
login_bool = False
register_bool=False
login_str=''
login_password=''
def Novice_Tutorial():
    bg=r'.\image\background_Novice_Tutorial.jpg'
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Menu()
            screen.blit(bg,(0,0))


def main():
    global bg_num,bg1

    while True: #无限次循环并进行事件监听与对玩家操作的处理
        if bg_num == 0:
            T0 = time.time()

        if time.time() - T0 > bg_num * (1. / FPS):
            ret, frame = bg_video.read()
            TimeStamp = bg_video.get(cv2.CAP_PROP_POS_MSEC)
        frame = pygame.surfarray.make_surface(cv2.transpose(cv2.cvColor(frame, cv2.COLOR_BGR2RGB)))
        screen.blit(frame, (0, 0))
        pygame.display.update()  # 实时更新窗口
        bg_num += 1
        for event in pygame.event.get(): #循环监听事件并将事件写入变量event

            if event.type == pygame.QUIT: #如果玩家想要退出
                pygame.quit() #关闭pygame模块
                sys.exit() #关闭python
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if mouse_x==   and mouse_y ==   :
                    break
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Menu()
            #视频继续
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
    main() #运行主程序
