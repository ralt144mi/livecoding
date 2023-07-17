          _______  _______  _______           _______   _________          ______         
|\     /|(  ___  )(       )(  ___  )|\     /|(  ___  )  \__   __/|\     /|/ ___  \        
( \   / )| (   ) || () () || (   ) || )   ( || (   ) |     ) (   ( \   / )\/   )  )       
 \ (_) / | (___) || || || || (___) || (___) || (___) |     | |    \ (_) /     /  /        
  \   /  |  ___  || |(_)| ||  ___  ||  ___  ||  ___  |     | |     ) _ (     /  /         
   ) (   | (   ) || |   | || (   ) || (   ) || (   ) |     | |    / ( ) \   /  /          
   | |   | )   ( || )   ( || )   ( || )   ( || )   ( |     | |   ( /   \ ) /  /           
   \_/   |/     \||/     \||/     \||/     \||/     \|     )_(   |/     \| \_/            
                                                                                          
 _______  _______  _       _________ _______  _______  _        _        _______  _______ 
(  ____ \(  ___  )( (    /|\__   __/(  ____ )(  ___  )( \      ( \      (  ____ \(  ____ )
| (    \/| (   ) ||  \  ( |   ) (   | (    )|| (   ) || (      | (      | (    \/| (    )|
| |      | |   | ||   \ | |   | |   | (____)|| |   | || |      | |      | (__    | (____)|
| |      | |   | || (\ \) |   | |   |     __)| |   | || |      | |      |  __)   |     __)
| |      | |   | || | \   |   | |   | (\ (   | |   | || |      | |      | (      | (\ (   
| (____/\| (___) || )  \  |   | |   | ) \ \__| (___) || (____/\| (____/\| (____/\| ) \ \__
(_______/(_______)|/    )_)   )_(   |/   \__/(_______)(_______/(_______/(_______/|/   \__/

===========================================================================================
___________ _____                                __   .__                     .__          
\_   _____//     \        ______ ___.__.  ____ _/  |_ |  |__    ____    ______|__|  ______ 
 |    __) /  \ /  \      /  ___/<   |  | /    \\   __\|  |  \ _/ __ \  /  ___/|  | /  ___/ 
 |     \ /    Y    \     \___ \  \___  ||   |  \|  |  |   Y  \\  ___/  \___ \ |  | \___ \  
 \___  / \____|__  /    /____  > / ____||___|  /|__|  |___|  / \___  >/____  >|__|/____  > 
     \/          \/          \/  \/          \/            \/      \/      \/          \/  
===========================================================================================


def tx7(algo, pattern: Union[int, str], iterator=None, 
        div:int = 1, rate:int = 1) -> midi._sysex:
    """
    Custom function for Rémi Georges. Allows the patterning of a Yamaha TX7.
    A pattern can be written for each and every declared Sysex parameter.
    """
    if isinstance(pattern, int):
        return tx7_params[algo](pattern)
    elif isinstance(pattern, str):
        return tx7_params[algo](int(Pat(pattern, i=iterator, div=div, rate=rate)))


tx7_params = {
        "Algorithme": lambda x: midi._sysex([67,16,1,6,(int(x)%31)-1]),
        "Feedback": lambda x: midi._sysex([67,16,1,7,(int(x)%7)-1]),
        # FreqCourse
        "FreqCourseOp1": lambda x: midi._sysex([67,16,0,123,int(x)%32]),
        "FreqCourseOp2": lambda x: midi._sysex([67,16,0,102,int(x)%32]),
        "FreqCourseOp3": lambda x: midi._sysex([67,16,0,60, int(x)%32]),
        "FreqCourseOp4": lambda x: midi._sysex([67,16,0,60, int(x)%32]),
        "FreqCourseOp5": lambda x: midi._sysex([67,16,0,39, int(x)%32]),
        "FreqCourseOp6": lambda x: midi._sysex([67,16,0,18, int(x)%32]),
        # FreqFine
        "FreqFineOp1": lambda x: midi._sysex([67,16,0,124,int(x)%127]),
        "FreqFineOp2": lambda x: midi._sysex([67,16,0,103,int(x)%127]),
        "FreqFineOp3": lambda x: midi._sysex([67,16,0,82, int(x)%127]),
        "FreqFineOp4": lambda x: midi._sysex([67,16,0,61, int(x)%127]),
        "FreqFineOp5": lambda x: midi._sysex([67,16,0,40, int(x)%127]),
        "FreqFineOp6": lambda x: midi._sysex([67,16,0,19, int(x)%127]),
        # Detune
        "DetuneOp1": lambda x: midi._sysex([67,16,0,125,int(x)%14]),
        "DetuneOp2": lambda x: midi._sysex([67,16,0,104,int(x)%14]),
        "DetuneOp3": lambda x: midi._sysex([67,16,0,83,int(x)%14]),
        "DetuneOp4": lambda x: midi._sysex([67,16,0,62,int(x)%14]),
        "DetuneOp5": lambda x: midi._sysex([67,16,0,41,int(x)%14]),
        "DetuneOp6": lambda x: midi._sysex([67,16,0,20,int(x)%14]),
        # Level
        "LevelOp1" : lambda x: midi._sysex([67,16,0,121,int(x)%99]),
        "LevelOp2" : lambda x: midi._sysex([67,16,0,100,int(x)%99]),
        "LevelOp3" : lambda x: midi._sysex([67,16,0,79,int(x)%99]),
        "LevelOp4" : lambda x: midi._sysex([67,16,0,58,int(x)%99]),
        "LevelOp5" : lambda x: midi._sysex([67,16,0,37,int(x)%99]),
        "LevelOp6" : lambda x: midi._sysex([67,16,0,16,int(x)%99]),
        # LFO
        "LFOWave":  lambda x: midi._sysex([67,16,1,14,int(x)%6]),
        "LFOSpeed": lambda x: midi._sysex([67,16,1,9,int(x)%99]),
        "LFODelay": lambda x: midi._sysex([67,16,1,10,int(x)%99]),
        "LFOPMD":   lambda x: midi._sysex([67,16,1,11,int(x)%99]),
        "LFOAMD":   lambda x: midi._sysex([67,16,1,12,int(x)%99]),
        "LFOSync":  lambda x: midi._sysex([67,16,1,12,int(x)%1]),
        "LFOPMS":   lambda x: midi._sysex([67,16,1,15,int(x)%5]),
        # Portamento
        "Retain/Follow"  : lambda x: midi._sysex([67,16,8,67,int(x)%1]),
        "GlissandoOffOn" : lambda x: midi._sysex([67,16,8,68,int(x)%1]),
        "Time"           : lambda x: midi._sysex([67,16,8,69,int(x)%99]),
        "Poly/Mono"      : lambda x: midi._sysex([67,16,8,64,int(x)%1]),
        #PitchENV
        "PitchEnvR1" : lambda x: midi._sysex([67,16,0,126,int(x)%127]),
        "PitchEnvL1" : lambda x: midi._sysex([67,16,0,127,int(x)%127]),
        "PitchEnvR2" : lambda x: midi._sysex([67,16,1,0,int(x)%127]),
        "PitchEnvL2" : lambda x: midi._sysex([67,16,1,1,int(x)%127]),
        "PitchEnvR3" : lambda x: midi._sysex([67,16,1,2,int(x)%127]),
        "PitchEnvL3" : lambda x: midi._sysex([67,16,1,3,int(x)%127]),
        "PitchEnvR4" : lambda x: midi._sysex([67,16,1,4,int(x)%127]),
        "PitchEnvL4" : lambda x: midi._sysex([67,16,1,5,int(x)%127]),
        #Op1ENV
        "Op1EnvR1" : lambda x: midi._sysex([67,16,0,105,int(x)%127]),
        "Op1EnvL1" : lambda x: midi._sysex([67,16,0,106,int(x)%127]),
        "Op1EnvR2" : lambda x: midi._sysex([67,16,0,107,int(x)%127]),
        "Op1EnvL2" : lambda x: midi._sysex([67,16,0,108,int(x)%127]),
        "Op1EnvR3" : lambda x: midi._sysex([67,16,0,109,int(x)%127]),
        "Op1EnvL3" : lambda x: midi._sysex([67,16,0,110,int(x)%127]),
        "Op1EnvR4" : lambda x: midi._sysex([67,16,0,111,int(x)%127]),
        "Op1EnvL4" : lambda x: midi._sysex([67,16,0,112,int(x)%127]),
        #Op2ENV
        "Op2EnvR1" : lambda x: midi._sysex([67,16,0,84,int(x)%127]),
        "Op2EnvL1" : lambda x: midi._sysex([67,16,0,85,int(x)%127]),
        "Op2EnvR2" : lambda x: midi._sysex([67,16,0,86,int(x)%127]),
        "Op2EnvL2" : lambda x: midi._sysex([67,16,0,87,int(x)%127]),
        "Op2EnvR3" : lambda x: midi._sysex([67,16,0,88,int(x)%127]),
        "Op2EnvL3" : lambda x: midi._sysex([67,16,0,89,int(x)%127]),
        "Op2EnvR4" : lambda x: midi._sysex([67,16,0,90,int(x)%127]),
        "Op2EnvL4" : lambda x: midi._sysex([67,16,0,91,int(x)%127]),
        #Op3ENV
        "Op3EnvR1" : lambda x: midi._sysex([67,16,0,63,int(x)%127]),
        "Op3EnvL1" : lambda x: midi._sysex([67,16,0,64,int(x)%127]),
        "Op3EnvR2" : lambda x: midi._sysex([67,16,0,65,int(x)%127]),
        "Op3EnvL2" : lambda x: midi._sysex([67,16,0,66,int(x)%127]),
        "Op3EnvR3" : lambda x: midi._sysex([67,16,0,67,int(x)%127]),
        "Op3EnvL3" : lambda x: midi._sysex([67,16,0,68,int(x)%127]),
        "Op3EnvR4" : lambda x: midi._sysex([67,16,0,69,int(x)%127]),
        "Op3EnvL4" : lambda x: midi._sysex([67,16,0,70,int(x)%127]),
        #Op4ENV
        "Op4EnvR1" : lambda x: midi._sysex([67,16,0,42,int(x)%127]),
        "Op4EnvL1" : lambda x: midi._sysex([67,16,0,43,int(x)%127]),
        "Op4EnvR2" : lambda x: midi._sysex([67,16,0,44,int(x)%127]),
        "Op4EnvL2" : lambda x: midi._sysex([67,16,0,45,int(x)%127]),
        "Op4EnvR3" : lambda x: midi._sysex([67,16,0,46,int(x)%127]),
        "Op4EnvL3" : lambda x: midi._sysex([67,16,0,47,int(x)%127]),
        "Op4EnvR4" : lambda x: midi._sysex([67,16,0,48,int(x)%127]),
        "Op4EnvL4" : lambda x: midi._sysex([67,16,0,49,int(x)%127]),
        #Op5ENV
        "Op5EnvR1" : lambda x: midi._sysex([67,16,0,21,int(x)%127]),
        "Op5EnvL1" : lambda x: midi._sysex([67,16,0,22,int(x)%127]),
        "Op5EnvR2" : lambda x: midi._sysex([67,16,0,23,int(x)%127]),
        "Op5EnvL2" : lambda x: midi._sysex([67,16,0,24,int(x)%127]),
        "Op5EnvR3" : lambda x: midi._sysex([67,16,0,25,int(x)%127]),
        "Op5EnvL3" : lambda x: midi._sysex([67,16,0,26,int(x)%127]),
        "Op5EnvR4" : lambda x: midi._sysex([67,16,0,27,int(x)%127]),
        "Op5EnvL4" : lambda x: midi._sysex([67,16,0,28,int(x)%127]),
        #Op6ENV
        "Op6EnvR1" : lambda x: midi._sysex([67,16,0,0,int(x)%1]),
        "Op6EnvL1" : lambda x: midi._sysex([67,16,0,1,int(x)%1]),
        "Op6EnvR2" : lambda x: midi._sysex([67,16,0,2,int(x)%1]),
        "Op6EnvL2" : lambda x: midi._sysex([67,16,0,3,int(x)%1]),
        "Op6EnvR3" : lambda x: midi._sysex([67,16,0,4,int(x)%1]),
        "Op6EnvL3" : lambda x: midi._sysex([67,16,0,5,int(x)%1]),
        "Op6EnvR4" : lambda x: midi._sysex([67,16,0,6,int(x)%1]),
        "Op6EnvL4" : lambda x: midi._sysex([67,16,0,7,int(x)%1]), 
}       

===========================================================================================

@swim
def algomedler(p=0.5, i=0, l=0):
    tx7("Algorithme",7+i%5)
    tx7("FreqCourseOp3",i%2)
    tx7("LevelOp5",25)
    tx7("FreqFineOp3",15+i%5)
    tx7("FreqFineOp4",5+l%20)
    tx7("FreqFineOp5",i%20)
    tx7("FreqFineOp6",l%2)
    tx7("FreqCourseOp2",10+i%10)
    tx7("FreqCourseOp6",l%2)
    again(algomedler, p=P("1!2,0.5!2,0.25!4",i), i=i+1, l=l+3)

@swim 
def tx7lead(p=0.5,i=0):
    dur =ZN("e 057 237 ^ 497 _ 451 9E2 s 9E2",dur=0.17, i=i)
    #tx7("Algorithme", P("1~8",i))
    tx7("LevelOp4", P("[1~18]",i))
    tx7("LevelOp5", P("[45~85]",i))
    tx7("FreqCourseOp4", P("[1~18]",i))
    tx7("Op4EnvL3", P("[1~118]",i))
    tx7("Op4EnvR3", P("[1~118]",i))
    tx7("Op4EnvR2", P("[1~118]",i))
    tx7("Op4EnvL2", P("[1~118]",i))
    #tx7("Op4EnvL4", P("[1~118]",i))
    #tx7("Op4EnvR4", P("[1~118]",i))
    dur2 = ZN("s ^ 4 5 1 2 4 5 8 9 7 45 6 1 2 7 5 4", dur=0.15, i=i)
    again(tx7lead,p=dur,i=i+1)

@die
def bouncer(p=0.5, i=0):
    tx7('Retain/Follow', 1,i)
    tx7('GlissandoOffOn', 1,i)
    tx7('Time', 40,i) #descendre pour plus de fun
    again(bouncer, p=0.5, i=i+1)

@swim
def algomedler(p=0.5, i=0, l=0):
    tx7("Algorithme",7+i%5)
    tx7("FreqCourseOp3",i%2)
    tx7("LevelOp5",25)
    tx7("FreqFineOp3",15+i%5)
    tx7("FreqFineOp4",5+l%20)
    tx7("FreqFineOp5",i%20)
    tx7("FreqFineOp6",l%2)
    tx7("FreqCourseOp2",10+i%10)
    tx7("FreqCourseOp6",l%2)
    again(algomedler, p=P("1!2,0.5!2,0.25!4",i), i=i+1, l=l+3)

===========================================================================================





























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
    #change2 = 5 if almostNever() else 0
    M(note=f'adisco(pal(G3@penta))+{change}', 
            #dur = 1000
            dur = 1000
            #dur = P("100~1000")
                        ).out(
                            i, 
                            div=
                            P("8!1,3!4,2!2",i),
                            #P("4,8",i), 
                            rate=1) #G3 #G4
    cc(channel=0, control=1, value=P('r*127',i))
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

Pn >> play_midi(note= ".,.,.,38,.,.", channel=9)

Pi >> play_midi(note = "42!7,46",channel=9)
Pi.div =1

Pb >> play_midi(note = "48,47,45,43,<48,47>,<47,46>", channel = 9)
Pb.div = 3
Pb.rate = 1

Pb >> None

hush()

Ps >> play_midi(note ="C5,.!40",channel=9) 

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
    #duration =300
    duration= "300!4,400!3,500!2,600"
    diviseur = 1
    ratte = 1
    #diviseur = 4 if rarely() else 1
    #ratte = 0.2 if rarely() else 0.5 
    #changer (1~1) en (1~2++) les hauteurs de LA et aussi les [1,(3~6] du dernier
    M(note="euclid(La6@hirajoshi&[0,(1~4)]^(-1),5,8)", dur=duration).out(i, div= diviseur, rate= ratte)
    #M(note="euclid(Lab3|La2@hirajoshi&[0,(1~4)]^(1~2),6,8)", dur=duration).out(i+2, div= diviseur, rate=ratte)
    M(note="euclid(La2@hirajoshi&[1,(3~6)]^(1~4),7,8)", dur=duration).out(i+1, div=diviseur, rate=ratte) 
    again(melodie, d=P(
        #'0.25,0.25,0.5,0.25',
        '0.5',
        i), i=i+1) 

#BIEN MAMUSER AVEC TOUS CES JOLIES PARAM avant de le tuer
hush()

c.bpm = 175

 

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
    M(note='F5 | F6 , .', dur=200).out(
    i,
    div=P('2,4,2,2'), rate= 1.2)
    #M(note='C3 | C4,.', dur=105).out(i, div= 2, speed =1.2)
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
