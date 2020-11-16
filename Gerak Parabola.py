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
pygame.display.set_caption('Gerak Parabola')
surface.fill(blueSky)

# Set a Text:
font1 = pygame.font.Font(None, 24)

# Set FPS:
FPS = 100
clock = pygame.time.Clock()

# Set ball state:
vBall = 10
vBall0 = vBall
thetaBall0 = 45
vXBall = vBall0*math.cos(math.radians(thetaBall0))
vY0Ball = (vBall0*math.sin(math.radians(thetaBall0)))
t = 0
vYBall = vY0Ball - (9.8*t)
tBall = 0
xBall = 99
xBall0 = xBall
yBall = 449
yBall0 = yBall

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
    pygame.draw.polygon(surface,darkGreen,((0,10+450),(799,10+450),(799,599),(0,799)))

    # Draw a horizontal ruler:
    xRuler = 100
    for i in range (0,7):
        pygame.draw.line(surface,white,(xRuler,10+450),(xRuler,10+474),3)
        text = str(int(xRuler/10)-10)
        text = font1.render(text, not False, white)
        surface.blit(text,[xRuler,500])
        xRuler += 100
    xRuler = 100
    for i in range (0,13):
        pygame.draw.line(surface,white,(xRuler,10+450),(xRuler,10+464),2)
        xRuler += 50
    xRuler = 100
    for i in range (0,61):
        pygame.draw.line(surface,white,(xRuler,10+450),(xRuler,10+454),1)
        xRuler += 10
        
    # Draw a vertical ruler:
    yRuler = 449
    for i in range (0,4):
        pygame.draw.line(surface,white,(700,yRuler),(724,yRuler),3)
        text = str(45 - int(yRuler+1)/10)
        text = font1.render(text, not False, white)
        surface.blit(text,[750,yRuler])
        yRuler -= 100
    yRuler = 449
    for i in range (0,7):
        pygame.draw.line(surface,white,(700,yRuler),(714,yRuler),2)
        yRuler -= 50
    yRuler = 449
    for i in range (0,31):
        pygame.draw.line(surface,white,(700,yRuler),(704,yRuler),1)
        yRuler -= 10    
    
    # Draw a ball
    if simulateState == "off":
        xBallFinal = int(xBall)
        yBallFinal = int(yBall)
        pygame.draw.circle(surface,red,(xBallFinal,yBallFinal),10,0)
        
        text = "t= " + str(round(tBall,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall-105])   
        
        text = "vx= " + str(round(vXBall,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 85])
        
        text = "vy= " + str(round(vYBall,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 65])
        
        text = "x= " + str(round(((xBall+1)/10)-10,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 45])
        
        text = "y= " + str(round((45-((yBall+1)/10)),2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 25])
        
    elif simulateState == "on":
        t = 1/FPS
        tBall += t
        vXBall = vBall0*math.cos(math.radians(thetaBall0))
        xBall = xBall0 + 10*(vXBall*tBall)
        vY0Ball = (vBall0*math.sin(math.radians(thetaBall0)))
        vYBall = vY0Ball - (9.8*t)
        yBall = yBall0 - 10*(vYBall*tBall) + 10*(0.5*9.8*tBall*tBall)  
        xBallFinal = int(xBall)
        yBallFinal = int(yBall)
        pygame.draw.circle(surface,red,(xBallFinal,yBallFinal),10,0)
        vYBall0 = vYBall
        if yBallFinal == 449 or yBallFinal > 449:
            simulateState = "off"
        if xBallFinal == 699 or xBall > 699:
            simulateState = "off"            
        
        text = "t= " + str(round(tBall,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall-105])   
        
        text = "vx= " + str(round(vXBall,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 85])
        
        text = "vy= " + str(round(vYBall,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 65])
        
        text = "x= " + str(round(((xBall+1)/10)-10,2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 45])
        
        text = "y= " + str(round((45-((yBall+1)/10)),2))
        text = font1.render(text, not False, white)
        surface.blit(text,[xBall-50,yBall- 25])
    
    # Draw a line:
    pygame.draw.line(surface,white,(xBall,yBall),(xBall,10+449),1)
    pygame.draw.line(surface,white,(xBall,yBall),(699,yBall),1)
        
    # Caption for initial speed:
    text = 'Initial Speed:'
    text = font1.render(text, not False, white)
    surface.blit(text,[ 25, 25])   
        
    text = str(round(vBall0,2)) + " m/s"
    text = font1.render(text, not False, white)
    surface.blit(text,[ 80, 65])
    
    # Caption for initial angle:
    text = 'Initial Angle:'
    text = font1.render(text, not False, white)
    surface.blit(text,[200+ 25, 25])   
        
    text = str(round(thetaBall0,2)) + " deg"
    text = font1.render(text, not False, white)
    surface.blit(text,[200+ 80, 65])
    
    # Caption for initial altitude:
    text = 'Initial Altitude:'
    text = font1.render(text, not False, white)
    surface.blit(text,[400+ 25, 25])   
        
    text = str(round((45-((yBall0+1)/10)),2)) + " m"
    text = font1.render(text, not False, white)
    surface.blit(text,[400+ 80, 65])
    
    # Draw a push button while simulation turned off
    if simulateState == "off":
    
        # (-) button for initial speed:
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

        # (+) button for initial speed:
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
        
        # Reset initial speed button:
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
        text = 'Reset Speed'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # (-) button for initial angel:
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

        # (+) button for initial angle:
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
        
        # Reset initial angle button:
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
        text = 'Reset Angle'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # (-) button for initial altitude:
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

        # (+) button for initial altitude:
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
        
        # Reset initial altitude button:
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
        text = 'Reset Altitude'
        text = font1.render(text, not False,white)
        surface.blit(text,[xButton[0]+10,yButton[0]+5])
        
        # Simulate button:
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
        
        # Reset all button:
        xButton = [200+ 20,200+180,200+180,200+ 20]
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
        text = 'Reset All'
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
    
        if simulateState == "off":
    
            # Control "-" button for initial speed:
            xButton = [ 20, 50, 50, 20]
            yButton = [ 60, 60, 90, 90]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vBall0 -= 1
                    if vBall0 < 0:
                        vBall = 0
                        vBall0 = 0
                
            # Control "+" button for initial speed:
            xButton = [150,180,180,150]
            yButton = [ 60, 60, 90, 90]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vBall0 += 1
                    if vBall0 > 24:
                        vBall0 = 24
                        
            # Control "Reset Speed" Button:
            xButton = [ 20,180,180, 20]
            yButton = [100,100,130,130]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vBall0 = 10
            
            # Control "-" button for initial angle:
            xButton = [200+ 20,200+ 50,200+ 50,200+ 20]
            yButton = [ 60, 60, 90, 90]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    thetaBall0 -= 5
                    if thetaBall0 < 0 and yBall0 == 449:
                        thetaBall0 = 0
                    elif thetaBall0 < 0 and thetaBall0 > -90 and yBall0 < 449:
                        thetaBall0 -= 5
                    elif thetaBall0 < -90  and yBall0 < 449:
                        thetaBall0 = -90
                
            # Control "+" button for initial angle:
            xButton = [200+150,200+180,200+180,200+150]
            yButton = [ 60, 60, 90, 90]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    thetaBall0 += 5
                    if thetaBall0 > 90:
                        thetaBall0 = 90
                        
            # Control "Reset Angle" Button:
            xButton = [200+ 20,200+180,200+180,200+ 20]
            yButton = [100,100,130,130]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    thetaBall0 = 45
                    
            # Control "-" button for initial altitude:
            xButton = [400+ 20,400+ 50,400+ 50,400+ 20]
            yButton = [ 60, 60, 90, 90]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    yBall += 10
                    yBall0 += 10
                    if yBall > 449:
                        yBall = 449
                        yBall0 = 449                    
                
            # Control "+" button for initial altitude:
            xButton = [400+150,400+180,400+180,400+150]
            yButton = [ 60, 60, 90, 90]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    yBall -= 10
                    yBall0 -= 10
                    if yBall < 299:
                        yBall = 299
                        yBall0 = 299                    
                        
            # Control "Reset Altitude" Button:
            xButton = [400+ 20,400+180,400+180,400+ 20]
            yButton = [100,100,130,130]
            if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    yBall = 449
                    yBall0 = 449
                
        # Control "Simulate" button:
        xButton = [ 20,180,180, 20]
        yButton = [140,140,170,170]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if simulateState == "off":
                    simulateState = "on"
                elif simulateState == "on":
                    simulateState = "off"
        
        # Control "Reset All" button:
        xButton = [200+ 20,200+180,200+180,200+ 20]
        yButton = [140,140,170,170]
        if xMouse > xButton[0] and xMouse < xButton[1] and yMouse > yButton[0] and yMouse < yButton[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if simulateState == "off":
                    vBall = 10
                    vBall0 = vBall
                    thetaBall0 = 45
                    tBall = 0
                    xBall = 99
                    xBall0 = xBall
                    yBall = 449
                    yBall0 = yBall
                    
        # Kill the Program:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update the Dislay:
    pygame.display.update()
    clock.tick(FPS)   
    
os.system("pause")