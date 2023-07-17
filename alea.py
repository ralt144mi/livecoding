#-------------------------------------------------------------
#------ooooo  oooooo oo   oooooo oo oo     oo     o   o oo----
#------oo  oo oo  oo oo     oo   oo oo oo  oo oo  oo oo oo----
#------ooooo  oooooo oo     oo   oo oooooo oooooo o o o oo----
#------oo  oo oo  oo oooooo oo   oo    oo     oo  o   o oo----
#-------------------------------------------------------------
#------10-DECEMBRE-2022-----ALEATRONOME------SAINT-ETIENNE----
#-------------------------------------------------------------
#----------------------------------------- <^[[[>< ------_____
#------------------------------------------------------_/-----
#Salut moi c'est Ralt144MI----------___---------------/-_-----
#----------------------------------[ooo]--------(---3)>[#]----
#-----------------------------------(-(-------)-)-(--|--------
#------------------------------------)-)----_-(-(-)-|---------
#------------------------------------------/-\)-)-(/----------

highlight Normal ctermbg=none
highlight NonText ctermbg=none

Or this:

highlight Normal guibg=none
highlight NonText guibg=none



= octave down
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

tx7_params = {
        "Algorithme": lambda x: midi._sysex([67,16,1,6,(int(x)%31)+1]),
        "Feedback": lambda x: midi._sysex([67,16,1,7,(int(x)%7)+1]),
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
        "Retain/Follow" : lambda x: midi._sysex([67,16,8,67,int(x)%1]),
        "GlissandoOffOn"          : lambda x: midi._sysex([67,16,8,68,int(x)%1]),
        "Time"                    : lambda x: midi._sysex([67,16,8,69,int(x)%99]),
        "Poly/Mono"               : lambda x: midi._sysex([67,16,8,64,int(x)%1]),
}


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

def E(step: int, maximum: int, index: int) -> bool:
    pattern = euclid(step, maximum)
    return True if pattern[index % len(pattern)] == 1 else False

def print_param(): 
    print(tx7_params.keys())

def print_scales():
    print(qualifiers.keys())

Pp >> tx7("Algorithme", 12)

c._midi_nudge = 0.5
#################

#OUBLIE PAS DE LINK LINK LINK LINK link

c.link()

c.unlink()

c.bpm = 150

c.bpm

Ph._div

####################################################
####################################################
####################################################

################################################################
################################################################
################################################################
################################################################
si soucis
dirt ahead 0.3 ?

Po >> d("leCASIO:[0,2,1,2,0,2,1,3]", #-8 #^[0~4]
        #speed ="[1, 2, 3, 4, 5]/[2~3]",
        p=0.5,
        #p = "0.5!7,0.25!2",
        gain = 1.1,
            #p = "[1:8]", #KIller
            #span = 8, #Killer
        legato = 1)

Po >> None

#RENTRER AU FADER C08EP
Pi >> n(note="[F2@maj,F2@hirajoshi]^[1~2]", #C08 EP
        p="[0.5!4,0.25]",
        dur = "[0.15]", 
        vel = 80,
        chan=1)

Pi >> None

#GRUSIN  RENTRER AU FADER
Pn >> n(note= ".,F2@hirajoshi^[(-2)~2]",
        vel=70,
        p="[0.25!3]*2")

Pn >> None



################MEDLERS###############
@swim #die
def tempomedler(p=0.5, i=0):
    if clock.tempo < 150 :
        clock.tempo = clock.tempo*1.02
    else :
        clock.tempo = 60
    again(tempomedler, p=0.5, i=i+1)

@swim
def algomedler(p=0.5, i=0):
    tx7("Algorithme",i)
    again(algomedler, p=0.5, i=i+1)

@swim 
def bouncer(p=0.5, i=0):
    tx7('Retain/Follow', 1,i)
    tx7('GlissandoOffOn', 1,i)
    tx7('Time', 100,i) #descendre pour plus de fun
    again(bouncer, p=0.5, i=i+1)


Pi >> None
Po >> None

Pn >> None

silence()

