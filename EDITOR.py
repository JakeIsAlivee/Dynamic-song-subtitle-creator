import pygame
import sys
import os
import time
import easygui  

from tkinter import messagebox

import random

"""
Before you start throwing tomatoes at me, i know this code is bad
Lets just collectively agree that it just works, okay?

"""





#more lines != good code
#throw this shit in the trash





#im still learning so i MIGHt be stupid with classes and not realizing it yet

class sbttl:
    def __init__(self, script_version: str):
        self.script_version = script_version

    def load(self, file_path: str):

        times = len(file_path)-1
        while True:
            times -= 1
            if str(file_path).find('\\',times,len(file_path)) != -1 or str(file_path).find('/',times,len(file_path)) != -1:
                break
        times += 1
        chosensave_name = file_path[times:len(file_path)]
        chosensave_folder = file_path[0:times]

        savefile = open(file_path,'r',encoding='utf-8').readlines()
        saveversion = savefile[0][9:len(savefile[0])-1]

        if saveversion == 'b0.1.0':
            
            global songbpm
            global offset
            global markedlistmsandtext
            global songlengthms
            global beatsmode
            global songfiledir
            global songchannel

            startpos_line = 0
            while savefile[startpos_line] != 'start\n':
                startpos_line += 1

            savesong = str(savefile[startpos_line + 1][10:len(savefile[startpos_line + 1])-1])
            songfiledir = str(chosensave_folder)+str(savesong)

            savebpm = float(savefile[startpos_line + 2][5:len(savefile[startpos_line + 2])-1])

            saveoffset = int(savefile[startpos_line + 3][8:len(savefile[startpos_line + 3])-1])

            savebeatsmode = str(savefile[startpos_line + 4][11:len(savefile[startpos_line + 4])-1])
            
            markspos = startpos_line + 5

            savemarksmsandtext = []

            while savefile[markspos] != 'end\n':
                times = 0
                while savefile[markspos][times] != ' ':
                    times += 1
                    print(str(markspos)+' '+str(times))


                savemarksmsandtext.append([float(savefile[markspos][0:times]),str(savefile[markspos][times+1:len(savefile[markspos])-1])])

                markspos += 1

            markedlistmsandtext = savemarksmsandtext

            songchannel = pygame.mixer.music
            songlengthms = pygame.mixer.Sound(str(chosensave_folder)+str(savesong)).get_length() * 1000
            songchannel.load(str(chosensave_folder)+str(savesong))
            songchannel.play(0,0)
            songchannel.pause()

            bpms = BPMS()
            bpms.new(savebpm,saveoffset,savebeatsmode,0,1)
            bpms.load(0)

            pygame.display.set_caption(chosensave_name)



    def save(self, savefile_path: str, songdir: str, bpm: float, offset: int, beatsmode: str, markslist: list, ):

        if self.script_version == 'b0.1.0':
            times = 0
            markslist_lines = ''
            while times < len(markslist): 
                markslist_lines = markslist_lines+str(float(markslist[times][0]))+' '+str(markslist[times][1])+'\n'
                times += 1


            times = len(songdir)-1
            while True:
                times -= 1
                if str(songdir).find('\\',times,len(songdir)) != -1 or str(songdir).find('/',times,len(songdir)) != -1:
                    break
            times += 1
            songname = songdir[times:len(songdir)]

            times = len(savefile_path)-1
            while True:
                times -= 1
                if str(savefile_path).find('\\',times,len(savefile_path)) != -1 or str(savefile_path).find('/',times,len(savefile_path)) != -1:
                    break
            times += 1
            savefile_dir_folder = savefile_path[0:times]
            savefile_name = savefile_path[times:len(savefile_path)]

            littledevletter = "So you're really curious, huh?\nGo on, do whatever you want and have fun! ^^\nThis program is a tool after all, right?\n\nDon't mind me, Im just gonna make a silly advertisement of me in this file. Please don't delete it, it would be really rude of you :(. Ahem...\n\nThis tool is made by @JakeIsAlivee\nuh...\nThe nickname is usually @JakeIsAlivee on all platforms...\nuh...\nPlease consider supporting me, either by words or giving me money, I will accept your support in any way ^^\n\n\n\n\n"

            sbttlfile_data = str('VERSION: '+self.script_version+'\n\n\n'+
                                 littledevletter+
                                 'start\n'+
                                 'Songname: '+songname+'\n'+
                                 'bpm: '+str(bpm)+'\n'+
                                 'offset: '+str(offset)+'\n'+
                                 'beatsmode: '+str(beatsmode)+'\n'+
                                 markslist_lines+
                                 'end\n')
            
            if savefile_dir_folder.find(savefile_name[0:len(savefile_name)-6]) == -1:
                    
                try:
                    os.mkdir(savefile_dir_folder+savefile_name[0:len(savefile_name)-6])
                except FileExistsError:
                    pass

                try:
                    open(savefile_dir_folder+savefile_name[0:len(savefile_name)-6]+slash+songname,'wb').writelines(open(songdir,'rb').readlines())
                except PermissionError:
                    pass

                open(savefile_dir_folder+savefile_name[0:len(savefile_name)-6]+slash+savefile_name,'w',encoding='utf-8').writelines(sbttlfile_data)
            else:
                try:
                    open(savefile_dir_folder+songname,'wb').writelines(open(songdir,'rb').readlines())
                except PermissionError:
                    pass
                open(savefile_dir_folder+savefile_name,'w',encoding='utf-8').writelines(sbttlfile_data)
                
            pygame.display.set_caption(savefile_name)



class BPMS:
    """
    Automatically creates an list that it will use to store any bpms you add

    The list has the variables:
        BPM
        Offset
        Beat mode (1/2 and so on...)
        Current beat (including halves and quads)
        Beat number (for beeps and bops you hear as sfx)
    """
    
    def __init__(self):
        self.bpmslist = []
        #offset bpm beatm curbeat beatnum



    def new(self, bpm: float, offset: int, beatmode: str, curbeat: int, beatnum: int):
        self.bpmslist.append([bpm,offset,beatmode,curbeat,beatnum])
    
    def delete(self, bpm_num: int):
        self.bpmslist.pop(bpm_num)



    def set(self, bpm_num: int, bpm, offset, beatmode, curbeat, beatnum):
        """
        Here you should ONLY type what you want to change

        Example:
            bpms.set(0, bpm=90, beatmode='1/4', offset=10)

        """
        if bpm:
            self.bpmslist[bpm_num][0] = bpm
        if offset:
            self.bpmslist[bpm_num][1] = offset
        if beatmode:
            self.bpmslist[bpm_num][2] = beatmode
        if curbeat:
            self.bpmslist[bpm_num][3] = curbeat
        if beatnum:
            self.bpmslist[bpm_num][4] = beatnum

    def get(self, bpm_num: int, bpm: bool, offset: bool, beatmode: bool, curbeat: bool, beatnum: bool):
        """
        Here you should ONLY type what you want to get

        Example:
            bpms.get(0, bpm=True, beatnum=True)

        """
        if bpm:
            yield self.bpmslist[bpm_num][0]
        if offset:
            yield self.bpmslist[bpm_num][1]
        if beatmode:
            yield self.bpmslist[bpm_num][2]
        if curbeat:
            yield self.bpmslist[bpm_num][3]
        if beatnum:
            yield self.bpmslist[bpm_num][4]


    def load(self, bpm_num: int):
        global allbeatmarksms

        global halfbeatmarkms
        global doublehalfbeatmarkms
        global triplehalfbeatmarkms

        global mainbeatmarkms

        if self.bpmslist[bpm_num][0] != None:
            global beatsmode
            global tickspersec
            global durationbetweenticks



            tickspersec = self.bpmslist[bpm_num][0] / 60
            durationbetweenticks = 1000 / tickspersec

            allbeatmarksms = []

            halfbeatmarkms = []
            doublehalfbeatmarkms = []
            triplehalfbeatmarkms = []

            mainbeatmarkms = [0+offset]
            times = 1
            while int(durationbetweenticks*times) < int(songlengthms):
                mainbeatmarkms.append(int(durationbetweenticks*times)+int(offset))
                times += 1

            times = 0
            while times < len(mainbeatmarkms):
                allbeatmarksms.append(mainbeatmarkms[times])
                times += 1




            #i MIGHT have lost the meaning of whats in there but its fiiine... i still know SOME of it soo

            if beatsmode == '1/2':
                times = 0
                while times < len(mainbeatmarkms)-1:
                    try:
                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2)+offset) not in allbeatmarksms:
                            halfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2)+offset)

                        times += 1
                    except ZeroDivisionError:
                        times += 1

                allbeatmarksms.append(halfbeatmarkms.copy())



            if beatsmode == '1/4':
                times = 0
                while times < len(mainbeatmarkms)-1:
                    try:
                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2)+offset) not in allbeatmarksms:
                            halfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2)+offset)

                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/4)+offset) not in allbeatmarksms:
                            doublehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/4)+offset)

                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.5)+offset) not in allbeatmarksms:
                            doublehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.5)+offset)


                        times += 1
                    except ZeroDivisionError:
                        times += 1

                allbeatmarksms.append(halfbeatmarkms.copy())
                allbeatmarksms.append(doublehalfbeatmarkms.copy())


            if beatsmode == '1/8':
                times = 0
                while times < len(mainbeatmarkms)-1:
                    try:
                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2)+offset) not in allbeatmarksms:
                            halfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2)+offset)


                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/4)+offset) not in allbeatmarksms:
                            doublehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/4)+offset)

                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.5)+offset) not in allbeatmarksms:
                            doublehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.5)+offset)


                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/8)+offset) not in allbeatmarksms:
                            triplehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/8)+offset)

                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/4*1.5)+offset) not in allbeatmarksms:
                            triplehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/4*1.5)+offset)

                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.25)+offset) not in allbeatmarksms:
                            triplehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.25)+offset)

                        if int((mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.75)+offset) not in allbeatmarksms:
                            triplehalfbeatmarkms.append(int(mainbeatmarkms[times]-offset)+((mainbeatmarkms[1]-offset)/2*1.75)+offset)


                        times += 1
                    except ZeroDivisionError:
                        times += 1

                allbeatmarksms.append(halfbeatmarkms.copy())
                allbeatmarksms.append(doublehalfbeatmarkms.copy())
                allbeatmarksms.append(triplehalfbeatmarkms.copy())





            allbeatmarksms.sort()

            halfbeatmarkms.sort()
            doublehalfbeatmarkms.sort()
            triplehalfbeatmarkms.sort()
        else:

            allbeatmarksms = [0]

            halfbeatmarkms = []
            doublehalfbeatmarkms = []
            triplehalfbeatmarkms = []

            mainbeatmarkms = [0]

currentbpm = 0

bpms = BPMS()

"""
bpm
offset
beatmode
curbet 
beatnum
"""

bpms.new(None,0,'1/1',0,4)
bpms.load(currentbpm)



#bpms = [[None,None,'1/1',0,0,4]]
#      offset bpm beatm lm la bn




EDITORVERSION = 'b0.1.2'

#dir of this script
scriptdirfolder = os.path.dirname(os.path.realpath(__file__))

#different types of slashes just in case if something goes wrong
if scriptdirfolder.find('\\') != -1:
    slash = '\\'
else:
    slash = '/'


windowscaled = True

pygame.init()

if windowscaled == True:
    window = pygame.display.set_mode((512,512),pygame.SCALED,display=0)

else:
    window = pygame.display.set_mode((512,512),display=0)

pygame.display.set_caption('Newfile.sbttl')

eyesclosedicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'subtitlesicon_eyesclosed.bmp')
eyesopenicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'subtitlesicon_eyesopen.bmp')

pygame.display.set_icon(eyesopenicon)


black = 0,0,0
gray = 50,50,50
white = 255,255,255

ultrabigfont = pygame.font.SysFont('couriernew', 64)
biggiefont = pygame.font.SysFont('couriernew', 28)
lilfont = pygame.font.SysFont('couriernew', 20)
lillilfont = pygame.font.SysFont('couriernew', 16)

#120bpm : 60s = 2
#1000ms : 2 = 500ms - duration

description = 'Choose the song or a subtitle file (.mp3 or .sbttl)'
while True:

    chosenfile = easygui.fileopenbox(description,'Editor')

    if chosenfile == None:
        pygame.quit()
        sys.exit()

    if chosenfile[len(chosenfile)-4:len(chosenfile)] == '.mp3':
        newproject = True
        break

    if str(chosenfile)[len(str(chosenfile))-6:len(str(chosenfile))] == '.sbttl':
        sbttl(EDITORVERSION).load(chosenfile)
        newproject = False
        break

    else:
        description = 'You need to choose an .mp3 or .sbttl file to continue'
        continue

devmode = False
if newproject == True:
    songfiledir = chosenfile


    songchannel = pygame.mixer.music
    songlengthms = pygame.mixer.Sound(songfiledir).get_length() * 1000
    songchannel.load(songfiledir)
    songchannel.play(0,0)
    songchannel.pause()

beepfiledir = scriptdirfolder+slash+'Data'+slash+'sounds'+slash+'beep.ogg'
bopfiledir = scriptdirfolder+slash+'Data'+slash+'sounds'+slash+'bop.ogg'
beepsound = pygame.mixer.Sound(beepfiledir)
bopsound = pygame.mixer.Sound(bopfiledir)

beepsound.set_volume(0.25)
bopsound.set_volume(0.25)
songchannel.set_volume(1)



markedlistmsandtext = []


def markssnap():
    beatmarktimes = 0
    marktimes = 0
    while True:
        try:
            beatmarkleftdistance = markedlistmsandtext[marktimes][0] - allbeatmarksms[beatmarktimes] 
            beatmarkrightdistance = allbeatmarksms[beatmarktimes+1] - markedlistmsandtext[marktimes][0]
            if beatmarkleftdistance > allbeatmarksms[1]:
                beatmarktimes += 1
                continue
            if beatmarkrightdistance > allbeatmarksms[1]:
                beatmarktimes += 1
                continue
            if beatmarkleftdistance < beatmarkrightdistance:
                markedlistmsandtext[marktimes].pop(0)
                markedlistmsandtext[marktimes].insert(0,allbeatmarksms[beatmarktimes])
                marktimes += 1
            if beatmarkleftdistance > beatmarkrightdistance:
                markedlistmsandtext[marktimes].pop(0)
                markedlistmsandtext[marktimes].insert(0,allbeatmarksms[beatmarktimes+1])
                marktimes += 1
            else:
                marktimes += 1
        except IndexError:
            break

playing = False



bpmsetbytap = []

animationopacity = 0



def bpmgraphframe():
    

    pygame.draw.polygon(window,(50,50,50),[(0,0),(512,0),(512,63),(0,63),(0,0)])

    middlesignup = lillilfont.render('>',False,(255,255,255))
    middlesigndown = lillilfont.render('<',False,(255,255,255))
    middlesignup = pygame.transform.rotate(middlesignup,-90)
    middlesigndown = pygame.transform.rotate(middlesigndown,-90)
    middlesignup.set_alpha(150)
    middlesigndown.set_alpha(150)

    window.blit(middlesignup,(247,-1))
    window.blit(middlesigndown,(247,56))


            
    if songbpm != None:
        timesstart = 0
        timesend = 0
        
        try:
            nextbpmstart = bpms.get(currentbpm+1, offset=True)
        except IndexError:
            nextbpmstart = songlengthms

        while True:
            try:
                if mainbeatmarkms[timesstart] < offset:
                    timesstart += 1
                    continue
                if mainbeatmarkms[timesstart]/2*zoomuserpreference < int(visualposition-256):
                    timesstart += 1
                    timesend = timesstart
                    continue
                elif mainbeatmarkms[timesend] > nextbpmstart:
                    break
                elif mainbeatmarkms[timesend]/2*zoomuserpreference > int(visualposition+256):
                    break

                timesend += 1
            except IndexError:
                break

        times = timesstart-1
        while times < timesend:
            try:
                pygame.draw.line(window,(255,255,255),(256-visualposition+float(mainbeatmarkms[times]/2) * zoomuserpreference,0), (256-visualposition+float(mainbeatmarkms[times]/2) * zoomuserpreference,0+64),1)
                times += 1
            except IndexError:
                break
        
        times = timesstart-1
        while times < timesend:
            try:
                pygame.draw.line(window,(255,0,0),(256-visualposition+float(halfbeatmarkms[times]/2) * zoomuserpreference,8), (256-visualposition+float(halfbeatmarkms[times]/2) * zoomuserpreference,0+56),1)
                times += 1
            except IndexError:
                break
        
        times = timesstart-1
        while times < timesend:
            try:
                pygame.draw.line(window,(0,0,255),(256-visualposition+float(doublehalfbeatmarkms[times]/2) * zoomuserpreference,16), (256-visualposition+float(doublehalfbeatmarkms[times]/2) * zoomuserpreference,0+48),1)
                times += 1
            except IndexError:
                times = timesstart-1
                break
        
        times = timesstart-1
        while times < timesend:
            try:
                pygame.draw.line(window,(255,255,0),(256-visualposition+float(triplehalfbeatmarkms[times]/2) * zoomuserpreference,32), (256-visualposition+float(triplehalfbeatmarkms[times]/2) * zoomuserpreference,0+32),1)
                times += 1
            except IndexError:
                times = timesstart-1
                break
    


        times = 0

        while True:
            try:
                pygame.draw.line(window,(255,0,0),(261-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,0),  (257-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,6),1)
                pygame.draw.line(window,(255,0,0),(257-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,57), (261-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,64),1)
                pygame.draw.line(window,(255,0,0),(251-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,0),  (255-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,6),1)
                pygame.draw.line(window,(255,0,0),(255-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,57), (251-visualposition+float(markedlistmsandtext[times][0]/2) * zoomuserpreference,64),1)
                times += 1
            except IndexError:
                break
    

    pygame.draw.polygon(window,(255,255,255),[(0,0),(16,0),(16,32),(0,32),(0,0)])
    pygame.draw.lines(window,(0,0,0),False,[(0,0),(16,0),(16,16),(0,16),(0,0)])
    pygame.draw.lines(window,(0,0,0),False,[(0,16),(16,16),(16,32),(0,32),(0,16)])
    
    zoomintext = lillilfont.render('+',False,(0,0,0))
    zoomouttext = lillilfont.render('-',False,(0,0,0))
    window.blit(zoomintext,(4,-1))
    window.blit(zoomouttext,(4,15))
    
    if devmode:
        pygame.draw.lines(window,(255,0,0),False,[(1,1),(1,15),(15,15),(15,1),(1,1)]) #+
        pygame.draw.lines(window,(255,0,0),False,[(1,17),(1,31),(15,31),(15,17),(1,17)]) #-

    pygame.draw.line(window,(100,100,100),(256-visualposition+0*zoomuserpreference,0), (256-visualposition+0*zoomuserpreference,0+64),1)
    pygame.draw.line(window,(100,100,100),(256-visualposition+songlengthms/2*zoomuserpreference,0), (256-visualposition+songlengthms/2*zoomuserpreference,0+64),1)
    


def bpmbuttonsbar():
    pygame.draw.polygon(window,(white),[(0,64),(512,64),(512,95),(0,95),(0,64)])
    


    bpmtext = lilfont.render('Bpm: '+str(songbpm),False,(black))
    window.blit(bpmtext,(6,70))

    pygame.draw.circle(window,(black),(492,81),14,2,True,False,False,True)
    pygame.draw.line(window,(black),(492,67),(460,67),2)
    pygame.draw.circle(window,(black),(460,81),14,2,False,True,True,False)
    pygame.draw.line(window,(black),(492,93),(460,93),2)
    taptext = lilfont.render('Tap',False,(black))
    window.blit(taptext,(459,70))

    fasterbpmtext = biggiefont.render('>',False,(black))
    slowerbpmtext = biggiefont.render('<',False,(black))
    window.blit(fasterbpmtext,(420,65))
    window.blit(slowerbpmtext,(396,65))

    window.blit(biggiefont.render('+',False,(black)),(248,64))
    pygame.draw.lines(window,(black),False,[(240,65),(272,65),(272,94),(240,94),(240,65)])

    if devmode:
        pygame.draw.lines(window,(255,0,0),False,[(446,67),(506,67),(506,94),(446,94),(446,67)]) #TAP
        pygame.draw.lines(window,(255,0,0),False,[(416,67),(440,67),(440,94),(416,94),(416,67)]) #>
        pygame.draw.lines(window,(255,0,0),False,[(392,67),(416,67),(416,94),(392,94),(392,67)]) #<
        pygame.draw.lines(window,(255,0,0),False,[(2,67),(132,67),(132,94),(2,94),(2,67)]) #BPM
        pygame.draw.lines(window,(255,0,0),False,[(239,64),(273,64),(273,95),(239,95),(239,64)]) #+ bpm

        pygame.draw.lines(window,(0,190,0),False,[(388,64),(444,64),(444,95),(388,95),(388,64)]) #<> wheel


def offsetbuttonsbar():

    pygame.draw.polygon(window,(white),[(0,64),(512,64),(512,95),(0,95),(0,64)])

    
    offsettext = lilfont.render('Offset: '+str(offset),False,(black))
    window.blit(offsettext,(6,70))

    plusoffsettext = biggiefont.render('>',False,(black))
    minusoffsettext = biggiefont.render('<',False,(black))
    window.blit(plusoffsettext,(490,65))
    window.blit(minusoffsettext,(470,65))

    if devmode:
        pygame.draw.lines(window,(255,0,0),False,[(2,67),(156,67),(156,94),(2,94),(2,67)]) #OFFSET
        pygame.draw.lines(window,(255,0,0),False,[(489,67),(508,67),(508,94),(489,94),(489,67)]) #>
        pygame.draw.lines(window,(255,0,0),False,[(466,67),(489,67),(489,94),(466,94),(466,67)]) #<

        pygame.draw.lines(window,(0,190,0),False,[(462,64),(511,64),(511,95),(462,95),(462,64)]) #<> wheel


marknum = 0

def beatbuttonsbar():
    pygame.draw.polygon(window,(white),[(0,96),(512,96),(512,127),(0,127),(0,96)])
    pygame.draw.line(window,(gray),(0,96),(512,96),1)

    if len(markedlistmsandtext) == 0:
        marknumtext = biggiefont.render('Mark 0',False,(black))
    else:
        marknumtext = biggiefont.render('Mark '+str(marknum),False,(black))
    window.blit(marknumtext,(5,97)) #Mark (num)
    
    deletemarktext = biggiefont.render('-',False,(black))
    addmarktext = biggiefont.render('+',False,(black))

    window.blit(deletemarktext,(237,97))
    window.blit(addmarktext,(257,97))

    minusbeatstext = biggiefont.render('<',False,(black))
    beatsmodetext = biggiefont.render(str(beatsmode),False,(black))
    plusbeatstext = biggiefont.render('>',False,(black))
    
    window.blit(minusbeatstext,(417,97))
    window.blit(beatsmodetext,(437,97))
    window.blit(plusbeatstext,(490,97))

    if devmode:
        pygame.draw.lines(window,(255,0,0),False,[(235,98),(255,98),(255,126),(235,126),(235,98)]) #-
        pygame.draw.lines(window,(255,0,0),False,[(255,98),(275,98),(275,126),(255,126),(255,98)]) #+

        pygame.draw.lines(window,(255,0,0),False,[(412,96),(438,96),(438,128),(412,128),(412,96)]) #<
        pygame.draw.lines(window,(255,0,0),False,[(488,96),(512,96),(512,128),(488,128),(488,96)]) #>

