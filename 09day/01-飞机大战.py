import pygame
from machao import * 
pygame.init()
#游戏代码

screen = pygame.display.set_mode((480, 700))#创建游戏主窗口
bg = pygame.image.load("./images/background.png")#绘制背景图 加载图像
hero=pygame.image.load('./images/hero.gif')#加载图像
screen.blit(bg, (0, 0))#绘制在屏幕

screen.blit(hero,(200,500))#绘制屏幕的什么位置


clock=pygame.time.Clock()#创建游戏时钟对象
#i=0#创建游戏时钟对象

herorect=pygame.Rect(200,500,120,120)#定义英雄的初始位置

enemy = EnemySprite()#创建第一个敌机
enemy1 = EnemySprite()#创建第二个敌机
enemy1.rect.x = 100
enemy1.speed = 4
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:#游戏循环
	clock.tick(60)#设置刷屏帧率
	herorect.y-= 2 #更新英雄位置
	
	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)

	if herorect.bottom<=0: #如果移除屏幕
		herorect.top=700 #则英雄的顶部移动到屏幕底部
	
	enemy_group.update()
	enemy_group.draw(screen)
	
	pygame.display.update()
	for event in pygame.event.get():#事件监听
		if event.type==pygame.QUIT:#判断用户是否点击了关闭按钮
			print('退出系统')
			pygame.quit()
			#exit()  #直接退出系统


