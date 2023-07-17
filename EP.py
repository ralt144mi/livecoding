from art import text2art
import random
from random import choice
# JOB ID 3
D("ralt144mi", shape=.6, delay=0.5, delaytime=.75, delayfeedback=.60, 
  room=0.8, dry=0.0, size=0.7, orbit=3, accelerate=0.15)

clock.tempo=142

clock.cps = (130/60/4)

D("softwareall",gain=0.9,lpf=2500)

d1 * s('software:3').striate(36)

d2 * s('~ software:1 [software:0 software:2]').striate(12)

hush()
"
░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░        ░░░░░      ░░░░░░░░
▒   ▒▒▒▒   ▒   ▒▒▒▒   ▒   ▒▒
▒   ▒▒▒▒   ▒▒   ▒▒▒▒▒▒▒▒   ▒
▓        ▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓
▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓   ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓▓   ▓
█   ██████████      ███     
████████████████████████████
"
Hommage à Parappa le Rapper

silence()

ps * d("ps1:7", p=8)

Ps * d("ps1:2",p=0.25,begin="rand", 
        leg="rand*0.25", lpf="1500*(ulsin 8)", res=0.4)

ss * d("ps1",p=8, orbit=2)

sS * d("ps1:6", p=8, coarse=8,triode=2)

tt * d("tekken:[0:4] leKICK:4", p=2, lpf=1500)

pp * d("parappa:[0~66]", p=1, leg=0.5/2, pan="rand", room=0.4, orbit=2)

Pp * d("parappa:[12:15]", p=0.5, leg=0.5/2, pan="0.5", accelerate=0.01)

pp * d("parappa:[0~66]", p=0.25, leg=0.125/2, pan="rand", room=0.8, orbit=2)

Pp * d("parappa:[12:15]", p=0.25, leg=0.125/2, pan="0.5", accelerate=0.01)

silence(tt)

tt * d("lsdelectro:15", p=1, leg=0.25,
        shape=0.15, lpf=1500, orbit=2)

hh * d("lsdelectro:4", p="0.5!12 0.25!8", leg=0.125/1.7)

Parappa shush

silence(pp, Pp)
rp * d("parappa:[13:19]", p=8, room=0.8, orbit=3, 
        #accelerate="-0.5",
        )

pp * d("[.]!4 parappa:[0~66]", p=0.25, leg=0.125/2, pan="rand", room=0.8, orbit=2)

Pp * d("parappa:[12:15] .!4", p=0.25, leg=0.125/2, pan="0.5", accelerate=0.01)

silence(tt,hh)

tt * d("lsdelectro:15", p=1, leg=0.25,
        shape=0.25, lpf=500, orbit=2)
hh * d("lsdelectro:4", p="[0.5!12 0.25!8]*.5", leg=0.125/1.7)

silence(tt, hh, pp, Pp)

silence(ss,Ps)

silence()
"
   _____                                 __   
  /     \   ____   _____   ____   ____ _/  |_ 
 /  \ /  \ / __ \ /     \_/ __ \ /    \\   __\
