'''
still have bugs need to solve
''''
f = file ('input.in','r')
w = file ('output.out','w')

T = int(f.readline())

for case in range (0,T):
    counter = int(f.readline())
    firstNum = f.readline().rstrip('\n')
    secondNum = f.readline().rstrip('\n')

    firstBackup = firstNum;
    secondBackup = secondNum;

    firstModified = ""
    secondModified = ""
    while (firstBackup != ""):
        if len(firstBackup) == 1:
            if len(firstModified) == 0:
                firstModified += firstBackup
            break
        if firstBackup[0] != firstBackup[1]:
            firstModified+=(firstBackup[0])
        firstBackup = firstBackup[1:]
    while (secondBackup != ""):
        if len(secondBackup) == 1:
            if len(secondModified) == 0:
                secondModified += secondBackup
            break
        if secondBackup[0] != secondBackup[1]:
            secondModified+=(secondBackup[0])
        secondBackup = secondBackup[1:]

    print firstModified
    if firstModified == secondModified:
        diff = 0
        for i in range(0,len(firstModified)):
            firstCounter = 0
            secondCounter = 0
            while (firstNum[0] == firstModified[i]):
                firstCounter += 1
                if (len(firstNum)==1):
                    break
                firstNum = firstNum[1:]
            while (secondNum[0] == secondModified[i]):
                secondCounter += 1
                if (len(secondNum)==1):
                    break
                secondNum = secondNum[1:]
            diff += abs(firstCounter - secondCounter)
        strings = "Case #" + str(case +1) +": " +str(diff)
    else:
        strings = "Case #" + str(case +1) +": Fegla Won"

    w.write (strings + "\n")
