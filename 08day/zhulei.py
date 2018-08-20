import pygame
from machao import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)#出现敌机间隔时间,500毫秒
	def start_game(self):
		while True:
			#1.设置刷新帧率
			self.clock.tick(60)
			#2.事件监听
			self.__event_handler()
			#3.碰撞检测
			self.__check_collide()
			#4.更新精灵组
			self.__update_sprites()
			#5.更新屏幕显示
			pygame.display.update()
	def __create_sprites(self):#精灵组
		bg1 = BackGroundSprite()#敌人
		bg2 = BackGroundSprite(True)
		self.enemy_group = pygame.sprite.Group()
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		
		self.hero = Hero()#英雄
		self.hero_group = pygame.sprite.Group(self.hero)
		
		
	
	def __event_handler(self):#敌机精灵
		for event in pygame.event.get():#事件监听
			if event.type==pygame.QUIT:
				PlanGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:#敌机出场
				enemy = EnemySprite()
				self.enemy_group.add(enemy)#通过add方法添加
					
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 12
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -12
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -12
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 12
		else:
			self.hero.speed = 0
			self.hero.speed1 = 0
		if keys_pressed[pygame.K_SPACE]:
			self.hero.fire()

	def __check_collide(self):
		# 1. 子弹摧毁敌机
		pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True, True)

		# 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

		# 判断列表时候有内容
		if len(enemies) > 0:

			# 让英雄牺牲
			self.hero.kill()

			# 结束游戏
			PlaneGame.__game_over()
	def __update_sprites(self):#更新
		self.bg_group.update()
		self.bg_group.draw(self.screen)
		
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		
		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)
	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()

if __name__ == "__main__":
	game = PlaneGame()
	game.start_game()
	








