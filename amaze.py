from art import text2art
import random
from random import choice
from random import random
# JOB ID 3
D("ralt144mi", shape=.6, delay=0.5, delaytime=.75, delayfeedback=.60, 
  room=0.8, dry=0.0, size=0.7, orbit=3, accelerate=0.15)

silence()

pi >> n("C4",p=0.5, channel=1)

silence(pi)

clock.tempo=137

bb >> zd("leCASIOvib:[0~10]", 
        "t (0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2",
        key="C", scale="chromatic", 
        #speed=0.5,
        pan=1,
        speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        #leg=0.8, octersub=1, 
        leg=0.1,
        triode = 4.6, shape=0.25, orbit=0,
        delay = 0.8, delaytime = "0.5!3 1", delayfeedback = "($%20)/20", gain=0.97
        )
bo >> zd("leCASIOvib:[0~10]", 
        "t (0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2", #< >
        key="C", scale="chromatic", 
        #speed=0.25, 
        pan=0,
        speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        #leg=0.8, octersub=1, 
        leg=0.1,
        triode = 4.6, shape=0.25, orbit=1,
        delay = 0.8, delaytime = "0.5!3 1", delayfeedback = "($%20)/20", gain=0.97
        )
#VOCODER

Pv >> zn("((e 0)+(4 <2 9 5> 7)):2", scale = "chromatic", key="C#",channel="1", dur=1, velocity=80)

dirt.nudge=(0.5)

Pv * None

panic()

Pb >> d("bassfoo . laSNARE leHIHAT:18", begin=0.082,hpf="10*($%10)*10",
        #p="0.5", 
        orbit = 2, real=0.9, imag=0.25
        )


clock.tempo = 187 #187.5 #rajoute un t au accord au dessus !




silence()