Pb >> d("morgan:0", begin ="r*0.8",
        legato = 4, p = "1,0.5", span = 4,
        bandf = 300, #300
        ) 

Ps >> d("morgan:0", 
        #scram = "r",
        legato = 4, begin = 0.425, 
        room= .4, cutoff = 4500, shape = 0.25,
        p=32
        #p="8!2,16!4"
        )

Pf >> d(".,morgan:1", 
        #scram = "r",
        legato = 4.5, begin = 0.430, 
        cutoff = 4500, hcutoff = 250,
        shape = 0.45,
        p=9
        #p="4.5"
        )

Pl >> d("long:[24~59]", p="2,1",
        legato = 0.5, pan = "r",
        scram = 0.2, gain = 0.9,
        room = .4
        )

#reduire les cutoff de Morgan
Ps >> None
Pf >> None



Pi >> d("long:42", p=4, 
        legato =2, gain = 0.8,
        speed = "2,1,0.5,0.25",
        room = .6
        )

PL >> d("long:45", 
        room = .4,
        p = 8,  
        legato =1)

PM >> d("long:40", p=0.25,
        span = 2, #1
        legato = 0.5)

clock.tempo = 135

Pl >> None
PL >> None
Pb >> None

silence()

dirt._ahead_amount = 0

Pk >> d("leKICK:2",
        span=1
        )

Pk >> None

#                  [x|.]       .5 
Ps >> d('.,laSNARE:6', span = 1,gain= 0.9, p=1)

Ph >> d("leHIHAT:$%5", cutoff = 6000, legato = 0.1, p=0.25)

#C15 DISCO BASS
Pn >> n(note="disco(E3@min7)^[1~2]",
        p="1,1,0.5,0.5,0.25,0.25,0.25,0.25",
        chan=1
        )

#SYNELECPNO CMB18
Pt >> n(note="pal(adisco(E4@min7)),<E4@min7>",
        p = ".5!3,1!2 ",
        chan=0
        )


silence()


####Po >> n(note="F2@maj, <F1@maj7>^[1~3]", 
        p = "[0.5!2, 0.125!2]*2", dur =0.15)

Po >> None

####Pi >> n(note="pal(F@maj7, <C@maj7>)", 
        p = "0.5!2, 0.125!3", dur = 0.2,
        vel = 60, chan=1)


Pn >> d("laPERC:10!2, laSNARE:12, laPERC:2",   
        p = "1,0.5",
        shape= 0.4 ,legato = 1, 
        span = 2, 
        #speed = "0.84,0.13,1,1" #"0.84,0.43,1,1"
        )

Ph >> d("leHIHAT:6", p=0.25, pan = "r",
        gain = .9)

D("ralt144mi,.!7", # accelerate = "1",
        enhance = .2, legato = 1.8)

silence()

Pi >> None

# C14 JOUER DELAY + C4
Pi >> n(note="disco(apal(G#3@maj, <C3@min7>))"
        , p = "0.5, 0.125"
                , span = 2 
        , chan = 1)

Pk >> d("leKICK:2!4",
        shape =0.4,
        legato = 0.2,
        #cutoff = 1000,
        resonance = 0.2,
        #p=8 #8
        p = 8, span =1
        )

Pc >> d(#"[.,.,laSNARE:4!2]!4",
        "[.,.,laSNARE:4!2]!3,[.,.,laSNARE:[r*16]!2]",
        p=1, accelerate= "0!12,0.5,0.75,0.80,1",
        span = 2)


Pc >> None



Pi >> None


###DOIT BIZAR
Pi >> d("son:[1]",
        speed = "euclid(([[1,2,3,4,5,6,7,8]/7]^[0.5~-1]),7,1)",
        shape = 0.5, gain =0.8,
        p="(0.125*r)!2", pan = "[1:7]",
        span = 1, 
        accelerate =1,
        legato=0.7)

clock.tempo = 152

silence()
i
#FINIT AVE CTRKN    A PUTAIN DE CASSETTE DE BLABLABLA

Pu >> d('juj:[r*150]')


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






