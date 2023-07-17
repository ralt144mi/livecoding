Pz >> zn("w 053 173", channel=1, dur=1.2, key="F", scale="min7")


Po >> zn("s ^ 5 3 0 r", channel=1, dur=0.1, vel=25, key="F", scale="min7")

Pt >> zn("w _ _ 0 r 7 0", channel=1, dur=1.8, key="F", scale="min7")

silence()

Pr >> d("(eu [ralt144mi!2] 2 16)", leg="0.1!8 0.12"
        ,p=0.125, pan="rand", hpf=500)

PR >> d("(eu [ralt144mi!2] 6 16 4)", leg="0.1!8 0.12", speed=1.2,
        p="0.25 0.5", pan="rand", hpf = 500)

PR >> None

silence()

Pi >> zn("w 057 h 057", channel=1, dur="0.08", key ="F", scale="min7")

Pe >> zn("s ^ 7 5 0 r 7 5 0 r r 7 5 0 r r r", channel=1, dur="0.08", key ="F", scale="min7")

Pi >> zn("h _ 0 5 r 7 0 5", channel=1, dur=0.5, key ="F", scale="min7")

Ps >> zd("long:40 long:41 long:42 long:43 long:44",
         "q 0 [2 [7 8]] 3 [4 [7 879]] 8 5", leg="0.4!16 0.8")

Pq >> zn("q 0 5 r [7 5 7] 0 [3 [9 8 9]] q 0 [5 [9 8 9]] r [7 5 7] 0 [3 [9 8 9]]", channel=1, dur=0.5, key ="F", scale="min7")

PQ >> zn("w 057 h 057", channel=1, dur="0.8", key ="G", scale="min7")

Pn >> zn("q ^ ^ r r [7 [5 [7 5]] 7] r r [7 5 [7 [5 7]]]", channel=1, dur="0.1", key ="G", scale="min7")

clock.tempo=110

@swim
def swimmer(p=0.5, i=0):
    D("morgan:[0~2]!16", shape=0.44,
            begin = "rand*4", room=0.8, sz=0.6,
            #accelerate = "(-0.4) 0.4",
            lpf=50, resonance=0.02,
            leg="rand*7.25", pan="rand", i=i)
    again(swimmer,p=P("0.125 0.25 (0.128/8)!4",i)*P("16 8 16",i)/4, i=i+1)


silence()



