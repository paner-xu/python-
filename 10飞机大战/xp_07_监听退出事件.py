# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/3/12 16:12'
__author__ = 'Remix'
import pygame
pygame.init()
# 创建窗口
screen = pygame.display.set_mode((480, 700))
# 1、图片加载
by = pygame.image.load("./images/background.png")
# 2、指定位置
screen.blit(by, (0, 0))
# 3、更新显示
pygame.display.update()
# 绘制英雄图像
# 1、图片加载
hero = pygame.image.load("./images/yingxiong.png")
# 2、指定位置
screen.blit(hero, (240, 500))
# 3、更新显示
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 用rect定义飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)
while True:
    # 制定循环体内部代码执行的频率
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否为退出
        if event.type == pygame.QUIT:
            print("退出游戏...")
        # 调用quit方法，退出游戏
            pygame.quit()
        # 退出系统
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= 0:
        hero_rect.y = 700
    pygame.display.update()
    pass
pygame.quit()