@swim 
def legrosbeat(p=0.5,i=0):
    D("kick:4 . kick:5 .. kick:10", triode=0.4,euclid=(3,3,1), 
            shape=0.65,pan = "{0 1}", div=2, i=i)
    D('. . snare:9 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i)
    D("long:15", n='{F2 F3} F2|F3', leg=0.15, pan="rand",
            amp='0.3~0.5', i=i)
    again(legrosbeat, p=1,i=i+1) #p=0.5

Pd * d('february:[0:10]', amp=0.4, p=.5, leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('.!8 october:[0:10]', p=.25, leg=.1, pan='rand', on=2, speed=2)

#Yelling/singing Time 

silence(legrosbeat)


Pm >> d("long:15", n='{F1 F2} F1|F2', leg=0.15, pan="rand", p=0.5, amp='0.3~0.5',
        accelerate = "-0.5*rand 0.5*rand", orbit=2, octersub=2, triode = 0.5
        )

@swim 
def legrosbeat(p=0.5,i=0):
    D("kick:4 . kick:5 .. kick:10", triode=0.4,euclid=(3,3,1), 
            shape=0.65,pan = "{0 1}", div=2, i=i)
    D('. . snare:9 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i)
    again(legrosbeat, p=0.5,i=i+1) #p=0.5

silence(Pk, Ps, Pi, Pn, Py, Pd, Pe,Pz)

silence(Pu)

'
 █▄ ▄█ ▄▀▄ █▄ █   ▄▀▄ █▀▄ █▀▄ █
 █ ▀ █ ▀▄▀ █ ▀█   ▀▄▀ █▀▄ █▄▀ █
 ██▀ ▄▀▀ ▀█▀   ▄▀▄ █▄ ▄█ ▄▀▄ █ █ █▀▄ ██▀ █ █ ▀▄▀
 █▄▄ ▄██  █    █▀█ █ ▀ █ ▀▄▀ ▀▄█ █▀▄ █▄▄ ▀▄█ █ █
'
#I think my computer is in love.


silence()
clock.tempo = 144
Pr * d("sid:0 ..",
        shape = 0.5,
        speed='{1 0.99}',
        p=0.5, div= 2,
)

Pu * d("sid:2", 
        euclid=(3,3,1), 
        shape=0.65,
        pan = "{0 1}"
)

Px * d("(eu sid:4 5 8)", 
       leg=.1, p=0.25, 
       on=3, speed=0.5,
       shape=0.65, pan = "0"
)

PX * d("(eu sid:4 5 8 2)", 
       leg=.1, p=0.25, 
       on=2, speed=1,
       shape=0.65, pan = "1"
)

xX * d("(eu sid:4 5 8 4)", 
       leg=.1, p="0.25", 
       on=4, speed=2,
       shape=0.65, pan = "0.5"
)


Pd * zd("braids", "s 9 8 7" , # 4 5 6 (après)
        model="25*rand",
        color=0.55, timbre = 0.1, 
        lpf=6000, gain=0.8, leg=0.25,
        scale="rocritonic", 
        pan="{0 1}", room=0.8, size=0.5,
        dry=0.2, orbit=4, amp=0.2, # fade in
)


Ph >> d("sid:[7~9]",
        pan = "(if(every 4) r 2/3+0.23)",
        shape = "(if(beat 3 4) 0.5 0.1)",
        euclid=(7,8,4),
        p="0.5!8 0.25!4"
)

##########PAD

Pp >> zd('braids', "0.25 <[_0 7 6 5] [_0 8 6 9]> <[8 9] [7 8]>", 
         model='10', scale = "rocritonic", channel = 0, gain=0.8, 
         speed='{1 0.5}', lpf='500 + (abs (sin $/2)) * 2000', dur=1.5,
         room=0.9, size=0.25, dry=0.5, orbit=2, amp=0.05 # fade in et fade out l'autre,
)

##########Break

Pu >> None 
Pr >> None


Pu * d("kick:4 . kick:5 .. kick:10", 
        triode=0.4,
        euclid=(3,3,1), 
        shape=0.65,
        pan = "{0 1}"
)

Pi * d ('. . snare:9 .', room=0.8, size=0.5, dry='0.3 0.5 0.1')

silence(Pu, Pi)

#Casio Solo ! 

# remettre le sidkick 
# remonter sur 9 8 7 et jouer

@swim #die
def tempomedler(p=0.5, i=0):
    if clock.tempo < 240 :
        clock.tempo = clock.tempo*1.009
    else:
        clock.tempo = 200
    print(text2art("try to dance on that","straight"))
    again(tempomedler, p=0.5, i=i+1)



'
 █ █ █▄ █   ▄▀▄ █▀▄ █▀▄ █
 ▀▄█ █ ▀█   ▀▄▀ █▀▄ █▄▀ █

 ██▀ ▄▀▀ ▀█▀   █ █ █▄ █ ██▀  
 █▄▄ ▄██  █    ▀▄█ █ ▀█ █▄▄  

 ▄▀  █▀▄ ▄▀▄ ▄▀▀ ▄▀▀ ██▀
 ▀▄█ █▀▄ ▀▄▀ ▄██ ▄██ █▄▄

 ▄▀▀ ▄▀▄ █   ▄▀▀ █ █ █   ██▀ ▀█▀ ▀█▀ ██▀
 ▀▄▄ █▀█ █▄▄ ▀▄▄ ▀▄█ █▄▄ █▄▄  █   █  █▄▄

 ▄▀▀ ▄▀▄ ▄▀▀ █ ▄▀▄
 ▀▄▄ █▀█ ▄██ █ ▀▄▀
'
#my computer is just a big casio calculator

#Casio Rock-1 playing [tempo-[   2]]

silence()
clock.tempo = 144

Ph >> d("casio:2", leg=0.1,
       p=0.5, euclid=(2,3),
       pan='0', amp='0.1 + rand/2',
        #scram=0.5
)

Ps >> d("casio:0", leg=0.1,
        p=0.5, euclid=(2,3,1),
        pan = 0.75, speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))"
        #scram = 0.5
)

Pp >> d("casio:1", leg=0.1, p=0.5, 
        n='[[A G F E D C]!!2]!!4',
        euclid=(2,3,2), pan = 0.5,
        #scram =0.25
        )

Pz >> d(". casio:2", leg=0.1, p=0.5,
        euclid=(3,3), pan = 1,
        # scram =2
)

Pk >> d(
        "sid:2 sid:[0~2]",
        n='C',
        #"sid:0",
        octersub = 1.2, 
        shape=0.4,
        pan="2/3+0.25 1/3+0.03",
        leg=0.15,
        p="0.5!8"
)


Pk >> None

# DE3
PA >> zd(
        "braids", 
        "(s _ 0 5 7 6 7 0 8 7 5 9 | s 0 5 6 7 5 1 6 3 0)+(5 <7 7 5> 5)", #modifie cela Rémi
        scale = "pentatonic", key="C",
        # lpf = 9000, 
        gain=0.78,
        model= 5, accelerate=0.05, #0.5
        color = "[0.9~0.2]", # scram=0.26,
        timbre = "[0.2~0.8]",
        leg=0.25,
        lpf="100 + (abs(cos($))*5000!16) ", res=0.38,orbit=1,
        #lpf="100 + 100*($%40)", res=0.40 # 0.2
)

bu * d('may:[1 2] . february:rand*4', p=.5, leg=.25, shape=.3, pan='rand', speed='1 2')

bi * d('(eu leHIHAT:6 7 8)', lpf='9000~11000', p=.25, leg=.1, shape=.2)

PA.stop()
Pk.stop()

Ph >> d("casio:2 casio:2 .. casio:2 ....", leg=0.1,
       p=0.25, euclid=(2,3),
       pan=0,
        #scram=0.5
)

Ps >> d("casio:0", leg=0.1,
        p=0.5, euclid=(2,3,1),
        speed='{1 0.5} {1 0.99} {0.5 0.25}',
        pan = "{0 0.5 1}",
        #scram = 0.5
)

Pk >> d(
        "(eu leKICK:3 5 8)",
        #"sid:0",
        p=0.5,
        lpf="500!8 (abs (sin($)))*1500!4", #res=0.4,
        octersub = 1.2, 
        shape=0.4,
        # pan="2/3+0.25 1/3+0.03",
)

#REMET LE LEAD REMI Va Y FAIT LE STp TSP STPb jzopklklkl,

PA.stop()

# Fade 1
silence(Pk, PA, Pz, Pp, Ph, Ps)

# Fade 2
silence()

'
 █▄ █ ██▀ █ █ ██▀ █▀▄ ▄▀▀
 █ ▀█ █▄▄ ▀▄▀ █▄▄ █▀▄ ▄██
'

silence()
clock.tempo = 187.5

#8-bit HURDYGURDY TIME

Pi >> d(". nevers:1", 
        coarse=6, crush=6, delay=0.8, delaytime=.05, delayfb=0.80, 
        room=0.8, wet=0.8, size=0.2,
        orbit=3, loaf=4, on=(1,2), leg=1, pan="0", p=1, gain=0.9)

Pn >> d("nevers:1 .",
        coarse=6, crush=6, delay=0.8, delaytime=.05, delayfb=0.80, 
        room=0.8, wet=0.8, size=0.2,
        begin=0.5, pan="0.5", leg=1, p=2, gain=0.9, orbit=3)

#APRES
Py >> d(". nevers:1 .", 
        coarse=6, crush=6, delay=0.8, delaytime=.05, delayfb=0.80, 
        room=0.8, wet=0.8, size=0.2,
        begin=0.8, pan="rand", leg=1, p=2, shape=0.4, orbit=3)

# DEBUT
ii >> d(".. nevers:1", 
        coarse=6, crush=6, delay=0.8, delaytime=.05, delayfb=0.80, 
        room=0.8, wet=0.8, size=0.2,
        loaf=4, on=(1,2), pan="0", p=1, gain=0.9, orbit=3, speed=4, leg=.2)


#2 3 4 15

Pm >> d("long:15", n='{C#3 C#4} C#3|C#4', leg=0.15, pan="rand", p=0.5, amp='0.3~0.5')

Pd * d('february:[0:10]', amp=0.4, p=.5, leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('.!8 october:[0:10]', p=.25, leg=.1, pan='rand', on=2, speed=2)

Py >> None

#f is a loud kick i think

Pk >> d("f",
        #binshift="1.5!4 2.5!4 3.5!4 4.5!4 5.5!4 6.5!4",#1.5 2.5 3.5
        #p="2 2 2 1 1", #alafin
        shape=0.6,
        leg='0.75~1',
        euclid = (5,6), #1 2 3
)

Ps >> d(#"laSNARE:3",
        "laSNARE:[2~9]",
        euclid = (4,5,3), #(5,5)
        room=0.25, lpf= 2000,
        leg= 0.08,
        pan="rand",
        p=0.5
)

Pz * d('... snare:10', shape=.5, room=0.5, dry=0.2, size=0.4)

silence(Pk, Ps, Pi, Pn, Py, Pd, Pe)

#H10

VV * zn("q. 0 e 0 q. 0 e r r 2 4 5 q 4 2", scale = "chromatic", dur=1,channel=1) 

vv * zn("q. 047", velocity=20, scale = "chromatic", dur=1,channel=1) 


PASSER SUR DU SOLO

silence()


'
 ▀█▀ █ █ ▀█▀   █▀▄ █ █▀▄   ██▄ ▄▀▄ █▀▄
  █  ▀▄█  █    █▀  █ █▀    █▄█ ▀▄▀ █▀ 
'

clock.tempo=144


Ll >> d("long:40 long:41 long:40 long:[40~44]", 
        speed = "0.5!7 0.7", pan="rand", shape=.45,
        leg=0.5)


Pk >> d("leKICK . . . leKICK:4 . .", shape=0.5, p=0.5,)

Pk >> d("leKICK laSNARE:8 leHIHAT leHIHAT leKICK:4 leHIHAT leHIHAT", shape=0.5, p=0.5, 
        )

Pk >> None

@swim
def croa(p=0.5, i=0):
    D("maloya",
    #begin=0.2,
    #begin=0.25,
    begin = "0.5 0.25 1 0 0.1",
    #leg=0.20, 
    leg = "0.20 0.1 0.25 0.1",
    pan="0.25 0.17 0.33",
    shape=0.1,
    i=i)
    again(croa, p=P("0.5",i), i=i+1)

#it needs more kick maybe

kk >> d("f", lpf=100, leg=0.5, p=1,gain=2)

PA >> None

PB * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(2,9,5), 
        speed="{1 2 3}", pan = 0,
        #real=0.9, imag=0.25
        )
OP * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(2,9,9), 
        speed="{1 2 3}", pan = 1, 
        #real=0.9, imag=0.25
        )


