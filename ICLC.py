'██            ██    ▄   
▄▄▄  ▄▄ ▄▄▄   ▄▄▄  ▄██▄  
 ██   ██  ██   ██   ██   
 ██   ██  ██   ██   ██   
▄██▄ ▄██▄ ██▄ ▄██▄  ▀█▄▀ 
'                         
                         
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
from random import random
from random import choice
from art import text2art
center = 1/3+0.03
anticenter = 2/3+0.23

listener = OSCInHandler(
        ip="localhost",
        port=4445,
        name="Listener",
        loop=osc_loop
        )

bowl.add_handler(listener)

listener.watch(
        '/roue')

def get_roue_value():
       roue_raw = listener.get('/roue')
       roue = roue_raw['args'][0]
       return 0 if roue is None else roue

@swim
def listen(p=0.5,i=1):
    roue = get_roue_value()
    D("numbers:rand*8 .!8", pan = roue, i=i)
    again(listen, p=0.125,i=i+1)

panic()

'j ai l habitude de faire des live sur une thématique  
▀██▀▀█▄ aquatique ▀██    ▄ utilisant▄ des▄  ▀██    ██▀ ▀██▀ 
 ██   ██   ▄▄▄▄    ██  ▄██▄   ██   ██   ██   ███  ███   ██  
 ██▀▀█▀   ▀▀ ▄██   ██   ██   ███  █ █  █ █   █▀█▄▄▀██   ██  
 ██   █▄  ▄█▀ ██   ██   ██    ██  █▄█▄ █▄█▄  █ ▀█▀ ██   ██  
▄██▄  ▀█▀ ▀█▄▄▀█▀ ▄██▄  ▀█▄▀  ██  ████ ████ ▄█▄ █ ▄██▄ ▄██▄ 
images sous-marines provenant ██    █    █ d un stock de                 
vidéos familiales. Ce soir   ▀▀▀▀  ███  ███ ce live sera un
peu différent. Les images sous-marines seront toujours 
 ███ quelque-part évoluant dans un██  ▀██ coin de la salle.   ▄▄▄▄ 
██ ██    ▄▄▄▄   ▄▄▄▄ ▄▄▄ ▄▄▄ ▄▄  ▄▄▄   ██      ██   ███   ██  ▀ ██ 
 █ █ ce ▀▀ ▄██   ▀█▄  █   ██▀ ▀▀  ██   ██     █  █ ██ ██ █  █  ██  
 ███    ▄█▀ ██    ▀█▄█    ██ soir ██   ██       ██ ██ ██   ██  ██  
██ ██   ▀█▄▄▀█▀    ▀█    ▄██▄    ▄██▄ ▄██▄     ██  ██ ██  ██    ██ 
██ ██ j ai prévu différentes musiques, des    ██   ██ ██ ██    ██  
 ███ musiques pour faire danser le corps et   █▄▄▄  ▀█▀  █▄▄▄ █▀   
d autres pour faire danser l esprit. il y aura aussi des happenings
 ▄▄█▀▀▀▄█  ▀██▀▀█▄   ▀██▀▀█▄   ▀██▀▀█▄   ▀█▄   ▀█▀ ▀██▀▀█▄   
▄█▀ et  ▀   ██   ██   ██   ██   ██   ██   █▀█   █   ██   ██  
██ des▄▄▄▄  ██▀▀█▀    ██▀▀█▀    ██▀▀█▀    █ ▀█▄ █   ██    ██ 
▀█▄    ██   ██   █▄   ██   █▄   ██   █▄   █   ███   ██    ██ 
 ▀▀█▄▄▄▀█  ▄██▄  ▀█▀ ▄██▄  ▀█▀ ▄██▄  ▀█▀ ▄█▄   ▀█  ▄██▄▄▄█▀  
hommages. J espère que vous allez appriecier :) 
█▀▀▀▀▀██  ▀██▀▀▀▀█  ▀██▀▀█▄ je ▄▄█▀▀██ remercie Raph bubo pour
    ▄█▀    ██  ▄ son ██   ██  ▄█▀    ██ aide pour cet évènement 
   ██  je  ██▀▀█ re  ██▀▀█▀   ██mercie██ Rose pour son soutien.
 ▄█▀ je re ██ mercie ██   █▄  ▀█▄tous ██ les artistes pour leur
██▄▄▄▄▄▄█ ▄██▄▄▄▄▄█ ▄██▄  ▀█▀  ▀▀█▄▄▄█▀  dévouement et 
JE vous remercie tous de votre présence ici ce soir.
'






