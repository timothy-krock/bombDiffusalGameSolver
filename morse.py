############################################
## MORSE CODE PARSER FOR THE BOMBGAME
## WRITTEN BY TIM KROCK
############################################
def parse(morse):
        if morse == '.-':
                return 'a'
        if morse == '-...':
                return 'b'
        if morse == '-.-.':
                return 'c'
        if morse == '-..':
                return 'd'
        if morse == '.':
                return 'e'
        if morse == '..-.':
                return 'f'
        if morse == '--.':
                return 'g'
        if morse == '....':
                return 'h'
        if morse == '..':
                return 'i'
        if morse == '.---':
                return 'j'
        if morse == '-.-':
                return 'k'
        if morse == '.-..':
                return 'l'
        if morse == '--':
                return 'm'
        if morse == '-.':
                return 'n'
        if morse == '---':
                return 'o'
        if morse == '.--.':
                return 'p'
        if morse == '--.-':
                return 'q'
        if morse == '.-.':
                return 'r'
        if morse == '...':
                return 's'
        if morse == '-':
                return 't'
        if morse == '..-':
                return 'u'
        if morse == '...-':
                return 'v'
        if morse == '.--':
                return 'w'
        if morse == '-..-':
                return 'x'
        if morse == '-.--':
                return 'y'
        if morse == '--..':
                return 'z'
        print 'CODE NOT FOUND TRY AGAIN'
        return ''

word = ""
possibilities_dict = {
        "shell": "3.505 MHz",
        "halls": "3.515 MHz",
        "slick": "3.522 MHz",
        "trick": "3.532 MHz",
        "boxes": "3.535 MHz",
        "leaks": "3.542 MHz",
        "strobe": "3.545 MHz",
        "bistro": "3.552 MHz",
        "flick": "3.555 MHz",
        "bombs": "3.565 MHz",
        "break": "3.572 MHz",
        "brick": "3.575 MHz",
        "steak": "3.582 MHz",
        "sting": "3.592 MHz",
        "vector": "3.595 MHz",
        "beats": "3.600 MHz",
}
list = [
        "shell","halls","slick","trick",
        "boxes","leaks","strobe","bistro",
        "flick","bombs","break","brick",
        "steak","sting","vector","beats"
       ]

#################################################
## NICE AND SLOW SCRIPT THAT LOOKS TO SEE WHAT
## POSSIBLE WORDS IN [list] that [word] could be
##################################################
def search(stringlist, substring):
    retval = [];
    for word in stringlist:
        #print word
        for i in range(len(word+word)-len(substring)):
            #print (word+word)[i:i+len(substring)]
            if((word+word)[i:i+len(substring)] == substring):
                #print '******hit******'
                retval.append(word)
                break;
    return retval










#####################################################
## PRINT USAGE
######################################################
def USAGE():
        print 'to use this funciton, enter morse code from bomb'
        print 'in the form of periods as "dits" [.]'
        print 'and dashes as "dahs" [-]'
        print 'EX: -..- is x, and will return 3.535MHz, because'
        print 'boxes, the only word with an x corresponds with that'


CONTINUING = True
USAGE()

poss = list
while CONTINUING:
        morse = raw_input("Letter:")
        word = word + (parse(morse))
        print 'CURRENT WORD is: ', word
        poss = search(poss, word)
        print 'THE POSSIBILITIES ARE: ', poss
        if len(poss) == 1:
                print 'THE ANSWER IS ', possibilities_dict[poss[0]]
                break

