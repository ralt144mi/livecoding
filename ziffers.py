BRAIDS_MODELS = {
    "csaw":0,
    "morph":1,
    "saw_square":2,
    "sine_triangle":3,
    "buzz":4,
    "square_sub":5,
    "saw_sub":6,
    "square_sync":7,
    "saw_sync":8,
    "triple_saw":9,
    "triple_square":10,
    "triple_triangle":11,
    "triple_sine":12,
    "triple_ring_mod":13,
    "saw_swarm":14,
    "saw_comb":15,
    "toy":16,
    "digital_filter_lp":17,
    "digital_filter_pk":18,
    "digital_filter_BP":19,
    "digital_filter_hp":20,
    "vosim":21,
    "vowel":22,
    "vowel_fof":23,
    "harmonics":24,
    "fm":25,
    "feedback_fm":26,
    "chaotic_feedback_fm":27,
    "plucked":28,
    "bowed":29,
    "blown":30,
    "fluted":31,
    "struck_bell":32,
    "struck_drum":33,
    "kick":34,
    "cymbal":35,
    "snare":36,
    "wavetables":37,
    "wave_map":38,
    "wave_line":39,
    "wave_paraphonic":40,
    "filtered_noise":41,
    "twin_peaks_noise":42,
    "clocked_noise":43,
    "granular_cloud":44,
    "particle_noise":45,
    "digital_modulation":46,
    "question_mark": 47,
}

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





clock.tempo = 120

Pa >> d('braids', p=4, model=3, sustain=4, octave=2, color='rand', timbre='rand')
Pb >> d('braids', p=1/3, color='rand', timbre='rand', model=34, shape=0.5, orbit=2)
Pc >> d('., braids, ..', p=1/3, color='rand', timbre='rand', model=36, shape=0.1, orbit=2, legato=0.1)
Pd >> d('braids', p='(1/3)/2|1', color='rand', timbre='rand', model=35, shape=0.1, orbit=2, legato=0.1)


panic()


Pz >> zd('arpy', '0 1 24 35', pan='rand')

clock.tempo = 152

from art import tprint

from art import *

from art import text2art

import art

art()

@swim
def ziff(p=0.5,i=0):
    var = " "
    dur = ZD('braids', var.join(
            ["0.5 _ [024 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _ ",
            '[024 ^ ^ [ 5 2 ] _ ] [027 ^ ^ [9 5]] _ ([024 ^ ^ [2 9]] _ _ ',
            '0.25 [057 ^ ^ [7 5 3]] _ _ 1.0 [024 ^ ^ [ 5 2 ] _ ] 0.5 [027 ^ ^ [7 5]]) ',
            '_ _ _ [022 ^ ^ [4 7]] _ _ [057 ^ ^ [7 5 3]] _ _',
            '0.5 [024 ^ ^ [ 5 2 ] _ ] [027 ^ [7 5]] _ [024 _ [4 7]]',
            '_ [056 _ [6 4 2]] _ _ [022 ^ ^ [ 4 1 ] _ ] [032 ^ ^ [7 5]]',
            '0.125 _ [023 ^ ^ [7 6]] _ _ [055 ^ ^ [(5 4 3)-4]] _ _ ',
            '0.5 [032 _ _ [ 5 2 ] _ ] [027 ^ ^ [7 5]]']), 
            legato = 0.5,
            scale = 'rocritonic',
            model = 22, 
            room = 0.5, size = 0.2,
            color = "0.8,0.5,0.4",timbre = "0.2,0.8,0.9",
            pan='rand',i=i)
    if dur >= 1 :
        print(art("waves")+art("Fish Swimming")+"\n")
    elif dur < 1 and dur >= 0.5 :
        print(art("chess")+art("Boom Box")+"\n")
    elif dur < 0.5 and dur >=0.25 :
        print(art("Cassette")+art("Cassette")+art("Cassette")+art("Cassette")+art("Cassette")+art("Cassette")+"\n")
    else : 
        print(art("Squid")+art("rocket")+"\n")
    again(ziff, p=dur,i=i+1)

clock.tempo = 120

Pa >> zd('braids', '<-3> 0.125 [1 [6 8]] #2 [3 [7 8]] <0> #(2,9)',
        scale = 'rocritonic',
        cutoff  = 1500, resonance = .2,
        key = "C", model="25", legato =0.2)

Pk >> d("eu(leKICK:3,2,5)", shape = 0.9, gain = 1.1, cutoff = 2500, resonance = .3)

Ph >> d("eu(leHIHAT:6,4,5)", p=0.5, hcutoff =2500, resonance = 0.2) 

Pv >> zd("leCASIOvib:[1]", "<-2> w 1 6 3 0", scale = 'rocritonic', legato = 2)


panic()


Pk >> d("if(beat(0,3), leKICK:3, laSNARE)", p=0.5, cutoff = 2500, resonance = .3)


Pk >> d("if(beat(0,3), leKICK:3, laSNARE)", p=0.5, cutoff = 2500, resonance = .3)


Pk >> d("if(every(2), leKICK:3, laSNARE:2)", p=0.5, legato = 0.25, cutoff = 2500, resonance = .3)


Pk >> d("if(beat(0,3), leKICK:3, laSNARE)", p=0.5, cutoff = 2500, resonance = .3)


def tempomedler():
    if clock.tempo < 280 :
        clock.tempo = clock.tempo*1.02
    else :
        clock.tempo = 160
   
@swim
def ziff(p=0.5, i = 0):
    tempomedler()
    dur = ZD('braids', '<-3> 3.0 [1 [8 8]] #2 [3 [7 8]] <0> #(2,9)',
        scale = 'rocritonic',
        cutoff  = 1500, resonance = ".2",
        key = "C", model="22", i=i)
    again(ziff, p=dur, i= i+1)


Ps >>


