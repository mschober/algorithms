import random, sys

#randoms_gen = ( random.randint(1, int(sys.argv[1])) for i in range(1, int(sys.argv[2])) )
randoms_gen = [ random.randint(1, int(sys.argv[1])) for i in range(1, int(sys.argv[2])) ]

int_counts = {}
curr_count = 0
max_count = 0
winner_key = 0

for val in randoms_gen:
    #print val
    if str(val) in int_counts.keys():
        int_counts[str(val)] += 1
    else:
        int_counts[str(val)] = 1

    curr_count = int_counts[str(val)]

    if curr_count > max_count:
        max_count = curr_count
        winner_key = str(val)

#randoms.sort()
#print randoms
print "Winning key is: %s" % winner_key
print "Winning value is: %s" % max_count