/    \    \  \_\ )  | |  \  ___/_   |  \|  |  
\____/\_  /\____/|__|_|  /\___  /___|  /|__|  
        \/             \/     \/     \/       
      _  _                                   
     ( )( )                                  
    _| ||/    _    _ __    __   _   _    __  
  / _  |    / _ \ (  __) / _  \( ) ( ) / __ \
 ( (_| |   ( (_) )| |   ( (_) || (_) |(  ___/
  ) _ _)    \ __/ (()    \__  | \___/  )\___)
 (__)       /(    (_)   ( )_) |       (__)   
           (__)          \___/               

"
clock.tempo=137

silence()

P('(set a 0)')

midi.nudge = 0.75

silence(pi)

pi >> zn("w 0704:4 595^0:4 7E7^2:2 595^0:2", scale="chromatic", key="C", dur=4,channel=1)
bb >> zd("leCASIOvib:[0~10]", 
        "(0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2",
        key="C", scale="chromatic", 
        pan=1,
        #speed=0.5,
        speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        #leg=0.8, octersub=1, 
        #leg=0.1,
        triode = 4.6, shape=0.25, orbit=0,
        delay = 0.5, delaytime = "0.5!3 1", delayfeedback = "(ulsaw 4)*0.80", gain=0.97
        )
bo >> zd("leCASIOvib:[0~10]", 
        "(0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2", #< >
        key="C", scale="chromatic", 
        #speed=0.25, 
        pan=0,
        speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        #leg=0.8, octersub=1, 
        #leg=0.1,
        triode = 4.6, shape=0.25, orbit=1,
        delay = 0.5, delaytime = "0.5!3 1", delayfeedback = "(ulsaw 4)*0.80", gain=0.97
        )
#????????????

panic()

Pb >> d("gretsch:[0 2 1 5 12 4 1 2 6 4 5 12 11]",
        #hpf="1000*(ulsaw 4)",
        p="0.5!2 1!7", shape=0.73, triode=2.8,
        orbit = 2, #real=0.95, imag=0.05
        )


clock.tempo = 187 #187.5 #rajoute un t au accord au dessus !

######?????????????

ll *  d("long:[10~20]", lpf="1500!10 3500!2", gain=0.9,leg=0.2, p=2)

Bo >> zd("leCASIOvib:[0~10]", 
        "e ^ (0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2", #< >
        key="C", scale="chromatic", 
        speed=0.25, 
        pan=0,
        #speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        leg=0.24,# octersub=1, 
        triode = 4.6, shape=0.25, orbit=1,
        #delay = 0.8, delaytime = "0.5!3 1", delayfeedback = "(ulsaw 4)*0.80", gain=0.97
        )

Bb >> zd("leCASIOvib:[0~10]", 
        "e ^ (0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2",
        key="C", scale="chromatic", 
        speed=0.5,
        pan=1,
        #speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        leg=0.24,# octersub=1, 
        triode = 4.6, shape=0.25, orbit=0,
        #delay = 0.8, delaytime = "0.5!3 1", delayfeedback = "(ulsaw 4)*0.80", gain=0.97
        )

BB >> zd("leCASIOvib:[0~10]", 
        "e (0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2",
        key="C", scale="chromatic", 
        pan=0.5,
        speed="{1 0.995 1.005}",
        #speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        leg=0.24,# octersub=1, 
        triode = 4.6, shape=0.25, orbit=0,
        #delay = 0.8, delaytime = "0.5!3 1", delayfeedback= "(ulsaw 4)*0.80", gain=0.97
        )



Pb >> d("gretsch:[0 2 1 5 12 4 1 2 6 4 5 12 11]",
        #hpf="10*($%10)*10",
        p="0.5!2 1!7", shape=0.83, octersub=2,triode=2.8,
        orbit = 2, #real=0.95, imag=0.05
        )
Ph * d("leHIHAT:[8 9 10]", p=0.25, leg=0.6)

silence(bb,bo,Bb,Bo)

Kk * d("(eu protokick 5 9)",  shape=0.8)

silence()

"
  ___                     _|_           
 |    __  __    _  \_/     |   __   \/ .
 |___ |  |__|_  /_  |      |_ |__|_ /\ |

"
D("crazytaxi", p=2,
        shape=0.45,
        # room=0.8
        )

Po * d("crazytaxi:[2~30]", p=8, leg=8, shape=0.15)

Pd * d('crazytaxi:[2:30]', amp=0.4, p=.25, leg=.05, pan='rand', 
       #speed='(if (beat 0 2) 1 0.5)*2', 
       hpf='2000+(ulsin 4)', orbit=5)
Pe * d('[.]!8 crazytaxi:[2:30]', p='.125', leg=.1, amp='0.3~0.5 * (ulsin 0.5)', 
       pan='(ultri 4)', #speed='2!4 4!4'
       )

Pa * d('(set kickpattern lsdelectro)',octersub=1,)

Pb * d('(get kickpattern)', speed=2)

silence()

D("crazytaxi", p=2,
        shape=0.45,
        room=0.8
        )

Pa * d('(set kickpattern [lsdelectro lsdelectro:[1 2 3]!2])', 
        p='0.5 0.25!2', octersub=4,
        )
Pb * d('(get kickpattern)',
        octersub=4, speed=2, p='0.25')

Pd * d('lsdlovely:[2:30]', amp=0.4, p=.25, leg=.05, pan='rand', 
       speed='(if (beat 0 2) 1 0.5)*2', 
       hpf='2000+(ulsin 4)', orbit=5)

Pe * d('[.]!8 lsdlovely:[2:30]', p='.125', leg=.1, amp='0.3~0.5 * (ulsin 0.5)', 
       pan='(ultri 4)', speed='2!4 4!4'
       )

silence()
"                    
       __ __    __       __      
      |  \  \  |  \     |  \     
       \▓▓ ▓▓  | ▓▓      \▓▓     
      |  \ ▓▓  | ▓▓     |  \     
      | ▓▓ ▓▓__/ ▓▓     | ▓▓     
      | ▓▓\▓▓    ▓▓     | ▓▓     
 __   | ▓▓ \▓▓▓▓▓▓ __   | ▓▓     
|  \__/ ▓▓        |  \__/ ▓▓     
 \▓▓    ▓▓         \▓▓    ▓▓     
  \▓▓▓▓▓▓           \▓▓▓▓▓▓      

"
silence()

@swim
def starter(p=0.5,i=1):
    D("long:0", leg=0.2, pan="rand", room="[0.1~0.5]", sz ="[0.2~0.8]")
    #D("(if(every 2) long:0 long:2)", pan="rand", leg=0.2, speed = "(if(every 2) 1 1.6)",i=i)
    again(starter, p=0.25, i=i+1)


Pk >> d("juj",
        shape=0.45,
        #octersub = 0.8
        room="[0.1~0.5]", sz ="[0.2~0.8]", orbit=2,
        )

Pi >> d(". juj:2",
        shape=0.45,
        p=4/3,
        #octersub = 0.8,
        orbit=2,
        )

Pl >> d("[.!8] juj:9!6",
        shape=0.45,
        p = "2!8 0.125!6",
        pan="rand", leg=0.2,
        #octersub = 0.8,
        orbit=2,
        )

Pn >> d("juj:[45]!6 .!8 ",
        shape=0.45,
        euclid=(2,3,2),
        p = "2!8 0.125!6",
        pan="rand", leg=0.2,
        #octersub = 0.8 
        orbit=2,
        )

Po >> d("juj:[92]!6 .!8 ",
        shape=0.45,
        euclid=(5,7,1),
        p = "0.5!6",
        pan="rand", leg=0.2,
        #octersub = 0.8, speed=0.75,
        orbit=2,
        )

PK * d("(eu sid:2 3 5)")
@swim
def starter(p=0.5,i=1):
    #D("long:0", leg=0.2, pan="rand", room="[0.1~0.5]", sz ="[0.2~0.8]")
    D("(if(every 2) long:0 long:2)", pan="rand", leg=0.2, speed = "(if(every 2) 1 1.6)",i=i)
    again(starter, p=0.25, i=i+1)


Pd * d('juj:[0~135]', amp=0.4, p=.5/4, leg=.1, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('[.!8] juj:[0~135]', p=.25/4, leg=.3, pan='rand', on=2, speed="(lsaw 4)")
PD * d('juj:[0~135]', amp=0.4, p=.5/4, leg=.1, pan='rand', speed='(if (beat 1 3) 1 0.5)')
PE * d('[.!8] juj:[0~135]', p=.25/4, leg=.3, pan='rand', on=1, 
        speed="(lsaw 4)",lpf="2502*(lsin 8)")

Pb >> d("jungbass",
        note="0 5 3 0",
        #note="0 5 3 079E",
        #p=0.5, gain=1,
        euclid = (5,5,3), #5
        shape=0.7,
        )

Pk >> d("juj",
        shape=0.45,
        #octersub = 0.8, 
        p=2/3,
        room="[0.5~0.9]", sz ="[0.2~0.8]", orbit=2,
        )

#SPEAKING


silence(Pd,Pe,PD,PE,PK,Pl, Pn, Po, starter, Pb)
SK * d("juj:[1~154]", p="rand*1.1", euclid=(5,7,1),
        shape=0.4, speed="{1 0.998 1.005}", pan="{0 1}",
        )

Pk >> d("juj",
        shape=0.45,
        #octersub = 0.8, 
        p="1/3 2/3 4/5 1/3 4/3 4/3 4/3",
        room="[0.1~0.5]", sz ="[0.2~0.8]", orbit=2,
        )

Pl >> d(". juj:9!6",
        shape=0.45,
        p = "1 0.125!6",
        pan="rand", leg=0.2,
        #octersub = 0.8,
        orbit=2,
        )

silence(Pk, Pi, Pl, Pn, Po, starter, Pb)

silence(Pd,Pe,PD,PE,PK)

"
___________________________________________________
_|_____|________|___|________|___|_____|___|___|___
____|____|___|__________|_____|_____|____|___|___|_
__/     \_____|_______|______|____/     \__|__||__|
_/  \ /  \__/ __ \__/    \__|____/  \ /  \_|  ||  |
/    \    \(  \_\ )|   |  \___|_/    \    \|  ||  |
\____/\_  /_\____/_|___|  /|____\____/\_  /|__||__|
___|____\/___|__________\/____|____|____\/__|___|__
__|__|_________|______|_____|_____|__|_______|___|_

"
#wii

pw * d("wiimusic:[0 1 2 3 4 5 6]", pan="0 1")

pW * d("wiimusic:[7 8 9 10 11 12]", p=0.5, 
        leg=0.2)

WW * d("wiimusic:[13 14 15 16 17 18]", p=0.25, 
        leg=0.125,  pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]")

Wi * zd("wiichannel", "q _ 0 5 7 [5 ^037]", 
        scale="chromatic", key="C", 
        orbit=3,room=0.25, sz=0.15)

WI * zd("wiichannel", "e 0 5 7 5", 
        scale="chromatic", key="C", 
        orbit=3)

silence(pw,pW,WW)

D("wiivoices:[0~39]")

pw * d("wiimusic:[0 1 2 3 4 5 6]", pan="0 1")
WW * d("wiimusic:[13 14 15 16 17 18]", p=0.25, 
        leg=0.125,  pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]")
Pk * d("sid:2", speed=0.5, shape=0.5, gain=0.9)


WI * zd("wiichannel", "(e 0 5 h 7 5)+(<0 7 5>)", 
        scale="chromatic", key="C", 
        orbit=3
        )

##VocoderMii-raconter une histoire sur mon midi

vv * zn("i v iv v", 
        scale="chromatic", key="C", channel=0, dur=2)

silence()

"
 ▄▄▄·  ▄▄·  ▄▄·       ▄▄▄  ·▄▄▄▄    
▐█ ▀█ ▐█ ▌▪▐█ ▌▪ ▄█▀▄ ▀▄ █·██· ██   
▄█▀▀█ ██ ▄▄██ ▄▄▐█▌.▐▌▐▀▀▄ ▐█▪ ▐█▌  
▐█▪ ▐▌▐███▌▐███▌▐█▌.▐▌▐█•█▌██. ██   
 ▀  ▀ ·▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•   

"

D("nevers:3")

silence()

Pv * d("accord:1",leg=16)

vv * d("accord:1", speed="{2 4}", p=16, coarse="(ulsin 8)*4", lpf=1500, leg=16)

PV * d("accord:[3:8]",leg=0.25,#p=0.25, 
        #gain="(ulsin 4)*0.8",
        pan="1 0.5 0.75 0 1 0.75 0.5 0.25 0 1", 
        begin="rand", euclid=(4,7),# shape=0.35, 
        #coarse=8,
        #speed="[1 0.5]+0.5*(g mov)", p=0.25, hpf="150+(g mov)*1000",
        #res=0.2, hpq=0.2,
        delay=0.75, delaytime="(g mov)/2", delayfeedback=0.65,orbit=4,
        )

Pl * d("[.]!8 accord:3!16", p=0.125, begin="[0.5:0.8]",pan="rand",
        gain="(ulsin 8)*0.8",
        leg=0.125,euclid=(3,7,2), coarse="16|4|8",
        )

PL * None

vv * None

PL * d("[.]!8 accord:3!16",speed=2, p=0.125, begin="[0.5:0.8]",pan="rand",
        leg=0.125,euclid=(3,7,5), coarse="16|4|8", gain=0.85
        )

Pj * d("juj:[0:45]", p=4, euclid=(3,7,2), shape=0.35,
        orbit=7, room=0.85, sz=0.85, gain=0.8, scram ="0.5 0 (ulsin 2) 2",
        delay=0.9,delaytime="0.01+(ulsin 4)/2", delayfeedback=0.67
        )

silence(Pj)

PA * zd("arp:[0:5]", "^ ^ t (7 5 3)+<0 7 5>",
        euclid=(6,8,2), scale="chromatic",
        key="F2",#F3 #F2
        lpf="1500*(ulsin 2)",res=0.4,
        gain=0.8,
        pan="0 0.5 1 0.5 0.75",
        )

Pa * zd("arp:[0:5]", "^ ^ t (7 5 3)+<0 7 5>",
        key="F6",
        euclid=(6,8,3), scale="chromatic", 
        lpf="1500*(ulsin 2)",res=0.4,
        gain=0.85, pan="0.5 0.75 0.25 0.15 0.5 075 0 1",
        )

solo(PA)

PA * None

silence()



'
 █▄█ ▄▀▄ █▄ ▄█ █▄ ▄█ ▄▀▄ ▄▀  ██▀   ▄▀▄
 █ █ ▀▄▀ █ ▀ █ █ ▀ █ █▀█ ▀▄█ █▄▄   █▀█

 █▄ ▄█ ▄▀▄   █▄ ▄█ ▄▀▄ █▄ █ ▀█▀ ▄▀▄ ▄▀  █▄ █ ██▀
 █ ▀ █ █▀█   █ ▀ █ ▀▄▀ █ ▀█  █  █▀█ ▀▄█ █ ▀█ █▄▄

 █▀▄ █▀▄ ██▀ █▀ ██▀ █▀▄ ██▀ ██▀
 █▀  █▀▄ █▄▄ █▀ █▄▄ █▀▄ █▄▄ █▄▄
'

ferrat = "| h 0 e r _ 0 q 4  | h _ 5 r | \
| h 0 e r _ 0 2 4  | h _ 5 e r _ 5 q ^ 5 | \
| h 1 e r _ 1 3 5  | h 1 r | \
| h 1 e r _ 1 4 6  | h 0 e r _ 0 q 4  | h 0 r | \
| h 0 r  | h _ 5 e r 0 2 5 | \
| h _4_6 e r __ 2 q ^ 6  | h 0 e r _ 0 3 5 | \
| h _ 6 e r _ 4 q ^6^^1  | h 1 e r __ 4 q ^ 6  | h _ 4 e r 0 q ^ 0 | \
| h 0 r  |"
ferrat2 = "| h _0_2_4 q r _0_2  | h _0_2 r | \
| h _0_2_4 r  | h __5_0_2 q r _0_2 | \
| h _1_3_5 r  | h _1_4_6 r | \
| h _1_4_6 r  | h _0_2_4 q r _0_2  | h _0_2_4 r | \
| h __5_0_2_5 r  | h _0_2 r | \
| h __2__6_2 q r __6_2_4  | h _0_3_5 r | \
| h __4_1_4 q r __4_1_4  | h _1_4_6 q r _1_4  | h _0_2 q r _0_2_4 | \
| h _0_2_4 r  |"
ferrat3 ="| q. ___ 0 e 0 q. 0 e 0  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 0 e 0 q. 0 e 0  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 1 e 1 q. 1 e 1  | q. ___ 4 e 4 q. 4 e 4 | \
| q. ___ 4 e 4 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 5 e 5 q. 5 e 5  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 2 e 2 q. 2 e 2  | q. ___ 3 e 3 q. 3 e 3 | \
| q. ___ 4 e 4 q. 4 e 4  | q. ___ 4 e 4 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 0 e 0 q. 0 e 0  |"
ferrat4 = "| e r _ 4 4 4 4 4 s r 4 t r s. 4  | q r  e _ 5 t r 5 s r 5 r e 5 5 ^ 0 _ 5 | \
| e. _ 4  s 4 t r  t 4 t r s 4 q 4 e r 4 4  | h _ 5 5 | \
| e r  e _ 3 s r 3 t r s. 3 e 3 3 3 s r e. 3  | q r  e _ 4 t r  t 4 t r e 4 4 4 4 4 | \
| q _ 6 e r s r 4 h r  | w _ 2  | e r 0 0 0 0  e 0 s 1 e 1 | \
| q 2 r h r  | q 0  e 0 s r 0 t r s. 0 s 0 t r s. 0 e _ 6 ^ 0 | \
| h _ 6 6  | e r _ 5 r s 5 5 e r 5 5 | \
| q _ 6 6 6 e 6 6 6 6  | e 1  e 1 s r e 1 1 1 1 1 2  | h 1  | "
ferrat5 = "| h 0 r  | h _ 6 e r 1 4 6  | h 2 e r __ 2 q ^^ 2 | \
| h 2 e r _ 2 4 6  | e _1_3_51 __ 1 ^ 1 ^ 1 q _ 6 e 1 4  | e _ 4 0 0 2 q ^ 0 e _ 2 4 | \
| h _ 5 e r _ 3 q ^0^3^5  | h __6_2_4_6 r | \
| q _3_5 e r _1_3_51 q _4_6 e _ 1 4  | h _ 4 e r r r r  |"
ferrat6 = "| h _0_3_5 r  | h _1_4 r  | h _2_4_6 q r _2_4_6 | \
| h _2_4_6 r  | q __ 1 e r ^1^3^5 q ^1^4 r  | q _0_2 r _2_4_#5 r | \
| h _0_3 q r __ 3  | h __ 2 r | \
| e _ 1 _ 1 ^ 1 _ 1 q ^ 1 r  | h _0_2 r  |"
ferrat7 = "| q. ___ 3 e 3 q. 3 e 3  | q. ___ 3 e 3 q. 3 e 3  | q. ___ 2 e 2 q. 2 e 2 | \
| q. ___ 2 e 2 q. 2 e 2  | q. ___ 1 e 1 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 3 e 3 q. 3 e 3  | q. ___ 2 e 2 q. 2 e 2 | \
| q. ___ 1 e 1 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0  |"
ferrat8 ="|   | w. _ 5 e ^ 0 1 1 _ 6  | h. _ 4 q r | \
| w r  | q. _ 3 e ^ 0 _ 6 5 6 4  |  | \
| w _ 2 e 5 3 4 5 6 ^ 0 1  | h 2  | \
| h _ 6  e 5 t r  t 5 t r s r e 6 6 5 4  | w 0 q r e r|" 






clock.tempo=120

panic()

Pa>> None
Pb >> None
Pc >> None
Pd >> None
def lead():
    Pa >> zd("braids",ferrat , pan = 0.5, channel = 0, dur=0.3)
    Pb >> zd("braids",ferrat2, pan = 0.25, channel = 0, dur=0.5)
    Pc >> zd("braids",ferrat3, model = 1, channel = 0, dur=0.25)
    Pd >> zd("braids",ferrat4, dur=1,orbit=1)
    Pn >> zn(ferrat4,dur=2, channel=0)
lead()

clock.tempo = 160 #160

Ils quittent un à un le pays
Pour s’en aller gagner leur vie
Loin de la terre où ils sont nés
Depuis longtemps ils en rêvaient
De la ville et de ses secrets
Du formica et du ciné
Les vieux ça n’était pas original
Quand ils s’essuyaient machinal
D’un revers de manche les lèvres
Mais ils savaient tous à propos
Tuer la caille ou le perdreau
Et manger la tomme de chèvre

Ps >> None

Pk >> d("leKICK:5", shape = 0.25,   lpf = 500)

PD * d('february:[0:10]', amp=0.4, p=0.5, leg=.05, pan='rand', 
       speed='(if (beat 0 2) 1 0.5)*2', hpf='2000+(ulsin 4)', 
       orbit=5,shape=0.25)
Pe * d('[.]!8 october:[0:10]', p='.25', leg=.1, amp='0.3~0.5 * (ulsin 0.5)', 
       pan='(ultri 4)', speed='2!4 4!4',shape=0.25)

Pk >> d("leKICK:5!15 protokick",  lpf = 1500)

Pk >> d("protokick", shape = 0.45, triode=0.8, lpf = 500, gain=1.1)


Pa >> None #POURTANT QUE LA MONTAGNE
Pb >> None #EST BELLE COMMENT PEUT ON
Pc >> None #SIMAGINER EN VOYANT UN 
Pd >> None #VOL DHIRONDELLE QUE LOTOMNE VIENT DARRIV2R !!!!!!
def lead():
    Pa >> zd("braids",ferrat5, pan = 0.5, channel=0)
    Pb >> zd("braids",ferrat6, pan = 0.25, channel=0)
    Pc >> zd("braids",ferrat7,  model = 1, channel=0)
    Pd >> zd("braids",ferrat8, #accelerate=0.05, scram=0.2,
            )
    Pn >> zn(ferrat8,dur=2, channel=0)
lead()

Pk >> None
Ps >> None

PS >> None

clock.tempo=670



clock.tempo=clock.tempo*2


clock.tempo=clock.tempo*0.5

panic()












ll * d("(lsdcartoon:[[0:6]])|(lsdethnova:[[0:6]])", p=0.5, leg=1)

lL * zd("lsdlovely:30", "w (074^0):4", scale="chromatic")

lL * zd("lsdlovely:30",
        "(h (074^0):4 (595^0):4 (7E7^2):2 (595^0):2)+(<0 0>)", 
        scale="chromatic", key = "D",
        )

#casio#+circuit_bent_bontempi

Pa * d('(set kickpattern kick)')

Pb * d('(get kickpattern)', speed=2)

Pc * n('(clamp 48|60 + (scl (set a (clamp (drunk (get a) ::span 4) 0 120))) 0 120)', p=.25)

Pa * n('(scl (set a (drunk (get a)))) + 48', p=.25)

Pa * d('(set a [kick hat!2 snare hat])', p='(set dur1 [0.5 1!2])')

Pb * d('(get a)', p='(get dur1)*[.5!4]', speed='2 4 1.5',
       room=0.9, orbit=2, dry=0.75, leg='.25 .5')


Pa * d('(set kickpattern [kick hat!2])', p='0.5 0.25!2')

Pb * d('(get kickpattern)', speed=2, p='0.25')


Pa * d('(set kickpattern [kick:7 hat!2 kick:7 hat!2 february!8 may!2])',
        p='(set pptrn [0.5 0.25!2])')

Pb * d('(get kickpattern)', speed='(disco [2 8 5] ::depth [4 2])',
       p='(get pptrn)*[2!16 0.5!4]', leg=.1, crush='[2:12,2]', 
       shape ='(get pptrn)', amp=0.3, room=0.9, pan='(get pptrn)',
       wet=1, size=0.24, orbit=4)




(    (     ( ( ( ( ([MEROU COMMUN]) ) ) ) ) ) )    )


d6 * s("FXliquid*6"
        #).striate(8
                ).n(irand(4)).pan(1).gain(1.2).crush(16).leslie(0.8)

#d7
d6 * s('FXliquid!12'
        #).striate(8
                ).n(irand(12)).pan(0).crush(16).leslie(0.8).gain(1.2)

d4 * s("[leHIHAT:2(4,5)]*2")

d5 * s("[~ laSNARE:4]*2"
        ).crush(4).room(0.2
                ) 

d2 * s("[leKICK(3,5)]*2").n(" 1 2 3 ").room(0.5) 

Pn * zn("i iv i v",channel=1,dur= 0.25,p=0.25, scale="chromatic",key="C")

Pn * zn("v iii iv",channel=1,dur= 0.25,p=0.25, scale="chromatic",key="C")

clock.tempo=clock.tempo*2

clock.tempo=clock.tempo*0.5

Le mérou commun émerge des abîmes putrides, se débattant dans un déluge chaotique de fluides visqueux. Ses écailles décrépites, éraflées par les échos macabres des batailles perdues, projettent une aura nauséabonde. Il est l'essence même de la noirceur et de la décadence, une créature maudite née des profondeurs putrides de l'enfer marin.

Son corps massif, déformé par les marées de la dépravation, porte les marques infâmes de son parcours de déchéance. Des ulcères purulents suintent, offrant un spectacle répugnant à l'œil averti. Il incarne l'isolement absolu, un gardien des secrets obscurs qui hantent les abysses insondables.

Les yeux du mérou commun, éteints et injectés de sang, reflètent les tourments d'une âme damnée. Ils sont des portails menant à un royaume malsain, où la nature et la souffrance se mêlent dans une danse macabre. Un regard qui scrute l'univers avec une conscience tordue, capturant la désolation des amours avortés et les échos lointains des souffrances endurées.

Ce mérou, une aberration marine, dérive parmi les courants impies de l'existence, se contorsionnant entre les lambeaux de lumière et les ténèbres putrides. Son être transcende les limites de la dépravation, fusionnant avec l'essence de l'abomination. Il est l'incarnation vivante de la dualité de l'existence, une créature à la fois immonde et vulnérable.

Lorsque le mérou commun s'agite dans les eaux viciées, il déclenche une cacophonie infernale de convulsions grotesques et de spasmes abjects. Chaque nageoire est un appendice tordu, semblable à une griffe acérée qui déchire les chairs des infortunés qui s'approchent trop près. Dans son sillage, des viscères flottent, offrant un festin macabre à la horde de parasites avide de chair en décomposition.

silence(Pn)
hush(d6,d4,d7,d5,d2)

Pk * n("rand*127",p=0.125,channel=9)

Pk * None

hush()

silence()

@swim
def starter(p=0.5,i=1):
    D("long:0", leg=0.2, pan="rand", room="[0.1~0.5]", sz ="[0.2~0.8]")
    #D("(if(every 2) long:0 long:2)", pan="rand", leg=0.2, speed = "(if(every 2) 1 1.6)",i=i)
    again(starter, p=0.25, i=i+1)


Pk >> d("juj",
        shape=0.45,
        #octersub = 0.8
        room="[0.1~0.5]", sz ="[0.2~0.8]", orbit=2,
        )

Pi >> d(". juj:2",
        shape=0.45,
        p=4/3,
        #octersub = 0.8,
        orbit=2,
        )

Pl >> d("[.!8] juj:9!6",
        shape=0.45,
        p = "2!8 0.125!6",
        pan="rand", leg=0.2,
        #octersub = 0.8,
        orbit=2,
        )

Pn >> d("juj:[45]!6 .!8 ",
        shape=0.45,
        euclid=(2,3,2),
        p = "2!8 0.125!6",
        pan="rand", leg=0.2,
        #octersub = 0.8 
        orbit=2,
        )

Po >> d("juj:[92]!6 .!8 ",
        shape=0.45,
        euclid=(5,7,1),
        p = "0.5!6",
        pan="rand", leg=0.2,
        #octersub = 0.8, speed=0.75,
        orbit=2,
        )

PK * d("(eu sid:2 3 5)")
@swim
def starter(p=0.5,i=1):
    #D("long:0", leg=0.2, pan="rand", room="[0.1~0.5]", sz ="[0.2~0.8]")
    D("(if(every 2) long:0 long:2)", pan="rand", leg=0.2, speed = "(if(every 2) 1 1.6)",i=i)
    again(starter, p=0.25, i=i+1)


Pd * d('juj:[0~135]', amp=0.4, p=.5/4, leg=.1, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('[.!8] juj:[0~135]', p=.25/4, leg=.3, pan='rand', on=2, speed="(lsaw 4)")
PD * d('juj:[0~135]', amp=0.4, p=.5/4, leg=.1, pan='rand', speed='(if (beat 1 3) 1 0.5)')
PE * d('[.!8] juj:[0~135]', p=.25/4, leg=.3, pan='rand', on=1, 
        speed="(lsaw 4)",lpf="2502*(lsin 8)")

Pb >> d("jungbass",
        note="0 5 3 0",
        #note="0 5 3 079E",
        #p=0.5, gain=1,
        euclid = (5,5,3), #5
        shape=0.7,
        )

Pk >> d("juj",
        shape=0.45,
        #octersub = 0.8, 
        p=2/3,
        room="[0.5~0.9]", sz ="[0.2~0.8]", orbit=2,
        )

#SPEAKING


silence(Pd,Pe,PD,PE,PK,Pl, Pn, Po, starter, Pb)
SK * d("juj:[1~154]", p="rand*1.1", euclid=(5,7,1),
        shape=0.4, speed="{1 0.998 1.005}", pan="{0 1}",
        )

Pk >> d("juj",
        shape=0.45,
        #octersub = 0.8, 
        p="1/3 2/3 4/5 1/3 4/3 4/3 4/3",
        room="[0.1~0.5]", sz ="[0.2~0.8]", orbit=2,
        )

Pl >> d(". juj:9!6",
        shape=0.45,
        p = "1 0.125!6",
        pan="rand", leg=0.2,
        #octersub = 0.8,
        orbit=2,
        )

silence(Pk, Pi, Pl, Pn, Po, starter, Pb)

silence(Pd,Pe,PD,PE,PK)


'
 ▄▀▀ ██▀ █ █ █     ▄▀▄   █▄ █ ▄▀▄ ██▀ █  
 ▄██ █▄▄ ▀▄█ █▄▄   █▀█   █ ▀█ ▀▄▀ █▄▄ █▄▄
'

FREE JAZZ PART


silence()

from random import choice

@swim 
def ziffattack(p=0.5, i=0):
    ZN("1.5 _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ \
            [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]] _ _ \
            ([024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ \
            [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]]) _ _ \
            [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ \
            [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]] _ \
            [024 _ [4 7]] _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ _ ]\
            [027 ^ ^ [7 5]] _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ \
            [(7 5 3)-2]] _ _ [024 _ [ 5 2 ] _ ] [027 ^ ^ [7 5]]",
            channel="rand*6",
    scale = choice(["rocritonic", "bocrian"]),
    key = choice(["Fs","C","A"]), dur=0.5,
    i=i)
    again(ziffattack, 
            p=choice([0.25,choice([0.5,0.25,0.125,0.125])])*4,
            i=i+12)

#0.125 0.125 0.125 puis reduire le 4 modifier le i+1

Pk >> d("(eu [gretsch:[0~7] gretsch:[9~25]] 3 7 )", 
        p="0.5!4 0.5|0.25!4", shape=0.4,
        )

D("ralt144mi .!7", accelerate = "1",
        gain = 1.4,enhance = .2, legato = 2)


silence()

clock.tempo=144

Pi >> None

Pi >> n(note = "[{F@maj}!2 {C@maj}!8]", p=0.5, # 0.25
        span= 2,
        chan = 0)


Pk >> d("[. leKICK:2]!4",
        shape =0.4,
        legato = 0.2,
        #cutoff = 1000,
        resonance = 0.2,
        #p=8 #8
        p = 4, span =1,
        )

Pc >> d(#"[. . laSNARE:4!2]!4",
        "[. . laSNARE:4!2]!3 [. . laSNARE:[16]!2]",
        p=1, accelerate= "0!12 0.5 0.75 0.80 1",
        span = 1,
        pan="rand")

###DOIT BIZAR
PI >> d("son:1",
        shape = 0.8, gain =0.8,
       #p="(0.125*rand)!2",
        span = 2,
        accelerate =1,
        legato=0.73,
        lpf=950)

Pl >> d("long:[40 41 40 40~44]", 
        speed="0.5!7 0.7", pan="rand", 
        leg=0.5, 
        shape=0.8, triode=2
        )

Pm >> d("long:42", 
        speed = "0.5!7 0.7",
        leg=0.35,
        euclid=(2,3,1),
        shape=0.8, triode=2
        )

PM >> d(". long:41", 
        speed = "0.5!7 0.7",
        leg=0.35,
        euclid=(4,7,4),
        shape=0.8, triode=2
        )

silence(Pi,PI)

clock.tempo=154

clock.tempo=164

Pk >> d("f!4",
        octer=1,
        octersub=2,        
        shape =0.6,
        legato = 0.2,
        #cutoff = "250+(ltri 8)*1000",
        resonance = 0.3,
        #p=8 #8
        p = "8 8 8 4!2 8 8 8 2!4", span =8,
        )

Pk * None

Pc >> d(#"[. . laSNARE:4!2]!4",
        "[. . laSNARE:4!2]!3 [. . laSNARE:[16]!2]",
        p="0.25 0.5", accelerate= "0!12 0.5 0.75 0.80 1",
        pan="rand"
        )

silence(Pk,Pi,Pl,Pm,PM)
Pl >> d("long:[40 41 40 40~44]", 
        speed = "0.5!7 0.7", pan="rand",
        leg=0.1, p=0.125,
        shape=0.8, triode=2
        )


Pk >> d("{f protokick}",
        octer=1, octersub=2,
        shape =0.5, legato = 0.2,
        #cutoff = "250+(lsaw 8)*500",
        resonance = 0.45, 
        #p=8 #8
        p = "8 8 8 4!2 8 8 8 2!4", span =8,
        )

PL >> d("long:[40 41 40 40~44]", 
        speed = "[0.5!7 0.7]*[2|4|8]", pan="rand",
        leg=0.1, p=0.125, euclid=(2,3,2),
        shape=0.8, triode=2, room=0.2, sz=0.2, orbit=5,gain=0.8
        )

Pk * None

solo(PL)

########################"

                                                             ▄    ██             
 ▄▄▄▄     ▄▄▄▄    ▄▄▄   ▄▄▄ ▄▄▄   ▄▄▄▄  ▄▄ ▄▄ ▄▄    ▄▄▄▄   ▄██▄  ▄▄▄    ▄▄▄▄     
▀▀ ▄██  ▄█   ▀▀ ▄█  ▀█▄  ██  ██  ██▄ ▀   ██ ██ ██  ▀▀ ▄██   ██    ██  ▄█   ▀▀    
▄█▀ ██  ██      ██   ██  ██  ██  ▄ ▀█▄▄  ██ ██ ██  ▄█▀ ██   ██    ██  ██         
▀█▄▄▀█▀  ▀█▄▄▄▀  ▀█▄▄█▀  ▀█▄▄▀█▄ █▀▄▄█▀ ▄██ ██ ██▄ ▀█▄▄▀█▀  ▀█▄▀ ▄██▄  ▀█▄▄▄▀    
                                                                                 
                                                                                 
█▀▀██▀▀█ ▀██▀▀▀▀█  ▀██▀  █▀  ▀█▄   ▀█▀  ▄▄█▀▀██      
   ██     ██  ▄     ██ ▄▀     █▀█   █  ▄█▀    ██     
   ██     ██▀▀█     ██▀█▄     █ ▀█▄ █  ██      ██    
   ██     ██        ██  ██    █   ███  ▀█▄     ██    
  ▄██▄   ▄██▄▄▄▄▄█ ▄██▄  ██▄ ▄█▄   ▀█   ▀▀█▄▄▄█▀     
                                                     
                                                     
clock.tempo=187

silence()

Pi * d("teratoma:[1~150]", leg=0.25, p=0.5, 
        begin="rand", pan="0 1/8 7/8 1")

PI * d("spore:[1~150]", leg=0.25, p=0.5, 
        begin="rand", pan="2/8~5/8")

Pd * d('teratoma:[0:150]', amp=0.4, p=.5, leg=.05, pan='rand', 
        speed='(if (beat 0 2) 1 0.5)'
        )

Pe * d('[.!8] spore:[0:50]', p=.25, leg=.1, 
        pan='rand', on=2, speed=2
        )

PD * d('crunchorganic:[0:150]', amp=0.4, p=.5, 
        leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)'
        )

PE * d('[.!8] proximity:[0:50]', p=.25, leg=.1, 
        pan='rand', on=2, speed=2
        )

Pk * d("kick:1 . laSNARE:[1~18] .", p=0.5, shape=0.45, room=0.15, 
        #pan="{0 2/8 4/8 6/8}", orbit=2
        )

ph * d("leHIHAT:[8]", leg=0.25, p=0.25, orbit=2, shape=0.2, 
        pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]"
        )

