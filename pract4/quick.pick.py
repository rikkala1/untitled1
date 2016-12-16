__author__ = 'jc446932'

from random import randint

num_of_picks = int(input('how many quick pick?'))

num = 0

for i in range(0,num_of_picks):
    num = randint(1, 45)
    pick_pf_6_num = []
    for j in range (0, 6):
        while num is pick_pf_6_num:
            num = (1, 45)
        pick_pf_6_num.append(num)

    print (sorted(pick_pf_6_num))