PJ >> d("birds:[0~10]", pan="rand", p=4,#p="0.25!16 0.125!8", leg=0.25, 
        gain=0.9, #speed=0.125,
        begin="rand/2", orbit=4,
        real="(if (beat 4) 0.9 0)", imag="(if (beat 4) 0.5 0)"     
        )
ob * d(".birds3:[0~10]", pan="rand",p=4,# p="0.25!16 0.125!8",leg=0.25, 
        gain=0.9, #speed= 0.1225,
        begin="rand/2", orbit=4,
        real="(if (beat 4) 0.9 0)", imag="(if (beat 4) 0.5 0)"         
        )

si * zd("jungbass:12","e 0 5 0 0 7 0",gain=1.1)

silence(kk)

Pl * d("leCASIO:[0~9]", leg=0.9, p="0.5!2 0.125!2 0.25!2 0.5"*2)


ll *  d("long:[10~20]", lpf="1500!10 3500!2", gain=0.9,leg=0.2, p=2)

PK * d("leKICK:[6] {leHIHAT:[12] leKICK:6} {laSNARE:[5] laSNARE:8} leHIHAT:[12]",
        leg=0.2, p=1,orbit="{0 1}", 
        shape=0.3, room=0.5, gain=0.9, pan="{0 1}",
        #real=0.9, imag=0.25
        )