PP * d("[proximity:[0:50] spore:[0:150]]", p=0.125, speed="(lsin 2)", 
        lpf="150*(lsaw 4)", leg=0.2, res=0.2, 
        pan="[4/16]!16 [6/16]!16 [8/16]!16 [10/16]!16"
        )

Pk * d("(kick:1) (kick:0~8) (laSNARE:1~18)", 
        p=0.5, shape=0.35,room=0.26,
        #pan="{0 2/8 4/8 6/8}", orbit=2
        )

ph * d("leHIHAT:[9:12]", leg=0.15, p=0.25, 
        orbit=2, shape=0.2,
        pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]"
        )

#double loud kicks c64 vibe

Pk * d("{(kick:1) (sid:2)} {(kick:0~8) (sid:2)} laSNARE:[1~18] sid:2", 
        p=0.5, room=0.26,shape=0.65,
        #pan="{0 2/8 4/8 6/8}", orbit=2
        )

#acousmatic break ?

silence()
Pk * d("{(kick:1) (sid:2)} {(kick:0~8) (sid:2)} laSNARE:[1~18] sid:2", 
        room=0.6,p="(rand)*0.5", shape=0.45,lpf=1000)
Pd * d('teratoma:[0:150]', amp=0.4, p=.5/4, leg=.1, pan='rand', 
        speed='(if (beat 0 2) 1 0.5)')
