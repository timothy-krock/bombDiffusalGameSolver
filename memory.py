############################################
##  Solver for the CONCERNING MEMORY
##  Portion of the 'bomb game'
##  CODE WRITTEN BY TIM KROCK
############################################

#########################################################################################
#  USAGE
#########################################################################################
print 'This one is easy. Just type in five numbers'
print 'first, the number oon top followed by the bottom four'
print 'example: [1   ]'
print '         [1324]'
print 'should be entered 11234. It will print out the number you should hit'


#########################################################################################
#  STAGE 1
#########################################################################################
stage1 = raw_input("STAGE 1:");
positions = [0,0,0,0,0]
if stage1[0] == "1":
	print stage1[2]
	positions[1] = 2
if stage1[0] == "2":
        print stage1[2]
	positions[1] = 2
if stage1[0] == "3":
        print stage1[3]
	positions[1] = 3
if stage1[0] == "4":
        print stage1[4]
	positions[1] = 4


#########################################################################################
#  STAGE 2
#########################################################################################
stage2 = raw_input("STAGE 2:");
if stage2[0] == "1":
        print "4"
	####################
	#    FIND POSITION
	####################
	j = 1;
	for i in stage2[1:]:
		if i == "4":
			positions[2] = j
		
		j = j + 1		
if stage2[0] == "2":
	positions[2] = positions[1]
	print stage2[positions[2]]	
if stage2[0] == "3":
        print stage2[1]
	positions[2] = 1
if stage2[0] == "4":
        positions[2] = positions[1]
        print stage2[positions[2]]


#########################################################################################
#  STAGE 3
#########################################################################################
stage3 = raw_input("STAGE 3:");
if stage3[0] == "4":
        print "4"
        ####################
        #    FIND POSITION
        ####################
        j = 1;
        for i in stage3[1:]:
                if i == "4":
                        positions[3] = j

                j = j + 1
if stage3[0] == "1":
	#  If the display is 1, press the button with the same label you pressed in stage 2
        print stage2[positions[2]]
	k = 1
	for i in stage3[1:]:
		if i == stage2[positions[2]]:
			positions[3] = k
		k = k + 1;
if stage3[0] == "2":
	#  If the display is 1, press the button with the same label you pressed in stage 1
        print stage1[positions[1]]
        k = 1
        for i in stage3[1:]:
                if i == stage1[positions[1]]:
                        positions[3] = k
                k = k + 1;
if stage3[0] == "3":
        positions[3] = 3
        print stage3[positions[3]]


#########################################################################################
#  STAGE 4
#########################################################################################
stage4 = raw_input("STAGE 4:");
if stage4[0] == "1":
        positions[4] = positions[1]
        print stage4[positions[4]]
if stage4[0] == "2":
        positions[4] = 1
        print stage4[positions[4]]
if stage4[0] == "3":
        positions[4] = piositions[2]
	print stage4[positions[4]]
if stage4[0] == "4":
        positions[4] = positions[2]
        print stage4[positions[4]]


#########################################################################################
#  STAGE 5
#########################################################################################
stage5 = raw_input("STAGE 5:");
if stage5[0] == "1":
        print stage1[positions[1]]
if stage5[0] == "2":
        print stage2[positions[2]]
if stage5[0] == "3":
        print stage3[positions[3]]
if stage5[0] == "4": 
        print stage4[positions[4]]