KK * d("maloya", 
        speed="{1 0.98 2 4}", 
        lpf="200+20*($%40)",res=0.1,gain=0.9, leg=1.2,
        )
Pl >> d("(eu maloya:1 9 16)", p=0.25, gain=0.8)
#Pj >> d("(eu {maloya:2 leKICK:2} 13 16)", p=0.5,
#        gain=1.2, octersub=2)

solo(KK) #descend

####
KK * d("maloya", 
        speed="{1 0.98 2 4}", 
        lpf="200+20*($%40)",res=0.1, gain=0.9, leg=1.2,
        )
Pl >> d("(eu maloya:1 9 16)", p=0.25, gain=0.8)
#Pj >> d("(eu {maloya:2 leKICK:2} 13 16)", p=0.5,
#        gain=1.2, octersub=2)

ll *  d("long:[10~20]", lpf="1500!10 3500!2", gain=0.9,leg=0.2, p=2)
PK * d("leKICK:[6] {leHIHAT:[12] leKICK:6} {laSNARE:[5] laSNARE:8} leHIHAT:[12]",
        leg=0.2, p=1,orbit="{2 3 0 1}", 
        shape=0.3, room=0.5, gain=0.6,
        delay=0.8, delaytime=.5, delayfeedback=.80, 
        )