Pe * d('[.!8] spore:[0:50]', p=.25/4, leg=.3, pan='rand', on=2, speed="(lsaw 8)")
PD * d('crunchorganic:[0:150]', amp=0.4, p=.5/4, leg=.1, pan='rand', 
        speed='(if (beat 1 3) 1 0.5)')
PE * d('[.!8] proximity:[0:50]', p=.25/4, leg=.3, pan='rand', on=1, 
        speed="(lsaw 8)",lpf="2502*(lsin 8)")

silence(Pk,Pd,Pe,PD)
Pk * d("protokick", lpf="250*(lsaw 4)",res="(lsin 1)*0.5",p=0.25,
        #pan="{0 2/8 4/8 6/8}"
        )

Pk * d("(eu protokick 3 5)", shape=0.9,lpf="250*(lsaw 4)",res="(lsin 1)*0.5",
        p=0.5,
        #pan="{0 2/8 4/8 6/8}", orbit=2
        )

Pd * d('teratoma:[0:150]', amp=0.4, p=.5, leg=.05, pan='rand', 
        speed='(if (beat 0 2) 1 0.5)')
Pe * d('[.!8] spore:[0:50]', p=.25, leg=.1, pan='rand', on=2, speed=2)
PD * d('crunchorganic:[0:150]', amp=0.4, p=.5, leg=.05, pan='rand', 
        speed='(if (beat 0 2) 1 0.5)')