markfontsize = 128
markfont = pygame.font.SysFont('couriernew', markfontsize)

def texteditingframe():
    global markfontsize
    global markfont
    global textlines

    
    #thats the renderer area
    pygame.draw.polygon(window,(white),[(0,160),(384,160),(384,512),(0,512),(0,160)])
    
    slicenum = 0
    textlines = []
    try:
        if str(markedlistmsandtext[marknum-1][1]).find('\t') == -1:
            textlines.append(markedlistmsandtext[marknum-1][1])
        if str(markedlistmsandtext[marknum-1][1]).find('\t') != -1:
            textlines.append(markedlistmsandtext[marknum-1][1][0:str(markedlistmsandtext[marknum-1][1]).find('\t')])

        while markedlistmsandtext[marknum-1][1].find('\t',slicenum,len(markedlistmsandtext[marknum-1][1])) != -1:
            slicenum = markedlistmsandtext[marknum-1][1].find('\t',slicenum,len(markedlistmsandtext[marknum-1][1])) + 1
            nextslicenum = markedlistmsandtext[marknum-1][1].find('\t',slicenum,len(markedlistmsandtext[marknum-1][1]))
            if nextslicenum == -1:
                textlines.append(markedlistmsandtext[marknum-1][1][slicenum:len(markedlistmsandtext[marknum-1][1])])
            else:
                textlines.append(markedlistmsandtext[marknum-1][1][slicenum:nextslicenum])
            
    except IndexError:
        try:
            textlines.append(markedlistmsandtext[marknum-1][1])
        except IndexError:
            pass
    times = 0
    longestlinelen = 0
    longestline = ''

    while times < len(textlines):
        if longestlinelen < len(textlines[times]):
            longestlinelen = len(textlines[times])
            longestline = textlines[times]
        times += 1
        
        
    

    try:


        marktextrender = markfont.render(longestline,False,(black))
        marktextwidth = marktextrender.get_width()

        if not playing:
            if marktextwidth >= 380: #zoom effect
                markfontsize -= 1
                markfont = pygame.font.SysFont('couriernew', markfontsize)
                marktextrender = markfont.render(longestline,False,(black))
                marktextwidth = marktextrender.get_width()

            possiblemarkfont = pygame.font.SysFont('couriernew', markfontsize+1)
            possiblemarktextrender = possiblemarkfont.render(longestline,False,(black))
            possiblemarktextwidth = possiblemarktextrender.get_width()
            if markfontsize < 128: #zoom effect
                if possiblemarktextwidth < 380:
                    markfontsize += 1
                    markfont = pygame.font.SysFont('couriernew', markfontsize)
                    marktextrender = markfont.render(longestline,False,(black))
                    marktextwidth = marktextrender.get_width()


        if playing:

            while marktextwidth >= 380: #no zoom effect
                markfontsize -= 1
                markfont = pygame.font.SysFont('couriernew', markfontsize)
                marktextrender = markfont.render(longestline,False,(black))
                marktextwidth = marktextrender.get_width()


            possiblemarkfont = pygame.font.SysFont('couriernew', markfontsize+1)
            possiblemarktextrender = possiblemarkfont.render(longestline,False,(black))
            possiblemarktextwidth = possiblemarktextrender.get_width()
            if markfontsize < 128: #zoom effect
                if possiblemarktextwidth < 380:
                    markfontsize += 1
                    markfont = pygame.font.SysFont('couriernew', markfontsize)
                    marktextrender = markfont.render(longestline,False,(black))
                    marktextwidth = marktextrender.get_width()
            
        marktextheight = marktextrender.get_height()

        times = 0
        ycord = (672 - float(len(textlines))*marktextheight) / 2 #chat gpt helping
        
        while times < len(textlines):
            marktextrender = markfont.render(textlines[times],False,(black))
            marktextwidth = marktextrender.get_width()
            marktextheight = marktextrender.get_height()
            window.blit(marktextrender,(192 - float(marktextwidth / 2),ycord))
            ycord += marktextheight

            times += 1

    except IndexError:
        pass





    #thats the mark (num) line
    pygame.draw.polygon(window,(white),[(0,128),(384,128),(384,160),(0,160),(0,128)])
    pygame.draw.line(window,(gray),(0,128),(512,128),1)
    pygame.draw.line(window,(gray),(384,128),(384,512),1)

    if len(markedlistmsandtext) == 0:
        markONLYnumtext = biggiefont.render('0',False,(black))
    else:
        markONLYnumtext = biggiefont.render(str(marknum),False,(black))
    window.blit(markONLYnumtext,(184,129)) #(num) (no mark before num.) (nuh uh.)
    
    snapmarktobeatbeforetext = biggiefont.render('<',False,(black))
    snapmarktobeataftertext = biggiefont.render('>',False,(black))

    window.blit(snapmarktobeatbeforetext,(5,129))
    window.blit(snapmarktobeataftertext,(364,129))

    pygame.draw.line(window,(gray),(0,160),(384,160),1)

    if devmode:
        pygame.draw.lines(window,(255,0,0),False,[(0,128),(26,128),(26,160),(0,160),(0,128)]) #<
        pygame.draw.lines(window,(255,0,0),False,[(356,128),(384,128),(384,160),(356,160),(356,128)]) #>


    


musicvolume = 100
beepsvolume = 100

def buttonsinteractivebar(mode = None):
    global musicvolume
    global beepsvolume

    pygame.draw.polygon(window,(white),[(385,129),(480,129),(480,512),(385,512),(385,129)])
    pygame.draw.line(window,(gray),(0,511),(512,511),1)

    if mode == 'volume':
        musictext = lillilfont.render('Music',False,(0,0,0))
        sfxtext = lillilfont.render('SFX',False,(0,0,0))
        window.blit(musictext,(388,320))
        window.blit(sfxtext,(444,320))
        pygame.draw.line(window,(0,0,0),(410,474),(410,355))
        pygame.draw.line(window,(0,0,0),(458,474),(458,355))

        musicvolume = int(songchannel.get_volume() * 100)
        beepsvolume = int(beepsound.get_volume() * 100)

        musicprocent = lillilfont.render(str(musicvolume)+'%',False,(0,0,0))
        sfxprocent = lillilfont.render(str(beepsvolume)+'%',False,(0,0,0))
        window.blit(musicprocent,(392,492))
        window.blit(sfxprocent,(439,492))

        pygame.draw.circle(window,(0,0,0),(411,465-int(musicvolume)),10,1,True,False,False,True)
        pygame.draw.circle(window,(0,0,0),(410,465-int(musicvolume)),10,1,False,True,True,False)
        
        pygame.draw.circle(window,(0,0,0),(459,465-int(beepsvolume)),10,1,True,False,False,True)
        pygame.draw.circle(window,(0,0,0),(458,465-int(beepsvolume)),10,1,False,True,True,False)

        if devmode:
            pygame.draw.lines(window,(255,0,0),False,[(440,340),(476,340),(476,485),(440,485),(440,340)]) #sfx slider
            pygame.draw.lines(window,(255,0,0),False,[(388,340),(430,340),(430,485),(388,485),(388,340)]) #music slider

            pygame.draw.lines(window,(0,190,0),False,[(439,339),(477,339),(477,486),(439,486),(439,339)]) #sfx slider wheel
            pygame.draw.lines(window,(0,190,0),False,[(387,339),(431,339),(431,486),(387,486),(387,339)]) #music slider wheel


settingsicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'Settings.png')
savethefileicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'export sd.png')
loadthefileicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'import sd.png')
volumeicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'Volume.png')
customizeicon = pygame.image.load(scriptdirfolder+slash+'Data'+slash+'icons'+slash+'Customize.png')

def bottomrightbuttons():
    pygame.draw.polygon(window,(white),[(480,129),(512,129),(512,512),(480,512),(480,129)])
    pygame.draw.line(window,(gray),(479,128),(479,512),1)

    window.blit(settingsicon,(480,480))
    window.blit(loadthefileicon,(480,448))
    window.blit(savethefileicon,(480,416))
    window.blit(volumeicon,(480,384))
    window.blit(customizeicon,(480,352))

    if devmode:
        pygame.draw.lines(window,(255,0,0),False,[(480,480),(480,511),(511,511),(511,480),(480,480)]) #settings
        pygame.draw.lines(window,(255,0,0),False,[(480,448),(480,480),(511,480),(511,448),(480,448)]) #loads
        pygame.draw.lines(window,(255,0,0),False,[(480,416),(480,448),(511,448),(511,416),(480,416)]) #saves
        pygame.draw.lines(window,(255,0,0),False,[(480,384),(480,416),(511,416),(511,384),(480,384)]) #volume
        pygame.draw.lines(window,(255,0,0),False,[(480,352),(480,384),(511,384),(511,352),(480,352)]) #customize
        

        



firstbarmode = 'BPM'

lastpressed12keyboardbuttons = []

lastmainbeatmark = 0
lastallbeatmark = 0

beatnum = 4

songposition = 0 #ms
songstartpoint = 0 #ms > convert to sec by multiplying by 1000

zoomuserpreference = 1
visualposition = float(songposition / 2) * zoomuserpreference


buttonsmode = None
        
settingsmenu = False
settingsdarknessfadein = 0
settingsmenufadein = 0

spookmode = False


holdingsfx = False
holdingmusic = False

textbox_typing = False

holdingbackspace = False
holdingbackspaceframes = 0

windowfps = pygame.time.Clock()

helpnoteopacity = 0



