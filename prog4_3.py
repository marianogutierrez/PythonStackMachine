'''
@author: marianogutierrez
'''

import sys
from prog4_2 import StackMachine
from prog4_1 import Tokenize
from prog4_1 import Parse


def main():
    print("Assignment #4-3, Mariano Gutierrez, margutierrez75@gmail.com")
    with open(sys.argv[1],mode = 'r') as f: # file resource will auto close once out of scope mode is set to read
        code = [x.replace('\t',' ').strip() for x in f.readlines()] # auto grader broken and had to include tabs
        filelines = len(code) - 1 # -1 because our program begins at line zero 
        toks = [x for x in code if len(x) > 0]  # ok ensure that we dont have blanks inputted
        goodTokens = [Tokenize(x) for x in toks] # just tokenize everything
        # list within a list, which is what we want...! Each inner list is a line

        # Tokenization process complete. Onward to Parsing
        for line in goodTokens: #  This is equivalent to: for i in range(0,len(goodTokens)):
            Parse(line)
        
        machine = StackMachine() # instantiate new machine; note no need to use the 'new' keyword
       
        toexec = "nothing yet..."
        #while(machine.currentline <= filelines):
            #try: # need to change because dictated by current line property
        i = 0
        try:
                while machine.currentline <= filelines: 
                    #toexec = line
                    toexec = goodTokens[i]
                    if toexec[0] == 'pop': # recall it is a list and I need to use []
                        print(machine.Execute(toexec))
                        i = machine.currentline
                    else:
                        machine.Execute(goodTokens[i])
                        i = machine.currentline
                if(machine.currentline < 0): 
                    print("Trying to execute invalid line: " + str(machine.currentline))
                    return
        except IndexError:
            toprint = ""
            if(len(toexec) == 2):
                str1 = toexec[0]
                toprint = str1 + " " + toexec[1]
            else:
                toprint = toexec[0]
            print("Line " + str(machine.currentline) + ": "  + "\'" + toprint + "\'" + " caused Invalid Memory Access")
            return

    # Nothing broke if we get to this point
    print("Program terminated correctly")
    return 0


if __name__ == "__main__":
    main()
