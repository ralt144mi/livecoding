#-------------------------------------------------------------
#------ooooo  oooooo oo   oooooo oo oo     oo     o   o oo----
#------oo  oo oo  oo oo     oo   oo oo oo  oo oo  oo oo oo----
#------ooooo  oooooo oo     oo   oo oooooo oooooo o o o oo----
#------oo  oo oo  oo oooooo oo   oo    oo     oo  o   o oo----
#-------------------------------------------------------------
#-------------------------------------------------------------
#----------------------------------------- <^[[[>< ------_____
#------------------------------------------------------_/-----
#Salut moi c'est Ralt144MI----------___---------------/-_-----
#----------------------------------[ooo]--------(---3)>[#]----
#-----------------------------------(-(-------)-)-(--|--------
#------------------------------------)-)----_-(-(-)-|---------
#------------------------------------------/-\)-)-(/----------

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

changing = 0

@swim
def changer(p=0.5,i=0):
    if changing < 12 :
        Pp >> tx7("Algorithme", changing)
        changing = changing +1
    else : changing = 1
    again(changer, p=0.5,i=i+1)


Pi >> n("64", dur = "0.2", velocity="20")

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
HI Im Ralt144MI, :)
################################################################
################################################################
################################################################
################################################################
si soucis
dirt ahead 0.3 ?

dirt._ahead_amount = 0.8

silence()

Po >> d("leCASIO:[0,2,1,2,0,2,1,3]", #-8 #^[0~4]
        speed ="[1, 2, 3, 4, 5]/[2~3]",
        p="0.50!4",
        gain = 1.1,
            #p = "[1:8]", #KIller
            #span = 8, #Killer
        span = 2,
        legato = 1)

Po >> None

#MODEL ACID BASS RIGHT EAR


@die
def labass(p=0.5, i=0):
    N(
            "bass(F3@maj7)^[1~2]",
            #"adisco(F3@maj7)^[1~2]",
            #"disco(F3@maj7)^[1~2]",
            #"pal(F3@maj7)^[2~3]",
            vel = '[45~85]',
            dur = 0.5,
            chan = 0,
            d="0.5!3,0.25!2",
            i=i,
            r=0.25/2
            )
    again(labass,p=P("0.5!3,0.3333!3",i),i=i+1)


from random import choice

#GRUSIN  ENSUIT AUG

@swim 
def ziffattack(p=0.5, i=0):
    ZN("1.5 _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [7 5]] _ ([024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [7 5]]) _ _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ [7 5]] _ [024 _ [4 7]] _ [057 _ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [7 5]] _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [(7 5 3)-2]] _ _ [024 _ _ [ 5 2 ] _ ] [027 ^ ^ [7 5]]",
    scale = choice(["rocritonic", "pentatonic", "chromatic"]),
    key = choice(["Db","Fs","Db","E"]),
    dur = choice([0.5,0.25,0.5,0.25]),
    i=i)
    again(ziffattack, p=choice([0.25,choice([0.5,0.25])]), i=i+1)

silence()

Pn >> zn("1.5 _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [7 5]] _ ([024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [7 5]]) _ _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ [7 5]] _ [024 _ [4 7]] _ [057 _ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [7 5]] _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [(7 5 3)-2]] _ _ [024 _ _ [ 5 2 ] _ ] [027 ^ ^ [7 5]]", scale = choice(["rocritonic", "pentatonic"]), key = "Db")

Pn >> None

#mute CASIOTIME

silence()

duree =0.1
Pa >> zn('2.0 035 1.0 027 2.0 047 017',
        dur =duree*1.5,
        scale="rocritonic", key="Db", vel = 1)
Pi >> zn('<0.25 0.5> 0..12', vel = 5,dur = duree,scale="rocritonic", key="Db")

Pk >> tx7('FreqCourseOp1', P("12,85,45,125"))

Pn >> tx7('Algorithme', P("1,5,8"))


Pb >> zd('sid:4', '0 0 0 2 w 8 8 q 8 8 0.75 4  0.25 4  0.75 4 0.25 4', 
         room=0.8, size=0.8, dry=0.4, scale="mixolydian", key="Db")
Pc >> d('sid:2!2, sid:4, sid:5~8', p=0.5, orbit=0)
Pd >> d('sid:10~20', p=0.25, legato=0.2, amp='0.3|0', orbit=0, speed='1!10,2!2')

