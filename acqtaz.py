pi * d(":[0:5] .!32", leg=0.125, begin="rand", p=0.125, pan="0 1")

pi * None

Pn * n("(scl 8 16)", channel=1)

panic()

PN * n(". 66", channel=1)

Pn * zn(" 0  3 5 7 1 2 5")

PB * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(1,9,5), 
        speed="{1 0.5 0.8}", pan = 0,
        #real=0.9, imag=0.25
        )

OP * d("bongobuchla:[0~32]", p="0.25!9 0.5", euclid=(1,9,0), 
        speed="{1 0.5 0.8}", pan = 1, 
        #real=0.9, imag=0.25
        )

Pl * d("leCASIO:[0~9]", leg=0.9, pan="0 1", 
        p="0.5!2 0.125!2 0.25!2 0.5"*2, euclid=(4,9,6),
        #real=0.6, imag=0.15,
        )

Pl * None

silence()

clock.tempo


clock.tempo=clock.tempo*2

clock.tempo=clock.tempo*0.5



Pn * Non

Pn * n("D4@min7 F4@min7 C4@min7",p=0.125,channel=1)

Pi * d("teratoma:[1~150]", leg=0.25, p=0.5, begin="rand")

Pi * d("spore:[1~150]", leg=0.25, p=0.5, begin="rand")

Pd * d('teratoma:[0:150]', amp=0.4, p=.5, leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('[.!8] spore:[0:50]', p=.25, leg=.1, pan='rand', on=2, speed=2)

PD * d('crunchorganic:[0:150]', amp=0.4, p=.5, leg=.05, pan='rand', speed='(if (beat 0 2) 1 0.5)')

PE * d('[.!8] proximity:[0:50]', p=.25, leg=.1, pan='rand', on=2, speed=2)

Pk * d("kick:1 . laSNARE:[1~18] .", p=0.5, shape=0.45, room=0.15)

ph * d("leHIHAT:[8]", leg=0.25, p=0.25, orbit=2, shape=0.2)

PP * d("[proximity:[0:50] spore:[0:150]]", p=0.125, speed="(lsin 2)", 
        lpf="150*(lsaw 4)", leg=0.2, res=0.2)

Pk * d("(kick:1) (kick:0~8) (laSNARE:1~18)", p=0.5, shape=0.45,room=0.26)

ph * d("leHIHAT:[9:12]", leg=0.15, p=0.25, orbit=2, shape=0.2)


Pn * zn("_ <0 5 0> <3 5 7> <5 7 5 3> [7 5]", velocity="30~45",scale="rocritonic", key="C", channel=1)


Pk * d("{(kick:1) (sid:2)} {(kick:0~8) (sid:2)} laSNARE:[1~18] sid:2", 
        room=0.6,p="(rand*0.5)", shape=0.45,lpf=1000)


Pd * d('teratoma:[0:150]', amp=0.4, p=.5/4, leg=.1, pan='rand', speed='(if (beat 0 2) 1 0.5)')
Pe * d('[.!8] spore:[0:50]', p=.25/4, leg=.3, pan='rand', on=2, speed="(lsaw 8)")
PD * d('crunchorganic:[0:150]', amp=0.4, p=.5/4, leg=.1, pan='rand', speed='(if (beat 1 3) 1 0.5)')
PE * d('[.!8] proximity:[0:50]', p=.25/4, leg=.3, pan='rand', on=1, 
        speed="(lsaw 8)",lpf="2502*(lsin 8)")


clock.tempo=clock.tempo*2


clock.tempo=clock.tempo*0.5

clock.tempo

silence()


PN * zn("_ r r r r e [7 5 3 0] [7 5 3 0]", 
        velocity=60, 
        scale="rocritonic", key="C", channel=1)

PN * None

Pi>>zn(" (((h 0 4 7)+(0 <7 0 0> 5)):2) \
         (((h 0 4 7)+(0 <0 5 0> 0)):2) \
         (((h 5 9 ^0)+(5 <7 0 0> 0)):2) \
         (((h 7 E ^2)+(0 <0 5 0> 5)):2) \
         (((h 5 9 ^0)+(0 <0 5 0> 0)):2)",
        scale='chromatic', p=0.5, channel=1)

PI>>zn("_ (((h 0 4 7)+(0 <7 0 0> 5)):2) \
          (((h 0 4 7)+(0 <0 5 0> 0)):2) \
          (((h 5 9 ^0)+(5 <7 0 0> 0)):2) \
         _ (((h 7 E ^2)+(0 <0 5 0> 5)):2) \
         _ (((h 5 9 ^0)+(0 <0 5 0> 0)):2)",
        scale='chromatic', dur = 2,channel=1)

