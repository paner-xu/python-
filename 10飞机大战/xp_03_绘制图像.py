# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/3/12 12:16'
__author__ = 'Colby'
import pygame
pygame.init()
screen = pygame.display.set_mode((480, 700))
# 1、图片加载
by = pygame.image.load("./images/background.png")
# 2、指定位置
screen.blit(by, (0, 0))
# 3、更新显示
pygame.display.update()
# while True:
#     pass
pygame.quit()