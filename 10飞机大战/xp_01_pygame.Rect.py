import pygame
hero_rect = pygame.Rect(200, 500, 120, 125)
print("英雄的原点为%d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸是%d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
