import pygame
from datetime import datetime
from random import randint

pygame.init()

image_variations = 3

winx = 1000
winy = 1000
win = pygame.display.set_mode((winx, winy))

white = (255, 255, 255)

run = True
old_time = ''
while run:
     
    with open('menu.txt', 'r') as menu_file:
        menu = menu_file.readlines()

        if 'cheat = true' in menu:
            cheat = True

        else:
            cheat = False
    
    now = datetime.now()
    complete_time = now.strftime("%H:%M")
    
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    
    if current_hour[0] == '0':
        current_hour = current_hour[1:]
        

    if current_minute[0] == '0':
        current_minute = current_minute[1:]
        
    
    current_time = current_hour + current_minute

    if current_time != old_time:

        if cheat == True:
            pygame.display.set_caption('Time is: '+complete_time)

        else:
            pygame.display.set_caption('Short On Time')
            
        win.fill(white)

        semicolon = pygame.image.load('images/semicolon.png')
        semicolon_rect = semicolon.get_rect()
        win.blit(semicolon, ((winx-semicolon_rect.width)/2, (winy - semicolon_rect.height)/2))
        
        random_image_number = str(randint(0, image_variations-1))
        
        if random_image_number == '0':
            top_image = pygame.image.load('images/complicated-equation-that-equals-'+current_hour+'.png')
            bottom_image = pygame.image.load('images/complicated-equation-that-equals-'+current_minute+'.png')
            
        else:
            top_image = pygame.image.load('images/complicated-equation-that-equals-'+current_hour+' ('+random_image_number+').png')
            bottom_image = pygame.image.load('images/complicated-equation-that-equals-'+current_minute+' ('+random_image_number+').png')

        top_image_rect = top_image.get_rect()
        bottom_image_rect = bottom_image.get_rect()

        win.blit(top_image, ((winx-top_image_rect.width)/2, (winy/5) - (top_image_rect.height/2)))
        win.blit(bottom_image, ((winx-bottom_image_rect.width)/2, (4*(winy/5)) - (bottom_image_rect.height/2)))

        pygame.display.update()


        old_time = current_time
           

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() 

pygame.quit()
