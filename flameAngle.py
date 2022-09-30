# FDI 100 Forest BAL 12.5
# Assigning initial values
# flame angle= m, view factor= n

# constants
fl=16.54    # flame length (m)
fw=100.0    # flame width (m)
d=5.0  # site to vegetation distance (m) as per BAL 12.5
m=float(input('Enter your initial flame angle (in degrees) m:'))
dm=float(input('Enter your flame angle increment (in degrees) dm:'))
i=0
err=1

nr0=10
nr1=1
nr2=4

while not((nr1 >= nr0) and (nr1 >= nr2)):

    import math  # import math library


    mr0=(math.radians(m+(i*dm)))     # convert flame angle to radians
    mr1=(math.radians(m+(i+1)*dm))     # convert flame angle to radians
    mr2=(math.radians(m+((i+2)*dm)))     # convert flame angle to radians


    h0=0.5*fl*(math.sin(mr0))   # elevation receiver
    x1_0=((fl*(math.sin(mr0)))-h0)/(d-(0.5*(fl*(math.cos(mr0)))))
    x2_0=(h0)/(d-(0.5*(fl*(math.cos(mr0)))))
    y1_0=y2_0=(0.5*fw)/(d-(0.5*(fl*(math.cos(mr0)))))

    # component of the eqn B8
    A0=(x1_0/(math.sqrt(1+(x1_0**2))))
    B0=(y1_0/(math.sqrt(1+(x1_0**2))))
    C0=(y1_0/(math.sqrt(1+(y1_0**2))))
    D0=(x1_0/(math.sqrt(1+(y1_0**2))))
    E0=(x2_0/(math.sqrt(1+(x2_0**2))))
    F0=(y2_0/(math.sqrt(1+(x2_0**2))))
    G0=(y2_0/(math.sqrt(1+(y2_0**2))))
    H0=(x2_0/(math.sqrt(1+(y2_0**2))))

    nr0=((A0*(math.atan(B0)))+ (C0*(math.atan(D0)))+(E0*(math.atan(F0)))+(G0*(math.atan(H0))))*(1/(math.pi))
    print('view factor nr0: ',nr0)

    # first iteration

    h1=0.5*fl*(math.sin(mr1))   # elevation receiver
    x1_1=((fl*(math.sin(mr1)))-h1)/(d-(0.5*(fl*(math.cos(mr1)))))
    x2_1=(h1)/(d-(0.5*(fl*(math.cos(mr1)))))
    y1_1=y2_1=(0.5*fw)/(d-(0.5*(fl*(math.cos(mr1)))))

    # component of the eqn B8
    A1=(x1_1/(math.sqrt(1+(x1_1**2))))
    B1=(y1_1/(math.sqrt(1+(x1_1**2))))
    C1=(y1_1/(math.sqrt(1+(y1_1**2))))
    D1=(x1_1/(math.sqrt(1+(y1_1**2))))
    E1=(x2_1/(math.sqrt(1+(x2_1**2))))
    F1=(y2_1/(math.sqrt(1+(x2_1**2))))
    G1=(y2_1/(math.sqrt(1+(y2_1**2))))
    H1=(x2_1/(math.sqrt(1+(y2_1**2))))

    nr1=((A1*(math.atan(B1)))+ (C1*(math.atan(D1)))+(E1*(math.atan(F1)))+(G1*(math.atan(H1))))*(1/(math.pi))
    print('view factor nr1: ',nr1)

    # second iteration

    h2=0.5*fl*(math.sin(mr2))   # elevation receiver
    x1_2=((fl*(math.sin(mr2)))-h2)/(d-(0.5*(fl*(math.cos(mr2)))))
    x2_2=(h2)/(d-(0.5*(fl*(math.cos(mr2)))))
    y1_2=y2_2=(0.5*fw)/(d-(0.5*(fl*(math.cos(mr2)))))

    # component of the eqn B8
    A2=(x1_2/(math.sqrt(1+(x1_2**2))))
    B2=(y1_2/(math.sqrt(1+(x1_2**2))))
    C2=(y1_2/(math.sqrt(1+(y1_2**2))))
    D2=(x1_2/(math.sqrt(1+(y1_2**2))))
    E2=(x2_2/(math.sqrt(1+(x2_2**2))))
    F2=(y2_2/(math.sqrt(1+(x2_2**2))))
    G2=(y2_2/(math.sqrt(1+(y2_2**2))))
    H2=(x2_2/(math.sqrt(1+(y2_2**2))))

    nr2=((A2*(math.atan(B2)))+ (C2*(math.atan(D2)))+(E2*(math.atan(F2)))+(G2*(math.atan(H2))))*(1/(math.pi))
    print('view factor nr2: ',nr2)



    i = i + 1
    print('processing iteration number',i)
    print('flame angle is : ', m+(i*dm))
