PE * d('[.!8] proximity:[0:50]', p=.25, leg=.1, pan='rand', on=2, speed=2)
ph * d("leHIHAT:[9:12]", leg=0.25, p=0.25, orbit=2,
        pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]")
Pk * d("(eu protokick 3 5)", gain=0.93,shape=0.9,
        lpf="2500*(lsaw 4)",res="(lsin 1)*0.5",p=0.5,
        #pan="{0 2/8 4/8 6/8}", orbit=2
        )

#boom boom [o] [o]

solo(Pk)

Pk * d("(eu protokick [2~5] [6~9])", gain=0.93,
        shape=0.9,lpf="2500*(lsaw 4)",res="(lsin 1)*0.5",p=0.5,
        #pan="{0 2/8 4/8 6/8}"
        )

silence()

'''
  )\__.__   )\.---. (\   /(   )\  )\     .-./( 
 ) _  __ ( (   .-._( )) \  ) (  \/ /   .'     )
 \( |(  )/  \  '-.  (  \/ /   ) \ (   (   _  ( 
    ) \      ) .-`   )   (   ( ( \ \   ) (_)  )
    \ (     (  ``-. (  /\ \   ))  ) ) (      ( 
     )/      ).--.(  )/  )/  (_/  \_(  )/____/ 

                       _           _                                
                      (_ )  _     ( ) _                             
    __   _   _    ___  |(| (_)   _| |(_)   __    ___    ___     __  
  / __ \( ) ( ) / ___) |() | | / _  || | / __ \/  _  \/  _  \ / __ \
 (  ___/| (_) |( (___  | | | |( (_| || |(  ___/| ( ) || ( ) |(  ___/
  )\___) \___/ )\____)( (_)( ) ) _ _)( ) )\___)(() (_)(() (_) )\___)
 (__)         (__)    (_)  /( (__)   /( (__)   (_)    (_)    (__)   
                          (__)      (__)                            

'''

silence()
clock.tempo=144
from random import random
P('(s del 0)')
P('(s speeder 1)')

Pk * d("(eu {sid:2 protokick} 3 5)", shape=0.9,
        lpf="100+150*(s mov (lsaw 4))",res="(lsin 1)*0.5",
        p=0.5,orbit=1,
        #pan="{0 2/8 4/8 6/8}", orbit=2
        )

PK * d("(eu sid:9 1 3)",coarse=4, 
        p="3/6", speed="(if (beat 1) (0.5) [1 2])*(g speeder)", 
        #scram="(if (beat 2) 0.8 0)", binshift="(if (beat 2) 8 -0.5)",
        shape=0.9,room=0.9, sz="(g mov)", gain=0.8,orbit=1, 
            delay="(g del)",delayfb="(g del)*0.8", delaytime=0.5,
        )

Ph * d("(eu casio:2 13 15)", p=0.5, leg=0.1, orbit=1,
            delay="(g del)",delayfb="(g del)*0.5", delaytime=0.5,
            speed="1*(g speeder)",
        )

Ps * d("(eu laSNARE:[56] 6 15)", shape=0.6, leg=0.25, orbit=1,
            delay="(g del)",delayfb="(g del)*0.5", delaytime=0.5,
            speed="1*(g speeder)",
        )

ph * d("leHIHAT:[8]", leg=0.25, p=0.25, orbit=1, shape=0.2, 
        pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]",
            delay="(g del)",delayfb="(g del)*0.5", delaytime=0.5,
            speed="1*(g speeder)",
        )

silence(Pk)
P('(s del 0.9)')
@swim
def breaker(p=0.5,i=0):
    P('(s speeder (0.5+(0.25*(lsaw 6))))',i)
    again(breaker,p=1, i=i+1)

clock.tempo=165

silence()

