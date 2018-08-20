import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):

		# 调用父类的初始化方法
		super().__init__()

		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed

	def update(self, *args):

		# 默认在垂直方向移动
		self.rect.y += self.speed
class EnemySprite(GameSprite):
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

