'''
Lolllllllllllll~~
'''
f = file ('input.in','r')
w = file ('output.out','w')


T = int(f.readline())

dwarCounter = []
warCounter = [] 

if __name__ == '__main__':
    for case in range(0,T):
        counter = 0
        dcounter = 0
        number = int(f.readline())
        naomi=f.readline().rstrip('\n').split(" ")
        ken=f.readline().rstrip('\n').split(" ")
        naomiSort = sorted(naomi)
        kenSort = sorted(ken)
        print naomiSort
        print kenSort

        while (naomi and ken):
            if (max(naomi) < max(ken)):
                naomi.remove(min(naomi))
                ken.remove(max(ken))
            else:
                naomi.remove(max(naomi))
                ken.remove(max(ken))
                dcounter = dcounter + 1
        dwarCounter.append(dcounter)

        while (naomiSort and kenSort):
            if max(naomiSort) > max(kenSort):
                naomiSort.remove(max(naomiSort))
                kenSort.remove(min(kenSort))
                counter = counter + 1
            else:
                i = 0
                while kenSort[i] < max(naomiSort):
                    i += 1
                kenSort.pop(i)
                naomiSort.remove(max(naomiSort))
        warCounter.append(counter)
        #for i in range (0, number):
        #    print naomiSort[i]
        #    print kenSort[i]
        #    print "\n"
        #    if naomiSort[i] > kenSort[i]:
        #        counter = counter +1
        #warCounter.append(counter) 

    for i in range(0,T):
        w.write("Case #"+str(i+1)+": ") 
        w.write(str(dwarCounter[i]) + " " + str(warCounter[i]))
        w.write("\n")
