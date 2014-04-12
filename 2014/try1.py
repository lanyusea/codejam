f = file ('input.in','r')
w = file ('output.out','w')


T = int(f.readline())
counter = 0
number = 0
line1 = []
line2 = []
strings = []

for case in range(0,T):
    choose1 = int(f.readline())
    for i in range (0,4):
        line=f.readline().rstrip('\n')
        line1.append(line)
    targetLine1 = ''.join(line1[choose1-1])
    targetNumber1 = targetLine1.split(" ")

    choose2 = int(f.readline())
    for i in range (0,4):
        line = f.readline().rstrip('\n')
        line2.append(line) 
    targetLine2 = ''.join(line2[choose2-1])
    targetNumber2 = targetLine2.split(" ")

    print targetNumber1
    print targetNumber2

    for item in targetNumber1:
        if item in targetNumber2:
            counter += 1
            number = item
    if counter == 0:
        strings.append("Case #"+str(case+1)+": Volunteer cheated!")
    elif counter == 1:
        strings.append("Case #"+str(case+1)+": "+number)
    else:
        strings.append("Case #"+str(case+1)+": Bad magician!")
    counter = 0
    line1 = []
    line2 = []

for item in strings:
    w.write(item) 
    w.write("\n")
