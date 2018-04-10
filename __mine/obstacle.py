import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,panel,x,midY,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("obs.png")
        self.rect = self.image.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height
        self.screen = panel
        self.x = x
        diff = 64
        self.midY = midY
        self.y = midY + diff
        self.top = top
        if(top):
            self.y -= 512

        
        
        self.updateDisplay()

    def updateDisplay(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.rect.x,self.rect.y = self.x,self.y
        
    def step(self):
        self.x -= 3

        self.updateDisplay()

    def setMidY(self):
        self
