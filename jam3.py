D("ralt144mi")


clock

@die
def ziff(p=0.5,i=0):
    #dur = ZN("h 035 r [075 ^ ^ [[5 7 5] _ [9 E 9]]] r", 
    #        key="D", scale="minor", channel=1, i=i)
    dur2 = ZN("q _ _ 0 0 5 0", i=i, scale="minor", channel=1, key="D")
    again(ziff, p=dur2, i=i+1)

Pz >> None

silence()

Ps >> n("({D2@maj}^[0..2])!4 ({F2@maj}^[0..4])!4", p="0.125!8 0.25!2", dur=0.05, channel=1)


Pz >> zn("h r [ _ 0 ^ [7 ^ [8 _ 5E ^ 8] _ _ [5 ^ [1 3 2 ^ 1 2 3]]]]", dur=0.1, channel=1)

PZ >> zn("h r [ 2 4 2 4 2 4 2 4 2 4 2 4 2 4 ]", dur=0.05, channel=1)

Po >> zn("h _ _ 4", dur=0.5, channel=1)


Pj >> zn("q [r 4] r [r [7 r 4]] [r [4 r 2]]", dur="0.25 0.125 0.25", channel=1)

Pa >> zn("q r q. ^ ^ [4 r r 4] [3 r r 3] [2 r r 3]", channel=1, dur=0.05) 

Pb >> zn("a 0", channel=1, dur=0.1)

Pa >> zn("e 1", channel=1, dur=0.1)

Pb >> None

Pf >> zn("f 2", channel=1, dur=0.1)

Po >> zn("a ^ 4 3 2 4 3 2 2 3 4 2 3 4 4 2 3", channel=1, dur=0.15)

Pl >> zn("s ^ 4 3 2 r 3 r 2 r 3 4 r 3 r 4 r r 2 3", channel=1, dur=0.05)

Py >> zn("t ^ ^ r r 4 3 r 2 4 3 r 2 r 2 3 r 4 2 3 r 4 4 r 2 3", channel=1, dur=0.15)

Pt >> zn("f _ 4 2 3 4 4 2 3", channel=1, dur=0.15)

