import pygame
import sys
import os
import easygui    
import time
import random

#dir of this script
scriptdirfolder = os.path.dirname(os.path.realpath(__file__))

#different types of slashes just in case if something goes wrong
if scriptdirfolder.find('\\') != -1:
    slash = '\\'
else:
    slash = '/'




renderer_dir = scriptdirfolder+slash+'RENDERER.py'
editor_dir = scriptdirfolder+slash+'EDITOR.py'

#checks if the RENDERER.py exists
while True:
    try:
        open(renderer_dir).close()
        break
    except FileNotFoundError:
        print('The RENDERER file was not found in the script folder. Please return the RENDERER file back to the folder for proper functioning.')
        time.sleep(999999999)
        continue

#checks if the EDITOR.py exists
while True:
    try:
        open(editor_dir).close()
        break
    except FileNotFoundError:
        print('The EDITOR file was not found in the script folder. Please return the EDITOR file back to the folder for proper functioning.')
        time.sleep(999999999)
        continue



white = 255,255,255
black = 0,0,0

animationopacity = 0



pygame.init()

window = pygame.display.set_mode((480,480))


def fontsinit():
    global BIGfont
    global nobigfont
    global errorfont
    global smalllilguyfont
    BIGfont = pygame.font.SysFont('couriernew', 56)
    nobigfont = pygame.font.SysFont('couriernew', 25)
    errorfont = pygame.font.SysFont('couriernew', 20)
    smalllilguyfont = pygame.font.SysFont('couriernew', 16)
    

fontsinit()

def mainframe():
    global animationopacity

    BIGtext = BIGfont.render('SONG SUBTITLE',True,(black))

    editortext = nobigfont.render('Editor',True,(black))
    renderertext = nobigfont.render('Renderer',True,(black))
    helptext = nobigfont.render('Help',True,(black))
    settingstext = nobigfont.render('Settings',True,(black))

    notrightfiletext1 = errorfont.render("That's not a",True,(black))
    notrightfiletext2 = errorfont.render("right file format.",True,(black))
    notrightfiletext1.set_alpha(animationopacity)
    notrightfiletext2.set_alpha(animationopacity)


    window.fill((white)),

    window.blit(BIGtext,(20,120)),


    pygame.draw.circle(window,(black),(60,300),40.0,2,False,True,True,False),
    pygame.draw.line(window,(black),(60,260),(180,260),2),
    pygame.draw.circle(window,(black),(180,300),40.0,2,True,False,False,True),
    pygame.draw.line(window,(black),(60,338),(180,338),2),

    window.blit(renderertext,(60,285)),

    pygame.draw.circle(window,(black),(420,300),40.0,2,True,False,False,True),
    pygame.draw.line(window,(black),(420,260),(300,260),2),
    pygame.draw.circle(window,(black),(300,300),40.0,2,False,True,True,False),
    pygame.draw.line(window,(black),(420,338),(300,338),2),

    window.blit(editortext,(315,285)),

    pygame.draw.circle(window,(black),(180,400),40.0,2,False,True,True,False),
    pygame.draw.line(window,(black),(180,360),(300,360),2),
    pygame.draw.circle(window,(black),(300,400),40.0,2,True,False,False,True),
    pygame.draw.line(window,(black),(180,438),(300,438),2),   

    window.blit(helptext,(208,388)),

    window.blit(settingstext,(355,450)),

    window.blit(notrightfiletext1,(5,435)),
    window.blit(notrightfiletext2,(5,455)),

    if animationopacity > 0:
        animationopacity -= 1
        notrightfiletext1.set_alpha(animationopacity)
        notrightfiletext2.set_alpha(animationopacity)


    #hitboxes render if devmode activates
    if devmode == True:
        pygame.draw.lines(window,(255,0,0),False,[(355,450),(475,450),(475,475),(355,475),(355,450)])
        pygame.draw.lines(window,(255,0,0),False,[(140,440),(340,440),(340,360),(140,360),(140,440)])
        pygame.draw.lines(window,(255,0,0),False,[(460,260),(260,260),(260,340),(460,340),(460,260)])
        pygame.draw.lines(window,(255,0,0),False,[(20,260),(220,260),(220,340),(20,340),(20,260)])


    pygame.display.update()

    



#i got a little silly :3
randomphrase = 1
darkmodephrases = {
    1: 'AHH MY EYES HURT',
    2: 'No vitamin D today',
    3: 'Im a vampire',
    4: 'racism.',
    5: 'no whites today',
    6: 'profecional racist'
}

