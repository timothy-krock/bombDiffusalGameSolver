#############################################
##  SOLVER FOR THE PASSWORDS MODULE
##  OF THE BOMB DIFFUSAL GAME
##  WRITTEN BY TIM KROCK
############################################
## NOTE : THIS WON'T NARROW THE GAME DOWN TO
##        A SINGLE OPTION EVERY TIME. IT'S
##        FASTER TO SELECT FROM THREE THAN
##        TO ENTER ADDITIONAL ROWS.
###########################################

potentials = [
"about", "after", "again", "below", "could",
"every", "first", "found", "great", "house",
"large", "learn", "never", "other", "place",
"plant", "point", "right", "small", "sound",
"spell", "still", "study", "their", "there",
"these", "thing", "think", "three", "water",
"where", "which", "world", "would", "write"
]




##############
# GET INPUT
#############
first = []
third = []
fifth = []
options = []
print 'INPUT FIRST AND THIRD ROWS FROM THE'
print 'PASSWORD MODULE AND RECIEVE A LIST'
print 'OF POSSIBLE ANSWERS. '
print "########FIRST LINE##########"
for i in range(6):
	first.append(raw_input("row " + str(i) + ":"));

print "#########FIFTH LINE#########"
for i in range(6):
	third.append(raw_input("row " + str(i) + ":"));

#print "#########FIFTH LINE#########"
#for i in range(6):
#        fifth.append(raw_input("row " + str(i) + ":"));
print "########END OF INPUT#######"




#for i in first:
#	for j in third:
#		for k in fifth:
#			for word in potentials:
#				if word[0] == i and word[2] == j and word[4] == k:
#					options.append(word)

for i in first:
    for j in third:
        for word in potentials:
            if word[0] == i and word[2] == j:
                options.append(word)







########
#OUTPUT
########


print first
print third
#print fifth
print "########## OPTIONS########"
print options