def settings_menu(transparency):

    transperent_black = pygame.Color(0,0,0,transparency)
    transperent_white = pygame.Color(255,255,255,transparency)

    window.blit(ultrabigfont.render('Menu',False,transperent_white),(179,80))

    #1st row
    pygame.draw.circle(window,transperent_black,(50,256),40.0,2,False,True,True,False)      #circle middle point to the left
    pygame.draw.line(window,transperent_black,(50,216),(196,216),2)                         #line from left to right
    pygame.draw.circle(window,transperent_black,(196,256),40.0,2,True,False,False,True)     #circle middle point to the right
    pygame.draw.line(window,transperent_black,(196,294),(50,294),2)                         #line from right to left (-2 pixels)
    
    pygame.draw.circle(window,transperent_white,(50,256),35.0,35,False,True,True,False)     #left circle background
    pygame.draw.polygon(window,transperent_white,[(50,221),(195,221),(195,290),(50,290)])   #middle background
    pygame.draw.circle(window,transperent_white,(196,256),35.0,35,True,False,False,True)    #right circle background
    


    pygame.draw.circle(window,transperent_black,(316,256),40.0,2,False,True,True,False)      #circle middle point to the left
    pygame.draw.line(window,transperent_black,(316,216),(462,216),2)                         #line from left to right
    pygame.draw.circle(window,transperent_black,(462,256),40.0,2,True,False,False,True)     #circle middle point to the right
    pygame.draw.line(window,transperent_black,(462,294),(316,294),2)                         #line from right to left (-2 pixels)

    pygame.draw.circle(window,transperent_white,(316,256),35.0,35,False,True,True,False)     #left circle background
    pygame.draw.polygon(window,transperent_white,[(316,221),(461,221),(461,290),(316,290)])   #middle background
    pygame.draw.circle(window,transperent_white,(462,256),35.0,35,True,False,False,True)    #right circle background
    
    





    #2nd row
    pygame.draw.circle(window,transperent_black,(50,356),40.0,2,False,True,True,False)      #circle middle point to the left
    pygame.draw.line(window,transperent_black,(50,316),(196,316),2)                         #line from left to right
    pygame.draw.circle(window,transperent_black,(196,356),40.0,2,True,False,False,True)     #circle middle point to the right
    pygame.draw.line(window,transperent_black,(196,394),(50,394),2)                         #line from right to left (-2 pixels)
    
    pygame.draw.circle(window,transperent_white,(50,356),35.0,35,False,True,True,False)     #left circle background
    pygame.draw.polygon(window,transperent_white,[(50,321),(195,321),(195,390),(50,390)])   #middle background
    pygame.draw.circle(window,transperent_white,(196,356),35.0,35,True,False,False,True)    #right circle background
    


    pygame.draw.circle(window,transperent_black,(316,356),40.0,2,False,True,True,False)      #circle middle point to the left
    pygame.draw.line(window,transperent_black,(316,316),(462,316),2)                         #line from left to right
    pygame.draw.circle(window,transperent_black,(462,356),40.0,2,True,False,False,True)      #circle middle point to the right
    pygame.draw.line(window,transperent_black,(462,394),(316,394),2)                         #line from right to left (-2 pixels)

    pygame.draw.circle(window,transperent_white,(316,356),35.0,35,False,True,True,False)      #left circle background
    pygame.draw.polygon(window,transperent_white,[(316,321),(461,321),(461,390),(316,390)])   #middle background
    pygame.draw.circle(window,transperent_white,(462,356),35.0,35,True,False,False,True)     #right circle background
    

    window.blit(biggiefont.render('Settings',False,transperent_black),(54,240))

    window.blit(biggiefont.render('Main menu',False,transperent_black),(48,340))

    

    window.blit(biggiefont.render('Help',False,transperent_black),(355,240))

    window.blit(biggiefont.render('Back',False,transperent_black),(355,340))



WASplaying = False
musicfadein = False

littledevletter = "So you're really curious, huh?\nGo on, do whatever you want and have fun! ^^\nThis program is a tool after all, right?\n\nDon't mind me, Im just gonna make a silly advertisement of me in this file. Please don't delete it, it would be really rude of you :(. Ahem...\n\nThis tool is made by @JakeIsAlivee\nuh...\nThe nickname is usually @JakeIsAlivee on all platforms...\nuh...\nPlease consider supporting me, either by words or giving me money, I will accept your support in any way ^^\n\n\n\n\n"

def sbttl_file_save_scene(version = str, songdir = str, bpm = float, offset = str, beatsmode = str, markslist = list):

    newfilename = pygame.display.get_caption()[0]
    savefile_dir = easygui.filesavebox(title='Saving your file...',default=scriptdirfolder+slash+newfilename)

    while True:

        if savefile_dir == None:
            return
        if savefile_dir[len(savefile_dir)-6:len(savefile_dir)] != '.sbttl':
            savefile_dir = easygui.filesavebox(title='Saving your file...',msg='Please make a .sbttl file',default=scriptdirfolder+slash+newfilename)
            continue
        else:

            times = 0
            markslist_lines = ''
            while times < len(markslist): 
                markslist_lines = markslist_lines+str(float(markslist[times][0]))+' '+str(markslist[times][1])+'\n'
                times += 1

            print(markslist_lines)

            times = len(songdir)-1
            while True:
                times -= 1
                if str(songdir).find('\\',times,len(songdir)) != -1 or str(songdir).find('/',times,len(songdir)) != -1:
                    break
            times += 1
            songname = songdir[times:len(songdir)]

            times = len(savefile_dir)-1
            while True:
                times -= 1
                if str(savefile_dir).find('\\',times,len(savefile_dir)) != -1 or str(savefile_dir).find('/',times,len(savefile_dir)) != -1:
                    break
            times += 1
            savefile_dir_folder = savefile_dir[0:times]
            savefile_name = savefile_dir[times:len(savefile_dir)]

            sbttlfile_data = str('VERSION: '+version+'\n\n\n'+
                                 littledevletter+
                                 'start\n'+
                                 'Songname: '+songname+'\n'+
                                 'bpm: '+str(bpm)+'\n'+
                                 'offset: '+str(offset)+'\n'+
                                 'beatsmode: '+str(beatsmode)+'\n'+
                                 markslist_lines+
                                 'end\n')
            
            if savefile_dir_folder.find(savefile_name[0:len(savefile_name)-6]) == -1:
                    
                try:
                    os.mkdir(savefile_dir_folder+savefile_name[0:len(savefile_name)-6])
                except FileExistsError:
                    pass

                try:
                    open(savefile_dir_folder+savefile_name[0:len(savefile_name)-6]+slash+songname,'wb').writelines(open(songdir,'rb').readlines())
                except PermissionError:
                    pass

                open(savefile_dir_folder+savefile_name[0:len(savefile_name)-6]+slash+savefile_name,'w',encoding='utf-8').writelines(sbttlfile_data)
            else:
                try:
                    open(savefile_dir_folder+songname,'wb').writelines(open(songdir,'rb').readlines())
                except PermissionError:
                    pass
                open(savefile_dir_folder+savefile_name,'w',encoding='utf-8').writelines(sbttlfile_data)
                
            pygame.display.set_caption(savefile_name)
            break





