D("ralt144mi")

D("leKICK:[0~16]")

Pe >> d("[(eu trombone:[0~213] 8 18)!!2]!!4", vowel ="a o i", 
        begin = "rand*1.5", accelerate="0.2 2 -0.2", # scram=0.8,
        leg=0.04, p=0.125*2, lpf= 1000, room=0.5)

Py >> d("(eu trombone:7 2 3)", p=0.25, leg=0.04, shape=0.2, room=0.5) 

Pn >> n("C2 C6", dur=2, p=2, channel=1)

Pl >> n("(disco C4@min7)", p=0.5, channel=1)

silence()

Pl >> zn(" s ^ ^ 7 5 [3 _ [7 5 3] ^ ] 7 5 3 w r q 7 [5 _ [7 3] ^ ] 3 r 7 [5 [7 5]] 3 w r r r", dur=0.1, channel=1, key="C", scale="min7")

Pi >> d("(eu [cowFUN:2 cowFUN:[0~16]!2] 4 5 2)", p="1", leg=0.2, shape=0.4,
        #accelerate=0.3
        )

PI >> None

PI >> d("(eu cowFUN:[4|10|11|6] 9 13)", p=0.25, accelerate="0!4 -0.6!2 0.8!4", leg=0.1)

Pk >> d("leCASIO:[0~4]", p="0.5!4 0.25!2", shape=0.65, gain=0.9)

PK >> d("leKICK:[4~6]",  gain=1)

PK >> None

@die
def tempomedler(p=0.5, i=0):
if clock.tempo > 40 :
    clock.tempo = clock.tempo*0.006
else :
    clock.tempo = 140
#print(text2art("try to dance on that","straight"))
again(tempomedler, p=0.5, i=i+1)


clock
