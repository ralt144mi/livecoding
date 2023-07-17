silence()

clock.tempo

Pn * zn("e (7 5 3)+<0 7 5>", octave="2 3 4",dur=0.5, scale="chromatic",  euclid=(6,8,2),
)

PA * zd("arp:[0:5]", "^ ^ t (7 5 3)+<0 7 5>",
        euclid=(6,8,2), scale="chromatic", 
        lpf="1500*(ulsin 2)",res=0.4,
        gain=0.7,
        pan="0 0.5 1 0.5 0.75",
        )

Pa * zd("arp:[0:5]", "^ ^ t (7 5 3)+<0 7 5>",
        speed=2,
        euclid=(6,8,3), scale="chromatic", 
        lpf="1500*(ulsin 2)",res=0.4,
        gain=0.7, pan="0.5 0.75 0.25 0.15 0.5 075 0 1",
        )


Pa >> d("groupama:[0~10]", leg=8, p=8, begin=0.8,gain="(g mov)",
        #speed="0.25*(g mov)", p=0.125,  lpf="(g mov)*1000", res=0.2,
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

P('(s note (C4))')

P('(s note 2)')

P('(s note 10)')

P('(s note 7)')

silence()

@swim
def pattern(p=0.5,i=0):
    P('(s note [C3 G3 E3 B4])',i)
    P('(s del (ulsin 16))',i)
    again(pattern, p=8,i=i+1)

P('(s del 0.25)')

P('(s del (ulsin 4))')

P('(s del 0.25)')

P('(s del 0.25)')

pi * n("(eu (g note) 3 5)",p="0.25", dur="(g del)*0.25")

pI * n("(eu ((g note)+24) 4 7 2)",p="0.125/2!8", euclid=(4,7,2), 
        #dur=.1,
        dur="(g del)*0.25"
        )

Pl * n("(eu ((g note)+7) 13 15 4)", p=0.25, dur="(g del)*0.125")

PL * n("(eu [. ((g note)+7)] 10 15 8)", p=0.25, dur="(g del)*0.125") 

Pi * d("accord",note="(g note)", delay=0.8, 
        delaytime=0.25, delayfeedback=0.5, p="1/3",
        gain="0.2+(ulsin 4)*0.8", pan="0", lpf="1500+200*(g del)",res="(g del)",
        coarse="8+(ulsaw 16)", leg=2,begin=0.5,
        binshift="0.2!16 0.8!8", orbit=2
        )

Pl * d("gtr",note="(g note)+[5 7]", speed=2, delay=0.8, 
        #delaytime=0.25, delayfeedback=0.5, 
        p="0.25",
        gain="0.2+(ulsin 4)*0.4", pan="1", lpf="1500+200*(g del)",res="(g del)",
        coarse="8+(ulsaw 16)", 
        #binshift="0.2!32 0.8!4",
        )

silence()

clock.tempo=clock.tempo*2

clock.tempo=clock.tempo*0.5

clock.tempo

silence()

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
        speed = 4, p="(set ryth [0.5!8 0.25!2])", 
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


PO * 