Po >> None

silence()

################MEDLERS###############
@die
def tempomedler(p=0.5, i = 0):
    if clock.tempo < 150 :
        clock.tempo = clock.tempo*1.02
        clock.tempo = 60
    again(tempomedler, p=0.5, i=i+1)

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

@die
def bouncer(p=0.5, i=0):
    tx7('Retain/Follow', 1,i)
    tx7('GlissandoOffOn', 1,i)
    tx7('Time', 40,i) #descendre pour plus de fun
    again(bouncer, p=0.5, i=i+1)



Pk >> d("leKICK:4,laSNARE")

Pi >> None
Po >> None

Pk >> None

silence()

Pb >> d("morgan:0", begin ="r*0.8",
        legato = 4, p = "1,0.5", span = 4,
        bandf = 300, #300
        ) 

Ps >> d("morgan:0", 
        scram = "r",
        legato = 4, begin = 0.425, 
        room= .4, cutoff = 4500, shape = 0.25,
        p=32
        #p="8!2,16!4"
        )

Pf >> d(".,morgan:1", 
        scram = "r",
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

Pn >> None

PM >> d("long:40", p=0.25,
        span = 2, #1
        legato = 0.5)

clock.tempo = 135

Pl >> None
PL >> None
Pb >> None

silence()

dirt._ahead_amount = 0.20


Pk >> d("leKICK:2",
        p="0.5!4",
        span=4
        )

Pk >> None

#                  [x|.]       .5 
Ps >> d('.,laSNARE:6', span = 1,gain= 0.9, p=1)

Ph >> d("leHIHAT:$%5", cutoff = 6000, legato = 0.1, p=0.25)

#C15 DISCO BASS
Pn >> n(note="pal(disco(E4@min7))^[1~3]",
        p="1,1,0.5,0.5,0.25,0.25,0.25,0.25",
        span = 4, dur = 0.1,
        chan="1"
        )

Pn >> None
#SYNELECPNO CMB18
Pt >> n(note="pal(adisco(E4@min7)),<E4@min7>",
        p = "[1!3,0.5!2]",
        span = 2,
        chan=0, dur = 0.1
        )

Pt >> None


silence()

Pn >> d("laPERC:10!2, laSNARE:12, laPERC:2",   
        p = "1,0.5",
        shape= 0.4 ,legato = 1, 
        span = 2, 
        #speed = "0.84,0.13,1,1" #"0.84,0.43,1,1"
        )

#mets le vocode

Ph >> d("leHIHAT:6", p=0.25, pan = "r",
        gain = .9)

D("ralt144mi,.!7", accelerate = "1",
        gain = 1.2,enhance = .2, legato = 2)

silence()

Pi >> None

Pi >> n(note = "[<F'@maj>!2,<C'@maj>!8]", p=0.5,
        span= 2,
        chan = 1)


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
        span = 1)


Pc >> None



Pi >> None



silence()
###DOIT BIZAR
Pi >> d("son:[1]",
        speed = "euclid(([[1,2,3,4,5,6,7,8]/7]^[0.5~-1]),7,1)",
        shape = 0.5, gain =0.8,
        p="(0.125*r)!2", pan = "[1:7]",
        span = 1, 
        accelerate =1,
        legato=0.7)

clock.tempo = 152

#VIBRATIME ORGANTIME VIDEOTIME

Pu >> n("euclid(<C3,E3,C4,E4>!8,5,8)",
        p = "0.25",
        vel = 65, span  = 0.5,
        chan = "0", dur = 0.25)

Pi >> None

n("apal(disco(F2@maj7))^[(1)~5]",
        vel=65,p="0.5!7,0.25!2",
        span = 4,
        #chan = "15,0,1,2",
        chan="0",
        dur = 0.15)

Pa >> None

Pa >> n("euclid(<E7>!8,3,5,2)",
        p = "0.125",
        vel = 85, span  = 0.5,
        chan = "0", dur = 0.25)

silence()


Pk >> d("leKICK:2!4",
        shape =0.4,
        legato = 0.2,
        #cutoff = 1000,
        resonance = 0.2,
        #p=8 #8
        p = 8, span =1
        )

Pk >> None

Pk >> d("leKICK:2!4",
        shape =0.4,
        legato = 0.2,
        #cutoff = 1000,
        resonance = 0.2,
        #p=8 #8
        p = 8, span =1
        )