def settingframe():
    global randomphrase


    darkmodesettingtext = smalllilguyfont.render('"'+darkmodephrases[randomphrase]+'" setting (dark mode): '+str(darkmodeswitch),True,(black))
    windowscalesettingtext = smalllilguyfont.render('Window scaling = '+str(windowscaling),True,(black))
    fullscreensettingtext = smalllilguyfont.render('Fullscreen = '+str(fullscreen),True,(black))

    backtext = nobigfont.render('Back',True,(black))


    window.fill((white))
    window.blit(darkmodesettingtext,(5,5))
    window.blit(windowscalesettingtext,(5,25))
    window.blit(fullscreensettingtext,(5,45))


    pygame.draw.lines(window,(black),False,[(5,450),(70,450),(70,475),(5,475),(5,450)],3)
    window.blit(backtext,(7,450))


    #hitboxes render if devmode activates
    if devmode == True:
        pygame.draw.lines(window,(255,0,0),False,[(0,25),(480,25)])
        pygame.draw.lines(window,(255,0,0),False,[(0,45),(480,45)])
        pygame.draw.lines(window,(255,0,0),False,[(0,65),(480,65)])
        pygame.draw.lines(window,(255,0,0),False,[(5,450),(70,450),(70,475),(5,475),(5,450)])
    pygame.display.update()

def helpframe():
    placeholdertext = smalllilguyfont.render('this is a placeholder',True,(black))

    backtext = nobigfont.render('Back',True,(black))
    window.fill((white))
    window.blit(placeholdertext,(5,5))

    pygame.draw.lines(window,(black),False,[(5,450),(70,450),(70,475),(5,475),(5,450)],3)
    window.blit(backtext,(7,450))

    if devmode == True:
        pygame.draw.lines(window,(255,0,0),False,[(5,450),(70,450),(70,475),(5,475),(5,450)])
    pygame.display.update()



mainscene = True
helpscene = False
settingsscene = False

try:
    try:
        if open(scriptdirfolder+slash+'settings.ini','r').readlines()[0] == 'DarkMode = True\n':
            darkmodeswitch = True
            white = 0,0,0
            black = 255,255,255
        else:
            darkmodeswitch = False
    except IndexError:
        allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
        allsettings.insert(0,'DarkMode = False\n')
        open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
        darkmodeswitch = False
    
    try:
        if open(scriptdirfolder+slash+'settings.ini','r').readlines()[1] == 'WindowScaling = True\n':
            windowscaling = True
        else:
            windowscaling = False
    except IndexError:
        allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
        allsettings.insert(1,'WindowScaling = False\n')
        open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
        windowscaling = False

    try:
        if open(scriptdirfolder+slash+'settings.ini','r').readlines()[2] == 'Fullscreen = True\n':
            fullscreen = True
        else:
            fullscreen = False
    except IndexError:
        allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
        allsettings.insert(2,'Fullscreen = False\n')
        open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
        fullscreen = False

except FileNotFoundError:
    open(scriptdirfolder+slash+'settings.ini','w').writelines('DarkMode = False\nWindowScaling = False\nFullscreen = False\n')
    darkmodeswitch = False
    windowscaling = False
    fullscreen = False



if windowscaling == True:
    pygame.quit()
    pygame.init()
    window = pygame.display.set_mode((480,480),pygame.SCALED)
    fontsinit()

if fullscreen == True:
    pygame.quit()
    pygame.init()
    window = pygame.display.set_mode((480,480),pygame.FULLSCREEN)
    fontsinit()


lastpressed12keyboardbuttons = []
devmode = False

