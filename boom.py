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

#A VERIFIER

c._midi_nudge = 0.5
#################

#OUBLIE PAS DE LINK LINK LINK LINK LINK

c.link()

c.unlink()

c.bpm = 150

c.bpm

Ph._div

####################################################
####################################################
####################################################

#CHANSON HOMMAGE à Jules Cipher

c.link()

# c.bpm = 125

#LEAD

#marimba
pgch(program=12, channel =0)

#vibraphone
pgch(program=11, channel=0)

@swim
def liquide(d=0.5,i=0):
    #minTheme #disco() #maj/min7                   #div=1
    #M(note="disco(C@maj)", channel = 0, dur=400).out(i, div = 1)
    #M(".!7,<C@min7>,.!7,<C@min7>,.!7,<C@maj7>",
    #        channel = 0, dur=300).out(i, div=4)
    #LeadTHEME  #apal #^[2~6]
    #M(note="pal(<C@maj, C@min7>,68,65,.,67,.)^[2~6]" , 
    #    velocity = P("70~90",i), 
    #    channel = 0, dur=5000).out(i)
    #Bass lente
    M(note="disco(<C@maj, C@min7>,68,65,.,67,.)" , 
        velocity = P("80~95",i), 
        channel = 0, dur=50).out(i, div = 2)
    again(liquide, d=P("0.25, 0.5",i), i=i+1)


#BAss TB303
pgch(program=38, channel=1)
cc(control=0, value =66, channel=1)

Pt >> play_midi('C2@min | ., C2@min7', channel = 1)
Pt.dur = 0.5
Pt._div = 6 #tidalmode


cc(control=1, value =127, channel=1)

Pt >> None

#DRUMSET 

#TR808
pgch(program=25, channel = 9)

#ROOM2
pgch(program=72, channel = 9)

#TR909
pgch(program=88, channel = 9)

PO >> play_midi("36,.,.,.", velocity = 127, channel = 9)
PO.dur = 0.5
PO._div = 12 #tidalmode

PO >> None

Ps >> play_midi(".,.,38,.", velocity = 100, channel = 9)
Ps.dur = 0.5
Ps._div = 12 #tidalmode


Ps >> None

Ph >> play_midi("44!7, 46", channel=9)
Ph.dur = 0.5
Ph._div =12 #tidalmode


Ph >> None

hush()

################################################################
################################################################
################################################################
################################################################

#SYNCLAVIER
@swim
def melodie(d=0.5, i=0):
    change = 0
    #change = 2 if rarely() else 0
    #change2 = 5 if almostNever() else 0
    M(note=f'adisco(pal(G3@penta))+{change}', 
            #dur = 1000
            dur = 1000
            #dur = P("100~1000")
                        ).out(
                            i, 
                            div=
                            #P("8!1,3!4,2!2",i),
                            P("4,8",i), 
                            rate=1) #G3 #G4
    #cc(channel=0, control=1, value=P('r*127',i))
    #cc(channel=0, control=1, value=P('r*127',i))
    #tx7('DetuneOp1', 16)
    #tx7('DetuneOp2', P('r*16',i))
    #tx7('DetuneOp3', 15)
    #tx7('DetuneOp4', P('r*16',i))
    #tx7('Retain/Follow', 1)
    #tx7('GlissandoOffOn', 1)
    #tx7('Time',P('r*12'),i)
    again(melodie, d=0.125, i=i+1)

hush()

######################################################
######################################################
######################CHOEURS 2#######################

@swim #CHOEURS 2 ou ENGLISH02
def melodie(d=0.5, i=0):
    duration =300
    #duration= "300!4,400!3,500!2,600"
    diviseur = 1
    ratte = 1
    #diviseur = 4 if rarely() else 1
    #ratte = 0.2 if rarely() else 0.5 
    #changer (1~1) en (1~2++) les hauteurs de LA et aussi les [1,(3~6] du dernier
    M(note="euclid(La6@hirajoshi&[0,(1~4)]^(-1),5,8)", dur=duration).out(i, div= diviseur, rate= ratte)
    #M(note="euclid(Lab3|La2@hirajoshi&[0,(1~4)]^(1~2),6,8)", dur=duration).out(i+2, div= diviseur, rate=ratte)
    #M(note="euclid(La2@hirajoshi&[1,(3~6)]^(1~4),7,8)", dur=duration).out(i+1, div=diviseur, rate=ratte) 
    again(melodie, d=P(
        #'0.25,0.25,0.5,0.25',
        '0.5',
        i), i=i+1) 

