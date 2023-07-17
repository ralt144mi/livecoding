silence()

Pk * d("gretsch:[0 7 6 1 0 12 2 2 0 26 12 3]", p="1 1 1 1/3!3 1 1 1 1/6!6", 
        leg=0.25, triode = 0.6, room=0.5, orbit="{2 1}", shape=0.8, gain=0.9)

Ph * d("gretsch:[6 6 6 8 6 8 6 6 8]", p=1/3)

Pa * d("contrebasse:165", triode=3.9, shape=0.96, gain=0.85, speed=0.42, p=8, leg=4)

Pb * d("trombone:[165~168]", triode=3.9, shape=0.4, 
        gain=0.9, speed=(0.42)*2, p="1 1 0.5!2 2 4 0.5!4", 
        vowel="a a a a o o i e e e",
        leg=0.8, room=0.9, sz=0.95, dry=1, orbit=2,
        delay = 0.8, delaytime=0.5, delayfb=0.85
        )

Pk * d("gretsch:[1 0 1 0 0 0]", p=0.125,triode = 0.6, room=0.5, orbit=2, shape=0.8, gain=0.9)

Pk * d("gretsch:[0 7 6 1 0 12 2 2 0 26 12 3]", 
        p="1 1/6!6 1 1/6!6 1 1/6!6 1 1/6!6", 
        leg=0.25, triode = 0.6, room=0.5, orbit=2, shape=0.8, gain=0.9)

Pc * d("trombone:[165~168]", triode=1.8, shape=0.4, 
        gain=0.8, speed="{((0.42)*4)}", p="1", 
        vowel="{e i}", on=2 , loaf=3, 
        leg=2, room=0.9, sz=0.9, orbit=3
        )

PD * d("trombone:[165~168]", triode=0.8, shape=0.2, 
        gain=0.8, speed="{((0.42)*0.42)}", p="1", 
        vowel="{e i}", on=2 , loaf=3, 
        leg=2, room=0.9, sz=0.9, orbit=3
        )

silence(Pb,Pc)

silence(Pk)
PK * d("[bdacous:[2] sdanalog]!6 .!12 [bdacous:[2] sdanalog]!6",
        triode = 0.6, shape=0.85,
        #gain="(if (beat 0 1 2) 1 0)",
        p="1/6",orbit=4, room=1, octersub=1)

silence(Ph)

Ps * d("(eu laSNARE:2 2 4 3)", triode = 0.6, shape=0.8, begin=0.2, gain=0.8)

def theme():

silence(PE,Pe,PK) 

PE * zd("gtr", "([0 5 3] 0)+(<0 0 0> <3 0 7> <5 0 0> <0 0 5>)",
        scale="rocritonic",key="C", leg=0.65,
        speed="{1 0.4995}",
        #speed="{0.5 0.4995}",
        triode=0.6, shape=0.9, gain=0.86,
        #leslie=0.25,
        )

PK * d("[bdacous:[2] sdanalog]!6 .!12 [bdacous:[2] sdanalog]!6",
        gain=1.1, triode = 0.6, shape=0.35,
        #gain="(if (beat 0 1 2) 1 0)",
        p="1/6",orbit=4, room=1, octersub=1)

Pe * zd("gtr", "(<w w h h w q> [0 5 3] 0)+(<0 0 0> <3 0 7> <5 0 0> <0 0 5>)",
        scale="rocritonic",key="C", leg=0.65,
        speed="{2.001 3.995}",
        #speed="{0.5 0.4995}",
        triode=0.6, shape=0.9, gain=0.82,
        pan="(lsin 2)",
        leslie=0.25,
        lpf ="(lsin 4)*1000", res=0.25,
        hpf ="(altri 2)*500", 
        )

silence(PE,PK)

Ph * d("(eu leHIHAT:[10 10 11] 3 5)",
         euclid=(3,5,2), 
         leg="0.9 0.7 0.8 0.6 0.5 0.9 0.8 0.5 0.6 0.9 0.7 0.3 0.9 0.8",
         hpf="1000",shape=0.4,p="1/3")

PH * d("(eu crashstandard:[5 4 3] 3 7 4)",
         euclid=(4,5,3),
         leg="0.9 0.7 0.8 0.6 0.5 0.9 0.8 0.5 0.6 0.9 0.7 0.3 0.9 0.8",
         lpf="3500",
         shape=0.4,
         p="1/3",gain=1.3)

silence(Ph)

silence()

theme()

PE * None

PE * zd("gtr", "(0 [0 5 3])+(<0 0 0> <3 0 0> <5 0 0> <0 0 0>)",
         scale="rocritonic",key="C", leg=0.65,
         speed="{1 0.4995}",
         #speed="{0.5 0.4995}",
         triode=0.6, shape=0.9, gain=0.85,
         leslie=0.25, 
         lpf="(lsin 8)*(2050)", res=0.26,
         )

PP * zd("gtr", "(t 0 [0 5 3])+(<0 0 0> <3 0 0> <5 0 0> <0 0 0>)",
         scale="rocritonic",key="C", leg=0.65,
         speed="{2 0.4995}",
         #speed="{0.5 0.4995}",
         triode=0.6, shape=0.9, gain=0.85,
         leslie=0.25, 
         lpf="(lsin 8)*(250)", res=0.26,
         )

silence(PP)

silence(Pa)


silence()

