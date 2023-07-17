from art import text2art
import random
from random import choice
# JOB ID 3
D("ralt144mi", shape=.6, delay=0.5, delaytime=.75, delayfeedback=.60, 
  pan= "0.25|0.75", room=0.8, dry=0.2, size=0.7, orbit=3, accelerate=0.15)

clock.tempo=137
bb >> zd("leCASIOvib:[0~10]", 
        "(0 7 0 4):4 (5 9 5 ^0):4 (7 E 7 ^2):2 (5 9 5 ^0):2",
        key="C", scale="chromatic", 
        #speed=0.25, 
        speed = "(if (rand > 0.5) 1 (if (rand > 0.5) {1.01 0.99} {1.01/2 0.99/2}))/4",
        leg=0.8, octersub=1, 
        triode = 4.6, shape=0.25,
        delay = 0.8, delaytime = "0.5!3 1", delayfeedback = "($%20)/20", gain=0.97
        )

Pb >> d("bassfoo", begin=0.12, hpf="10*($%10)*10",
        #p="0.5", 
        orbit = 2
        )

ll *  d("long:[10~20]", lpf="1500!10 3500!2", gain=0.9,leg=0.2, p=2)

Pb >> None

clock.tempo=144

Pk * d("leKICK:[6] {leHIHAT:[12] leKICK:6} {laSNARE:[5] laSNARE:8} leHIHAT:[12]",leg=0.2, p=0.5, 
        shape=0.3, room=0.5, gain=0.9, pan="{0 1}"
        )

Pi>>zd("leCASIOvib:5",
        "(((s 0 4 7)+(0 <0 0 0> 5)):2) \
         (((s 0 4 7)+(0 <0 0 0> 0)):2) \
         (((s 5 9 ^0)+(5 <0 0 0> 0)):2) \
         (((s 7 E ^2)+(0 <0 0 0> 5)):2) \
         (((s 5 9 ^0)+(0 <0 5 0> 0)):2)",
        scale='chromatic', pan = "{0 1}", triode=5.9, shape=0.65,
        p=0.25, leg=0.75, gain=0.7)

silence(Pk, Pb, bb)

silence()

Ps * d(". laSNARE:[rand*25]", leg=0.5, gain=1.2)

PK * d("maloya", 
        speed="{1 0.98 2}", 
        lpf="100*($%40)"
        )

Pl >> d("(eu maloya:1 9 16)", p=0.25, gain=0.8)

Pj >> d("(eu {maloya:2 leKICK:2} 13 16)", p=0.5,
        gain=1.2, octersub=2)

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
        #speed="{1 0.98}/2",
        speed="({1 0.98})/2!16 ({1 0.98})/1.5!15 ({2 2.98})",
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
    Pd >> zd("braids",ferrat4, channel = 0, 
            dur=0.8,room = 0.8, sz=0.6, orbit=1)
lead()

clock.tempo = 160 #160

Ps >> None

Pk >> d("leKICK:5", shape = 0.25,   lpf = 500)

Pk >> d("leKICK:5!15 protokick",  lpf = 500)

Pk >> d("protokick", shape = 0.25, triode=0.8, lpf = 1500, gain=1.2)

Ps >> d("[amencutup:[1~12]!!2]!!4",p=0.5,
        phaserrate=0.8,phasdp=0.8,
        shape=0.55, leg=0.15)
PS >> d("[sid:[1~12]!!2]!!4",p=0.5,
        phaserrate=0.8,phasdp=0.8,
        shape=0.55)

Pa >> None #POURTANT QUE LA MONTAGNE
Pb >> None #EST BELLE COMMENT PEUT ON
Pc >> None #SIMAGINER EN VOYANT UN 
Pd >> None #VOL DHIRONDELLE QUE LOTOMNE VIENT DARRIV2R !!!!!!
def lead():
    Pa >> zd("braids",ferrat5, pan = 0.5, channel = 0, dur=0.3)
    Pb >> zd("braids",ferrat6, pan = 0.25, channel = 0, dur=0.5)
    Pc >> zd("braids",ferrat7,  model = 1, channel = 0, dur=0.55)
    Pd >> zd("braids",ferrat8,# accelerate=0.05, scram=0.2,
            channel = 0, dur=0.8, room = 0.8, sz=0.6, orbit=1)
lead()

Pk >> None
Ps >> None

PS >> None

clock.tempo=670

silence()

