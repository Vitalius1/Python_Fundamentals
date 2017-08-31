import random
def scores_grades(num):
    print "Scores and grades."
    for i in range(num):
        randnum = random.randint(0, 100)
        if randnum >= 60 and randnum <=69:
            print "Score is {}; Your grade is D".format(randnum)
        elif randnum >=70 and randnum <=79:
            print "Score is {}; Your grade is C".format(randnum)
        elif randnum >=80 and randnum <=89:
            print "Score is {}; Your grade is B".format(randnum)
        elif randnum >=90 and randnum <=100:
            print "Score is {}; Your grade is A".format(randnum)
        else:
            print "Score is {}; You failed".format(randnum)
    print "End of program. Bye!"

scores_grades(10)