silence(Ph,Ps,ph,PK,Pk)
@swim 
def lerythme(p=0.5,i=0):
    D("f . sid:2 .. sid:2", triode=0.3, euclid=(3,3,1), leg=.4,
            shape=0.65, div=2, i=i, hpf='40~50') # régler
    D('. . snare:10 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i, orbit=1, hpf=200, lpf=9000)
    D('(eu hat 14 16)', i=i, orbit=3)
    again(lerythme, p=.25, i=i+1) #p=0.5


Pg * d("long:[21]", n='{F2 F3} F2|F3', shape=.5, leg=0.133, pan="(ulsin 2)", amp='0.3~0.5', orbit=2, p=.25, euclid=(3,4,2), speed='{0.5 1}')

lerythme.stop()

Pk * d("jungbass:4", p="0.75 1 0.25!2 0.5"*8, release=0.20)

silence(Pd, Pe)

Pd * d('february:[0:10]', amp=0.4, p=.25, leg=.05, pan='rand', 
       speed='(if (beat 0 2) 1 0.5)*2', hpf='2000+(ulsin 4)', orbit=5)
Pe * d('[.]!8 october:[0:10]', p='.125', leg=.1, amp='0.3~0.5 * (ulsin 0.5)', 
       pan='(ultri 4)', speed='2!4 4!4')

silence(Pk)
@swim 
def lerythme(p=0.5,i=0):
    D("kick:4 . kick:5 .. kick:10", triode=0.3, euclid=(3,3,1), leg=.4,
            shape=0.65, div=2, i=i, hpf='40~50') # régler
    D('. . snare:10 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i, orbit=1,hpf=200, lpf=9000)#9000
    again(lerythme, p=.25, i=i+1) #p=0.5

Ph * d('(eu hat 14 16)', amp="0.25~0.45", p="0.25!15 0.125!4", orbit=3)

silence(Pe,Pd,Pk,lerythme,Ps,Ph)

silence()




@swim
def progger(p=0.5,i=0):
    randomer = random()
    period = 2
    #print("randomer :" +str(randomer))
    if (randomer>0.8):
        clock.tempo=clock.tempo*8/7
    if (randomer>0.6 and randomer<0.8):
        clock.tempo=clock.tempo*4/3
    if (randomer>0.3 and random()<0.6):
        clock.tempo=clock.tempo*6/5
    if (randomer<0.2):
        clock.tempo=clock.tempo*0.5
    if (clock.tempo > 300):
        period = 8
        clock.tempo=clock.tempo*0.5
    if (clock.tempo < 120):
        period = 0.5
        clock.tempo=clock.tempo*2
    if(clock.tempo>200 and clock.tempo<300):
        period = 4
    if(clock.tempo>120 and clock.tempo<200):
        period = 2
    print("clock :"+str(int(clock.tempo))) 
    again(progger, p=period, i=i+1)

silence()

clock.tempo=271.54

Pb >> d("kit8085:[0 2 1 5 12 4 1 2 6 4 5 12 11]",
        #hpf="1000*(ulsaw 4)",
        p="0.25!2 0.5!7", shape=0.73, triode=2.8,
        coarse=10, 
        pan=1,
        orbit = 2, #real=0.95, imag=0.05
        )

PB >> d("kit8086:[0 2 1 5 12 4 1 2 6 4 5 12 11]",
        hpf="1000*(ulsaw 4)",
        p="0.5!7 0.25!2", shape=0.73, triode=2.8,
        coarse=10,
        pan=0,
        orbit = 2, #real=0.95, imag=0.05
        )

PE * d('[.!8] proximity:[0:50]', p=.25, leg=.3, pan='rand', on=1, 
        speed="(lsaw 8)",lpf="2502*(lsin 8)")

Pk * d("f",p=2,
        shape=0.8, 
        lpf="2500*(lsaw 8)",res="(lsin 1)*0.5",
        )

Pg * d("clic:[0~152]",
        shape=0.8,pan="[[[0:8]!!2!!4]/8]|[[[8:0]!!2!!4]/8]", 
        lpf="1000*(lsaw 12)",res="(lsin 1)*0.5",p=0.25,
        )

solo(Pg)

panic()

clock.tempo

##DUB PART


Pb >> None

clock.tempo=144

@swim
def tempochange(p=0.5, i=0):
    if clock.tempo == 144 :
        clock.tempo = 137
    else :
        clock.tempo=144
    print(clock.tempo)
    again(tempochange, p=4,i=i+1)

clock.tempo=137

silence()

panic()


Pk * d("leKICK:[6] {leHIHAT:[12] leKICK:6} {laSNARE:[5] laSNARE:8} leHIHAT:[12]",
        leg=0.2, p=1,orbit="{0 1}", 
        shape=0.3, room=0.5, gain=0.9,
        delay = 1, delaytime = "0.25", delayfeedback = "0!16 0.5!2",
        )

PB * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(1,9,5), 
        speed="{1 0.5 0.8}", pan = 0,
        #real=0.9, imag=0.25
        )

OP * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(1,9,9), 
        speed="{1 0.5 0.8}", pan = 1, 
        #real=0.9, imag=0.25
        )

PJ >> d("morgan:[0~10]", pan="rand", p="0.25!16 0.125!8", leg=0.25, 
        gain=0.9, #speed=0.125,
        begin="rand", orbit=4, hpf=600,
        #real="(if (beat 4) 0.9 0)", imag="(if (beat 4) 0.5 0)"     
        )

ob * d(".morgan:[0~10]", pan="rand", p="0.25!16 0.125!8",leg=0.25, 
        gain=0.9, #speed= 0.1225,
        begin="rand", orbit=4, hpf=600,
        #real="(if (beat 4) 0.9 0)", imag="(if (beat 4) 0.5 0)"         
        )

ss * zd("jungbass:14"," r 5 r 7 q r r", speed= 1.5,
        octersub=3, orbit = 4, triode = 0.9, gain=1)

Pl * d("leCASIO:[0~9]", leg=0.9, p="0.5!2 0.125!2 0.25!2 0.5"*2, euclid=(4,9,5))

Ps * d("leCASIOvib",
        speed="0.25*(lsaw 6)", p=0.125, gain=0.8, lpf="(lsaw 8)*1000", res=0.2, orbit=3)

Pk * None
PJ * None
ob * None

Pk * d("leKICK:[2~8] {may:[12~45] leKICK:2} {may:[5] february:[8~16]} may:[12~32]",
        leg=0.2, p="0.5!4",orbit="{0 1}", 
        shape=0.3, room=0.5, gain=0.9,
        delay = 1, delaytime = "0.25", delayfeedback = "0!16 0.5!2",
        )

clock.tempo = 137/2

clock.tempo = 137/4

clock.tempo

clock.tempo=clock.tempo*2

clock.tempo=clock.tempo*0.5


silence(tempochange)










APRES CEST A MES RISQUE ET PERILS

clock.tempo=135

silence()

Ps * d(". laSNARE:[rand*25]", leg=0.5, gain=1.2)

PK * d("maloya", 
        #speed="{1 0.98 2}", 
        lpf="400*(ulsaw 4)", gain=0.9
        )

Pl >> d("(eu maloya:1 9 16)", p=0.25, gain=0.8)

Pj >> d("(eu {(maloya:2) (leKICK:2)} 13 16)", p=1,
        gain=1.2, octersub=2, speed=0.92)

PJ >> d("birds:[0~10]", pan="rand", p=3, 
        gain=0.9, #speed=0.125,
        begin="rand"
        )
Pb * d(".birds3:[0~10]", pan="rand", p=4, 
        gain=0.9, #speed= 0.1225,
        begin="rand"
        )

PB * d("bongobuchla:[0~32]", p=0.25, euclid=(2,3,5), 
        speed="{1 2 3}", pan = "rand",
        )

silence(Ps, PK, Pl, Pj)

Pk * d("leKICK:1", shape=0.2)

Ps * d("(eu {sid:0 sid:4} 2 3)", p=0.25, #leg = 0.10,
        speed="{1 0.98}/2",
        #speed="({1 0.98})/2!16 ({1 0.98})/1.5!15 ({2 2.98})",
        note="C0", octer = 0.8,
        )


PK * d("maloya", 
        speed="{1 0.98 2 4}", 
        lpf="20*($%40)"
        )
Pl >> d("(eu maloya:1 9 16)", p=0.25, gain=0.8)
Pj >> d("(eu {maloya:2 leKICK:2} 13 16)", p=0.5,
        gain=1.2, octersub=2)

clock.tempo = 127


'
 █▄█ ▄▀▄ █▄ ▄█ █▄ ▄█ ▄▀▄ ▄▀  ██▀   ▄▀▄
 █ █ ▀▄▀ █ ▀ █ █ ▀ █ █▀█ ▀▄█ █▄▄   █▀█

 █▄ ▄█ ▄▀▄   █▄ ▄█ ▄▀▄ █▄ █ ▀█▀ ▄▀▄ ▄▀  █▄ █ ██▀
 █ ▀ █ █▀█   █ ▀ █ ▀▄▀ █ ▀█  █  █▀█ ▀▄█ █ ▀█ █▄▄

 █▀▄ █▀▄ ██▀ █▀ ██▀ █▀▄ ██▀ ██▀
 █▀  █▀▄ █▄▄ █▀ █▄▄ █▀▄ █▄▄ █▄▄
'