'            
 ▄█     ▄▀▀ ▀█▀ ▄▀▄ █▀▄ ▀█▀ ██▀ █▀▄
  █ ▄   ▄██  █  █▀█ █▀▄  █  █▄▄ █▀▄                                            
'                                                   

clock.tempo = 142

@swim
def starter(p=0.5,i=1):
    D("long:0", leg=0.2, pan="rand", room="[0.1~0.5]", sz ="[0.2~0.8]")
    #D("(if(every 2) long:0 long:2)", pan="rand", leg=0.2, speed = "(if(every 2) 1 1.6)",i=i)
    again(starter, p=0.25, i=i+1)

Pk >> d("leKICK:4",
        #shape=0.25,
        #octersub = 0.8
        pan = center
        )

Ps >> d(#"laSNARE:3",
        "laSNARE:[2~9]",
        euclid = (1,5), #(5,5)
        room=0.25,
        leg= 0.1,
        pan="rand",
        p=0.25
        )

Pi >> d("numbers:[0~10]", p=2, #0.5
        leg=0.9, pan = "0.25|0.75")

Pb >> d("jungbass",
        note="0 5 3 0",
        #note="0 5 3 079E",
        #p=0.5, gain=1,
        euclid = (5,5,3), #5
        pan=center)

Pk>> None
Ps >> None
Pi >> None

Pb >> None

'
 █   ██▀   ▀█▀ █▀▄ ▄▀▄ █▄ ▄█ ██▄ ▄▀▄ █▄ █ ██▀
 █▄▄ █▄▄    █  █▀▄ ▀▄▀ █ ▀ █ █▄█ ▀▄▀ █ ▀█ █▄▄

 ▄▀▄ █ █ █   █▀▄ ▄▀▄ █▀▄ █   ██▀
 ▀▄█ ▀▄█ █   █▀  █▀█ █▀▄ █▄▄ █▄▄
'

Po >> d(". trombone:145", p=0.5,#p="0.5 1 0.5",
        leg="[0.15~0.5]"*10,
        #phaserdepth=0.85,phaserrate=0.9,
        #vowel="a e i o u a i e o u e a", accelerate = "0.1 0.2 0.6 -1 -2 0.8",
        shape=0.3,
        pan=center)

Po >> None

Pk >> d("leKICK:10 laSNARE:10 laSNARE:10",
        pan=center)

Ph >> d("leHIHAT:10!6", p=0.5,
        pan="rand")

Pk >> None
Ph >> None

##########LECTEUR K7 ??



starter.stop()
//////

silence()

'
 █▄ ▄█ ▄▀▄ █▄ █   ▄▀▄ █▀▄ █▀▄ █
 █ ▀ █ ▀▄▀ █ ▀█   ▀▄▀ █▀▄ █▄▀ █
 ██▀ ▄▀▀ ▀█▀   ▄▀▄ █▄ ▄█ ▄▀▄ █ █ █▀▄ ██▀ █ █ ▀▄▀
 █▄▄ ▄██  █    █▀█ █ ▀ █ ▀▄▀ ▀▄█ █▀▄ █▄▄ ▀▄█ █ █
'

clock.tempo = 144

Pr >> d("sid:0 . .", shape = 0.5, p=0.5, div= 2,
        pan=center
        )

Pu >> d("sid:2", 
        euclid=(3,3,1), 
        shape=0.65,
        pan = anticenter)

Pd >> zd("braids", "s 9 8 7" , model = "25*rand", #25*rand
        color=0.55, timbre = 0.1, 
        leg=0.25, scale="rocritonic", pan=center)


Ph >> d("sid:[7~9]",
        pan = "(if(every 4) r 2/3+0.23)",
        shape = "(if(beat 3 4) 0.5 0.1)",
        euclid=(7,8,4),
        p=0.5)

##########PAD A TROUVER

Pp >> zn("w r 09E", scale = "rocritonic", channel = 0, dur=3)

##########Break

Pu >> None 
Pr >> None

@swim #die
def tempomedler(p=0.5, i=0):
    if clock.tempo < 190 :
        clock.tempo = clock.tempo*1.009
    else :
        clock.tempo = 122
    print(text2art("try to dance on that","straight"))
    again(tempomedler, p=0.5, i=i+1)

