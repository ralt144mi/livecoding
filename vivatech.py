# Idée X : LKSJDMQLKSJD

clock.tempo=135

Pa * d('pastfuture:13', leg=.25, p=.5, hpf=200, amp='0.2~0.3', 
       triode='.2~.3', shape=.5, speed=0.5, accel='0~0.0002',
       n="[0 7]!!24 + [C C']!4 [Eb Eb']!4 [D D']!4")

Pc * d('kit93:[.. 11]', p=.25, amp='0.3~0.4', hpf=500, shape=.25)

Pb * d('kit93:[0 4]', p=1, amp='0.4~0.5', shape=.2)

Pd * d('. snare:15', room=0.2, size=0.2, dry=0.4, orbit=2)

Pe * d('pastfuture:[2~3]', p=.5, room=0.8, amp="0.1~0.2",
       orbit=3, lpf='500+(ulsin 4)*4000', size=0.7, dry=0.3, hpf=200,
       speed=0.5, n="[0 7]!!24 + [G5 Ab5 G5 Eb5 C6 Eb5 C5 G5 Ab5]")

Pf * d('pastfuture:[2~3]', p=.5, room=0.8, amp="0.1~0.2", 
       orbit=3, lpf='500+(ulsin 2)*4000', size=0.7, dry=0.3, hpf=200,
       speed=0.5, n="[0 7]!!24 + [C6 G6 Bb6 F6 G6]!!8", accel=0.005)

# plus rapide
Pf * d('pastfuture:[2~3]', p=.25, room=0.8, amp="0.2~0.35-0.05", 
       orbit=3, lpf='500+(ulsin 2)*4000', size=0.7, dry=0.3, hpf=200,
       speed=0.5, n="[0 7]!!24 + 12+[C6 Bb5 Ab5 G5]!!4", accel=0.005)

silence(Pc, Pb)

Pb * d('kit94:[0 5 0 4 0 2]', p=.5, amp='0.4~0.5', shape=.2)

silence()


samples()



# Idée 1 : Allez Raphaël, musique
# 2 11 (filt)

Pa * d('juppad:2', leg=1, speed='{1 0.99}', amp='0.3')

# Partir de 200 juqsu'à 
Pk * d("kit91:[0 1 4 4 0 4 4 4]", lpf="120+(lsaw 4)*2200", p=0.5)

Pe * d('. snare:15', orbit=2, room=0.5, size=.2, dry=.3, speed='0.94')

Pf * d('. perc:2 .. perc:8', p=.25, shape=.3, hpf=3000)

Pb * d('juppad:2', speed='{1 0.996}', pan="{0 1}", leg=.7, accel='0.003')

PK * d("(eu kick:0 3 5)", shape=0.2, orbit=1)

silence(Pb)

Pb * d('juppad:2', speed='{2 1.996}', pan="0 {0 1} 1", leg=.145, p=0.125, accel='0.003')

Ph * d("ihat:13", amp="0.25~0.3", p=0.25, leg=0.05)


silence(Pa, Pe, PK)
Pb * d('juppad:2', speed='{1 0.996}', lpf=1000, pan="{0 1}", begin=0.10, 
        attack=0.2, release=0.25, leg=.5, p=1, accel='0.003')

Pi * d('kit8085:[0 2 4 0 10 12]', octsub=.5,
       speed='1 {1 0.5}', p=.5, leg=.2, shape='.5~.7')
Pe * d('(eu proksa:[8:14] 14 16)', p='.25', speed='0.5', octer=1,
       leg=.2, orbit=3, cut=0, release=1.2)


# Idée 2 : Clic [ANNULEEEEEEEEEEER]

clock.tempo = 118

Pa * d('clic:[1:4]', p=.25, cut=1, 
       orbit=2, pan='(ulsin 4)/2', leg=.2,
       room=0.8,size=0.3,dry=0.7)

