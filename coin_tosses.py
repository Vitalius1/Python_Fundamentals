import random
"Starting the program..."
def coin_toss(times):
    head = 0
    tail = 0
    for i in range(1, times + 1):
        randcoin = 0
        coin = round(random.random())
        # print coin
        if coin == 1:
            head += 1
            print "Attempt #{}: Trowing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far!".format(i, head, tail)
        else:
            tail += 1
            print "Attempt #{}: Trowing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far!".format(i, head, tail)
coin_toss(20)
print "Ending program. Thank you!"