ferrat = "| h 0 e r _ 0 q 4  | h _ 5 r | \
| h 0 e r _ 0 2 4  | h _ 5 e r _ 5 q ^ 5 | \
| h 1 e r _ 1 3 5  | h 1 r | \
| h 1 e r _ 1 4 6  | h 0 e r _ 0 q 4  | h 0 r | \
| h 0 r  | h _ 5 e r 0 2 5 | \
| h _4_6 e r __ 2 q ^ 6  | h 0 e r _ 0 3 5 | \
| h _ 6 e r _ 4 q ^6^^1  | h 1 e r __ 4 q ^ 6  | h _ 4 e r 0 q ^ 0 | \
| h 0 r  |"
ferrat2 = "| h _0_2_4 q r _0_2  | h _0_2 r | \
| h _0_2_4 r  | h __5_0_2 q r _0_2 | \
| h _1_3_5 r  | h _1_4_6 r | \
| h _1_4_6 r  | h _0_2_4 q r _0_2  | h _0_2_4 r | \
| h __5_0_2_5 r  | h _0_2 r | \
| h __2__6_2 q r __6_2_4  | h _0_3_5 r | \
| h __4_1_4 q r __4_1_4  | h _1_4_6 q r _1_4  | h _0_2 q r _0_2_4 | \
| h _0_2_4 r  |"
ferrat3 ="| q. ___ 0 e 0 q. 0 e 0  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 0 e 0 q. 0 e 0  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 1 e 1 q. 1 e 1  | q. ___ 4 e 4 q. 4 e 4 | \
| q. ___ 4 e 4 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 5 e 5 q. 5 e 5  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 2 e 2 q. 2 e 2  | q. ___ 3 e 3 q. 3 e 3 | \
| q. ___ 4 e 4 q. 4 e 4  | q. ___ 4 e 4 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 0 e 0 q. 0 e 0  |"
ferrat4 = "| e r _ 4 4 4 4 4 s r 4 t r s. 4  | q r  e _ 5 t r 5 s r 5 r e 5 5 ^ 0 _ 5 | \
| e. _ 4  s 4 t r  t 4 t r s 4 q 4 e r 4 4  | h _ 5 5 | \
| e r  e _ 3 s r 3 t r s. 3 e 3 3 3 s r e. 3  | q r  e _ 4 t r  t 4 t r e 4 4 4 4 4 | \
| q _ 6 e r s r 4 h r  | w _ 2  | e r 0 0 0 0  e 0 s 1 e 1 | \
| q 2 r h r  | q 0  e 0 s r 0 t r s. 0 s 0 t r s. 0 e _ 6 ^ 0 | \
| h _ 6 6  | e r _ 5 r s 5 5 e r 5 5 | \
| q _ 6 6 6 e 6 6 6 6  | e 1  e 1 s r e 1 1 1 1 1 2  | h 1  | "
ferrat5 = "| h 0 r  | h _ 6 e r 1 4 6  | h 2 e r __ 2 q ^^ 2 | \
| h 2 e r _ 2 4 6  | e _1_3_51 __ 1 ^ 1 ^ 1 q _ 6 e 1 4  | e _ 4 0 0 2 q ^ 0 e _ 2 4 | \
| h _ 5 e r _ 3 q ^0^3^5  | h __6_2_4_6 r | \
| q _3_5 e r _1_3_51 q _4_6 e _ 1 4  | h _ 4 e r r r r  |"
ferrat6 = "| h _0_3_5 r  | h _1_4 r  | h _2_4_6 q r _2_4_6 | \
| h _2_4_6 r  | q __ 1 e r ^1^3^5 q ^1^4 r  | q _0_2 r _2_4_#5 r | \
| h _0_3 q r __ 3  | h __ 2 r | \
| e _ 1 _ 1 ^ 1 _ 1 q ^ 1 r  | h _0_2 r  |"
ferrat7 = "| q. ___ 3 e 3 q. 3 e 3  | q. ___ 3 e 3 q. 3 e 3  | q. ___ 2 e 2 q. 2 e 2 | \
| q. ___ 2 e 2 q. 2 e 2  | q. ___ 1 e 1 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 3 e 3 q. 3 e 3  | q. ___ 2 e 2 q. 2 e 2 | \
| q. ___ 1 e 1 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0  |"
ferrat8 ="|   | w. _ 5 e ^ 0 1 1 _ 6  | h. _ 4 q r | \
| w r  | q. _ 3 e ^ 0 _ 6 5 6 4  |  | \
| w _ 2 e 5 3 4 5 6 ^ 0 1  | h 2  | \
| h _ 6  e 5 t r  t 5 t r s r e 6 6 5 4  | w 0 q. r |" 



Pourtant que la montagne est belle
Comment peut-on s’imaginer
En voyant un vol d’hirondelles
Que l’automne vient d’arriver?


clock.tempo=120

panic()

Pa>> None
Pb >> None
Pc >> None
Pd >> None
def lead():
    Pa >> zd("braids",ferrat , pan = 0.5, channel = 0, dur=0.3)
    Pb >> zd("braids",ferrat2, pan = 0.25, channel = 0, dur=0.5)
    Pc >> zd("braids",ferrat3, model = 1, channel = 0, dur=0.25)
    Pd >> zd("braids",ferrat4, dur=1,orbit=1)
lead()

clock.tempo = 160 #160

Ils quittent un à un le pays
Pour s’en aller gagner leur vie
Loin de la terre où ils sont nés
Depuis longtemps ils en rêvaient
De la ville et de ses secrets
Du formica et du ciné
Les vieux ça n’était pas original
Quand ils s’essuyaient machinal
D’un revers de manche les lèvres
Mais ils savaient tous à propos
Tuer la caille ou le perdreau
Et manger la tomme de chèvre

Ps >> None

Pk >> d("leKICK:5", shape = 0.25,   lpf = 500)

Pk >> d("leKICK:5!15 protokick",  lpf = 1500)

Pk >> d("protokick", shape = 0.25, triode=0.8, lpf = 500, gain=1.1)

Ps >> d("[amencutup:[1~12]!!2]!!4",p=0.5,
        phaserrate=0.8,phasdp=0.8,
        shape=0.55, leg=0.15)

Pa >> None #POURTANT QUE LA MONTAGNE
Pb >> None #EST BELLE COMMENT PEUT ON
Pc >> None #SIMAGINER EN VOYANT UN 
Pd >> None #VOL DHIRONDELLE QUE LOTOMNE VIENT DARRIV2R !!!!!!
def lead():
    Pa >> zd("braids",ferrat5, pan = 0.5, channel = 0, dur=0.3)
    Pb >> zd("braids",ferrat6, pan = 0.25, channel = 0, dur=0.5)
    Pc >> zd("braids",ferrat7,  model = 1, channel = 0, dur=0.55)
    Pd >> zd("braids",ferrat8, accelerate=0.05, scram=0.2,
            )
lead()

Pk >> None
Ps >> None

PS >> None

clock.tempo=670

clock.tempo=clock.tempo*2


clock.tempo=clock.tempo*0.5



silence()

clock.tempo=144

Ps * d("(eu {sid:0 sid:4} 2 3)", p=0.25, leg = 0.15,
        #speed="{1 0.98}/2",
        speed="({1 0.98})/2!16 ({1 0.98})/1.5!15 ({2 2.98})",
        note="C0", octer = 0.8, octersub=1,
        )

Pj >> d("(eu {leKICK:2} 16 16)", p=1,
        gain=1.2, octersub=2, speed=0.92)


Pk * d("leKICK:[6] {leHIHAT:[12] leKICK:6} {laSNARE:[5] laSNARE:8} leHIHAT:[12]",
        leg=0.2, p=0.5,orbit="{0 1}", 
        shape=0.3, room=0.5, gain=0.9, pan="{0 1}",
        #real=0.9, imag=0.25
        )

clock.tempo=170

Ps * None

silence(PJ,ob,Pl,ss,OP,PB,Pk,Pj)

SS * zd("{sid:0 sid:4}", " s ^ ^ ^ 5 3 0", triode=4,shape=0.45,
        lpf="150*(ulsaw 6)", res=0.27,orbit=1
        )

##ALLo ? 

pp * d("leHIHAT:6",p=0.25,leg=0.125,speed="0.25+(ulsin 5)*2(ulsaw 1)",gain=0.89)
Pj * d("leKICK:2", gain=1, octersub=2, speed=0.92,p=1)

silence(PJ,ob,Pl,ss,OP,PB,Pk,Pj)

Pj * d("leKICK:2", gain=1, octersub=2, speed=0.92,p=1)

silence(PJ,ob)

silence()

solo(pp)

silence()

Pi>>zn( "(((e 0 4 7)+(0 <0 0 0> 0)):2) \
         (((e 0 4 7)+(0 <0 3 0> 0)):2) \
         (((e 5 9 ^0)+(0 <0 7 0> 0)):2) \
         (((e 7 E ^2)+(0 <0 0 0> 0)):2) \
         (((e 5 9 ^0)+(0 <0 0 0> 0)):2)",
        scale='chromatic', channel="0~7",
        dur=0.75, gain=0.7,velocity=40,
        )

Pi>>zn( "(((s 0 4 7)+(0 <0 0 0> 0)):2) \
         (((t 0 4 7)+(0 <0 3 0> 0)):2) \
         (((s 5 9 ^0)+(0 <0 7 0> 0)):2) \
         (((t 7 E ^2)+(0 <0 0 0> 0)):2) \
         (((s 5 9 ^0)+(0 <0 0 0> 0)):2)",
        scale='chromatic', channel="0~8",
        dur=0.75, gain=0.7,velocity=40,
        )

PI>>zn( "(((s 0 4 7)+(0 <0 0 0> 0)):2) \
         (((e 0 4 7)+(0 <0 3 0> 0)):2) \
         (((s 5 9 ^0)+(0 <0 7 0> 0)):2) \
         (((e 7 E ^2)+(0 <0 0 0> 0)):2) \
         (((s 5 9 ^0)+(0 <0 0 0> 0)):2)",
        scale='chromatic', octave=1, channel=1,
        dur=0.75, gain=0.7,velocity=40,
        )

iI>>zn( "(((s _ 0 4 7)+(0 <0 0 0> 0)):2) \
         (((e _ 0 4 7)+(0 <0 3 0> 0)):2) \
         (((t _ 5 9 ^0)+(0 <0 7 0> 0)):2) \
         (((e _ 7 E ^2)+(0 <0 0 0> 0)):2) \
         (((e _ 5 9 ^0)+(0 <0 0 0> 0)):2)",
        scale='chromatic', octave=1, channel=1,
        dur=0.75, gain=0.7, velocity=40,
        )

Pk * n("36 42 38 [42~125]", p= 0.5, velocity = "70~100", channel=9)

silence(Pk, Pb, bb,bo)


##########SILVER APPLE

silence()

clock.tempo =125

P('(s note (0))')

P('(s note 5)')

P('(s note 10)')

P('(s note 7)')

silence()

@swim
def pattern(p=0.5,i=0):
    P('(s note [0|7|5|10])',i)
    P('(s del (ulsin 32))',i)
    again(pattern, p=2,i=i+1)

P('(s del 0.25)')

P('(s del (ulsin 4))')

P('(s del 0.25)')

P('(s del 0.25)')