'
 █ █ █▄ █   ▄▀▄ █▀▄ █▀▄ █
 ▀▄█ █ ▀█   ▀▄▀ █▀▄ █▄▀ █

 ██▀ ▄▀▀ ▀█▀   █ █ █▄ █ ██▀  
 █▄▄ ▄██  █    ▀▄█ █ ▀█ █▄▄  

 ▄▀  █▀▄ ▄▀▄ ▄▀▀ ▄▀▀ ██▀
 ▀▄█ █▀▄ ▀▄▀ ▄██ ▄██ █▄▄

 ▄▀▀ ▄▀▄ █   ▄▀▀ █ █ █   ██▀ ▀█▀ ▀█▀ ██▀
 ▀▄▄ █▀█ █▄▄ ▀▄▄ ▀▄█ █▄▄ █▄▄  █   █  █▄▄

 ▄▀▀ ▄▀▄ ▄▀▀ █ ▄▀▄
 ▀▄▄ █▀█ ▄██ █ ▀▄▀
'

silence()
clock.tempo = 134

Ph>> d("casio:2", leg=0.1, p=0.5, euclid=(2,3), pan = 0,
        #scram=0.5
        )

Ps >> d("casio:0", leg=0.1, p=0.5, euclid=(2,3,1), pan = 0.25,
        #scram = 0.5
        )

Pp>> d("casio:1", leg=0.1, p=0.5, euclid=(2,3,2), pan = 0.5,
        #scram =0.25
        )

Pz >> d(". casio:2", leg=0.1, p=0.5, euclid=(2,3), pan = 0.75,
        #scram =2
        )

Pk >> d(
        "sid:2 sid:[0~8]",
        #"sid:0",
        #octersub = 1.2, 
        shape=0.4,
        pan="2/3+0.25 1/3+0.03",
        leg=0.15,
        p="0.5!8"
        )

Pk >> None

PA >> zd("braids",
        "e _ 0 5 6 e 7 0 8 7 5 9 | e 0 5 6 7 5 1 6 3 0" #modifie cela Rémi
        , scale = "rocritonic",
        lpf = 9000,
        model= 5,# accelerate=0.05, #0.5
        color = "[0.9~0.2]", # scram=0.26,
        timbre = "[0.2~0.8]", leg=0.25,
        pan = center
        #lpf="[6500..500]", res=0.6
        )

#SCRAM TOUT a la fin

###############SOLO DE CASIOTONE##################
#sans leKICK

#fade out

Pk >> None
PA >> None
Pz >> None
Pp >> None
Ph >> None
Ps >> None

'
 ▀█▀ █ █ ▀█▀   █▀▄ █ █▀▄   ██▄ ▄▀▄ █▀▄
  █  ▀▄█  █    █▀  █ █▀    █▄█ ▀▄▀ █▀ 
'

Pl >> d("long:40 long:41 long:40 long:[40~44]", 
        speed = "0.5!7 0.7", pan="rand", shape=.25,
        leg=0.5)

PA >> zd("braids", "_ _ e 4 2 4 3" ,
        model= 8, accelerate=0.05, #0.5
        color = "[0.9~0.2]", 
        timbre = "[0.2~0.8]", leg=0.25,
        #lpf="[6500..500]", res=0.6
        pan=center,
        )
PA >> None


Pk >> d("leKICK . . . leKICK:4 . .", shape=0.5, p=0.5,
        pan=center)

Pk >> d("leKICK laSNARE:8 leHIHAT leHIHAT leKICK:4 leHIHAT leHIHAT", shape=0.5, p=0.5, 
        pan=center)

Pk >> None

@swim(until=25)
def croa(p=0.5, i=0):
    D("maloya",
    begin=0.2,
    #begin=0.25,
    #begin = "0.5 0.25 1 0 0.1",
    leg=0.20, 
    #leg = "0.20 0.1 0.25 0.1",
    #pan="0.25 0.17 0.33",
    pan=0.25,
    shape=0.2,
    i=i)
    again(croa, p=P("0.5",i), i=i+1)

Pk >> d("leKICK:4", p=1, pan=center)

PA >> None

####rythmique à TROUVER
'
 ▄▀▄ █   ▄▀  ▄▀▄   █▄▀ ▄▀▄ █▀▄ ▄▀▄ ▄▀▄ █▄▀ ██▀
 █▀█ █▄▄ ▀▄█ ▀▄▀   █ █ █▀█ █▀▄ █▀█ ▀▄▀ █ █ █▄▄
'

silence()

