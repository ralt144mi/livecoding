@swim
def loopman(p=0.25, i=0):
    D("laloopRec", i=i)
    print("jerec")
    again(loopman, p=4, i=i+1)

silence(loopman)


D("maloya")

Pi >> d("[nevers .!4]!!4", lpf="1500!8 2500", gain=0.65,
        begin = "0 0.5 0.8",
        leg="0.60 0.53 0.68", shape=0.25, room=0.25, sz = 0.5, p=1)

Pl >> d("(eu laloop:3 3 5)", leg=.1, shape=0.25, room=0.25, p=.25)

Pz >> zd("braids", "w v r r iv r r i r r", model="25*rand", timbre=0.5,
        gain=0.4, lpf=1200)

Px >> d(". laloop:5", p="0.25", lpf=3500,leg=0.5, shape=0.25, room=0.5)

Pk >> d("leKICK:[4]", gain = 0.8)

Pn >> d("long:42 long:[40~49]",# scram=0.2,
        vowel = " a e i o u a e i o u",
        gain =0.8, accelerate = "0.8 (-0.8)",
        speed = 0.5,
        begin= "0.5 0", pan="rand",
        p="0.125!16", d="1 2 3", leg="0.15!16 0.55 0.65")

Pe >> d("son:1", until=3, lpf=3500, gain=0.7)

Pi >> d("(eu [son:[3]!4] 1 7 2)", until=25,
        speed = "[1 2 3 4 5 7]/[2~4]",
        shape = 0.5, gain =0.60, 
        p="0.125 0.5", pan = "[1:7]",
        #span = 1, 
        accelerate = "1.5 0.5",
        legato=0.7)

Pj >> d("accord:[rand]", 
        leg="0.10", begin=0.5, #pan="rand", 
        accelerate = "0!7 1.8|0.8", p="0.125/4",
        #speed="1!3 2!2 1!4 2!1",
        #room=0.2, sz=0.5, shape=0.1,
        #gain=0.8,
        #p="0.5!7 0.25!2",
        )


PK >> d("[(eu laSNARE:[rand*24] 4 5 2)!!2]", binshift leg=0.15, p="0.5!19 0.125!2 0.25!5", div=2, gain = 0.75, lpf="3200~5500", resonance = 0.15 #until=25
        ,leslie="0!4 0.8")

panic()

Pj >> None

PK >> None

clock

clock.tempo

