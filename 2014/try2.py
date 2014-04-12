f = file ('input.in','r')
w = file ('output.out','w')


T = int(f.readline())
data = []
output = []
rate = 2

def rateChange ():
    if (((goal - current)/rate) < ((goal + cost - current)/(rate+farmRate))):
        return False
    else:
        return True
if __name__ == '__main__':
    for case in range(0,T):
        data=f.readline().rstrip('\n').split(" ")

        cost = float(data[0])
        farmRate = float(data[1])
        goal = float(data[2])

        #print str(cost)
        #print str(farmRate)
        #print str(goal)

        current = 0
        time = 0
        rate = 2
        while (goal > current):
            if current >= cost:
                if (rateChange()):
                    rate = rate + farmRate
                    current = current - cost
            if goal - current < cost:
                difference = goal-current
            else:
                difference = cost
            #print "diff",
            #print difference
            current = current + difference 
            time = time + difference/rate
        output.append(time)
        #print output

    for i in range(0,T):
        w.write("Case #"+str(i+1)+": ")
        w.write("{0:.8f}".format(output[i]) )
        w.write("\n")