def drunk(text: str=" ", i: int=0, dry: float=0.5):
    done = text.split()
    done2 = text.split()
    wet_or_dry = random() >= dry 
    randomtrue = random() >= 0.5
    if wet_or_dry:
        return done[i % len(done)]
    else:
        if randomtrue:
            i=i-2
        else:
            i=i
        return done2[i % len(done2)]
        

montexte = join("C'est une maison remplie de poissons Une Maison remplie de poissons,",
                "il y a des poissons de partout de partout il y a des poissons une maison",
                "remplie de poissons c'est ca deborde de poissons a la fenetre on ne peut",
                "plus rien voir il y a trop de poissons une maison remplie de poissons plus",
                "personne ne peut rentrer a linterieur il y a trop de poissons",
                "trop de poissons dans la maison remplie de poissons")

montexte = join("C'est une maison remplie de poissons Une Maison remplie de poissons,",
                "il y a des poissons de partout de partout il y a des poissons une maison",
                "remplie de poissons c'est ca deborde de poissons a la fenetre on ne peut",
                "plus rien voir il y a trop de poissons une maison remplie de poissons plus",
                "personne ne peut rentrer a linterieur il y a trop de poissons",
                "trop de poissons dans la maison remplie de poissons")



@swim
def drunktext(p=0.5, i=0):
    dur=ZN("h _ 0 5 0 7 ^ q 7 05 07 03", channel = 2, i=i)#ms2000
    #CC(channel = 2 , control = 65, value=P("[50~127]",i)) #PORTAMENTO
    print(text2art(drunk(montexte, i,P("0.1 0.2 0.5 0.7 0.8",i)), font="small"))
    again(drunktext,p=dur,i=i+1)

Pr >> d("(eu leKICK:2 2 3)", pan=center)
Pi >> d("(eu laSNARE:4 2 3 4)", pan=center)


@swim 
def tx7lead(p=0.5,i=0):
    dur =ZN("e 057 237 ^ 497 _ 451 9E2 s 9E2",dur=0.17, i=i)
    tx7("Algorithme", P("1~8",i))
    #tx7("LevelOp4", P("[1~18]",i))
    #tx7("LevelOp5", P("[45~85]",i))
    #tx7("FreqCourseOp4", P("[1~18]",i))
    #tx7("Op4EnvL3", P("[1~118]",i))
    #tx7("Op4EnvR3", P("[1~118]",i))
    tx7("Op4EnvR2", P("[1~118]",i))
    tx7("Op4EnvL2", P("[1~118]",i))
    tx7("Op4EnvL4", P("[1~118]",i))
    tx7("Op4EnvR4", P("[1~118]",i))
    dur2 = ZN("s ^ 4 5 1 2 4 5 8 9 7 45 6 1 2 7 5 4", dur=0.15, i=i)
    again(tx7lead,p=dur,i=i+1)

'
 █▄ █ ██▀ █ █ ██▀ █▀▄ ▄▀▀
 █ ▀█ █▄▄ ▀▄▀ █▄▄ █▀▄ ▄██
'

clock.tempo = 187.5

#Lecteur K7 Part

Pi >> d(". nevers:1", loaf=4, on=(1,2), leg=1, pan="0", p=1, gain=0.9)

Pn >> d("nevers:1 .", begin=0.5, pan="0.5", leg=1, p=2, gain=0.9)

#APRES
Py >> d(". nevers:1 .", begin=0.8, pan="rand", leg=1, p=2, shape=0.4)

clock.tempo

#2 3 4 15

Pm >> d("long:15", leg=0.15, pan="rand", p=0.5)

Py >> None

Pk >> d("protokick", lpf=500, #800
        #binshift=3.5,#1.5 2.5 3.5
        #p="2 2 2 1 1", #alafin
        shape=0.45,
        euclid = (6,6), #1 2 3
        pan = 0.25        
        )

Ps >> d(#"laSNARE:3",
        "laSNARE:[2~9]",
        euclid = (3,5,3), #(5,5)
        room=0.25,
        leg= 0.1,
        pan="rand",
        p=0.5
        )

TROUVER SURAIGU ENTRAINANT


Pk >> None
Ps >> None

Pi >> None
Pn >> None 
Py >> None
Pm >> None

PASSER SUR DU SOLO

silence()

