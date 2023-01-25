import pygame
import sys
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
FPS=60
clock = pygame.time.Clock()
card_list=[] #创建卡牌列表
pygame.init() #pygame初始化
pygame.display.set_caption("Karta") #设置标题
background_movie=pygame.movie.Movie(r".\image\background.mp4")
screen=pygame.display.set_mode(movie.get_size())
def Novice_Tutorial():
    bg=''
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

    movie_screen=pygame.Surface(movie.get_size()).convert()
    movie.set_display(movie_screen)
    movie.play()
    playing=True

    bg1=pygame.image.load(r'.\image\background1.jpg')
    while True: #无限次循环并进行事件监听与对玩家操作的处理
        for event in pygame.event.get(): #循环监听事件并将事件写入变量event
            if event.type == pygame.QUIT: #如果玩家想要退出
                pygame.quit() #关闭pygame模块
                sys.exit() #关闭python
                movie.stop()
                playing=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if mouse_x==   and mouse_y ==   :
                    playing=False
                    movie.stop()
                    break
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Menu()
            screen.blit(movie_screen,(0,0))
            clock.ticks(FPS)
            pygame.display.update() #实时更新窗口

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Menu()
            screen.blit(bg1)
            pygame.display.update()
if __name__ == '__main__': #主程序
    main() #运行主程序
