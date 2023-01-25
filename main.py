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

def main():
    card_list=[] #创建卡牌列表
    pygame.init() #pygame初始化
    screen = pygame.display.set_mode((1440, 940)) #搭建窗口
    pygame.display.set_caption("Karta") #设置标题
    background = pygame.image.load("background.jpg") #设置背景图片 目前是临时的背景图片
    screen.blit(background, (0,0)) #将背景图片显示在窗口中
    while True: #无限次循环并进行事件监听与对玩家操作的处理
        for event in pygame.event.get(): #循环监听事件并将事件写入变量event
            if event.type == pygame.QUIT: #如果玩家想要退出
                pygame.quit() #关闭pygame模块
                sys.exit() #关闭python
            pygame.display.update() #实时更新窗口

if __name__ == '__main__': #主程序
    main() #运行主程序