'
 █▄█ ▄▀▄ █▄ ▄█ █▄ ▄█ ▄▀▄ ▄▀  ██▀   ▄▀▄
 █ █ ▀▄▀ █ ▀ █ █ ▀ █ █▀█ ▀▄█ █▄▄   █▀█

 █▄ ▄█ ▄▀▄   █▄ ▄█ ▄▀▄ █▄ █ ▀█▀ ▄▀▄ ▄▀  █▄ █ ██▀
 █ ▀ █ █▀█   █ ▀ █ ▀▄▀ █ ▀█  █  █▀█ ▀▄█ █ ▀█ █▄▄

 █▀▄ █▀▄ ██▀ █▀ ██▀ █▀▄ ██▀ ██▀
 █▀  █▀▄ █▄▄ █▀ █▄▄ █▀▄ █▄▄ █▄▄
'

ferrat = "| h 0 e r _ 0 q 4  | h _ 5 r | \
| h 0 e r _ 0 2 4  | h _ 5 e r _ 5 q ^ 5 | \
| h 1 e r _ 1 3 5  | h 1 r | \
| h 1 e r _ 1 4 6  | h 0 e r _ 0 q 4  | h 0 r | \
| h 0 r  | h _ 5 e r 0 2 5 | \
| h _4_6 e r __ 2 q ^ 6  | h 0 e r _ 0 3 5 | \
| h _ 6 e r _ 4 q ^6^^1  | h 1 e r __ 4 q ^ 6  | h _ 4 e r 0 q ^ 0 | \
| h 0 r  |"
ferrat2 = "| h _0_2_4 q r _0_2  | h _0_2 r | \
| h _0_2_4 r  | h __5_0_2 q r _0_2 | \
| h _1_3_5 r  | h _1_4_6 r | \
| h _1_4_6 r  | h _0_2_4 q r _0_2  | h _0_2_4 r | \
| h __5_0_2_5 r  | h _0_2 r | \
| h __2__6_2 q r __6_2_4  | h _0_3_5 r | \
| h __4_1_4 q r __4_1_4  | h _1_4_6 q r _1_4  | h _0_2 q r _0_2_4 | \
| h _0_2_4 r  |"
ferrat3 ="| q. ___ 0 e 0 q. 0 e 0  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 0 e 0 q. 0 e 0  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 1 e 1 q. 1 e 1  | q. ___ 4 e 4 q. 4 e 4 | \
| q. ___ 4 e 4 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 5 e 5 q. 5 e 5  | q. ___ 5 e 5 q. 5 e 5 | \
| q. ___ 2 e 2 q. 2 e 2  | q. ___ 3 e 3 q. 3 e 3 | \
| q. ___ 4 e 4 q. 4 e 4  | q. ___ 4 e 4 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 0 e 0 q. 0 e 0  |"
ferrat4 = "| e r _ 4 4 4 4 4 s r 4 t r s. 4  | q r  e _ 5 t r 5 s r 5 r e 5 5 ^ 0 _ 5 | \
| e. _ 4  s 4 t r  t 4 t r s 4 q 4 e r 4 4  | h _ 5 5 | \
| e r  e _ 3 s r 3 t r s. 3 e 3 3 3 s r e. 3  | q r  e _ 4 t r  t 4 t r e 4 4 4 4 4 | \
| q _ 6 e r s r 4 h r  | w _ 2  | e r 0 0 0 0  e 0 s 1 e 1 | \
| q 2 r h r  | q 0  e 0 s r 0 t r s. 0 s 0 t r s. 0 e _ 6 ^ 0 | \
| h _ 6 6  | e r _ 5 r s 5 5 e r 5 5 | \
| q _ 6 6 6 e 6 6 6 6  | e 1  e 1 s r e 1 1 1 1 1 2  | h 1  | "
ferrat5 = "| h 0 r  | h _ 6 e r 1 4 6  | h 2 e r __ 2 q ^^ 2 | \
| h 2 e r _ 2 4 6  | e _1_3_51 __ 1 ^ 1 ^ 1 q _ 6 e 1 4  | e _ 4 0 0 2 q ^ 0 e _ 2 4 | \
| h _ 5 e r _ 3 q ^0^3^5  | h __6_2_4_6 r | \
| q _3_5 e r _1_3_51 q _4_6 e _ 1 4  | h _ 4 e r r r r  |"
ferrat6 = "| h _0_3_5 r  | h _1_4 r  | h _2_4_6 q r _2_4_6 | \
| h _2_4_6 r  | q __ 1 e r ^1^3^5 q ^1^4 r  | q _0_2 r _2_4_#5 r | \
| h _0_3 q r __ 3  | h __ 2 r | \
| e _ 1 _ 1 ^ 1 _ 1 q ^ 1 r  | h _0_2 r  |"
ferrat7 = "| q. ___ 3 e 3 q. 3 e 3  | q. ___ 3 e 3 q. 3 e 3  | q. ___ 2 e 2 q. 2 e 2 | \
| q. ___ 2 e 2 q. 2 e 2  | q. ___ 1 e 1 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0 | \
| q. ___ 3 e 3 q. 3 e 3  | q. ___ 2 e 2 q. 2 e 2 | \
| q. ___ 1 e 1 q. 4 e 4  | q. ___ 0 e 0 q. 0 e 0  |"
ferrat8 ="|   | w. _ 5 e ^ 0 1 1 _ 6  | h. _ 4 q r | \
| w r  | q. _ 3 e ^ 0 _ 6 5 6 4  |  | \
| w _ 2 e 5 3 4 5 6 ^ 0 1  | h 2  | \
| h _ 6  e 5 t r  t 5 t r s r e 6 6 5 4  | w 0 q. r |" 



