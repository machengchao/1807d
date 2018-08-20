import pygame
from machao import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
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
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()
	def __event_handler(self):
		for event in pygame.event.get():#事件监听
			if event.type==pygame.QUIT:
				PlanGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print("敌机出场")
				enemy = EnemySprite()
				self.enemy_group.add(enemy)

	def __check_collide(self):
		pass
	def __update_sprites(self):
		self.bg_group.update()
		self.bg_group.draw(self.screen)
		
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		
	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()

if __name__ == "__main__":
	game = PlaneGame()
	game.start_game()
	