while True:
    
    if len(lastpressed12keyboardbuttons) > 12:
        lastpressed12keyboardbuttons.pop(0)
    if lastpressed12keyboardbuttons == ['j','a','k','e','i','s','a','l','i','v','e','e']:
        lastpressed12keyboardbuttons = []
        temp = devmode
        if temp == False:
            devmode = True
        if temp == True:
            devmode = False

    if mainscene == True:

        mainframe()

        for event in pygame.event.get():
            
            if event.type == pygame.TEXTINPUT:
                lastpressed12keyboardbuttons = lastpressed12keyboardbuttons + list(event.text)

            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:

                #editor button hitbox down below
                if event.pos[0] > 260 and event.pos[0] < 460 and event.pos[1] > 260 and event.pos[1] < 340:
                    pygame.quit()
                    exec(open(editor_dir).read())
                    sys.exit()

                #help button hitbox down below
                if event.pos[0] > 140 and event.pos[0] < 340 and event.pos[1] > 360 and event.pos[1] < 440:
                    helpscene = True
                    mainscene = False

                #settings button hitbox down below
                if event.pos[0] > 355 and event.pos[0] < 475 and event.pos[1] > 450 and event.pos[1] < 475:
                    randomphrase = random.randint(1,6)
                    settingsscene = True
                    mainscene = False

            if event.type == pygame.MOUSEBUTTONUP:

                #renderer button hitbox down below
                if event.pos[0] > 20 and event.pos[0] < 220 and event.pos[1] > 260 and event.pos[1] < 340:

                    filetorenderDIR = easygui.fileopenbox('Choose an .sbtitl file to render','Renderer')

                    try:
                        if filetorenderDIR[len(filetorenderDIR)-7:len(filetorenderDIR)] != '.sbtitl':
                            animationopacity = 255

                        if filetorenderDIR[len(filetorenderDIR)-7:len(filetorenderDIR)] == '.sbtitl':
                            pygame.quit()
                            exec(open(renderer_dir).read(),{'filetorenderDIR':filetorenderDIR})
                            sys.exit()

                    except TypeError:
                        animationopacity = 255

            print(event)
        pygame.time.Clock().tick(60)

    if settingsscene == True:
        settingframe()
        
        for event in pygame.event.get():

            if event.type == pygame.TEXTINPUT:
                lastpressed12keyboardbuttons = lastpressed12keyboardbuttons + list(event.text) 

            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                #dark mode hitbox down below
                if event.pos[1] < 25:
                    temp = darkmodeswitch
                    if temp == True:
                        try:
                            allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
                            allsettings.pop(0)
                            allsettings.insert(0,'DarkMode = False\n')
                            open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
                        except FileNotFoundError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('DarkMode = False\n')
                        except IndexError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('DarkMode = False\n')
                            
                        darkmodeswitch = False
                        black = 0,0,0
                        white = 255,255,255

                    if temp == False:
                        try:
                            allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
                            allsettings.pop(0)
                            allsettings.insert(0,'DarkMode = True\n')
                            open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
                        except FileNotFoundError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('DarkMode = True\n')
                        except IndexError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('DarkMode = True\n')
                        darkmodeswitch = True
                        black = 255,255,255
                        white = 0,0,0

                if event.pos[1] > 25 and event.pos[1] < 45:
                    
                    temp = windowscaling
                    if temp == True:
                        try:
                            allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
                            allsettings.pop(1)
                            allsettings.insert(1,'WindowScaling = False\n')
                            open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
                        except FileNotFoundError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('WindowScaling = False\n')
                        except IndexError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('WindowScaling = False\n')
                            
                        windowscaling = False
                        if fullscreen == True:
                            pass
                        else:
                            pygame.quit()
                            pygame.init()
                            window = pygame.display.set_mode((480,480))
                            fontsinit()

                        
                        

                    if temp == False:
                        try:
                            allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
                            allsettings.pop(1)
                            allsettings.insert(1,'WindowScaling = True\n')
                            open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
                        except FileNotFoundError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('WindowScaling = True\n')
                        except IndexError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('WindowScaling = True\n')
                            
                        windowscaling = True
                        if fullscreen == True:
                            pass
                        else:
                            pygame.quit()
                            pygame.init()
                            window = pygame.display.set_mode((480,480),pygame.SCALED)
                            fontsinit()
                        
                        


                if event.pos[1] > 45 and event.pos[1] < 65:

                    temp = fullscreen
                    if temp == True:
                        try:
                            allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
                            allsettings.pop(2)
                            allsettings.insert(2,'Fullscreen = False\n')
                            open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
                        except FileNotFoundError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('Fullscreen = False\n')
                        except IndexError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('Fullscreen = False\n')
                            
                        fullscreen = False
                        if windowscaling == True:
                            pygame.quit()
                            pygame.init()
                            window = pygame.display.set_mode((480,480),pygame.SCALED)
                            fontsinit()
                        else:
                            pygame.quit()
                            pygame.init()
                            window = pygame.display.set_mode((480,480))
                            fontsinit()
                        
                        

                    if temp == False:
                        try:
                            allsettings = open(scriptdirfolder+slash+'settings.ini','r').readlines()
                            allsettings.pop(2)
                            allsettings.insert(2,'Fullscreen = True\n')
                            open(scriptdirfolder+slash+'settings.ini','w').writelines(allsettings)
                        except FileNotFoundError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('Fullscreen = True\n')
                        except IndexError:
                            open(scriptdirfolder+slash+'settings.ini','w').writelines('Fullscreen = True\n')
                            
                        fullscreen = True
                        pygame.quit()
                        pygame.init()
                        window = pygame.display.set_mode((480,480),pygame.SCALED | pygame.FULLSCREEN)
                        fontsinit()
                        
                        

                    
                if event.pos[0] > 5 and event.pos[0] < 70 and event.pos[1] > 450 and event.pos[1] < 475:
                    settingsscene = False
                    mainscene = True

            print(event)
        pygame.time.Clock().tick(60)

    if helpscene == True:
        helpframe()

        for event in pygame.event.get():

            if event.type == pygame.TEXTINPUT:
                lastpressed12keyboardbuttons = lastpressed12keyboardbuttons + list(event.text) 

            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.pos[0] > 5 and event.pos[0] < 70 and event.pos[1] > 450 and event.pos[1] < 475:
                    helpscene = False
                    mainscene = True

        pygame.time.Clock().tick(60)