Pa * d('clic:[1:8]', p=.25, cut=1, orbit=0, 
       pan='(ulsin 4)/2', leg=.2, room=0.8,size=0.3,dry=0.7)

Pa * d('clic:[30:40]', p=.25, cut=1, 
       orbit=0, pan='(ulsin 4)/2', leg=.2,
       room=0.8,size=0.3,dry=0.7)

Pc * d('clic:1~80', p=.25, leg=.2, cut=1, 
       speed=2, orbit=0, pan='0.25+(ulsin 2)/2',
       room=0.8,size=0.3,dry=0.7)

Pe * d('(eu kit8086 15 16)', p=.25, shape=.1)

Pb * d('kit8085:[0 2 4 0 10 12]', octsub=.5,
       speed='1 {1 0.5}', p=.5, leg=.2, shape='.5~.7')

Pe * d('(eu proksa:[8:14] 14 16)', p='.25', speed='0.5',
       leg=.2, orbit=3, cut=0, release=1.2)

samples()

silence()

# Transi ici

Pb * d('kit8085:[0 2 4 0 10 12 0 2 4 0 3 5 2 8]', octsub=.5, 
       speed='1 {1 0.5} 1 {1 2}', p=.5, leg=.2, shape='.5~.7')

Pb * d('kit8085:[0 2 4 0 10 12 0 2 4 0 3 5 2 8]', octsub=.5, 
       speed='1 {1 0.5} 1 {1 2}', p='.5!8 .25!4', leg=.2, shape='.5~.7')

silence()

# Idée 3 : Starter [TRAVAILLER]

clock.tempo = 142

Pa * d('(if (every 2) long:0 long:2)', leg=0.2,
       lpf='1200+(ulsin 8)*4000', room=1, dry=0.6,
       size=0.5, speed='(if (every 2) 1 1.6)', p=0.25)

Pb * d('(eu ihat:13 7 12)', p=.25, leg=.02, amp='0.3',
       lpf='2000+(ulsin 8)*800', pan='(ulsin 4)')

Pd * d('kit8085 .', shape=.5, p='(e 6 8)/2')

Pe * d('kit8085:11~12', shape=.5, p='(e 9 12)/[2 4]!!8', amp='.2~.4')

silence()

# Idée 4 : Le Gros Rythme

