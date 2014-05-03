f = file ('input.in','r')
w = file ('output.out','w')

T = int(f.readline())

for case in range (0,T):
    counter = 0
    number = f.readline().rstrip('\n').split(" ")
    firstNum = int(number[0])
    secnodNum = int(number[1])
    goal = int(number[2])
    for i in range (0,firstNum):
        for j in range(0,secnodNum):
            if i&j < goal:
                counter+=1
    w.write ("Case #" + str(case +1)+ ": ")
    w.write (str(counter) + "\n")