while True:
    try:
        #this does NOT work right now
        #spoiler: the code is ass
        if settingsmenu:

            if settingsdarknessfadein < 200:
                settingsdarknessfadein += 10
            if settingsmenufadein < 250:
                settingsmenufadein += 10

            window.fill((0,0,0))

            texteditingframe()

            bpmgraphframe()

            temp = firstbarmode

            if temp == 'OFFSET':
                offsetbuttonsbar()
            if temp == 'BPM':
                bpmbuttonsbar()

            beatbuttonsbar()

            buttonsinteractivebar(buttonsmode)
            bottomrightbuttons()

            fade_in_darkness = pygame.Surface((1000,1000),pygame.SRCALPHA)
            fade_in_darkness.fill((0,0,0))
            fade_in_darkness.set_alpha(settingsdarknessfadein)
            window.blit(fade_in_darkness,(0,0))

            settings_menu(settingsmenufadein)

            pygame.display.update()

            marknum = 0
            while True:
                songposition = songchannel.get_pos()
                try:
                    if songposition >= markedlistmsandtext[marknum][0]:
                        marknum += 1
                        continue
                    else:
                        break
                except IndexError:
                    break
                
                
            if playing:
                songposition = songchannel.get_pos()
                visualposition = float(songposition / 2) * zoomuserpreference

                try:
                    if songposition > mainbeatmarkms[lastmainbeatmark]:
                        lastmainbeatmark += 1
                        temp = beatnum
                        if temp < 4:
                            beepsound.play()
                            beatnum += 1
                        if temp == 4:
                            bopsound.play()
                            beatnum = 1
                except IndexError:
                    playing = False

                try:
                    if songposition > allbeatmarksms[lastallbeatmark]:
                        lastallbeatmark += 1
                except IndexError:
                    pass












            if devmode:
                fps = lilfont.render(str(int(windowfps.get_fps())),False,(255,255,255),(0,0,0))
                window.blit(fps,(0,492))
                if windowfps.get_fps() < 100:
                    print('fps drop to '+str(int(windowfps.get_fps())))

            if len(lastpressed12keyboardbuttons) > 12:
                lastpressed12keyboardbuttons.pop(0)
            if lastpressed12keyboardbuttons == ['j','a','k','e','i','s','a','l','i','v','e','e']:
                lastpressed12keyboardbuttons = []
                temp = devmode
                if temp == False:
                    devmode = True
                if temp == True:
                    devmode = False

            for event in pygame.event.get():
                if devmode:
                    print(event)
                if event.type == pygame.WINDOWCLOSE:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.TEXTINPUT:
                    lastpressed12keyboardbuttons = lastpressed12keyboardbuttons + list(event.text)


                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.pos[0] > 274 and event.pos[0] < 500 and event.pos[1] > 316 and event.pos[1] < 394: #BACK
                        #this looks so ugly i hate it
                        #works tho
                        fadeinvolume = 0
                        songchannel.set_volume(fadeinvolume)
                        fadeinvolume_addperframe = musicvolume / 100 / 20

                        while settingsdarknessfadein > 0:
                            if WASplaying:
                                playing = True
                                fadeinvolume += fadeinvolume_addperframe
                                songchannel.set_volume(fadeinvolume)
                            settingsdarknessfadein -= 10
                            settingsmenufadein -= 10

                            window.fill((0,0,0))

                            texteditingframe()

                            bpmgraphframe()

                            temp = firstbarmode

                            if temp == 'OFFSET':
                                offsetbuttonsbar()
                            if temp == 'BPM':
                                bpmbuttonsbar()

                            beatbuttonsbar()

                            buttonsinteractivebar(buttonsmode)
                            bottomrightbuttons()

                            fade_in_darkness = pygame.Surface((1000,1000),pygame.SRCALPHA)
                            fade_in_darkness.fill((0,0,0))
                            fade_in_darkness.set_alpha(settingsdarknessfadein)
                            window.blit(fade_in_darkness,(0,0))

                            settings_menu(settingsmenufadein)

                            pygame.display.update()

                            marknum = 0
                            while True:
                                songposition = songchannel.get_pos()
                                try:
                                    if songposition >= markedlistmsandtext[marknum][0]:
                                        marknum += 1
                                        continue
                                    else:
                                        break
                                except IndexError:
                                    break
                                
                                
                            if playing:
                                songposition = songchannel.get_pos()
                                visualposition = float(songposition / 2) * zoomuserpreference

                                try:
                                    if songposition > mainbeatmarkms[lastmainbeatmark]:
                                        lastmainbeatmark += 1
                                        temp = beatnum
                                        if temp < 4:
                                            beepsound.play()
                                            beatnum += 1
                                        if temp == 4:
                                            bopsound.play()
                                            beatnum = 1
                                except IndexError:
                                    playing = False

                                try:
                                    if songposition > allbeatmarksms[lastallbeatmark]:
                                        lastallbeatmark += 1
                                except IndexError:
                                    pass
                                





                            if devmode:
                                fps = lilfont.render(str(int(windowfps.get_fps())),False,(255,255,255),(0,0,0))
                                window.blit(fps,(0,492))
                                if windowfps.get_fps() < 100:
                                    print('fps drop to '+str(int(windowfps.get_fps())))

                            if len(lastpressed12keyboardbuttons) > 12:
                                lastpressed12keyboardbuttons.pop(0)
                            if lastpressed12keyboardbuttons == ['j','a','k','e','i','s','a','l','i','v','e','e']:
                                lastpressed12keyboardbuttons = []
                                temp = devmode
                                if temp == False:
                                    devmode = True
                                if temp == True:
                                    devmode = False

                            for event in pygame.event.get():
                                if devmode:
                                    print(event)
                                if event.type == pygame.WINDOWCLOSE:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.TEXTINPUT:
                                    lastpressed12keyboardbuttons = lastpressed12keyboardbuttons + list(event.text)

                            windowfps.tick(120)

                        settingsmenu = False

            windowfps.tick(120)


        if not settingsmenu:

            if holdingbackspace:
                holdingbackspaceframes += 1
                if holdingbackspaceframes > 60:
                    holdingbackspaceframes += 1
                    if holdingbackspaceframes%3 == 0:
                        try:
                            previoustext = markedlistmsandtext[marknum-1][1][0:len(markedlistmsandtext[marknum-1][1])-1]
                            markedlistmsandtext[marknum-1].pop(1)
                            markedlistmsandtext[marknum-1].insert(1,previoustext)
                        except IndexError:
                            pass


            window.fill((0,0,0))
            if songbpm != None:
                if songbpm > 9999: #spookyyyy :p
                    bpms.set(currentbpm, bpm=1)
                    
                    WHYfont = pygame.font.SysFont('couriernew', 256)
                    spooksound1dir = scriptdirfolder+slash+'Data'+slash+'sounds'+slash+'oooh spoooky soundddd1.ogg'
                    spooksound2dir = scriptdirfolder+slash+'Data'+slash+'sounds'+slash+'oooh spoooky soundddd2.ogg'
                    spooksound3dir = scriptdirfolder+slash+'Data'+slash+'sounds'+slash+'oooh spoooky soundddd3.ogg'
                    spooksound1 = pygame.mixer.Sound(spooksound1dir)
                    spooksound2 = pygame.mixer.Sound(spooksound2dir)
                    spooksound3 = pygame.mixer.Sound(spooksound3dir)

                    youre_text = ultrabigfont.render(str("You're"),False,(255,255,255))
                    tortuing_text = ultrabigfont.render( str('torturing'),False,(255,255,255))
                    it_text = ultrabigfont.render(  str('it.'),False,(255,255,255))

                    WHY_text = WHYfont.render('WHY?',False,(255,255,255))
                    pygame.mouse.set_pos(500,0)

                    while True:
                        if spookmode == False:

                            window.fill((0,0,0))

                            window.blit(youre_text,(140,160))
                            window.blit(tortuing_text,(90,220))
                            window.blit(it_text,(200,280))

                            for event in pygame.event.get():
                                if event.type == pygame.WINDOWCLOSE:
                                    spooksound1.set_volume(0.1)
                                    spooksound1.play(loops=999)
                                    messagebox.showerror('Error','Why?')
                                    spooksound1.stop()
                                    spooksound2.set_volume(0.1)
                                    spooksound2.play(loops=999)
                                    messagebox.showerror('ERROR','Why?')
                                    spooksound2.stop()
                                    spooksound3.set_volume(0.1)
                                    spooksound3.play(loops=999)
                                    messagebox.showerror('ERROR','WHY?')
                                    spookmode = True

                            pygame.display.update()

                        else:
                            times = 2000
                            spooksound3.set_volume(1)
                            spooksound3.stop()
                            while times > 0:
                                spooksound3.play(loops=10)
                                window2 = pygame.display.set_mode((608,256),pygame.NOFRAME)
                                window2.fill((0,0,0))
                                window2.blit(WHY_text,(0,0))
                                pygame.mouse.set_pos(random.randint(0,596),random.randint(0,240))
                                pygame.display.update()

                                spooksound3.stop()
                                window2 = pygame.display.set_mode((1,1),pygame.NOFRAME)
                                pygame.display.update()
                                times -= 1
                            pygame.quit()
                            sys.exit()
                        continue

                if songbpm > 999 and songbpm < 2000:
                    darkness = pygame.Surface((1000,1000),pygame.SRCALPHA)
                    darkness.fill((0,0,0))
                    darkness.set_alpha(75)
                    window.blit(darkness,(0,0))

                    whydid_text = ultrabigfont.render(str('Why did'),False,(50,50,50))
                    youdo_text = ultrabigfont.render( str('you do'),False,(50,50,50))
                    this_text = ultrabigfont.render(  str('this?'),False,(50,50,50))
                    window.blit(whydid_text,(130,160))
                    window.blit(youdo_text,(145,220))
                    window.blit(this_text,(160,280))
                if songbpm > 1999 and songbpm < 5000:
                    darkness = pygame.Surface((1000,1000),pygame.SRCALPHA)
                    darkness.fill((0,0,0))
                    darkness.set_alpha(150)
                    window.blit(darkness,(0,0))

                    stop_text = ultrabigfont.render(str('Stop.'),False,(0,0,0))
                    window.blit(stop_text,(160,224))
                if songbpm > 4999 and songbpm < 10000:
                    darkness = pygame.Surface((1000,1000),pygame.SRCALPHA)
                    darkness.fill((0,0,0))
                    darkness.set_alpha(200)
                    window.blit(darkness,(0,0))

                    areyou_text = ultrabigfont.render (str('Are you'),False,(200,200,200))
                    fucking_text = ultrabigfont.render(str('fucking'),False,(200,200,200))
                    insane_text = ultrabigfont.render (str('insane?'),False,(200,200,200))
                    window.blit(areyou_text,(130,160))
                    window.blit(fucking_text,(130,220))
                    window.blit(insane_text,(130,280))


                #os.system('cls')
                #print(bpms)
                #print(lastmainbeatmark)
                #print(lastallbeatmark)



                if songposition < bpms.get(currentbpm, offset=True):
                    try:
                        
                        currentbpm -= 1
                        bpms.load(currentbpm)

                        songstartpoint = allbeatmarksms[lastallbeatmark-1]
                        
                    except IndexError:
                        currentbpm += 1
                        bpms.load(currentbpm)

                try:
                    if songposition >= bpms.get(currentbpm+1, offset=True):
                        currentbpm += 1
                        bpms.load(currentbpm)
                except IndexError:
                    pass

            texteditingframe()

            bpmgraphframe()

            temp = firstbarmode

            if temp == 'OFFSET':
                offsetbuttonsbar()
            if temp == 'BPM':
                bpmbuttonsbar()

            beatbuttonsbar()

            buttonsinteractivebar(buttonsmode)
            bottomrightbuttons()

            if devmode:
                fps = lilfont.render(str(int(windowfps.get_fps())),False,(255,255,255),(0,0,0))
                window.blit(fps,(0,492))
                if windowfps.get_fps() < 100:
                    print('fps drop to '+str(int(windowfps.get_fps())))





            marknum = 0
            songposition = songchannel.get_pos() + songstartpoint
            visualposition = float(songposition / 2) * zoomuserpreference


            if songposition > songlengthms:
                songchannel.pause()
                playing = False




            while True:
                try:
                    if songposition >= markedlistmsandtext[marknum][0]:
                        marknum += 1
                        continue
                    else:
                        break
                except IndexError:
                    break
                

            if playing:
                try:
                    if songposition > mainbeatmarkms[lastmainbeatmark]:
                        lastmainbeatmark += 1
                        bpms[currentbpm][3] = lastmainbeatmark
                        temp = beatnum
                        if temp < 4:
                            beepsound.play()
                            beatnum += 1
                        if temp == 4:
                            bopsound.play()
                            beatnum = 1
                        bpms[currentbpm][5] = beatnum
                        if lastmainbeatmark % 2 == 1:
                            pygame.display.set_icon(eyesopenicon)
                        else:
                            pygame.display.set_icon(eyesclosedicon)

                except IndexError:
                    pass

                try:
                    if songposition > allbeatmarksms[lastallbeatmark]:
                        lastallbeatmark += 1
                        bpms[currentbpm][4] = lastallbeatmark
                except IndexError:
                    pass
                

                
                
                

            if len(lastpressed12keyboardbuttons) > 12:
                lastpressed12keyboardbuttons.pop(0)
            if lastpressed12keyboardbuttons == ['j','a','k','e','i','s','a','l','i','v','e','e']:
                lastpressed12keyboardbuttons = []
                temp = devmode
                if temp == False:
                    devmode = True
                if temp == True:
                    devmode = False


            if len(bpmsetbytap) == 0:
                configurebpmclicks = ultrabigfont.render(str('Done!'),False,(gray))
                configurebpmclicks.set_alpha(animationopacity)
                window.blit(configurebpmclicks,(164,224))
            else:
                configurebpmclicks = ultrabigfont.render(str(8-len(bpmsetbytap)),False,(gray))
                configurebpmclicks.set_alpha(animationopacity)
                window.blit(configurebpmclicks,(224,224))

            if animationopacity > 0:
                animationopacity -= 1
                configurebpmclicks.set_alpha(animationopacity)

            if helpnoteopacity > 0:
                helpnotetext1 = pygame.font.SysFont('couriernew',40).render('You know you',False,(gray))
                helpnotetext1.set_alpha(helpnoteopacity)
                helpnotetext2 = pygame.font.SysFont('couriernew',40).render('can PRESS ENTER,',False,(gray))
                helpnotetext2.set_alpha(helpnoteopacity)
                helpnotetext3 = pygame.font.SysFont('couriernew',40).render('right..?',False,(gray))
                helpnotetext3.set_alpha(helpnoteopacity)

                window.blit(helpnotetext1,(50,250))
                window.blit(helpnotetext2,(5,290))
                window.blit(helpnotetext3,(110,330))
                helpnoteopacity -= 1

            #print(markedlistmsandtext)

            pygame.display.update()

            for event in pygame.event.get():

                if devmode:
                    print(event)

                if event.type == pygame.TEXTINPUT:
                    if textbox_typing:
                        if marknum != 0:
                            times = len(textlines)-1

                            if len(textlines[times]) >= 49:
                                helpnoteopacity = 300
                            else:
                                previoustext = markedlistmsandtext[marknum-1][1]
                                markedlistmsandtext[marknum-1].pop(1)
                                markedlistmsandtext[marknum-1].insert(1,previoustext+str(event.text))




                    lastpressed12keyboardbuttons = lastpressed12keyboardbuttons + list(event.text)

                if event.type == pygame.KEYDOWN:
                    if event.unicode == '\x08': #backspace

                    
                        if textbox_typing:
                            holdingbackspace = True
                            holdingbackspaceframes = 1
                            if marknum != 0:
                                previoustext = markedlistmsandtext[marknum-1][1][0:len(markedlistmsandtext[marknum-1][1])-1]
                                markedlistmsandtext[marknum-1].pop(1)
                                markedlistmsandtext[marknum-1].insert(1,previoustext)

                        try:
                            lastpressed12keyboardbuttons.pop(len(lastpressed12keyboardbuttons)-1)
                        except IndexError:
                            pass

                    if event.unicode == '\r': #enter
                        if textbox_typing:
                            if marknum != 0:
                                previoustext = markedlistmsandtext[marknum-1][1]
                                markedlistmsandtext[marknum-1].pop(1)
                                markedlistmsandtext[marknum-1].insert(1,previoustext+'\t')

                if event.type == pygame.KEYUP:
                    if event.unicode == '\x08':
                        holdingbackspace = False
                        holdingbackspaceframes = 0



                if event.type == pygame.WINDOWCLOSE:
                    pygame.quit()
                    sys.exit()



                if event.type == pygame.MOUSEBUTTONDOWN: 
                
                    if event.button == 1: #LMB
                    

                        if event.pos[0] > 0 and event.pos[0] < 384 and event.pos[1] > 160 and event.pos[1] < 512: #textbox
                            textbox_typing = True
                        else: 
                            textbox_typing = False

                        if event.pos[0] > 0 and event.pos[0] < 16 and event.pos[1] > 0 and event.pos[1] < 16: #+ zoom

                            zoomuserpreference += 0.03
                            visualposition = float(songposition / 2) * zoomuserpreference

                        if event.pos[0] > 0 and event.pos[0] < 16 and event.pos[1] > 16 and event.pos[1] < 32: #- zoom
                            if zoomuserpreference <= 0.06:
                                #pass
                                zoomuserpreference -= 0.005
                                visualposition = float(songposition / 2) * zoomuserpreference

                            else:
                                zoomuserpreference -= 0.03
                                visualposition = float(songposition / 2) * zoomuserpreference


                        if event.pos[0] > 255 and event.pos[0] < 275 and event.pos[1] > 98 and event.pos[1] < 126: #+
                            try:
                                beatmarkleftdistance = songposition - allbeatmarksms[lastallbeatmark-1]
                                beatmarkrightdistance = allbeatmarksms[lastallbeatmark] - songposition
                            except IndexError:
                                tempnum = 1

                                times = 0
                                found = False
                                while True:
                                    try:
                                        found = bool(allbeatmarksms[lastallbeatmark-tempnum] == markedlistmsandtext[times][0])
                                        if found:
                                            break
                                        times += 1
                                    except IndexError:
                                        break
                                if found != True:
                                    try:
                                        previoustext = markedlistmsandtext[marknum-tempnum][1]
                                        markedlistmsandtext.append([allbeatmarksms[lastallbeatmark-tempnum],str(previoustext)])
                                        markedlistmsandtext.sort()
                                    except ValueError:
                                        markedlistmsandtext.append([allbeatmarksms[lastallbeatmark-tempnum],str(previoustext)])
                                        markedlistmsandtext.sort()
                                    except IndexError:
                                        markedlistmsandtext.append([allbeatmarksms[lastallbeatmark-tempnum],''])
                                        markedlistmsandtext.sort()
                                continue

                            try: 

                                if beatmarkleftdistance < beatmarkrightdistance:
                                    if beatmarkleftdistance < 0:
                                        tempnum = 0
                                    else:
                                        tempnum = 1

                                if beatmarkleftdistance > beatmarkrightdistance:
                                    tempnum = 0

                            except IndexError:
                                tempnum = 1

                            times = 0
                            found = False
                            while True:
                                try:
                                    found = bool(allbeatmarksms[lastallbeatmark-tempnum] == markedlistmsandtext[times][0])
                                    if found:
                                        break
                                    times += 1
                                except IndexError:
                                    break
                            if found != True:
                                try:
                                    previoustext = markedlistmsandtext[marknum-tempnum][1]
                                    markedlistmsandtext.append([allbeatmarksms[lastallbeatmark-tempnum],str(previoustext)])
                                    markedlistmsandtext.sort()
                                except ValueError:
                                    markedlistmsandtext.append([allbeatmarksms[lastallbeatmark-tempnum],str(previoustext)])
                                    markedlistmsandtext.sort()
                                except IndexError:
                                    markedlistmsandtext.append([allbeatmarksms[lastallbeatmark-tempnum],''])
                                    markedlistmsandtext.sort()


                        if event.pos[0] > 235 and event.pos[0] < 255 and event.pos[1] > 98 and event.pos[1] < 126: #-
                            try:
                                beatmarkleftdistance = songposition - allbeatmarksms[lastallbeatmark-1]
                                beatmarkrightdistance = allbeatmarksms[lastallbeatmark] - songposition
                            except IndexError:
                                try:
                                    if markedlistmsandtext[marknum-1][0] <= songposition:
                                        markedlistmsandtext.pop(marknum-1)
                                except IndexError:
                                    pass
                                continue

                            if beatmarkleftdistance < beatmarkrightdistance:
                                try:
                                    if markedlistmsandtext[marknum-1][0] <= songposition:
                                        markedlistmsandtext.pop(marknum-1)
                                except IndexError:
                                    pass

                            if beatmarkleftdistance > beatmarkrightdistance:
                                try:
                                    if beatmarkrightdistance == 0:
                                        if markedlistmsandtext[marknum-1][0] <= songposition:
                                            markedlistmsandtext.pop(marknum-1)
                                    else:
                                        if markedlistmsandtext[marknum][0] <= songposition+allbeatmarksms[1]:
                                            markedlistmsandtext.pop(marknum)
                                except IndexError:
                                    pass

                        if event.pos[0] > 240 and event.pos[0] < 272 and event.pos[1] > 65 and event.pos[1] < 95: #+bpm
                            if bpms.get(currentbpm, bpm=True) == None:
                                bpms.set(currentbpm, bpm=120.0, offset=songposition, beatmode='1/1', curbeat=0, beatnum=4)
                                bpms.load(currentbpm)

                            else:
                                bpms.new(bpms.get(bpm=True,offset=True,beatmode=True,curbeat=True,beatnum=True))
                                currentbpm += 1
                                bpms.load(currentbpm)

                        if event.pos[0] > 0 and event.pos[0] < 26 and event.pos[1] > 128 and event.pos[1] < 160: #<
                            try:
                                if songposition == markedlistmsandtext[marknum-1][0]:
                                    tempnum = 2 
                                else:
                                    tempnum = 1
                            except IndexError:
                                tempnum = 1


                            try:
                                songstartpoint = int(markedlistmsandtext[marknum-tempnum][0])
                                visualposition = float(songstartpoint / 2) * zoomuserpreference

                                while True:
                                    try:
                                        if songstartpoint < mainbeatmarkms[lastmainbeatmark]:
                                            lastmainbeatmark -= 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            if beatnum > 0:
                                                beatnum -= 1
                                            elif beatnum == 1:
                                                beatnum = 4
                                            bpms[currentbpm][5] = beatnum
                                        else:
                                            break
                                    except IndexError:
                                        break
                                    
                                while True:
                                    try:
                                        if songstartpoint < allbeatmarksms[lastallbeatmark]:
                                            lastallbeatmark -= 1
                                            bpms[currentbpm][4] = lastallbeatmark
                                        else:
                                            break
                                    except IndexError:
                                        break
                                    
                                if playing:
                                    songchannel.play(0,songstartpoint/1000)
                                else:
                                    songchannel.play(0,songstartpoint/1000)
                                    songchannel.pause()

                            except pygame.error:
                                print('pygameerror')
                                songchannel.pause()
                                playing = False
                            except IndexError:
                                pass

                        if event.pos[0] > 358 and event.pos[0] < 384 and event.pos[1] > 128 and event.pos[1] < 160: #>

                            try:
                                songstartpoint = int(markedlistmsandtext[marknum][0])
                                visualposition = float(songstartpoint / 2) * zoomuserpreference

                                while True:
                                    try:
                                        if songstartpoint > mainbeatmarkms[lastmainbeatmark]:
                                            lastmainbeatmark += 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            if beatnum < 4:
                                                beatnum += 1
                                            elif beatnum == 4:
                                                beatnum = 1
                                            bpms[currentbpm][5] = beatnum
                                        else:
                                            break
                                    except IndexError:
                                        break
                                    
                                while True:
                                    try:
                                        if songstartpoint > allbeatmarksms[lastallbeatmark]:
                                            lastallbeatmark += 1
                                            bpms[currentbpm][4] = lastallbeatmark
                                        else:
                                            break
                                    except IndexError:
                                        break

                                while True:
                                    try:
                                        if songstartpoint < mainbeatmarkms[lastmainbeatmark]:
                                            lastmainbeatmark -= 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            if beatnum > 0:
                                                beatnum -= 1
                                            elif beatnum == 1:
                                                beatnum = 4
                                            bpms[currentbpm][5] = beatnum
                                        else:
                                            break
                                    except IndexError:
                                        break

                                while True:
                                    try:
                                        if songstartpoint < allbeatmarksms[lastallbeatmark]:
                                            lastallbeatmark -= 1
                                            bpms[currentbpm][4] = lastallbeatmark
                                        else:
                                            break
                                    except IndexError:
                                        break
                                    
                                if playing:
                                    songchannel.play(0,songstartpoint/1000)
                                else:
                                    songchannel.play(0,songstartpoint/1000)
                                    songchannel.pause()

                            except pygame.error:
                                print('pygameerror')
                                songchannel.pause()
                                playing = False
                            except IndexError:
                                marknum = 0
                                try:
                                    songstartpoint = int(markedlistmsandtext[marknum][0])
                                    visualposition = float(songstartpoint / 2) * zoomuserpreference
                                except IndexError:
                                    pass

                                
                        if event.pos[0] > 412 and event.pos[0] < 438 and event.pos[1] > 96 and event.pos[1] < 128: # < ?/? 
                            if songbpm != None:
                                if beatsmode == '1/2':
                                    lastallbeatmark = int(lastallbeatmark / 2)
                                    beatsmode = '1/1'
                                elif beatsmode == '1/4':
                                    lastallbeatmark = int(lastallbeatmark / 2)
                                    beatsmode = '1/2'
                                elif beatsmode == '1/8':
                                    lastallbeatmark = int(lastallbeatmark / 2)
                                    beatsmode = '1/4'
                                bpms.set(currentbpm,beatmode=beatsmode,curbeat=lastallbeatmark)
                                bpms.load(currentbpm)
                        if event.pos[0] > 488 and event.pos[1] > 96 and event.pos[1] < 128: # ?/? >
                            if songbpm != None:
                                if beatsmode == '1/1':
                                    lastallbeatmark = int(lastallbeatmark * 2)
                                    beatsmode = '1/2'
                                elif beatsmode == '1/2':
                                    lastallbeatmark = int(lastallbeatmark * 2)
                                    beatsmode = '1/4'
                                elif beatsmode == '1/4':
                                    lastallbeatmark = int(lastallbeatmark * 2)
                                    beatsmode = '1/8'
                                bpms.set(currentbpm,beatmode=beatsmode,curbeat=lastallbeatmark)
                                bpms.load(currentbpm)

                        if event.pos[0] > 480 and event.pos[1] > 480: #settings button
                            settingsmenu = True 

                            if playing:
                                WASplaying = True
                                playing = False

                                #songposition = songchannel.get_pos() 
                                #visualposition = float(songposition / 2) * zoomuserpreference
                                #зачем это здесь??


                                songchannel.fadeout(400) #stops music automaticly

                        if event.pos[0] > 480 and event.pos[1] > 448 and event.pos[1] < 480: # load button

                            while True:
                                chosensave = easygui.fileopenbox(title='Choose your .sbttl file',default=scriptdirfolder+slash+'*.sbttl')
                                if chosensave == None:
                                    break
                                if chosensave[len(chosensave)-6:len(chosensave)] != '.sbttl':
                                    chosensave = easygui.filesavebox(title='Choose your .sbttl file',msg='Please choose a .sbttl file',default=scriptdirfolder+slash+'*.sbttl')
                                    
                            sbttl(EDITORVERSION).load(chosenfile)


                        if event.pos[0] > 480 and event.pos[1] > 416 and event.pos[1] < 448: # save button
                            try:
                                
                                newfilename = pygame.display.get_caption()[0]
                                savefile_dir = easygui.filesavebox(title='Saving your file...',default=scriptdirfolder+slash+newfilename)

                                while True:
                                    if savefile_dir == None:
                                        break
                                    if savefile_dir[len(savefile_dir)-6:len(savefile_dir)] != '.sbttl':
                                        savefile_dir = easygui.filesavebox(title='Saving your file...',msg='Please make a .sbttl file',default=scriptdirfolder+slash+newfilename)
                                
                                sbttl(EDITORVERSION).save(savefile_dir, songfiledir, bpms.get(currentbpm, bpm=True, offset=True, beatmode=True), markedlistmsandtext)
        
                            except Exception:
                                easygui.exceptionbox('ERROR OCCURED WHILE SAVING THE PROJECT','ERROR')
                        if event.pos[0] > 480 and event.pos[1] > 384 and event.pos[1] < 416: #volume button
                            if buttonsmode == 'volume':
                                buttonsmode = None
                            else:
                                buttonsmode = 'volume'
                        if event.pos[0] > 480 and event.pos[1] > 352 and event.pos[1] < 384: #customize button 
                            if buttonsmode == 'customize':
                                buttonsmode = None
                            else:
                                buttonsmode = 'customize'


                        if buttonsmode == 'volume':
                            if event.pos[0] > 440 and event.pos[0] < 476 and event.pos[1] > 340 and event.pos[1] < 485: #sfx slider
                                holdingsfx = True
                                newvolume = int(465-event.pos[1]) / 100
                                if newvolume > 1:
                                    newvolume = 1
                                if newvolume < 0:
                                    newvolume = 0
                                beepsound.set_volume(newvolume)
                                bopsound.set_volume(newvolume)
                            if event.pos[0] > 388 and event.pos[0] < 430 and event.pos[1] > 340 and event.pos[1] < 485: #music slider
                                holdingmusic = True
                                newvolume = int(465-event.pos[1]) / 100
                                if newvolume > 1:
                                    newvolume = 1
                                if newvolume < 0:
                                    newvolume = 0
                                songchannel.set_volume(newvolume)


                        

                        if firstbarmode == 'BPM':
                        
                            if event.pos[0] > 2 and event.pos[0] < 132 and event.pos[1] > 67 and event.pos[1] < 94: #BPM
                                firstbarmode = 'OFFSET'
                            if event.pos[0] > 392 and event.pos[0] < 416 and event.pos[1] > 67 and event.pos[1] < 94: #<
                                if bpms[currentbpm][1] != None:
                                    if songbpm > 1:
                                        songbpm -= 1
                                        bpms[currentbpm][1] = songbpm
                                        bpmupdate(songbpm)
                                        markssnap()
                            if event.pos[0] > 416 and event.pos[0] < 440 and event.pos[1] > 67 and event.pos[1] < 94: #>
                                if bpms[currentbpm][1] != None:
                                    songbpm += 1
                                    bpms[currentbpm][1] = songbpm
                                    bpmupdate(songbpm)
                                    markssnap()
                            if event.pos[0] > 446 and event.pos[0] < 506 and event.pos[1] > 67 and event.pos[1] < 94: #TAP button

                                #not lazy for once
                                if songbpm != 0:
                                    songchannel.unpause()

                                    animationopacity = 60
                                    bpmsetbytap.append(songchannel.get_pos())
                                    if len(bpmsetbytap) == 8:
                                        clicksdelayonetoeigth = [(bpmsetbytap[1]-bpmsetbytap[0]),(bpmsetbytap[2]-bpmsetbytap[1]),(bpmsetbytap[3]-bpmsetbytap[2]),(bpmsetbytap[4]-bpmsetbytap[3]),(bpmsetbytap[5]-bpmsetbytap[4]),(bpmsetbytap[6]-bpmsetbytap[5]),(bpmsetbytap[7]-bpmsetbytap[6])]
                                        clicksdelaycombined = clicksdelayonetoeigth[0]+clicksdelayonetoeigth[1]+clicksdelayonetoeigth[2]+clicksdelayonetoeigth[3]+clicksdelayonetoeigth[4]+clicksdelayonetoeigth[5]+clicksdelayonetoeigth[6]
                                        averagedelay = clicksdelaycombined / len(clicksdelayonetoeigth) #in ms

                                        tickspersec = 1000 / averagedelay
                                        songbpm = tickspersec * 60
                                        songbpm = round(songbpm,0)
                                        bpms[currentbpm][1] = songbpm
                                        bpmupdate(songbpm)

                                        bpmsetbytap.clear()


                                    

                        elif firstbarmode == 'OFFSET':
                            if event.pos[0] > 2 and event.pos[0] < 156 and event.pos[1] > 67 and event.pos[1] < 94: #OFFSET
                                firstbarmode = 'BPM'
                            if event.pos[0] > 489 and event.pos[0] < 508 and event.pos[1] > 67 and event.pos[1] < 94: #>
                                if bpms[currentbpm][1] != None:
                                    offset += 1
                                    bpms[currentbpm][0] = offset
                                    bpmupdate(songbpm)
                                    markssnap()
                            if event.pos[0] > 466 and event.pos[0] < 489 and event.pos[1] > 67 and event.pos[1] < 94: #<
                                if bpms[currentbpm][1] != None:
                                    offset -= 1
                                    bpms[currentbpm][0] = offset
                                    bpmupdate(songbpm)
                                    markssnap()

                    if event.button == 2: #scroll wheel click
                        pass

                    if event.button == 3: #RMB
                        pass

                    if event.button == 4: #scroll wheel up
                        if windowscaled:

                            desktopsize = pygame.display.get_desktop_sizes()
                            if desktopsize[0][1] > 1023:
                                eventpos = []
                                eventpos.append(event.pos[0] / 2)
                                eventpos.append(event.pos[1] / 2)
                            else:
                                eventpos = []
                                eventpos.append(event.pos[0])
                                eventpos.append(event.pos[1])
                        if not windowscaled:
                            eventpos = []
                            eventpos.append(event.pos[0])
                            eventpos.append(event.pos[1])


                        if buttonsmode == 'volume':
                            if eventpos[0] > 439 and eventpos[0] < 477 and eventpos[1] > 339 and eventpos[1] < 486: #sfx scroll
                                newvolume = int(beepsound.get_volume()*100+5) / 100
                                if newvolume > 1:
                                    newvolume = 1
                                beepsound.set_volume(newvolume)
                                bopsound.set_volume(newvolume)
                                continue
                            if eventpos[0] > 387 and eventpos[0] < 431 and eventpos[1] > 339 and eventpos[1] < 486: #music scroll
                                newvolume = int(songchannel.get_volume()*100+5) / 100
                                if newvolume > 1:
                                    newvolume = 1
                                songchannel.set_volume(newvolume)
                                continue

                      

                        if firstbarmode == 'BPM':
                            if eventpos[0] > 388 and eventpos[0] < 444 and eventpos[1] > 64 and eventpos[1] < 96: #<>
                                if bpms[currentbpm][1] != None:
                                    songbpm += 1
                                    bpms[currentbpm][1] = songbpm
                                    bpmupdate(songbpm)
                                    lastmainbeatmark = 0
                                    lastallbeatmark = 0

                                    try:
                                        while songposition > mainbeatmarkms[lastmainbeatmark]:
                                            lastmainbeatmark += 1  
                                    except IndexError:
                                        pass

                                    try:
                                        while songposition > allbeatmarksms[lastallbeatmark]:
                                            lastallbeatmark += 1
                                    except IndexError:
                                        pass

                                    bpms[currentbpm][3] = lastmainbeatmark
                                    bpms[currentbpm][4] = lastallbeatmark

                                    markssnap()
                            else:
                                if playing:
                                    try:

                                        lastmainbeatmark -= 2
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        beatnum -= 2
                                        if beatnum == 0:
                                            beatnum = 4
                                        if beatnum == -1:
                                            beatnum = 3
                                        bpms[currentbpm][5] = beatnum
                                        songstartpoint = mainbeatmarkms[lastmainbeatmark]

                                        songchannel.play(0,songstartpoint/1000)
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference


                                        if lastmainbeatmark < 0:
                                            lastmainbeatmark = 0
                                            lastallbeatmark = 0
                                            beatnum = 4
                                            songstartpoint = 0
                                            songchannel.play(0,0)
                                            visualposition = 0 
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            bpms[currentbpm][4] = lastallbeatmark
                                            bpms[currentbpm][5] = beatnum

                                        while songstartpoint < allbeatmarksms[lastallbeatmark]:
                                            lastallbeatmark -= 2
                                            bpms[currentbpm][4] = lastallbeatmark




                                    except pygame.error:
                                        print('pygameerror')
                                        songstartpoint = mainbeatmarkms[lastmainbeatmark]
                                        songchannel.pause()
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference
                                        playing = False

                                    except IndexError:
                                        lastmainbeatmark = 0
                                        lastallbeatmark = 0
                                        beatnum = 4
                                        songstartpoint = 0
                                        songchannel.play(0,0)
                                        visualposition = 0 
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        bpms[currentbpm][4] = lastallbeatmark
                                        bpms[currentbpm][5] = beatnum

                                else: #not playing
                                    try:

                                        lastallbeatmark -= 1
                                        bpms[currentbpm][4] = lastallbeatmark
                                        songstartpoint = allbeatmarksms[lastallbeatmark]
                                        songchannel.play(0,songstartpoint/1000)
                                        songchannel.pause()
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference

                                        while songstartpoint < mainbeatmarkms[lastmainbeatmark-1]:
                                            lastmainbeatmark -= 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            beatnum -= 1
                                            if beatnum == 0:
                                                beatnum = 4
                                            bpms[currentbpm][5] = beatnum

                                        if lastallbeatmark < 0:
                                            if currentbpm > 0:
                                                currentbpm -= 1

                                                offset = bpms[currentbpm][0]
                                                songbpm = bpms[currentbpm][1]
                                                beatsmode = bpms[currentbpm][2]
                                                lastmainbeatmark = bpms[currentbpm][3]
                                                lastallbeatmark = bpms[currentbpm][4]
                                                beatnum = bpms[currentbpm][5]

                                                bpmupdate(songbpm)

                                                bpms[currentbpm+1][4] = 1

                                                songstartpoint = offset
                                                songposition = allbeatmarksms[lastallbeatmark]
                                                songchannel.play(songposition,songstartpoint/1000)
                                                songchannel.pause()
                                                visualposition = allbeatmarkspixels[lastallbeatmark]
                                            else:
                                                lastallbeatmark = 0
                                                lastmainbeatmark = 0
                                                beatnum = 4
                                                songstartpoint = 0
                                                songchannel.play(0,0)
                                                songchannel.pause()
                                                visualposition = 0
                                                bpms[currentbpm][3] = lastmainbeatmark
                                                bpms[currentbpm][4] = lastallbeatmark
                                                bpms[currentbpm][5] = beatnum


                                    except pygame.error:
                                        print('pygameerror')
                                        songchannel.stop()

                                        songstartpoint = allbeatmarksms[lastallbeatmark]
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference

                                        playing = False

                                    except IndexError:
                                        lastallbeatmark = 0
                                        lastmainbeatmark = 0
                                        beatnum = 4
                                        songstartpoint = 0
                                        songchannel.play(0,0)
                                        songchannel.pause()
                                        visualposition = 0
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        bpms[currentbpm][4] = lastallbeatmark
                                        bpms[currentbpm][5] = beatnum

                        elif firstbarmode == 'OFFSET':
                            if eventpos[0] > 462 and eventpos[1] > 64 and eventpos[1] < 96: #<>
                                if bpms[currentbpm][1] != None:
                                    offset += 5
                                    bpms[currentbpm][0] = offset
                                    bpmupdate(songbpm)
                                    markssnap()
                            else:
                                if playing:
                                    try:

                                        lastmainbeatmark -= 2
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        beatnum -= 2
                                        if beatnum == 0:
                                            beatnum = 4
                                        if beatnum == -1:
                                            beatnum = 3
                                        bpms[currentbpm][5] = beatnum
                                        songstartpoint = mainbeatmarkms[lastmainbeatmark]

                                        songchannel.play(0,songstartpoint/1000)
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference


                                        if lastmainbeatmark < 0:
                                            lastmainbeatmark = 0
                                            lastallbeatmark = 0
                                            beatnum = 4
                                            songstartpoint = 0
                                            songchannel.play(0,0)
                                            visualposition = 0 
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            bpms[currentbpm][4] = lastallbeatmark
                                            bpms[currentbpm][5] = beatnum

                                        while songstartpoint < allbeatmarksms[lastallbeatmark]:
                                            lastallbeatmark -= 2
                                            bpms[currentbpm][4] = lastallbeatmark




                                    except pygame.error:
                                        print('pygameerror')
                                        songstartpoint = mainbeatmarkms[lastmainbeatmark]
                                        songchannel.pause()
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference
                                        playing = False

                                    except IndexError:
                                        lastmainbeatmark = 0
                                        lastallbeatmark = 0
                                        beatnum = 4
                                        songstartpoint = 0
                                        songchannel.play(0,0)
                                        visualposition = 0 
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        bpms[currentbpm][4] = lastallbeatmark
                                        bpms[currentbpm][5] = beatnum

                                else: #not playing
                                    try:

                                        lastallbeatmark -= 1
                                        bpms[currentbpm][4] = lastallbeatmark
                                        songstartpoint = allbeatmarksms[lastallbeatmark]
                                        songchannel.play(0,songstartpoint/1000)
                                        songchannel.pause()
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference

                                        while songstartpoint < mainbeatmarkms[lastmainbeatmark-1]:
                                            lastmainbeatmark -= 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            beatnum -= 1
                                            if beatnum == 0:
                                                beatnum = 4
                                            bpms[currentbpm][5] = beatnum

                                        if lastallbeatmark < 0:
                                            lastallbeatmark = 0
                                            lastmainbeatmark = 0
                                            beatnum = 4
                                            songstartpoint = 0
                                            songchannel.play(0,0)
                                            songchannel.pause()
                                            visualposition = 0
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            bpms[currentbpm][4] = lastallbeatmark
                                            bpms[currentbpm][5] = beatnum


                                    except pygame.error:
                                        print('pygameerror')
                                        songchannel.stop()

                                        songstartpoint = allbeatmarksms[lastallbeatmark]
                                        visualposition = float(songstartpoint / 2) * zoomuserpreference

                                        playing = False

                                    except IndexError:
                                        lastallbeatmark = 0
                                        lastmainbeatmark = 0
                                        beatnum = 4
                                        songstartpoint = 0
                                        songchannel.play(0,0)
                                        songchannel.pause()
                                        visualposition = 0
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        bpms[currentbpm][4] = lastallbeatmark
                                        bpms[currentbpm][5] = beatnum

                    if event.button == 5: #scroll wheel down

                        if windowscaled:

                            desktopsize = pygame.display.get_desktop_sizes()
                            if desktopsize[0][1] > 1023:
                                eventpos = []
                                eventpos.append(event.pos[0] / 2)
                                eventpos.append(event.pos[1] / 2)
                            else:
                                eventpos = []
                                eventpos.append(event.pos[0])
                                eventpos.append(event.pos[1])
                        
                        if not windowscaled:
                            eventpos = []
                            eventpos.append(event.pos[0])
                            eventpos.append(event.pos[1])

                        if buttonsmode == 'volume':
                            if eventpos[0] > 439 and eventpos[0] < 477 and eventpos[1] > 339 and eventpos[1] < 486: #sfx scroll
                                newvolume = int(beepsound.get_volume()*100-5) / 100
                                if newvolume < 0:
                                    newvolume = 0
                                beepsound.set_volume(newvolume)
                                bopsound.set_volume(newvolume)
                                continue
                            if eventpos[0] > 387 and eventpos[0] < 431 and eventpos[1] > 339 and eventpos[1] < 486: #music scroll
                                newvolume = int(songchannel.get_volume()*100-5) / 100
                                if newvolume < 0:
                                    newvolume = 0
                                songchannel.set_volume(newvolume)
                                continue

                        

                        if firstbarmode == 'BPM':
                            if eventpos[0] > 388 and eventpos[0] < 444 and eventpos[1] > 64 and eventpos[1] < 96: #<>
                                if songbpm > 1:
                                    if bpms[currentbpm][1] != None:
                                        songbpm -= 1
                                        bpms[currentbpm][1] = songbpm
                                        bpmupdate(songbpm)
                                        markssnap()
                            else:
                                if playing:
                                    try:

                                        if songposition == mainbeatmarkms[lastmainbeatmark]:
                                        
                                            lastmainbeatmark += 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            beatnum += 1
                                            if beatnum == 5:
                                                beatnum = 1
                                            bpms[currentbpm][5] = beatnum

                                        try:
                                            songstartpoint = mainbeatmarkms[lastmainbeatmark]
                                            songchannel.play(0,songstartpoint/1000)
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                        except pygame.error:
                                            print('pygameerror')
                                            songchannel.pause()

                                            songstartpoint = mainbeatmarkms[lastmainbeatmark]
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                            playing = False

                                    except IndexError:
                                        pass
                                    
                                else: #not playing
                                    try:
                                        if songposition == allbeatmarksms[lastallbeatmark]:

                                            lastallbeatmark += 1
                                            bpms[currentbpm][4] = lastallbeatmark

                                        try:

                                            songstartpoint = allbeatmarksms[lastallbeatmark]
                                            songchannel.play(0,songstartpoint/1000)
                                            songchannel.pause()
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                            while songstartpoint > mainbeatmarkms[lastmainbeatmark]:
                                                lastmainbeatmark += 1
                                                bpms[currentbpm][3] = lastmainbeatmark
                                                beatnum += 1
                                                if beatnum == 5:
                                                    beatnum = 1
                                                bpms[currentbpm][5] = beatnum

                                        except IndexError:
                                            while songstartpoint > mainbeatmarkms[lastmainbeatmark-1]:
                                                lastmainbeatmark += 1
                                                bpms[currentbpm][3] = lastmainbeatmark
                                                beatnum += 1
                                                if beatnum == 5:
                                                    beatnum = 1
                                                bpms[currentbpm][5] = beatnum

                                        except pygame.error:
                                            print('pygameerror')
                                            songchannel.pause()

                                            songstartpoint = allbeatmarksms[lastallbeatmark]
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                            playing = False

                                    except IndexError:
                                        pass
                                    
                        elif firstbarmode == 'OFFSET':
                            if eventpos[0] > 462 and eventpos[1] > 64 and eventpos[1] < 96: #<>
                                if offset > 1:
                                    if bpms[currentbpm][1] != None:
                                        offset -= 5
                                        bpms[currentbpm][0] = offset
                                        bpmupdate(songbpm)
                                        markssnap()
                            else:
                                if playing:
                                    try:

                                        if songposition == mainbeatmarkms[lastmainbeatmark]:
                                        
                                            lastmainbeatmark += 1
                                            bpms[currentbpm][3] = lastmainbeatmark
                                            beatnum += 1
                                            if beatnum == 5:
                                                beatnum = 1
                                            bpms[currentbpm][5] = beatnum

                                        try:
                                            songstartpoint = mainbeatmarkms[lastmainbeatmark]
                                            songchannel.play(0,songstartpoint/1000)
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                        except pygame.error:
                                            print('pygameerror')
                                            songchannel.pause()

                                            songstartpoint = mainbeatmarkms[lastmainbeatmark]
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                            playing = False

                                    except IndexError:
                                        pass
                                    
                                else: #not playing
                                    try:
                                        if songposition == allbeatmarksms[lastallbeatmark]:

                                            lastallbeatmark += 1
                                            bpms[currentbpm][4] = lastallbeatmark

                                        try:

                                            songstartpoint = allbeatmarksms[lastallbeatmark]
                                            songchannel.play(0,songstartpoint/1000)
                                            songchannel.pause()
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                            while songstartpoint > mainbeatmarkms[lastmainbeatmark]:
                                                lastmainbeatmark += 1
                                                bpms[currentbpm][3] = lastmainbeatmark
                                                beatnum += 1
                                                if beatnum == 5:
                                                    beatnum = 1
                                                bpms[currentbpm][5] = beatnum
                                        except IndexError:
                                            while songstartpoint > mainbeatmarkms[lastmainbeatmark-1]:
                                                lastmainbeatmark += 1
                                                bpms[currentbpm][3] = lastmainbeatmark
                                                beatnum += 1
                                                if beatnum == 5:
                                                    beatnum = 1
                                                bpms[currentbpm][5] = beatnum

                                        except pygame.error:
                                            print('pygameerror')
                                            songchannel.pause()

                                            songstartpoint = allbeatmarksms[lastallbeatmark]
                                            visualposition = float(songstartpoint / 2) * zoomuserpreference

                                            playing = False

                                    except IndexError:
                                        pass
                                    
                if event.type == pygame.MOUSEBUTTONUP:
                    holdingsfx = False
                    holdingmusic = False

                if event.type == pygame.MOUSEMOTION:
                    if buttonsmode == 'volume':
                        if holdingmusic:
                            holdingmusic = True
                            newvolume = int(465-event.pos[1]) / 100
                            if newvolume > 1:
                                newvolume = 1
                            if newvolume < 0:
                                newvolume = 0
                            songchannel.set_volume(newvolume)

                        if holdingsfx:
                            newvolume = int(465-event.pos[1]) / 100
                            if newvolume > 1:
                                newvolume = 1
                            if newvolume < 0:
                                newvolume = 0
                            beepsound.set_volume(newvolume)
                            bopsound.set_volume(newvolume)

                if event.type == pygame.KEYDOWN:
                    if not textbox_typing:
                        if event.key == 32: #space button

                            
                            if playing == False:
                                if offset == None:
                                    if songposition > songlengthms-10:
                                        lastmainbeatmark = 0
                                        lastallbeatmark = 0
                                        beatnum = 4
                                        songposition = 0
                                        songstartpoint = 0
                                        visualposition = 0
                                        songchannel.play(0,0)
                                        songchannel.pause()
                                        playing = False
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        bpms[currentbpm][4] = lastallbeatmark
                                        bpms[currentbpm][5] = beatnum

                                        continue
                                else:
                                    if songposition > songlengthms-10-offset:
                                        lastmainbeatmark = 0
                                        lastallbeatmark = 0
                                        beatnum = 4
                                        songposition = 0
                                        songstartpoint = 0
                                        visualposition = 0
                                        songchannel.play(0,0)
                                        songchannel.pause()
                                        playing = False
                                        bpms[currentbpm][3] = lastmainbeatmark
                                        bpms[currentbpm][4] = lastallbeatmark
                                        bpms[currentbpm][5] = beatnum

                                        continue
                                playing = True
                                songstartpoint = songposition
                                songchannel.play(0,songstartpoint / 1000)
                            elif playing == True:
                                playing = False
                                songchannel.pause()




        windowfps.tick(120)
    except Exception as error_traceback:
        easygui.exceptionbox('A Fatal Error Occured!\n\nPlease report this bug to the creator of this program.\nIm very sorry that this happened.\nYour project should save.\n\nThe program will close right after.','Fatal Error!')
        savingerrors = 0
        while True:
            try:
                sbttl_file_save_scene(EDITORVERSION,songfiledir,songbpm,offset,beatsmode,markedlistmsandtext)
                break
            except Exception:
                if savingerrors == 0:
                    easygui.exceptionbox('Can not save the project properly.\nGiving it a second chance.\n\nImportant data could be lost.','SAVING ERROR')
                    savingerrors += 1
                    continue
                if savingerrors < 5 and savingerrors > 0:
                    easygui.exceptionbox('Can not save the project properly.\nTrying again.\n\nImportant data could be lost.','SAVING ERROR')
                    savingerrors += 1
                    continue
                if savingerrors >= 5:
                    messagebox.showerror(' ','I tried.')
                    messagebox.showerror(' ',"It's all gone.")
                    messagebox.showerror(' ',"Forgive me.")
                    break
        break
            

        