clock.tempo=120

panic()

Pa>> None
Pb >> None
Pc >> None
Pd >> None
def lead():
    Pa >> zd("braids",ferrat , pan = 0.5, channel = 0, dur=0.3)
    Pb >> zd("braids",ferrat2, pan = 0.25, channel = 0, dur=0.5)
    Pc >> zd("braids",ferrat3, pan = anticenter, model = 1, channel = 0, dur=0.25)
    Pd >> zd("braids",ferrat4, pan = center, channel = 0, dur=0.8)
lead()

clock.tempo = 160 #160

Ps >> None

Pk >> d("leKICK:5", shape = 0.25, pan=center,  lpf = 500)

Pk >> d("leKICK:5!15 protokick", pan=center,  lpf = 500)

Pk >> d("protokick", shape = 0.25, pan=center,  lpf = 500)

Ps >> d("[amencutup:[1~12]!!2]!!4",p=0.5,
        phaserrate=0.8,phasdp=0.8,
        pan=anticenter, shape=0.55)

PS >> d("[sid:[1~12]!!2]!!4",p=0.5,
        phaserrate=0.8,phasdp=0.8,
        pan=center, shape=0.55)

Pa >> None #POURTANT QUE LA MONTAGNE
Pb >> None #EST BELLE COMMENT PEUT ON
Pc >> None #SIMAGINER EN VOYANT UN 
Pd >> None #VOL DHIRONDELLE QUE LOTOMNE VIENT DARRIV2R !!!!!!
def lead():
    Pa >> zd("braids",ferrat5, pan = 0.5, channel = 0, dur=0.3)
    Pb >> zd("braids",ferrat6, pan = 0.25, channel = 0, dur=0.5)
    Pc >> zd("braids",ferrat7, pan = center, model = 1, channel = 0, dur=0.25)
    Pd >> zd("braids",ferrat8, pan = center,# accelerate=0.05,# scram=0.2,
            channel = 0, dur=0.8)
lead()

Pk >> None
Ps >> None

PS >> None

silence()

'
 ▄▀▀ ██▀ █ █ █     ▄▀▄   █▄ █ ▄▀▄ ██▀ █  
 ▄██ █▄▄ ▀▄█ █▄▄   █▀█   █ ▀█ ▀▄▀ █▄▄ █▄▄
'

from random import choice

@swim 
def ziffattack(p=0.5, i=0):
    ZN("1.5 _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]] _ _ ([024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]]) _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]] _ [024 _ [4 7]] _ [057 ^ ^ [7 5 3]] _ _ [024 ^ ^ [ 5 2 ] _ _ ] [027 ^ ^ [7 5]] _ _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [(7 5 3)-2]] _ _ [024 _ [ 5 2 ] _ ] [027 ^ ^ [7 5]]",
    scale = choice(["pentatonic", "maj"]),
    key = choice(["Fs","C","A"]),i=i)
    again(ziffattack, p=choice([0.25,choice([0.5,0.25])])*4, i=i+1)


Pk >> d("(eu leKICK:[0~25] 3 7 )", p=0.5, pan =center)

D("ralt144mi .!7", accelerate = "1",
        pan = center,
        gain = 1.4,enhance = .2, legato = 2)


silence()

Pi >> None

Pi >> n(note = "[{F'@maj}!2 {C'@maj}!8]", p=0.5, # 0.25
        span= 2,
        chan = 0)