PJ >> d("birds:[0~10]", pan="rand", p="0.25!16 0.125!8", leg=0.25, 
        gain=0.9, speed=0.125,
        begin="rand/2", orbit=4,
        real="(if (beat 4) 0.9 0)", imag="(if (beat 4) 0.5 0)"     
        )
ob * d(".birds3:[0~10]", pan="rand",p="0.25!16 0.125!8",leg=0.25, 
        gain=0.9, speed= 0.1225,
        begin="rand/2", orbit=4,
        real="(if (beat 4) 0.9 0)", imag="(if (beat 4) 0.5 0)"         
        )
PB * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(2,9,5), 
        speed="{1 2 3}", pan = 0,
        real=0.9, imag=0.25, gain=1.2
        )
OP * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(2,9,9), 
        speed="{1 2 3}", pan = 1, 
        real=0.9, imag=0.25, gain=1.2
        )

clock.tempo = 200 #220

####
silence()

############STOP we don't really need some mental techno thing 
###WHAT do we really need ????
#####An algorhythmic Karaoké ???? And some eurodance thing i think...


'
 ▄▀▄ █   ▄▀  ▄▀▄   █▄▀ ▄▀▄ █▀▄ ▄▀▄ ▄▀▄ █▄▀ ██▀
 █▀█ █▄▄ ▀▄█ ▀▄▀   █ █ █▀█ █▀▄ █▀█ ▀▄▀ █ █ █▄▄
'


silence()

from random import random
def drunk(text: str=" ", i: int=0, dry: float=0.5):
    done = text.split()
    done2 = text.split()
    wet_or_dry = random() >= dry 
    randomtrue = random() >= 0.5
    if wet_or_dry:
        return done[i % len(done)]
    else:
        if randomtrue:
            i=i-2
        else:
            i=i
        return done2[i % len(done2)]

montexte = join("Boom boom boom boom",
                "I want you in my room",
                "Let's spend the night together",
                "From now until forever",
                "Boom boom boom boom",
                "I wanna duble boom",
                "Let's spend the night together",
                "Together in my room",
                "Whoa oh whoa oh",
                "(Everybody get on down)",
                "Whoa oh whoa oh",
                "(Vengaboys are back in town)",
                "Whoa oh whoa oh",
                "This is what I wanna do",
                "Whoa oh whoa oh",
                "Let's have some fun",
                "Whoa oh whoa oh")


vengaboys = "| e _40 _40 e. _40 s _40 e _1_4 _1_4 q _1_4  |\
            e _2_5 _2_5 e. _2_5 s _2_5 e _2_5 _2_5 q _2_5  |\
            e _0_3 _0_3 e. _0_3 s _0_3 e _1_4 _1_4 q _1_4 | \
            | e _40 _40 e. _40 s _40 e _40 _40 q _40  |"
