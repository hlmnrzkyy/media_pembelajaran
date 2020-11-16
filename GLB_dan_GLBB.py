import pygame, random, sys, time, math
from pygame.locals import *
pygame.init()

###################
##               ##
##  Declaration  ##
##               ##
###################

# Colouring:
white      = [255,255,255]
grey       = [127,127,127]
darkGrey   = [ 63, 63, 63]
red        = [255,  0,  0]
darkRed    = [127,  0,  0]
yellow     = [255,255,  0]
darkYellow = [127,127,  0]
green      = [  0,255,  0]
darkGreen  = [  0,127,  0]
blue       = [  0,  0,255]
blueSky    = [ 32, 32,255]
navyBlue   = [  0,  0,128]
purple     = [255,  0,255]
darkPurple = [127,  0,127]
black      = [  0,  0,  0]

# Initiate Display Surface:
surface=pygame.display.set_mode((800,600))
pygame.display.set_caption('GLB dan GLBB')
surface.fill(blueSky)

# Set a Text:
font1 = pygame.font.Font(None, 24)

# Set FPS:
FPS = 100
clock = pygame.time.Clock()

# Set car state:
tCar = 0
tCar0 = tCar
aCar = 0
aCar0 = aCar
vCar = 10
vCar0 = vCar
xCar = 99
xCar0 = xCar


# Simulate state:
simulateState = "off"

# Set mouse position:
xMouse = 0
yMouse = 0

#######################
##                   ##
##  Main Game Loop:  ##
##                   ##
#######################


