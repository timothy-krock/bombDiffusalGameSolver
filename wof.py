############################################
##  PROGRAM FOR THE WHO'S ON FIRST
##  MODULE OF THE BOMB DIFFUSAL GAME
##  WRITTEN BY TIM KROCK
###########################################

display = {
    'yes': 'left middle',
        'first': 'top right',
        'display': 'bottom right',
        'okay': 'top right',
        'says': 'bottom right',
        'nothing': 'left middle',
        '[]': 'bottom left',
        '': 'bottom left',
        'blank': 'right middle',
        'no': 'bottom right',
        'led': 'left middle',
        'lead': 'bottom right',
        'read': 'right middle',
        'red': 'right middle',
        'reed': 'bottom left',
        'leed': 'bottom left',
        'hold on': 'bottom right',
        'you': 'right middle',
        'you are': 'bottom right',
        'your': 'right middle',
        "you're": 'right middle',
        'youre': 'right middle',
        'ur': 'top left',
        'u r': 'top left',
        'there': 'bottom right',
        "they're": 'bottom left',
        'theyre': 'bottom left',
        'their': 'right middle',
        'they are': 'left middle',
        'see': 'bottom right',
        'c': 'top right',
        'cee': 'bottom right'
}
arrays = {
    "ready":    ["YES", "OKAY", "WHAT", "MIDDLE",
                 "LEFT", "PRESS", "RIGHT", "BLANK",
                 "READY", "NO", "FIRST", "UHHH",
                 "NOTHING", "WAIT"
                 ],
                 "first":    ["LEFT", "OKAY", "YES", "MIDDLE",
                              "NO", "RIGHT", "NOTHING", "UHHH",
                              "WAIT", "READY", "BLANK", "WHAT",
                              "PRESS", "FIRST"
                              ],
                 "no":       ["BLANK", "UHHH", "WAIT", "FIRST",
                              "WHAT", "READY", "RIGHT", "YES",
                              "NOTHING", "LEFT", "PRESS",
                              "OKAY", "NO", "MIDDLE"
                              ],
                 "blank":    ["WAIT", "RIGHT", "OKAY", "MIDDLE",
                              "BLANK", "PRESS", "READY", "NOTHING",
                              "NO", "WHAT", "LEFT", "UHHH", "YES",
                              "FIRST"
                              ],
                 "nothing":  ["UHHH", "RIGHT", "OKAY", "MIDDLE",
                              "YES", "BLANK", "NO", "PRESS",
                              "LEFT", "WHAT", "WAIT", "FIRST",
                              "NOTHING", "READY"
                              ],
                 "yes":      ["OKAY", "RIGHT", "UHHH", "MIDDLE",
                              "FIRST", "WHAT", "PRESS", "READY",
                              "NOTHING", "YES", "LEFT", "BLANK",
                              "NO", "WAIT"
                              ],
                 "what":     ["UHHH", "WHAT", "LEFT", "NOTHING",
                              "READY", "BLANK", "MIDDLE", "NO",
                              "OKAY", "FIRST", "WAIT", "YES",
                              "PRESS", "RIGHT"
                              ],
                 "uhhh":     ["READY", "NOTHING", "LEFT", "WHAT",
                              "OKAY", "YES", "RIGHT", "NO", "PRESS",
                              "BLANK", "UHHH", "MIDDLE", "WAIT",
                              "FIRST"
                              ],
                 "left":     ["RIGHT", "LEFT", "FIRST", "NO",
                              "MIDDLE", "YES", "BLANK", "WHAT",
                              "UHHH", "WAIT", "PRESS", "READY",
                              "OKAY", "NOTHING"
                              ],
                 "right":    ["YES", "NOTHING", "READY", "PRESS",
                              "NO", "WAIT", "WHAT", "RIGHT",
                              "MIDDLE", "LEFT", "UHHH", "BLANK",
                              "OKAY", "FIRST"
                              ],
                 "middle":   ["BLANK", "READY", "OKAY", "WHAT",
                              "NOTHING", "PRESS", "NO", "WAIT",
                              "LEFT", "MIDDLE", "RIGHT", "FIRST",
                              "UHHH", "YES"
                              ],
                 "okay":     ["MIDDLE", "NO", "FIRST", "YES",
                              "UHHH", "NOTHING", "WAIT", "OKAY",
                              "LEFT", "READY", "BLANK", "PRESS",
                              "WHAT", "RIGHT"
                              ],
                 "wait":     ["UHHH", "NO", "BLANK", "OKAY",
                              "YES" "LEFT", "FIRST", "PRESS",
                              "WHAT", "WAIT", "NOTHING", "READY",
                              "RIGHT", "MIDDLE"
                              ],
                 "press":    ["RIGHT", "MIDDLE", "YES", "READY",
                              "PRESS", "OKAY", "NOTHING", "UHHH",
                              "BLANK", "LEFT", "FIRST", "WHAT",
                              "NO", "WAIT"
                              ],
                 "you":      ["SURE", "YOU ARE", "YOUR", "YOU'RE",
                              "NEXT", "UH HUH", "UR", "HOLD", "WHAT?",
                              "YOU", "UH UH", "LIKE", "DONE", "U"
                              ],
                 "you are":  ["YOUR", "NEXT", "LIKE", "UH HUH",
                              "WHAT?", "DONE", "UH UH", "HOLD",
                              "YOU", "U", "YOU'RE", "SURE", "UR",
                              "YOU ARE"
                              ],
                 "your":     ["UH UH", "YOU ARE", "UH HUH", "YOUR",
                              "NEXT", "UR", "SURE", "U", "YOU'RE",
                              "YOU", "WHAT?", "HOLD", "LIKE", "DONE"
                              ],
                 "you're":   ["YOU", "YOU'RE", "UR", "NEXT", "UH UH",
                              "YOU ARE", "U", "YOUR", "WHAT?", "UH HUH",
                              "SURE", "DONE", "LIKE", "HOLD"
                              ],
                 "youre":    ["YOU", "YOU'RE", "UR", "NEXT", "UH UH",
                              "YOU ARE", "U", "YOUR", "WHAT?", "UH HUH",
                              "SURE", "DONE", "LIKE", "HOLD"
                              ],
                 "ur":       ["DONE", "U", "UR", "UH HUH", "WHAT?",
                              "SURE", "YOUR", "HOLD", "YOU'RE", "LIKE",
                              "NEXT", "UH UH", "YOU ARE", "YOU"
                              ],
                 "u":        ["UH HUH", "SURE", "NEXT", "WHAT?",
                              "YOU'RE", "UR", "UH UH", "DONE", "U",
                              "YOU", "LIKE", "HOLD", "YOU ARE", "YOUR"
                              ],
                 "uh huh":   ["UH HUH", "YOUR", "YOU ARE", "YOU",
                              "DONE", "HOLD", "UH UH", "NEXT",
                              "SURE", "LIKE", "YOU'RE", "UR",
                              "U", "WHAT?"
                              ],
                 "uh uh":    ["UR", "U", "YOU ARE", "YOU'RE", "NEXT",
                              "UH UH", "DONE", "YOU", "UH HUH", "LIKE",
                              "YOUR", "SURE", "HOLD", "WHAT?"
                              ],
                 "what?":    ["YOU", "HOLD", "YOU'RE", "YOUR",
                              "U", "DONE", "UH UH", "LIKE", "YOU ARE",
                              "UH HUH", "UR", "NEXT", "WHAT?", "SURE"
                              ],
                 "done":     ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR",
                              "UR", "YOU'RE", "HOLD", "LIKE", "YOU", "U",
                              "YOU ARE", "UH UH", "DONE"
                              ],
                 "next":     ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", 
                              "SURE", "NEXT", "LIKE", "DONE", "YOU ARE", 
                              "UR", "YOU'RE", "U", "YOU"
                              ],
                 "hold":     ["YOU ARE", "U", "DONE", "UH UH", "YOU", 
                              "UR", "SURE", "WHAT?", "YOU'RE", "NEXT", 
                              "HOLD", "UH HUH", "YOUR", "LIKE"
                              ],
                 "sure":     ["YOU ARE", "DONE", "LIKE", "YOU'RE", 
                              "YOU", "HOLD", "UH HUH", "UR", "SURE", 
                              "U", "WHAT?", "NEXT", "YOUR", "UH UH"
                              ],
                 "like":     ["YOU'RE", "NEXT", "U", "UR", "HOLD", 
                              "DONE", "UH UH", "WHAT?", "UH HUH", 
                              "YOU", "LIKE", "SURE", "YOU ARE", 
                              "YOUR"
                              ]
}

#######################################
# USAGE:
#######################################
print 'Type in the label on the module, and then the word'
print 'corresponding with the position returned by the program'
print 'after that, read off the list of words until one appears'
print 'on the bomb module. Type that in and repeat'
print 'type quit to exit, or press ctrl+c'

while(1):
    ##############
    # GET INPUT
    #############
    
    options = []
        
        print "########   LINE    ########"
        
        word = raw_input("word:");
        if word == 'quit':
            exit(0)
        
        ########
        #OUTPUT
        ########
        
        print "########  SELECT  ########"
        print 'select',display[word]
        
        
        
        
        word = raw_input("word:");
        if word == 'quit':
            exit(0)
        print "########## WORDS #########"
        for i in arrays[word]:
            print i



