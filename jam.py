. = octave down
. = silence
' = octave up
b = bémol
# = dièse
1-9 = spécificateur d'octave
@ = qualifier
nom() = modifier (après qualifier)

out(i, div=x, speed=x)
dur = la longeur de note 

x~y nb rand entre x et y

print_param()

print_scales()

#EMERGENCY RECALAGE

c._superdirt_nudge = 0

c._midi_nudge = 0.75
#################

#OUBLIE PAS DE LINK LINK LINK LINK LINK

c.link()

c.unlink()

c.bpm = 150

c.bpm

@swim
def synchro(d=0.5, i=0):
    S("bd",dur=100).out()
    a(synchro, d=0.5, i=i+1)

hush(synchro)

#SYNCLAVIER
@swim
def melodie(d=0.5, i=0):
    change = 2 if rarely() else 0
    change2 = 5 if almostNever() else 0
    M(note=f'adisco(pal(G3@penta))+{change+change2}', 
            #dur = 1000
            dur = 10
            #dur = P("100~1000")
                        ).out(
                            i, 
                            div= 
                            #P("8!1,3!4,2!2",i),
                            #P("4,8",i), 
                            rate=2) #G3 #G4
    #cc(channel=0, control=1, value=0)
    #cc(channel=0, control=1, value=P('r*127',i))
    #tx7('DetuneOp1', 16)
    #tx7('DetuneOp2', 'r*16',i)
    #tx7('DetuneOp3', 15)
    #tx7('DetuneOp4', 'r*16',i)
    #tx7('Retain/Follow', 1)
    #tx7('GlissandoOffOn', 1)
    #tx7('Time','r*12',i)
    again(melodie, d=0.125, i=i+1)


#808/909
pgch(channel = 9, program=88)

@swim 
def batterie(d=0.5,i=0):
    M(note ="36,.,.,36,.,C", channel = 9).out(i)
    #M(note ="42,42,42,42", channel = 9).out(i)
    again(batterie, d=0.5,i=i+1)

hush() ne reset pas le rate

Pa >> play_midi(note = "36,.,.,36,.,C4",channel=9)
Pa.div = 1

Pa >> None

Pn >> play_midi(note= "38,.,.,38,.,.", channel=9)
Pn.div = 1

Pn >> None

Pi >> play_midi(note = "42!7,46",channel=9)
Pi.div =1

Pb >> play_midi(note = "48,47,46,43", channel = 9)
Pb.div = 1
Pb.rate = 1

Pb >> None

Pa >> play_midi(note="73!3, 74", channel = 9)
Pa.div = 2

Pa >> play_midi(note="42!7,46", channel =9)

Pa >> None

Pn >> play_midi(note="36,.,.,.,.,.,38,38", channel=9)

Pn >> None

Ph >> play_midi(note="36,.,.,.", channel=9)

Ph >> None

Pi >> play_midi(note="<disco(G3@maj)>, aspeed(G4@maj)", dur = 100, channel=0)
Pi.rate = 2
Pi.div = 1


cc(control = 1, channel=1, value=0)

hush()

Ps >> play_midi(note ="C5,.!4",channel=9) 

Ps >> None

#OBSOLETER NE PAS ME JOUER
@swim #CHOEURS 2 ou ENGLISH02
def melodie(d=0.5, i=0):
    #if almostAlways() :
    #   tx7('Algorithme', 'r*10',i)
    for _ in ['A->hirajoshi:palindrome:braid', 
            'A->hirajoshi:palindrome', 
            'A->penta:drop4']:
        M(note=_,
                dur=300,
                #dur="300!4,400!3,500!2,600"
                ).out(i,
                #div = 4 if rarely() else 1,
                #speed= 0.2 if rarely() else 0.5 
                        )
    again(melodie, d=P(
        #'0.25,0.25,0.5,0.25',
        '0.5',
        i), i=i+1)

