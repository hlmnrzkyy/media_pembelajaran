import pygame, random, sys, time, math
from pygame.locals import *
pygame.init()


## Declaration ##

# Colouring:
white      = [255,255,255]
grey       = [127,127,127]
red        = [255,  0,  0]
darkRed    = [127,  0,  0]
yellow     = [255,255,  0]
darkYellow = [127,127,  0]
green      = [  0,255,  0]
darkGreen  = [  0,127,  0]
blue       = [  0,  0,255]
blueSky    = [128,128,255]
suddenBlue = [  0,  0,192]
navyBlue   = [  0,  0,128]
purple     = [255,  0,255]
darkPurple = [127,  0,127]
black      = [  0,  0,  0]

# Initiate Display Surface:
surface=pygame.display.set_mode((800,600))
pygame.display.set_caption('Torricelli')
surface.fill(black)

# Set a Text:
font1 = pygame.font.Font(None, 20)
font2 = pygame.font.Font(None, 40)

# Set FPS:
FPS = 100
clock = pygame.time.Clock()

# Air yang Tertekan
dx = 0
dy = 0
t = 0
h = 0
H = 200

# Tinggi tiang
y = 0

# Simulasikan?
simulasikan = 'no'

# Posisi Kursor Mouse
xm = 0
ym = 0

## Main Game Loop: ##