while not False:

    # Draw Sky
    surface.fill(blueSky)
    
    # Draw a land:
    pygame.draw.polygon(surface,darkGreen,((0,450),(799,450),(799,599),(0,799)))

    # Draw a ruler:
    xRuler = 100
    for i in range (0,7):
        pygame.draw.line(surface,white,(xRuler,450),(xRuler,474),3)
        text = str(int(xRuler/10)-10)
        text = font1.render(text, not False, white)
        surface.blit(text,[xRuler,500])
        xRuler += 100
    xRuler = 100
    for i in range (0,13):
        pygame.draw.line(surface,white,(xRuler,450),(xRuler,464),2)
        xRuler += 50
    xRuler = 100
    for i in range (0,61):
        pygame.draw.line(surface,white,(xRuler,450),(xRuler,454),1)
        xRuler += 10

    # Draw a car
    if simulateState == "off":
        xCar = xCar
        pygame.draw.polygon(surface,red,(
            (xCar-50,425),
            (xCar-20,425),
            (xCar-10,434),
            (xCar-00,439),
            (xCar-00,449),
            (xCar-50,449)))         
            
        text = "t= " + str(round(tCar,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425-100])   
        
        text = "a= " + str(round(aCar,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425- 75])
        
        text = "v= " + str(round(vCar,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425- 50])
        
        text = "x= " + str(round(((xCar+1)/10)-10,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425- 25])
        
    elif simulateState == "on":
        t = 1/FPS
        tCar += t
        vCar = vCar + aCar*t
        xCar = xCar + 10*(vCar*t) + 10*(0.5*aCar*t*t)
        pygame.draw.polygon(surface,red,(
            (xCar-50,425),
            (xCar-20,425),
            (xCar-10,434),
            (xCar-00,439),
            (xCar-00,449),
            (xCar-50,449)))
        if xCar >= 699 and vCar > 0:
            simulateState = "off"       
        elif xCar <= 99 and vCar < 0:
            simulateState = "off"
            
        text = "t= " + str(round(tCar,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425-100])   
        
        text = "a= " + str(round(aCar,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425- 75])
        
        text = "v= " + str(round(vCar,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425- 50])
        
        text = "x= " + str(round(((xCar+1)/10)-10,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xCar-50,425- 25])
        
    # Caption for initail time:
    text = 'Initial Time:'
    text = font1.render(text, not False, white)
    surface.blit(text,[ 25, 25])   
        
    text = str(round(tCar0,2)) + " s"
    text = font1.render(text, not False, white)
    surface.blit(text,[ 80, 65])
    
    # Caption for initial acceleration:
    text = 'Initial Acceleration:'
    text = font1.render(text, not False, white)
    surface.blit(text,[200+ 25, 25])   
        
    text = str(round(aCar,2)) + " m/s^2"
    text = font1.render(text, not False, white)
    surface.blit(text,[200+ 80, 65])
        
    # Caption for initial velocity:
    text = 'Initial Velocity:'
    text = font1.render(text, not False, white)
    surface.blit(text,[400+ 25, 25])   
        
    text = str(round(vCar0,2)) + " m/s"
    text = font1.render(text, not False, white)
    surface.blit(text,[400+ 80, 65])
    
    # Caption for initial position:
    text = 'Initial Position:'
    text = font1.render(text, not False, white)
    surface.blit(text,[600+ 25, 25])   
        
    text = str(round(((xCar0+1)/10-10),2)) + " m"
    text = font1.render(text, not False, white)
    surface.blit(text,[600+ 80, 65])

    # Draw a push button while simulation turned off
    if simulateState == "off":
    
        # (-) button for initial time:
        xButton = [ 20, 50, 50, 20]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkRed,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,red,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '-'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])

        # (+) button for initial time:
        xButton = [150,180,180,150]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkGreen,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,green,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '+'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # Reset time button:
        xButton = [ 20,180,180, 20]
        yButton = [100,100,130,130]
        pygame.draw.polygon(surface,darkGrey,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,grey,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = 'Reset time'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5]) 
        
        # (-) button for initial acceleration:
        xButton = [200+ 20,200+ 50,200+ 50,200+ 20]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkRed,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,red,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '-'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])

        # (+) button for initial acceleration:
        xButton = [200+150,200+180,200+180,200+150]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkGreen,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,green,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '+'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # Reset acceleration button:
        xButton = [200+ 20,200+180,200+180,200+ 20]
        yButton = [100,100,130,130]
        pygame.draw.polygon(surface,darkGrey,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,grey,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = 'Reset acceleration'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
    
        # (-) button for initial velocity:
        xButton = [400+ 20,400+ 50,400+ 50,400+ 20]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkRed,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,red,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '-'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])

        # (+) button for initial velocity:
        xButton = [400+150,400+180,400+180,400+150]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkGreen,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,green,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '+'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # Reset velocity Button:
        xButton = [400+ 20,400+180,400+180,400+ 20]
        yButton = [100,100,130,130]
        pygame.draw.polygon(surface,darkGrey,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,grey,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = 'Reset Velocity'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # (-) button for initial position:
        xButton = [600+ 20,600+ 50,600+ 50,600+ 20]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkRed,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,red,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '-'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
                
        # (+) button for initial position:
        xButton = [600+150,600+180,600+180,600+150]
        yButton = [ 60, 60, 90, 90]
        pygame.draw.polygon(surface,darkGreen,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,green,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = '+'
        text = font1.render(text, not False, white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])       
        
        # Reset Position Button:
        xButton = [600+ 20,600+180,600+180,600+ 20]
        yButton = [100,100,130,130]
        pygame.draw.polygon(surface,darkGrey,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,grey,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = 'Reset Position'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])

        # Simulate Button:
        xButton = [ 20,180,180, 20]
        yButton = [140,140,170,170]
        pygame.draw.polygon(surface,darkGrey,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,grey,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = 'Simulate'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
    
    # Draw a push button while simulation turned on
    elif simulateState == "on":
        # Stop Simulution Button:
        xButton = [ 20,180,180, 20]
        yButton = [140,140,170,170]
        pygame.draw.polygon(surface,darkGrey,(
            (xButton[0],yButton[0]),
            (xButton[1],yButton[1]),
            (xButton[2],yButton[2]),
            (xButton[3],yButton[3])))
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            pygame.draw.polygon(surface,grey,(
                (xButton[0],yButton[0]),
                (xButton[1],yButton[1]),
                (xButton[2],yButton[2]),
                (xButton[3],yButton[3])))
        text = 'Stop Simulate'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        

    # Control an arrow with a mouse:
    mousePosition = pygame.mouse.get_pos()
    xMouse = mousePosition[0]
    yMouse = mousePosition[1]
     
    ###########################
    ##                       ##
    ##  Control the pygame:  ##
    ##                       ##
    ###########################
    for event in pygame.event.get():
        
        # Control "-" button for initial time:
        xButton = [ 20, 50, 50, 20]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                tCar -= 1
            
        # Control "+" button for initial time:
        xButton = [150,180,180,150]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                tCar += 1
                    
        # Control "Reset time" Button:
        xButton = [ 20,180,180, 20]
        yButton = [100,100,130,130]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                tCar = 0
                
        # Control "-" button for initial acceleration:
        xButton = [200+ 20,200+ 50,200+ 50,200+ 20]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                aCar -= 1
            
        # Control "+" button for initial aceeleration:
        xButton = [200+150,200+180,200+180,200+150]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                aCar += 1
                    
        # Control "Reset acceleration" Button:
        xButton = [200+ 20,200+180,200+180,200+ 20]
        yButton = [100,100,130,130]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                aCar = 0
                
        # Control "-" button for initial velocity:
        xButton = [400+ 20,400+ 50,400+ 50,400+ 20]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                vCar -= 1
                vCar0 -= 1
                if vCar < 0 and xCar == 99:
                    vCar = 0
                    vCar0 = 0
            
        # Control "+" button for initial velocity:
        xButton = [400+150,400+180,400+180,400+150]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                vCar += 1
                vCar0 += 1
                if vCar > 0 and xCar == 699:
                    vCar = 0
                    vCar0 = 0
                    
        # Control "Reset Velocity" Button:
        xButton = [400+ 20,400+180,400+180,400+ 20]
        yButton = [100,100,130,130]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                vCar = 10
                vCar0 = 10
        
        # Control "-" button for initial position:
        xButton = [600+ 20,600+ 50,600+ 50,600+ 20]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                xCar -= 10
                xCar0 -= 10
                if xCar<99:
                    xCar = 99
                    xCar0 = 99
            
        # Control "+" button for initial position:
        xButton = [600+150,600+180,600+180,600+150]
        yButton = [ 60, 60, 90, 90]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                xCar += 10
                xCar0 += 10
                if xCar>699:
                    xCar = 699
                    xCar0 = 699
                    
        # Control "Reset Position" Button:
        xButton = [600+ 20,600+180,600+180,600+ 20]
        yButton = [100,100,130,130]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                xCar = 99
                xCar0 = 99
        
        # Control "Simulate" button:
        xButton = [ 20,180,180, 20]
        yButton = [140,140,170,170]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if simulateState == "off" and xCar == 99 and vCar > 0:
                    simulateState = "on"
                elif simulateState == "off" and xCar == 99 and vCar < 0:
                    simulateState = "off"
                elif simulateState == "off" and xCar == 699 and vCar < 0:
                    simulateState = "on"
                elif simulateState == "off" and xCar == 699 and vCar > 0:
                    simulateState = "off"
                elif simulateState == "off" and xCar > 99 and xCar < 699:
                    simulateState = "on"
                elif simulateState == "on":
                    simulateState = "off"
                   
        # Kill the Program:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update the Dislay:
    pygame.display.update()
    clock.tick(FPS)   
    
os.system("pause")