Pk >> d("leKICK:2!4",
        shape =0.4,
        legato = 0.2,
        #cutoff = 1000,
        resonance = 0.2,
        #p=8 #8
        p = 8, span =1,
        pan=center
        )

Pc >> d(#"[. . laSNARE:4!2]!4",
        "[. . laSNARE:4!2]!3 [. . laSNARE:[16]!2]",
        p=1, accelerate= "0!12 0.5 0.75 0.80 1",
        span = 1,
        pan="rand")

###DOIT BIZAR
PI >> d("son:1",
        shape = 0.5, gain =0.8,
       #p="(0.125*rand)!2",
        pan = anticenter,
        span = 2,
        #accelerate =1,
        legato=0.7)

'
 ____  ___   _   _  _  __
|_  / / _ \ | | | || |/ /
 / / | (_) || |_| ||   <
/___| \___/  \___/ |_|\_\
'


silence()
clock.tempo = 136

kassav1 = "| h _3_50 _3_40  | h _2_40 _1_4_6  |"
kassav2="| e _1_4_6 _1_4_6 _1_4_6 _1_4_6 s r e. _3_50 e _3_50 _3_50  | e _2_40 _2_40 _2_40 _2_40 s r e. _3_50 e _3_50 _3_50  |"
kassav3="| q r e 6 ^ 1 s r e. _ 5 q ^ 0  | q r e 4 ^ 0 s r e. _ 4 q 5 | \
| e 4 4 4 4 e. 4 s 3 r e. 5  | e 2 4 q r h r | \
| q r e 6 ^ 1 s r e. _ 5 q ^ 0  | q r e 4 ^ 0 s r e. _ 4 q 5 | \
| e 4 4 4 4 s r e 4 s 3 r e. 5  | e 2 4 q r h r  |"
kassav4="| e 6 6 6 6 s 6 e ^ 1 s _ 6 e 5 4  | q ^ 0 e r 0 s r e. _ 4 q 5  |"

PC(program =26, channel=0)

Pa >> zn(kassav1, channel = 0, dur=0.8)

def kassav():
    silence()
    D("crow", room=0.5, pan= center)
    Pb >> zn(kassav2, channel = 0, dur=0.2)
kassav()

def kassavryt():
    Pk >> n("(36)" , channel = 9, dur=0.1, p=1)
    Ps >> n("(eu [38] 2 18 2)" , channel = 9, dur=0.1, p=0.25)
    Ph >> n("(eu [44!7 46] 7 8 )", channel=9, p=0.25)
kassavryt()

Pa >> None
Pb >> None
def kassavs():
    Pa >> zn(kassav2, channel = 0, dur=0.2)
    Pb >> zn(kassav3, channel = 3, dur=0.1)
kassavs()

Pa >> None
Pb >> None
def kassavs():
    Pa >> zn(kassav2, channel = 0, dur=0.2)
    Pb >> zn(kassav4, channel = 3, dur=0.1)
    #Pg >> n("A1!7 A1|C2",channel = 2, dur=0.5)
kassavs()

Pq >> d("crow", p=0.25, leg=0.1, 
        pan=center, 
        leslie=0.75, lrate="0.5 0.9 0.7 0.2", lsize=0.8
        )

Pg >> None

print(text2art("ZOUK", "small"))

silence()


'
 █▀▄ █ █   █▀▄ ▄▀▄ ██▄
 █▄▀ ▀▄█   █▀▄ █▀█ █▄█
'

vengaboys = "| e _40 _40 e. _40 s _40 e _1_4 _1_4 q _1_4  |\
            e _2_5 _2_5 e. _2_5 s _2_5 e _2_5 _2_5 q _2_5  |\
            e _0_3 _0_3 e. _0_3 s _0_3 e _1_4 _1_4 q _1_4 | \
            | e _40 _40 e. _40 s _40 e _40 _40 q _40  |"
vengaboys1 = "| q 0 e _ 5 4 q ^ 0 e _ 5 4  | r r r r |"
vengaboys2 = "| q 0 e _ 5 4 q ^ 0 e _ 5 4  | e 2 2 2 3 4 2 q 0  |"
vengaboys3="| q r 2 2 1  |"
vengaboys4="| q 0 e r _ 4 4 4 ^ 1 1  | q 0 e r _ 5 5 5 ^ 0 1 | \
| e. 2  s 0 s r e _ 3 3 3 3 3  | e. _ 2 s ^ 0 q 2 2 1 | \
| q 0 e r _ 4 4 4 ^ 1 1  | q 0 e r _ 5 5 5 ^ 0 1 | \
| e. 2  s 0 s r e 0 2 2 1 1  | q 0 r h r  |"