while not False:

    if simulasikan == 'yes':

        # Menggambar
        pygame.draw.polygon(surface,red,((50,50+y),(199,50+y),(199,299+y),(50,299+y)))
        pygame.draw.polygon(surface,darkRed,((53,50+y),(196,50+y),(196,294+y),(53,294+y)))
        pygame.draw.polygon(surface,blue,((53,95+h+y),(196,95+h+y),(196,294+y),(53,294+y)))
        pygame.draw.polygon(surface,yellow,((50,300+y),(199,300+y),(199,309+y),(50,309+y)))
        pygame.draw.polygon(surface,yellow,((110,310+y),(139,310+y),(139,550),(110,550)))    
            
        # Celah Sempit
        pygame.draw.polygon(surface,blue,((197,292+y),(199,292+y),(199,294+y),(197,294+y)))

        # Air yang Tertekan

        pygame.draw.polygon(surface,blue,((197+dx,292+dy+y),(199+dx,292+dy+y),(199+dx,294+dy+y),(197+dx,294+dy+y)))

        t = t + 1/FPS
        High = (H/100)
        v = math.sqrt(2*10*High)
        dx = int(100*v*t)
        dy = int(100*5*t*t)

        # Menggambar Tanah
        pygame.draw.polygon(surface,green,((0,599),(0,545),(799,545),(799,599)))

        # Menggambar Penggaris
        xmeter = 0
        xnumber = 0
        for i in range(1,7):
            pygame.draw.line(surface,black,(199+xmeter, 545),(199+xmeter, 565))
            text5 = str(xnumber)
            text5 = font1.render(text5, not False, black)
            surface.blit(text5,[199+xmeter,565])
            xnumber = xnumber + 1
            xmeter = xmeter + 100
        xmeter = 0
        for i in range(1,6):
            pygame.draw.line(surface,black,(249+xmeter, 545),(249+xmeter, 555))
            xmeter = xmeter + 100
        xmeter = 0
        for i in range(1,50):
            pygame.draw.line(surface,black,(209+xmeter, 545),(209+xmeter, 550))
            xmeter = xmeter + 10
        ymeter = 0
        ynumber = 0
        for i in range(1,5):
            pygame.draw.line(surface,white,(30,545-ymeter),(49,545-ymeter))
            text6 = str(ynumber)
            text6 = font1.render(text6, not False, white)
            surface.blit(text6,[20,535-ymeter])
            ynumber = ynumber + 1
            ymeter = ymeter + 100
        ymeter = 0 
        for i in range(1,8):
            pygame.draw.line(surface,white,(40,545-ymeter),(49,545-ymeter))
            ymeter = ymeter + 50
        ymeter = 0
        for i in range(1,32):
            pygame.draw.line(surface,white,(45,545-ymeter),(49,545-ymeter))
            ymeter = ymeter + 10
        hmeter = 0
        hnumber = 0
        for i in range(1,4):
            pygame.draw.line(surface,white,(53,295-hmeter+y),(72,295-hmeter+y))
            text7 = str(hnumber)
            text7 = font1.render(text7, not False, white)
            surface.blit(text7,[72,285-hmeter+y])
            hnumber = hnumber + 1
            hmeter = hmeter + 100
        hmeter = 0 
        for i in range(1,5):
            pygame.draw.line(surface,white,(53,295-hmeter+y),(62,295-hmeter+y))
            hmeter = hmeter + 50
        hmeter = 0
        for i in range(1,21):
            pygame.draw.line(surface,white,(53,295-hmeter+y),(57,295-hmeter+y))
            hmeter = hmeter + 10

        text7 = 'h =         m'
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[250,50])
        strHigh = float(H/100)
        text7 = str(strHigh)
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[300,50])
        
        text7 = 'y =         m'
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[250,100])
        strY = float((250-y)/100)
        text7 = str(strY)
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[300,100])
        
        text7 = 'v =         m/s'
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[250,150])
        strV = round(v,2)
        text7 = str(strV)
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[300,150])

        text7 = 'x =         m'
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[250,200])
        intY = float((250-y)/100)
        fallTime = math.sqrt(intY/5)
        strX = v*fallTime 
        strX = round(strX,2)
        text7 = str(strX)
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[300,200])
        

    elif simulasikan == 'no':

        # Menggambar
        pygame.draw.polygon(surface,black,((0,0),(799,0),(799,599),(0,599)))
        pygame.draw.polygon(surface,red,((50,50+y),(199,50+y),(199,299+y),(50,299+y)))
        pygame.draw.polygon(surface,darkRed,((53,50+y),(196,50+y),(196,294+y),(53,294+y)))
        pygame.draw.polygon(surface,blue,((53,95+h+y),(196,95+h+y),(196,294+y),(53,294+y)))
        pygame.draw.polygon(surface,yellow,((50,300+y),(199,300+y),(199,309+y),(50,309+y)))
        pygame.draw.polygon(surface,yellow,((110,310+y),(139,310+y),(139,550),(110,550)))    
            
        # Celah Sempit
        pygame.draw.polygon(surface,blue,((197,292+y),(199,292+y),(199,294+y),(197,294+y)))

        # Menggambar Tanah
        pygame.draw.polygon(surface,green,((0,599),(0,545),(799,545),(799,599)))

        # Menggambar Penggaris
        xmeter = 0
        xnumber = 0
        for i in range(1,7):
            pygame.draw.line(surface,black,(199+xmeter, 545),(199+xmeter, 565))
            text5 = str(xnumber)
            text5 = font1.render(text5, not False, black)
            surface.blit(text5,[199+xmeter,565])
            xnumber = xnumber + 1
            xmeter = xmeter + 100
        xmeter = 0
        for i in range(1,6):
            pygame.draw.line(surface,black,(249+xmeter, 545),(249+xmeter, 555))
            xmeter = xmeter + 100
        xmeter = 0
        for i in range(1,50):
            pygame.draw.line(surface,black,(209+xmeter, 545),(209+xmeter, 550))
            xmeter = xmeter + 10
        ymeter = 0
        ynumber = 0
        for i in range(1,5):
            pygame.draw.line(surface,white,(30,545-ymeter),(49,545-ymeter))
            text6 = str(ynumber)
            text6 = font1.render(text6, not False, white)
            surface.blit(text6,[20,535-ymeter])
            ynumber = ynumber + 1
            ymeter = ymeter + 100
        ymeter = 0 
        for i in range(1,8):
            pygame.draw.line(surface,white,(40,545-ymeter),(49,545-ymeter))
            ymeter = ymeter + 50
        ymeter = 0
        for i in range(1,32):
            pygame.draw.line(surface,white,(45,545-ymeter),(49,545-ymeter))
            ymeter = ymeter + 10
        hmeter = 0
        hnumber = 0
        for i in range(1,4):
            pygame.draw.line(surface,white,(53,295-hmeter+y),(72,295-hmeter+y))
            text7 = str(hnumber)
            text7 = font1.render(text7, not False, white)
            surface.blit(text7,[72,285-hmeter+y])
            hnumber = hnumber + 1
            hmeter = hmeter + 100
        hmeter = 0 
        for i in range(1,5):
            pygame.draw.line(surface,white,(53,295-hmeter+y),(62,295-hmeter+y))
            hmeter = hmeter + 50
        hmeter = 0
        for i in range(1,21):
            pygame.draw.line(surface,white,(53,295-hmeter+y),(57,295-hmeter+y))
            hmeter = hmeter + 10

        text7 = 'h =         m'
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[250,50])
        strHigh = float(H/100)
        text7 = str(strHigh)
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[300,50])
        
        text7 = 'y =         m'
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[250,100])
        strY = float((250-y)/100)
        text7 = str(strY)
        text7 = font2.render(text7, not False, white)
        surface.blit(text7,[300,100])

    # Push Button Simulasikan
    pygame.draw.polygon(surface,navyBlue,((10,10),(149,10),(149,30),(10,30)))
    if xm < 149 and xm > 10 and ym < 30 and ym > 10:
        pygame.draw.polygon(surface,blue,((10,10),(149,10),(149,30),(10,30)))
    if simulasikan == 'no':
        text1 = 'SIMULASIKAN'
    if simulasikan == 'yes':
        text1 = 'ULANGI'
    text1 = font1.render(text1, not False, white)
    if simulasikan == 'no':
        surface.blit(text1,[35,15])
    if simulasikan == 'yes':
        surface.blit(text1,[55,15])

    if simulasikan == 'no':
        # Push Button Tambahkan h
        pygame.draw.polygon(surface,navyBlue,((160,10),(309,10),(309,30),(160,30)))
        if xm < 309 and xm > 160 and ym < 30 and ym > 10:
            pygame.draw.polygon(surface,blue,((160,10),(309,10),(309,30),(160,30)))
        text2 = 'TAMBAHKAN h'
        text2 = font1.render(text2, not False, white)
        surface.blit(text2,[185,15])

        # Push Button Kurangi h
        pygame.draw.polygon(surface,navyBlue,((320,10),(469,10),(469,30),(320,30)))
        if xm < 469 and xm > 320 and ym < 30 and ym > 10:
            pygame.draw.polygon(surface,blue,((320,10),(469,10),(469,30),(320,30)))
        text3 = 'KURANGI h'
        text3 = font1.render(text3, not False, white)
        surface.blit(text3,[360,15])

        # Push Button Tambahkan y
        pygame.draw.polygon(surface,navyBlue,((480,10),(629,10),(629,30),(480,30)))
        if xm < 629 and xm > 480 and ym < 30 and ym > 10:
            pygame.draw.polygon(surface,blue,((480,10),(629,10),(629,30),(480,30)))
        text4 = 'TAMBAHKAN y'
        text4 = font1.render(text4, not False, white)
        surface.blit(text4,[505,15])

        # Push Button Kurangi y
        pygame.draw.polygon(surface,navyBlue,((640,10),(789,10),(789,30),(640,30)))
        if xm < 789 and xm > 640 and ym < 30 and ym > 10:
            pygame.draw.polygon(surface,blue,((640,10),(789,10),(789,30),(640,30)))
        text5 = 'KURANGI y'
        text5 = font1.render(text5, not False, white)
        surface.blit(text5,[680,15])

    # Control an arrow with Mouse:
    pos = pygame.mouse.get_pos()
    xm = pos[0]
    ym = pos[1]

    # Control the Program:
    for event in pygame.event.get():

        # Simulasikan atau ulangi
        if xm < 149 and xm > 10 and ym < 30 and ym > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if simulasikan == 'no':
                    pygame.draw.polygon(surface,black,((0,0),(799,0),(799,599),(0,599)))
                    simulasikan = 'yes'
                elif simulasikan == 'yes':
                    t = 0
                    simulasikan = 'no'

        if simulasikan == 'no':

            # Tambahkan h
            if xm < 309 and xm > 160 and ym < 30 and ym > 10:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if h >= 25:
                        h = h - 25
                        H = H + 25

            # Kurangi h
            if xm < 469 and xm > 320 and ym < 30 and ym > 10:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if h <= 150:
                        h = h + 25
                        H = H - 25

            # Tambahkan y
            if xm < 629 and xm > 480 and ym < 30 and ym > 10:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if y >= 25:
                        y = y - 25

            # Kurangi y
            if xm < 789 and xm > 640 and ym < 30 and ym > 10:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if y <= 200:
                        y = y + 25
                    
        # Kill the Program:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update the Dislay:
    pygame.display.update()
    clock.tick(FPS)   