import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1,speed1=1):

		# 调用父类的初始化方法
		super().__init__()

		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed
		self.speed1 = speed1
	def update(self, *args):

		# 默认在垂直方向移动
		self.rect.y += self.speed

class EnemySprite(GameSprite):#敌机
	def __init__(self):
		self.imagename = "./images/enemy1.png"
		super().__init__(self.imagename)
		self.speed = random.randint(1, 10)
	
		# 3. 设置敌机的随机初始位置
		self.rect.bottom = 0

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, max_x)
	def update(self):
		super().update()

class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename="./images/background.png"
		super().__init__(self.imagename,5)
		if is_alt:
			self.rect.y = - self.rect.height
	def update(self):
		super().update()	
		if self.rect.top>=SCREEN_RECT.height:
			self.rect.y = - self.rect.height
		elif self.rect.y>=SCREEN_RECT.height: 
			self.kill()

class Hero(GameSprite):
	#"""英雄精灵"""
	def __init__(self):
		super().__init__("./images/hero.gif", 10)
		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 60
		self.bullet_group = pygame.sprite.Group()#子弹
	def update(self):
		# 飞机水平移动
		self.rect.x += self.speed
		self.rect.y += self.speed1
		# 判断屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
	def fire(self):
		bullet= BulletSprite()#创建多发子弹
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.y = self.rect.top - 18
		self.bullet_group.add(bullet)	
			
		bullet1= BulletSprite()
		bullet1.rect.centerx = self.rect.centerx -36
		bullet1.rect.y = self.rect.top - 20
		self.bullet_group.add(bullet1)
		
		bullet2 = BulletSprite()
		bullet2.rect.centerx = self.rect.centerx + 36
		bullet2.rect.y = self.rect.top - 20
		self.bullet_group.add(bullet2)	



class BulletSprite(GameSprite):#子弹精灵
	def __init__(self):
		self.imagename = "./images/bullet.png"
		super().__init__(self.imagename,-8)
	
	def update(self):
		super().update()
		if self.rect.bottom <= 0:#销毁子弹
			self.kill()