@swim #CHOEURS 2 ou ENGLISH02
def melodie(d=0.5, i=0):
    #duration =30
    duration= "300!4,400!3,500!2,600"
    #diviseur = 1
    #ratte = 1
    diviseur = 4 if rarely() else 1
    ratte = 0.2 if rarely() else 0.5 
    #changer (1~1) en (1~2++) les hauteurs de LA et aussi les [1,(3~6] du dernier
    M(note="euclid(La4@hirajoshi&[0,(1~4)]^(-1),5,8)", dur=duration).out(i, div= diviseur, rate= ratte)
    #M(note="euclid(Lab3|La2@hirajoshi&[0,(1~4)]^(1~2),6,8)", dur=duration).out(i+2, div= diviseur, rate=ratte)
    #M(note="euclid(La2@hirajoshi&[1,(3~6)]^(1~4),7,8)", dur=duration).out(i+1, div=diviseur, rate=ratte) 
    again(melodie, d=P(
        #'0.25,0.25,0.5,0.25',
        '0.5',
        i), i=i+1) 

#BIEN MAMUSER AVEC TOUS CES JOLIES PARAM avant de le tuer
hush()

c.bpm = 175

@swim
def liquide(d=0.5,i=0):
    M(note="pal(<C@maj, C@min>,68,65,.,67,.)" , channel = 0, dur=5000).out(i)
    again(liquide, d=P("0.25",i), i=i+1)

hush(liquide)

@swim
def liquide2(d=0.5,i=0):
    M(note="disco(C1@maj),C2@maj" , channel = 1, dur="10~100").out(i)
    again(liquide2, d=P("0.25",i), i=i+1)

hush(liquide2)

#STRINGS BF
@swim
def melodie(d=0.5, i=0):
    M(note='<disco(E4@min7)>, disco(C5@maj7), <adisco(E2@min7)>'
            ,dur=500
            #,dur="[10:1]*100"
            ).out(
                    #i,
                    i if rarely() else -i,
                    div=P("2,4,1,2,4,1",i), rate=1)
    #tx7('Retain/Follow', 1,i)
    #tx7('GlissandoOffOn', 1,i)
    #tx7('Time', 100,i)
    #tx7('Algorithme', "r*30", i, div=1, speed=1)
    again(melodie, d=0.5, i=i+1)

PO >> play("bd:4,sn:4,sn:4,.,.", speed = "<r,4>", legato = 4, shape=0.7, crush=16, leslie = 1.5)
PD >> play("hh",speed = "<r, 2>")
PO.div = 1
PO.rate = 3

#LEVEL BEPBOPROBOT ENGLISH01
@swim
def melodie(d=0.5, i=0):
    M(note='aspeed(disco(F2@hirajoshi))', dur=1200).out(
    i,
    div=P('8',i), rate= 1)
    cc(channel = 0, control = 1, value =P('52~127',i))
    #M(note='C3 | C4,.', dur=105).out(i, div= 2, rate =1)
    #tx7('Retain/Follow', 1,i)
    #tx7('GlissandoOffOn', 1,i)
    #tx7('Time', 140,i)
    #tx7('Algorithme', "r*30", i, div=1, speed=1)
    #tx7('Algorithme', '4,5,7,8',i, div=16)
    #tx7('LevelOp1', 'r*125',i, div =8)
    #tx7('LevelOp2', 'r*125',i, div =8)
    #tx7('LevelOp3', 'r*125',i, div =8)
    #tx7('LevelOp4', 'r*125',i, div =8)
    #tx7('LevelOp5', 'r*125',i, div =8)
    #tx7('LevelOp6', 'r*125',i, div =8)
    again(melodie, d=0.125, i=i+1)


hush()

#l'HORREUR'

#PERMUTER ENTRE EFFECT 01 et EFFECT 0.2
#CASIOTIME 
@swim
def melodie(d=0.5, i=0):
    #tx7('Algorithme', "9*r",i)
    M(note='C->tritone, D->tritone:palindrome', dur=1000).out(i)
    if E(4,8,i):
        tx7('Algorithme', 21)
    if E(1,8,i):
        tx7('Algorithme', '9',i)
        tx7('LFOWave', '0:6',i)
        tx7('LFOPMS','0:5', i)
        tx7('LFOSpeed', '40:50',i)
    if E(5,7,i):
        tx7('Algorithme', 20)
        M(note = 90).out(i)
    again(melodie, d=P('0.5',i), i=i+1)

hush()