clock.tempo = 93
@swim 
def lerythme(p=0.5,i=0):
    D("kick:4 . kick:5 .. kick:10", triode=0.3, euclid=(3,3,1), leg=.4,
            shape=0.65, div=2, i=i, hpf='40~50') # régler
    D('. . snare:10 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i, orbit=1,hpf=200, lpf=9000)
    D('(eu hat 14 16)', i=i, orbit=3)
    D("long:15", n='{F2 F3} F2|F3', leg=0.15, pan="rand", amp='0.3~0.5', orbit=2,
       #lpf='3500*(ulsin 4)/4', res=0.2
       )
    again(lerythme, p=.5, i=i+1) #p=0.5


Pd * d('february:[0:10]', amp=0.4, p=.25, leg=.05, pan='rand', 
       speed='(if (beat 0 2) 1 0.5)*2', hpf='2000+(ulsin 4)', orbit=5)
Pe * d('october:[0:10]', p='.25!8 .125!4', leg=.1, amp='0.3~0.5 * (ulsin 0.5)', 
       pan='(ultri 4)', speed='2!4 4!4')

lerythme.stop()
PB * d("jungbass:4", p="2")
Pb * d("long:15", n='{F2 F3} F2|F3', leg=0.15, pan="rand", amp='0.3~0.5', orbit=2, p=.25,
       lpf='500+1000*(ulsaw 8)', res=0.30,
        )#lfo 400 -> 1000

# HPF avec lfo
silence(PB)
@swim 
def lerythme(p=0.5,i=0):
    D("kick:4 . kick:5 .. kick:10", triode=0.3, euclid=(3,3,1), leg=.4,
            shape=0.65, div=2, i=i, hpf='40~50') # régler
    D('. . snare:10 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i, orbit=1, hpf=200, lpf=9000)
    D('(eu hat 14 16)', i=i, orbit=3)
    again(lerythme, p=.25, i=i+1) #p=0.5

Pg * d("long:[21]", n='{F2 F3} F2|F3', shape=.5, leg=0.133, pan="(ulsin 2)", amp='0.3~0.5', orbit=2, p=.25, euclid=(3,4,2), speed='{0.5 1}')

lerythme.stop()
Pk * d("jungbass:4", p="0.75 1 0.25!2 0.5"*8, release=0.20)
silence(Pd, Pe)

Pd * d('february:[0:10]', amp=0.4, p=.25, leg=.05, pan='rand', 
       speed='(if (beat 0 2) 1 0.5)*2', hpf='2000+(ulsin 4)', orbit=5)
Pe * d('[.]!8 october:[0:10]', p='.125', leg=.1, amp='0.3~0.5 * (ulsin 0.5)', 
       pan='(ultri 4)', speed='2!4 4!4')

silence(Pk)
@swim 
def lerythme(p=0.5,i=0):
    D("kick:4 . kick:5 .. kick:10", triode=0.3, euclid=(3,3,1), leg=.4,
            shape=0.65, div=2, i=i, hpf='40~50') # régler
    D('. . snare:10 .', room=0.8, size=0.5, dry='0.3 0.5 0.1',
            div=2, i=i, orbit=1,hpf=200, lpf=9000)#9000
    again(lerythme, p=.25, i=i+1) #p=0.5

Ph * d('(eu hat 14 16)', amp="0.25~0.45", p="0.25!15 0.125!4", orbit=3)

silence(Pe,Pd,Pk,lerythme,Ps,Ph)

silence()


# Idée X : LKSJDMQLKSJD

clock.tempo = 129

Pa * d('pastfuture:13', leg=.25, p=.5, hpf=200, amp='0.2~0.3', 
       triode='.2~.3', shape=.5, speed=0.5, accel='0~0.0002',
       n="[0 7]!!24 + [C C']!4 [Eb Eb']!4 [D D']!4")

Pc * d('kit93:[[.. 11]!14 [.. {29}]!1]', p=.25, 
       amp='0.3~0.4', hpf=500, shape=.25)

Pb * d('kit93:[[0 4]!7 [0 5]]', p=1, amp='0.4~0.5', shape=.2)
Pd * d('[. snare:15]!3 [. snare:19]', room=0.2, size=0.2, dry=0.4, orbit=2)

Pz * d('pastfuture:[12]', begin=.1, p=.5, room=0.8, amp="(s amp 0.1~0.12)",
       orbit=3, lpf='500+(ulsin 4)*4000', size=0.7, dry=0.3, hpf=200,
       speed=0.5, n="(s mel [0 7]!!24 + [G5 Ab5 G5 Eb5 C6 Eb5 C5 G5 Ab5])")

Pf * d('pastfuture:[15]', p='0.5|0.25', room=0.8, amp="(g amp)", 
       orbit=3, lpf='500+(ulsin 2)*4000', size=0.7, dry=0.3,
       hpf=200, speed=0.5, n="(g mel)+12", leg=.1, accel=0.005)

# plus rapide
Pf * d('pastfuture:[15]', begin=.1, p=.25, room=0.8, amp="(g amp)", 
       leg=.1, orbit=3, lpf='100+(ulsin 2)*3000', size=0.7, dry=0.3, 
       hpf=200, speed=0.5, n="[0 7]!!24 + [C6 Bb5 G5 Eb5]!!4", 
       accel=0.005)

silence(Pc, Pb)

# plus rapide
Pf * d('pastfuture:[15]', begin=.1, p=.25, room=0.8, amp="(g amp)", 
       leg=.1, orbit=3, lpf='100+(ulsin 2)*3000', size=0.7, dry=0.3, 
       hpf=200, speed=0.5, n="[0 7]!!24 + [C6 Bb5 G5 Eb5]!!4 - [12 24]", 
       accel=0.005)

Pb * d('kit93:[[0 4]!7 [0 5]]', p='1 0.5!2', amp='0.4~0.5', shape=.2)
Pd * d('[. snare:15]!3 [. snare:19]', p='1', room=0.2, crush=8,
       size=0.2, dry=0.4, orbit=2)

silence(Pb, Pd, Pe)

Pa * d('pastfuture:13', leg=.25, p=.5, hpf=200, amp='0.3', 
       triode='.2~.3', shape=.5, speed=0.5, accel='0~0.0002',
       n="[0 7]!!24 + [C C']!4 [G3 G']!4")

P('(set amp 0)', 1) # de 0.1 à 0.0

silence()

# Idée 5 : avec le dossier sound

Pa * d('sound:7', leg=2, release=1.8, n='(scl 0 2 4 0 3 5)', p=.5)

silence()



# Idée X : LKSJDMQLKSJD

clock.tempo = 129

Pa * d('pastfuture:13', leg=.25, p=.5, hpf=200, amp='0.2~0.3', 
       triode='.2~.3', shape=.5, speed=0.5, accel='0~0.0002',
       n="[0 7]!!24 + [C C']!4 [Eb Eb']!4 [D D']!4")

Pc * d('kit93:[[.. 11]!14 [.. {29}]!1]', p=.25, 
       amp='0.3~0.4', hpf=500, shape=.25)

Pb * d('kit93:[[0 4]!7 [0 5]]', p=1, amp='0.4~0.5', shape=.2)
Pd * d('[. snare:15]!3 [. snare:19]', room=0.2, size=0.2, dry=0.4, orbit=2)

Pz * d('pastfuture:[12]', begin=.1, p=.5, room=0.8, amp="(s amp 0.1~0.12)",
       orbit=3, lpf='500+(ulsin 4)*4000', size=0.7, dry=0.3, hpf=200,
       speed=0.5, n="(s mel [0 7]!!24 + [G5 Ab5 G5 Eb5 C6 Eb5 C5 G5 Ab5])")

Pf * d('pastfuture:[15]', p='0.5|0.25', room=0.8, amp="(g amp)", 
       orbit=3, lpf='500+(ulsin 2)*4000', size=0.7, dry=0.3,
       hpf=200, speed=0.5, n="(g mel)+12", leg=.1, accel=0.005)

# plus rapide
Pf * d('pastfuture:[15]', begin=.1, p=.25, room=0.8, amp="(g amp)", 
       leg=.1, orbit=3, lpf='100+(ulsin 2)*3000', size=0.7, dry=0.3, 
       hpf=200, speed=0.5, n="[0 7]!!24 + [C6 Bb5 G5 Eb5]!!4", 
       accel=0.005)

silence(Pc, Pb)

# plus rapide
Pf * d('pastfuture:[15]', begin=.1, p=.25, room=0.8, amp="(g amp)", 
       leg=.1, orbit=3, lpf='100+(ulsin 2)*3000', size=0.7, dry=0.3, 
       hpf=200, speed=0.5, n="[0 7]!!24 + [C6 Bb5 G5 Eb5]!!4 - [12 24]", 
       accel=0.005)

Pb * d('kit93:[[0 4]!7 [0 5]]', p='1 0.5!2', amp='0.4~0.5', shape=.2)
Pd * d('[. snare:15]!3 [. snare:19]', p='1', room=0.2, crush=8,
       size=0.2, dry=0.4, orbit=2)

silence(Pb, Pd, Pe)

Pa * d('pastfuture:13', leg=.25, p=.5, hpf=200, amp='0.3', 
       triode='.2~.3', shape=.5, speed=0.5, accel='0~0.0002',
       n="[0 7]!!24 + [C C']!4 [G3 G']!4")

P('(set amp 0)', 1) # de 0.1 à 0.0

silence()
