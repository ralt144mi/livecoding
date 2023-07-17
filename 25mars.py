import ephem
from datetime import datetime, time

moon = ephem.Moon()
jupiter = ephem.Jupiter()
pluto = ephem.Pluto()
mars = ephem.Mars()
algorave = ephem.Observer()
algorave.date = '2023/04/08 00:50:22'
algorave.lat='45.765908'
algorave.long='9.926945'
moon.compute(algorave)
jupiter.compute(algorave)
pluto.compute(algorave)
mars.compute(algorave)
algorave.compute('2023/04/08 00:50:22')
###
pressure = algorave.compute_pressure()


print('%s %s' % , moon.az) )

ephem.constellation(moon)

climax = ephem.next_new_moon(algorave.date)
moon.moon_phase

@swim
def ephem (p=.25,i=0):
    ###
    pressure = algorave.compute_pressure() 
    print(algorave.pressure)
    print(moon.ra+ 0.0,mars.dec+ 0.0,mars.az+ 0.0,mars.alt+ 0.0)
    again(ephem,p=0.5, i=i+1)
































Pa >> zd("maloya:0", "e _ i:4 iv:4 v:4",
        #scale = "rocritonic", 
        accelerate = -0.01,
        leg=0.5,
        #leg = "0.8!8,0.1!4",
        #color = "cos($.p)"
        #,timbre = "sin($.p)"
        )

panic()

Ph >> d("if(beat(1,4),maloya:1,.)", leg=0.65, p = 1, shape = 0.6)

Ph >> None

Pl >> d("leKICK:[0~12], laSNARE:[0~12], .", p=0.125, d=8)

Pk >> zd('superpiano', "w 0 <1 5> h 35 e 2 [8 ^ [2 5]]", legato = 2, room = 0.8, sz =0.5, scale = 'rocritonic', lpf = 1500)

Pk >> None

Pi >> d("if(beat(2,4),maloya:1,maloya:0)", leg=0.65, p = 1, shape = 0.6)

clock.tempo = 135

@swim 
def euctrib(p=0.5,i=1):
    D("eu(leKICK:[2~5], 3,5)", p=2, shape =0.8,i=i)
    D("eu(laSNARE:[2~5], 2,5,2)", leg=0.25, p=2, d = "2,4", shape =0.8,i=i)
    D("eu(leHIHAT:[2~5], 9,10)", r=0.45, leg=0.025, p=0.25, d="1,2", shape =0.8,i=i)
    again(euctrib, p=0.5, i=i+1)

@die
def euctrib(p=0.5,i=1):
    D("eu(leKICK:[2~5], 3,5)", p=0.5, shape =0.8,i=i)
    D("eu(laSNARE:[2~5], 2,5,2)", leg=0.25, p=0.5, shape =0.8,i=i)
    D("eu(leHIHAT:(2|16), 9,10)", r=0.25, leg=0.025, p=0.25, shape =0.8,i=i)
    again(euctrib, p=2, i=i+1)

@die
def ziffprog(p=0.5,i=1):
    dur = ZD("braids",
            "e _ 7 q 5 (3,8)",
            #"e _ 7 q <5 3> (3,8) | e _ 7 q <7 5> (2,9)",
            model = 17, 
            color = "cos($)", timbre = "sin($.p)/2",
            scale ="rocritonic",i=i,
            shape =0.5)
    again(ziffprog, p=dur/2, i=i+1)

@swim 
def debile(p=0.5,i=1):
    D("morgan:2", leg = 8, accelerate = "-2, 0.5",
            begin = 0.8, end= 2,
            i=-i, shape = 0.9, lpf = 1500)
    again(debile, p=8, i=i+1)

from art import *

import random

printv("lol")

@swim 
def letest(p=0.5, i=1):
    #D("long", n="C5,.!4,E4,.!4", p=2, d=8,leg =5,
    #        i=i, lpf=1500, pan="rand"
    #        )
    #D("leKICK:2,.!3|leKICK:[2~50],.!3",shape=0.8, i=i,div=4,p=1)
    #D("leHIHAT:[2~8]!8", leg=0.15,i=i)
    D("braids", model=2, lpf=1500, n="pal(C3@min7,C4@min7, E4@min7)|pal(C4@min7)", i=i, delay="sin($)", delayfb="cos($)", delaytime=2.5 ,leg = 0.25, room=0.8, orbit =2, shape=0.8)
    print(text2art(str(clock.,"random"))
    again(letest,p=2/3, i=i+1)

panic()

Ph >> d

s >> 