vengaboys1 = "| q 0 e _ 5 4 q ^ 0 e _ 5 4  | r r r r |"
vengaboys2 = "| q 0 e _ 5 4 q ^ 0 e _ 5 4  | e 2 2 2 3 4 2 q 0  |"
vengaboys3="| q r 2 2 1  |"
vengaboys4="| q 0 e r _ 4 4 4 ^ 1 1  | q 0 e r _ 5 5 5 ^ 0 1 | \
| e. 2  s 0 s r e _ 3 3 3 3 3  | e. _ 2 s ^ 0 q 2 2 1 | \
| q 0 e r _ 4 4 4 ^ 1 1  | q 0 e r _ 5 5 5 ^ 0 1 | \
| e. 2  s 0 s r e 0 2 2 1 1  | q 0 r h r 0.125 r | "

#resync
midi.nudge=0.5

silence()
clock.tempo=135

Pi >> None
Pj >> None
pJ >> None
def intro():
    Pi >> zd('synthi:67', vengaboys, gain=0.9, dur=0.1, leg=1, triode=.3)
    #Pj >> zd('synthi:63',vengaboys1, dur=0.1, leg=1, orbit=2, room=0.5, size=0.7, dry=0.5)
    Pj >> zd('synthi:65', vengaboys2, dur=0.1, orbit=2, amp=0.25, leg=1, room=0.5, size=0.7, dry=0.5)
    pJ * zn(vengaboys2, channel=1, dur=0.8)
intro()


dd * d('. hat . hat',p=.25, amp='0.2~0.5')
de * d('kick . snare:10 .', shape=.5, triode=.3)


@swim
def drunktext(p=0.5, i=0):
    dur=ZN(vengaboys4, channel = 8, i=i)#ms2000 
    print(text2art(drunk(montexte, i,P("0.2!8 0.8!2",i)), font="small"))
    again(drunktext,p=dur,i=i+1)
Pi>> None
Pj>> None
pJ * None
def refrain():
    Pi >> zd('{synthi:65 synthi:60}', vengaboys4, dur=0.1, orbit=2, 
            amp=0.25, leg=1, room=0.5, size=0.7, dry=0.5,
            #accelerate = "{-0.5*rand 0.5*rand}"
            )
    Pj >> zd('synthi:67', vengaboys, dur=0.1,orbit=2, amp=0.25, 
            leg=1, room=0.5, size=0.7, dry=0.5,
            #accelerate = "{-0.5*rand 0.5*rand}"
            )
    pJ * zn(vengaboys4, channel=1, dur=1)
########
refrain()

dd * d('. hat!2 . hat',p=.25, amp='0.2~0.5')
de * d('kick!2 snare:10 .', shape=.5, triode=.3)

Pd * d('february:[0:10]', amp=0.4, p=.5, leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('.!8 october:[0:10]', p=.25, leg=.1, pan='rand', on=2, speed=2)


PB * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(2,9,5), 
        speed="{1 2 3}", pan = 0,
        #real=0.9, imag=0.25
        )
OP * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(2,9,9), 
        speed="{1 2 3}", pan = 1, 
        #real=0.9, imag=0.25
        )

Pu * d("sid:2", 
        euclid=(3,3,1), 
        shape=0.65,
        pan = "{0 1}"
)

Ph >> d("casio:2 casio:2 .. casio:2 ....", leg=0.1,
       p=0.25, euclid=(2,3),
       pan=0,
        #scram=0.5
)

@swim #die
def tempomedler(p=0.5, i=0):
    if clock.tempo < 540 :
        clock.tempo = clock.tempo*1.9
    else:
        clock.tempo = 122
    print(text2art("IZBnzlnkf_è&éç~#[#{|[{|{#{{~#[~#&à","straight"))
    again(tempomedler, p=0.5, i=i+1)


silence()