Pi * d("gtr", note="(g note)+[5 7 5 0]+12", delay=0.8, 
        delaytime=0.25, delayfeedback=0.5,
        p="(set ryth [0.5!8 0.25!2])*(2/3)*2",
        gain="0.2+(ulsin 4)*0.4", pan="0 1", lpf=1500,res="(g del)",
        #coarse="8+(ulsaw 16)",
        )

Ii * d(". gtr", note="(g note)+[5 7 5 0]+12", delay=0.8, 
        delaytime=0.25, delayfeedback=0.5,
        gain="0.2+(ulsin 16)*0.8", pan="0 1",
        #coarse="8+(ulsaw 16)",
        )

PI * d("gtr", note="(g note)+ [5 7 5 0]", speed=2,
        delay=0.8, delaytime=0.25, p="(g ryth)", 
        delayfeedback=0.5, gain=0.7,
        #coarse=16,
        )

PN * d("gtr", note="(g note) + [5 7 5 0]", 
        speed = 4, p="(g ryth)", 
        delay=0.8, delaytime="(g del)", 
        delayfeedback=0.9, orbit=2,
        gain="(ulsin 8)*0.8",
        coarse=2, scram = 1.5, lpf=200
        )

PO * d("gtr", note="(g note) +[5 7 5 0]", speed=0.5, p="(g ryth)*4", 
        delay=0.8, delaytime="(g del)", pan="(ultri 7)*(-1)",
        delayfeedback=0.7, gain=0.9, orbit=4,
        #coarse=16, room = 0.7, size = "(g del)",
        #octersub=0.5, attack="(g del)*2",
        #scram=0.8, 
        #binshift=32,
        )

Op * d("gtr", note="(g note)", speed="[4!8 8!2]", rel=4, p=0.5, 
        delay=0.8, delaytime=0.25, pan="(ultri 8)", 
        delayfeedback=0.8, gain=0.8, orbit=3,
        coarse=4,
        )

silence(Pi,Po,PN,PI,Ii)

Pl * d("gtr", note="(g note)+[19 17 12]", p=0.25,
        delay=0.8, delaytime=0.25, pan="(ultri 7)", 
        delayfeedback=0.8, gain=0.7, euclid=(1,7,2), orbit=3,
        attack="(g del)*2",
        coarse=4)

PL * d("gtr", note="(g note)+[19 17 12]", p=0.25,
        delay=0.8, delaytime=0.25, speed = 2, pan="(ultri 8)", 
        delayfeedback=0.8, gain=0.7, euclid=(1,7,7), orbit=3,
        attack="(g del)/4",
        coarse=4)

ll * d("gtr", note="(g note)+[14 12 7]", p=0.25,
        delay=0.8, delaytime=0.25, pan="(ultri 6)", 
        delayfeedback=0.8, gain=0.7, euclid=(1,7,4), orbit=3,
        attack="(g del)*2",
        coarse=4)

PP * d("gtr", note="(g note)+[19 17 12]", p=0.25,
        delay=0.8, delaytime=0.25, speed = "4|2|0.5", pan="(ultri 8)", 
        delayfeedback=0.8, gain=0.5, euclid=(1,7,6), orbit=3,
        attack="(g del)*2",
        coarse=4)

Pl * d("gtr", note="(g note)+[19 17 12]", p=0.25,
        delay=0.8, delaytime=0.25, pan="(ultri 8)", 
        delayfeedback=0.8, gain=0.5, euclid=(1,7,2), orbit=3,
        attack="(g del)/2",
        coarse=4)

silence(Pl,PP,ll,PL,PL)

silence()

silence()

Pa >> d("long", leg=0.25, begin=0.8,gain="(g mov)",
        speed="0.25*(g mov)", p=0.125,  lpf="(g mov)*1000", res=0.2,)

Pb >> d("[long:[1:3] . .]!!2!!16", pan="(g mov)", leg=0.25, p=0.25)

Pi * d("long:[12|16|18|20]", begin="(g mov)",gain=0.5,room=0.8,sz=0.8,p=1,leg=1)

Pl * d("[.]!8",#begin="(ulsaw 4)/2", p=0.125,leg=0.125, orbit =2, 
        #room=0.5, 
        p="(s mov (ulsin 4))", #pan="0 1",
        )

PO * d("long:40", leg=0.125, begin="(g mov)/2",
        speed="1 2",
        p=0.125, lpf=500,#attack=0.15, delay=0.5, 
        #delaytime="(g mov)",delayfeedback=0.6
        )

Pm * d("long:42", leg=0.25, #begin="(g mov)", 
        gain="(g mov)-0.5",speed="0.25*(g mov)", p=0.125,  
        lpf="(g mov)*2500", res=0.5, attack=0.1,# delay=0.5, 
        #delaytime="(g mov)",delayfeedback=0.6, orbit=3
        )

Pk * d("(eu long:2 4 7 2)", p=0.5, speed=1, leg=0.25)

Pp * d("(eu long:36 3 7 1)", p=0.5,leg=0.25)

PK * d("(eu leKICK:2 4 7 2)", p=0.5, speed=1, leg=0.25, gain="(g mov)")

Ps * d("(eu laSNARE:4 3 7 1)",p=0.5,gain="1-(g mov)")

it crashed a bit sorry


clock.tempo=clock.tempo*2
       
clock.tempo

clock.tempo=clock.tempo*0.5

clock.tempo

silence(Pb,Pi,Pl)

Ps * d("leCASIOvib",
        speed="0.25*(g mov)", p=0.125, gain=0.5, 
        lpf="(g mov)*1000", res=0.2, orbit=6)

Ps * None


silence(Pk,P)

D("nevers:3")

silence()

Pv * d("accord:1",leg=16)

vv * d("accord:1", speed="{2 4}", p=16, coarse="(ulsin 8)*4", lpf=1500, leg=16)

PV * d("accord:[3:8]",leg=0.25,#p=0.25, 
        #gain="(ulsin 4)*0.8",
        pan="1 0.5 0.75 0 1 0.75 0.5 0.25 0 1", 
        begin="rand", euclid=(4,7),# shape=0.35, 
        #coarse=8,
        #speed="[1 0.5]+0.5*(g mov)", p=0.25, hpf="150+(g mov)*1000",
        #res=0.2, hpq=0.2,
        delay=0.75, delaytime="(g mov)/2", delayfeedback=0.65,orbit=4,
        )

Pl * d("[.]!8 accord:3!16", p=0.125, begin="[0.5:0.8]",pan="rand",
        gain="(ulsin 8)*0.8",
        leg=0.125,euclid=(3,7,2), coarse="16|4|8",
        )

PL * None

vv * None

PL * d("[.]!8 accord:3!16",speed=2, p=0.125, begin="[0.5:0.8]",pan="rand",
        leg=0.125,euclid=(3,7,5), coarse="16|4|8", gain=0.85
        )

Pj * d("juj:[0:45]", p=4, euclid=(3,7,2), shape=0.35,
        orbit=7, room=0.85, sz=0.85, gain=0.8, scram ="0.5 0 (ulsin 2) 2",
        delay=0.9,delaytime="0.01+(ulsin 4)/2", delayfeedback=0.67
        )

silence(Pj)

PA * zd("arp:[0:5]", "^ ^ t (7 5 3)+<0 7 5>",
        euclid=(6,8,2), scale="chromatic",
        key="F2",#F3 #F2
        lpf="1500*(ulsin 2)",res=0.4,
        gain=0.8,
        pan="0 0.5 1 0.5 0.75",
        )

Pa * zd("arp:[0:5]", "^ ^ t (7 5 3)+<0 7 5>",
        key="F6",
        euclid=(6,8,3), scale="chromatic", 
        lpf="1500*(ulsin 2)",res=0.4,
        gain=0.85, pan="0.5 0.75 0.25 0.15 0.5 075 0 1",
        )

solo(PA)

PA * None

silence()

silence(PV,PL)

silence()

D("nevers:3")

PI * d("nevers:[15:29]",p=0.25, leg=0.25, euclid=(6,7,2), begin="rand",
        #coarse="16 32 8 16 32 8 4 2 0 16 32 0 4 8",
        pan="(ltri 8)",vowel="e o i u", 
        accelerate="[0.75 -0.5 0.25 -1]/16",
        #leg=1,
        delay=0.9, delaytime="0.2", delayfeedback=0.2,
        )

clock.tempo

clock.tempo=clock.tempo*0.5

clock.tempo=clock.tempo*2

D("auqua:2")

dd * d("(eu auqua:[0|1] 13 15 7)", room=0.8, p="[.]!8 0.25|0.125!16", 
        euclid=(4,7),
        pan="0.75 0"
        )








Pa >> d("long", leg=0.25, begin=0.8,gain="(g mov)",
        speed="0.25*(g mov)", p=0.125,  lpf="(g mov)*1000", res=0.2,)

Pb >> d("[long:[1:3] . .]!!2!!16", pan="(g mov)", leg=0.25, p=0.25)

Pi * d("long:[12|16|18|20]", begin="(g mov)",gain=0.5,room=0.8,sz=0.8,p=1,leg=1)

Pl * d("[.]!8",#begin="(ulsaw 4)/2", p=0.125,leg=0.125, orbit =2, 
        #room=0.5, 
        p="(s mov (ulsin 4))", #pan="0 1",
        )

silence()

PO * d("long:40", leg=0.125, begin="(g mov)/2",
        speed="1 2",
        p=0.125, lpf=500,#attack=0.15, delay=0.5, 
        #delaytime="(g mov)",delayfeedback=0.6
        )

Pm * d("long:42", leg=0.25, #begin="(g mov)", 
        gain="(g mov)-0.5",speed="0.25*(g mov)", p=0.125,  
        lpf="(g mov)*2500", res=0.5, attack=0.1,# delay=0.5, 
        #delaytime="(g mov)",delayfeedback=0.6, orbit=3
        )











