#BIEN MAMUSER AVEC TOUS CES JOLIES PARAM avant de le tuer
hush()

###############################################################
#CHANSON NUMERO 2, dowaping in the DOO-wap (nourriture)

c.unlink()

c.bpm = 152

#ROOM2
pgch(program=72, channel = 9)

PO >> play_midi("36,.,.,36,.,.,.,.",
        velocity = 130, channel =9)
PO.dur = 0.5
PO._div = 12

PO >> None

Ps >>  play_midi(".,.,.,38", velocity = 85,  channel =9)
Ps.div = 0.5

Ps >> None

Ph >> play_midi("44!7,46", channel = 9)

hush()

pgch(program = 33, channel = 1)
cc(control = 0, value =66, channel = 1)

@swim
def dubibass(d=0.5, i=0):
    duration = 400
    M(note=".,D3", channel = 1, dur = duration).out(i, div=2, rate=1)
    M(note = 'D2,.,D2',channel = 1, dur = duration).out(i, div=1, rate=1) 
    again(dubibass, d=1, i=i+1)


pgch(program=63, channel = 3)
cc(control=0, value=64, channel=3)

@swim
def orgie(d=0.5, i=0):
    M(note="<D4@maj7>", 
            channel = 3, 
            velocity = P("[45:55]",i), 
            dur = 300).out(i,div=4, rate=1) 
    M(note=".!8,adisco(F4@maj7)", 
            channel = 3, 
            velocity = P("[75:45]",i), 
            dur = 650).out(i,div=4, rate=1)
    again(orgie, d=0.125, i=i+1)


@swim
def dowap(d=0.5,i=0):
    pgch(program = 53, channel=4)
    if E(2,3,i):
        pgch(program = 54 , channel = 4)
    M(note="D5,.,disco(D4@maj7),.,F3@hirajoshi | .", channel = 4).out(i, div = 2, rate = 1)
    M(note="D6,.,disco(D5@maj7),.,disco(F4@maj7)", channel=4).out(i, div=4, rate=P("1,2,3",i))
    again(dowap, d=0.125, i=i+1)

#laisser que le hh

@swim
def tempomedler(d=0.5, i=0):
    if c.bpm < 80 :
        c.bpm = c.bpm*1.02
    else :
        c.bpm = 60
    again(tempomedler, d=0.5, i=i+1)

hush()


###################################################"
#####################RAB TX7##########################"


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

PO >> play("bd:4,sn:4,sn:4,.,.", speed = "<r,4>", legato = 4, shape=0.7, crush=16, leslie = 1.5, gain=0.8)
PD >> play("hh",speed = "<r, 2>")
PO.div = 1
PO.rate = 3

PO >> None
PD >> None

#LEVEL BEPBOPROBOT ENGLISH01
@swim
def melodie(d=0.5, i=0):
    M(note='Bb6 | C5 , .', dur=200).out(
    i,
    div=P('2,4,2,2')*0.5, rate= 1)
    #M(note='C3 | C4,.', dur=105).out(i, div= 2, rate =1.2)
    #tx7('Retain/Follow', 1,i)
    #tx7('GlissandoOffOn', 1,i)
    #tx7('Time', 140,i)
    #tx7('Algorithme', "r*30", i, div=1, rate=1)
    #tx7('Algorithme', '4,5,7,8',i, div=16)
    #tx7('LevelOp1', 'r*125',i, div =8)
    #tx7('LevelOp2', 'r*125',i, div =8)
    #tx7('LevelOp3', 'r*125',i, div =8)
    #tx7('LevelOp4', 'r*125',i, div =8)
    #tx7('LevelOp5', 'r*125',i, div =8)
    #tx7('LevelOp6', 'r*125',i, div =8)
    again(melodie, d=1, i=i+1)


#l'HORREUR'

#PERMUTER ENTRE EFFECT 01 et EFFECT 0.2
#CASIOTIME 
@swim
def melodie(d=0.5, i=0):
    tx7('Algorithme', "9*r",i)
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