###
##MORE vengaboys cover ???
###
silence()
clock.tempo = 136
updown ="| q __#3_#5 e r __#3_#5 q __6#1 __6#1  | q _#03 e r _#03 q __6#1 __6#1  | q __#3_#5 e r __#3_#5 q __6#1 __6#1  | q _#03 e r _#03 q __6#1 __6#1  |"
updown2 ="| e. __#3_#5 s __#3_#5 e r _#03 _#03 _#03 __6#1 __6#1  | e __#3_#5 __#3_#5 __#3_#5 s _#03 _#03 e _#03 _#03 __6#1 __6#1 | \
| e. __#3_#5 s __#3_#5 e r _#03 s _#03 _#03 e _#03 __6#1 __6#1  | q __#3_#5 e r s _#03 _#03 e _#03 _#03 __6#1 __6#1  |"
updownbass ="| e ___ #3 s ^ #3 #3 e _ #3 s ^ #3 #3 e _ #3 s ^ #3 #3 e _ #3 s ^ #3 #3  |"


Pi >> None
PI >> None
Po >> None
Pb * None
def part1():
    Pi >> zd("synthi:63",updown,leg=0.1)
    Po >> zd("synthi:66",updown2, leg=0.1)
part1()

PK * d("kick")

Pd * d('february:[0:10]', amp=0.4, p=.5, 
        leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('.!8 october:[0:10]', p=.125, leg=.1, pan='rand', on=3, speed=2)

Pi >> None
PI >> None
Po >> None
Pb * None
def updown():
    Pi >> zd("{synthi:66 synthi:63}",updown2, leg=0.3)
    PI >> zd("synthi:66",updown2, leg=0.3)
    Pb >> zd("jungbass:4",updownbass, speed = "{8 4}", leg=0.15)
########
updown()


PK * d("protokick",gain=1.5)

silence()


##maybe some zouk or maybe it's already over i dontknow already 
###message for the future me which is now me i think

'
 ____  ___   _   _  _  __
|_  / / _ \ | | | || |/ /
 / / | (_) || |_| ||   <
/___| \___/  \___/ |_|\_\
'


silence()
clock.tempo = 136

kassav1 = "| h _3_50 _3_40  | h _2_40 _1_4_6  |"
kassav2="| e _1_4_6 _1_4_6 _1_4_6 _1_4_6 s r e. _3_50 e _3_50 _3_50  | e _2_40 _2_40 _2_40 _2_40 s r e. _3_50 e _3_50 _3_50  |"
kassav3="| q r e 6 ^ 1 s r e. _ 5 q ^ 0  | q r e 4 ^ 0 s r e. _ 4 q 5 | \
| e 4 4 4 4 e. 4 s 3 r e. 5  | e 2 4 q r h r | \
| q r e 6 ^ 1 s r e. _ 5 q ^ 0  | q r e 4 ^ 0 s r e. _ 4 q 5 | \
| e 4 4 4 4 s r e 4 s 3 r e. 5  | e 2 4 q r h r  |"
kassav4="| e 6 6 6 6 s 6 e ^ 1 s _ 6 e 5 4  | q ^ 0 e r 0 s r e. _ 4 q 5  |"

#This is the code transcription of Zouk la se sel medikaman nou ni by KAssav

PC(program =26, channel=0)

Pa >> zd("synthi:60",kassav1,leg=0.8)

def kassav():
    silence()
    D("crow", room=0.5)
    Pb >> zd("synthi:65",kassav2,leg=0.45)
kassav()

Pk * d("(eu kick 2 3)")
Ph * d("(eu leHIHAT 13 16)", p=0.25)
Ps * d("(eu laSNARE:8 1 3 2)")

Pa >> None
Pb >> None
def kassavs():
    Pa >> zd("synthi:65",kassav2,leg=0.2)
    Pb >> zd("synthi:60",kassav3, leg=0.1)
kassavs()

Pa >> None
Pb >> None
def kassavs():
    Pa >> zd("synthi:65",kassav2,leg=0.2)
    Pb >> zd("synthi:60",kassav4, leg=0.1)
    #Pg >> n("A1!7 A1|C2",channel = 2, dur=0.5)
kassavs()

Pq >> d("crow", p=0.25, leg=0.1, gain=0.8,
        leslie=0.75, lrate="0.5 0.9 0.7 0.2", lsize=0.8
        )

Pg >> None

clock.tempo = 144

print(text2art("ZOUK", "small"))

silence()



#Thank you very much :)





<^{{{><

    R.
