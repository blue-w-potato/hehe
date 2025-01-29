import pygame as pg
import os

pg.init()
screen = pg.display.set_mode(( 480, 720 ))
pg.display.set_caption("hun?")
clock = pg.time.Clock()

images = {
    "background" : pg.image.load( os.path.join("hey", "image/background.png") ).convert(),
    "paw" : pg.image.load( os.path.join("hey", "image/paw.png") ).convert()
}

class Paw(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.original_image = images['paw']  
        self.images = []  
        for angle in range(0, 361, 5):
            rotated_image = pg.transform.rotate(self.original_image, angle)
            self.images.append(rotated_image)
        self.current_angle_index = 0 
        self.image = self.images[self.current_angle_index] 
        self.rect = self.image.get_rect()
        self.rect.center = (240, 0)
        self.turn = True
    
    def update(self):
        if self.current_angle_index == 45//5 or self.current_angle_index == 315//5:
            self.turn = not self.turn
        if self.turn:
            self.current_angle_index = (self.current_angle_index + 1) % len(self.images) 
        else:
            self.current_angle_index = (self.current_angle_index - 1) % len(self.images)  
        
        self.image = self.images[self.current_angle_index]  
        self.rect = self.image.get_rect(center=self.rect.center)

all_sprites = pg.sprite.Group()
paw = Paw()
all_sprites.add(paw)

running = True
FPS = 25

while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    
    screen.blit(images['background'], (0,0))
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.update()


pg.quit()