panic()

Pi >> None
PI >> None
def intro():
    Pi >> zn(vengaboys, channel = 0, dur=0.1)
    #PI >> zn(vengaboys1, channel = 1, dur=0.1)
    PI >> zn(vengaboys2, channel = 1, dur=0.1)
    Pk >> n("36 44 38 44", channel = 9, p=0.5)
    Ph >> n("44!7 46", channel=9, p=0.25)
#######
intro()

#BREAK
def lebreak():
    PC(program = 88, channel = 1)
    Pi >> None
    PI >> zn(vengaboys3, channel=1,dur=0.75)
    Pk >> None
    Ph >> n("44!7 46", channel=9, p=0.25)
###
lebreak()

Ph>> None
PI>> None
def refrain():
    Pi >> zn(vengaboys, channel = 0, dur=0.1)
    PI >> zn(vengaboys4, channel = 1, dur=0.1)
    Pk >> n("36 44 38 44", channel = 9, p=0.5)
    Ph >> n("44!7 46", channel=9, p=0.25)
########
refrain()

PH >> n("64 63 62", channel=9, p=0.25)

PH >> None

silence()

clock.tempo = 136
updown ="| q __#3_#5 e r __#3_#5 q __6#1 __6#1  | q _#03 e r _#03 q __6#1 __6#1  | q __#3_#5 e r __#3_#5 q __6#1 __6#1  | q _#03 e r _#03 q __6#1 __6#1  |"
updown2 ="| e. __#3_#5 s __#3_#5 e r _#03 _#03 _#03 __6#1 __6#1  | e __#3_#5 __#3_#5 __#3_#5 s _#03 _#03 e _#03 _#03 __6#1 __6#1 | \
| e. __#3_#5 s __#3_#5 e r _#03 s _#03 _#03 e _#03 __6#1 __6#1  | q __#3_#5 e r s _#03 _#03 e _#03 _#03 __6#1 __6#1  |"
updownbass ="| e ___ #3 s ^ #3 #3 e _ #3 s ^ #3 #3 e _ #3 s ^ #3 #3 e _ #3 s ^ #3 #3  |"

Pi >> zn(updown, channel = 0, dur=0.1)
Po >> zn(updown2, channel = 1, dur=0.1)

Pi >> None
Po >> None
def updown():
    PC(program = 39, channel = 2)
    Pi >> zn(updown2, channel = 0, dur=0.1)
    Pb >> zn(updownbass, channel = 2, dur=0.15)
########
updown()


@swim 
def tx7lead(p=0.5,i=0):
    dur =ZN("e 057 237 ^ 497 _ 451 9E2 s 9E2",dur=0.17, i=i)
    tx7("Algorithme", P("1~8",i))
    #tx7("LevelOp4", P("[1~18]",i))
    #tx7("LevelOp5", P("[45~85]",i))
    #tx7("FreqCourseOp4", P("[1~18]",i))
    #tx7("Op4EnvL3", P("[1~118]",i))
    #tx7("Op4EnvR3", P("[1~118]",i))
    tx7("Op4EnvR2", P("[1~118]",i))
    tx7("Op4EnvL2", P("[1~118]",i))
    tx7("Op4EnvL4", P("[1~118]",i))
    tx7("Op4EnvR4", P("[1~118]",i))
    dur2 = ZN("s ^ 4 5 1 2 4 5 8 9 7 45 6 1 2 7 5 4", dur=0.15, i=i)
    again(tx7lead,p=dur,i=i+1)


#TX7 TROUVER TRUC

PA >> None
Pk >> None
Pl >> None
Pr >> None
tx7lead.stop()

@swim 
def scaledingo(p=0.25,i=0):
    dur = ZD("leCASIOvib" ,
                "s _ _ _ 0 3 6 q 0 5 4 0 3 2 1 ",
                scale="chromatic", accelerate = -0.1,
                i=i, lpf = "[3500~500]", resonance = 0.65,
                leg=0.25, pan=center, gain=0.85)
    #D("sid:[0~8]", leg= 0.2, pan = anticenter,i=i)
    D("sid:2", 
            leg=0.2,# binshift=1.5, pan="rand",
            pan = center,
            i=i)
    #print(text2art("<^[[[><","rand"))
    again(scaledingo,p=dur,i=i+1)

