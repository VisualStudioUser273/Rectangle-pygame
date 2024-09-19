import pygame

WIDTH=500
HEIGHT=500

pygame.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))

class cir():
    def __init__(self,color,dimensions):
          self.cir_color=color
          self.size=dimensions
          self.surface=screen

    def create_cir(self):
           pygame.draw.circle(self.surface,self.rect_color,self.size) 


#Creating Objects Within Pygame


green_circle=cir('green',(30,40,34,57))
green_circle.create_cir()

red_rect=green_circle('red',(40,50,65,57))
red_rect.create_cir()

pygame.display.update()
            
     


