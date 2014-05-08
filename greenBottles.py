import time
bottles = 10
for x in range(bottles,0,-1):#counts down a for loop until it reaches 0
    print("{0} green bottles, hanging on the wall\n{0} green bottles, hanging on the wall".format(x))#prints bottles within the {0}
    print("And if 1 green bottle should acidentally fall,\nThey'll be {0} green bottles hanging on the wall\n\n\n\n".format(x-1))
    time.sleep(3)#prints every verse after 3 seconds
        
