import sys
from prog4_2 import StackMachine
from prog4_1 import Tokenize
from prog4_1 import Parse


def main():
    print("Assignment #4-3, Mariano Gutierrez, margutierrez75@gmail.com\n")
    with open(sys.argv[1],mode = 'r') as f: # file resource will auto close once out of scope mode is set to read
        code = [x.strip() for x in f.readlines()] # strip off trailing or additonal white space
        filelines = len(code) # code alread has the length so we are good to go
        toks = [x for x in code if len(x) > 0]  # ok ensure that we dont have blanks inputted
        goodTokens = [Tokenize(x) for x in toks] # just tokenize everything
        # list within a list, which is what we want...! Each inner list is a line
        #print(goodTokens) debug

        # Tokenization process complete. Onward to Parsing
        for line in goodTokens: #  This is equivalent to: for i in range(0,len(goodTokens)):
            toparse = line # give me the first list
            Parse(toparse)
        # Parsing complete
        machine = StackMachine() # instantiate new machine; note no need to use the 'new' keyword
        #execution process begins
        # file lines are indeed correct
        #print('no lines: ' + str(filelines))
        #print()
        toexec = "nada"
        while(machine.currentline <= filelines):
            if(machine.currentline < 0): # if at anytime current line proprty becomes zero
                print("Trying to execute an invalid line: " + str(machine.currentline))
                return
            try:
                for line in goodTokens:
                    toexec = line
                    if toexec[0] == 'pop': # recall it is a list and I need to use []
                        print(machine.Execute(toexec))
                    else:
                        machine.Execute(toexec)
            except IndexError:
                print("Line " + str(machine.currentline) + " "  + str(toexec[0]) + " caused Invalid Memory Access")
                # could strip [] or something if necessary above
                return #

    # Nothing broke if we get to this point
    print("Program terminated correctly")
    return 0


if __name__ == "__main__":
    main()

'''
prog4_3.py In python, you are going to implement a driver program. You should import the
functions/classes you have implemented in prog4_1.py and prog4_2.py. Your driver should use
a main function specification and read the first command line argument as a file.

 Your program should tokenize and parse all of the lines of the file. You should tokenize all of the lines before
you begin parsing (same behavior as assignment #2). Your program should then parse all of the
lines. As all of the lines have been tokenized and parsed, they should be stored in an indexable
structure so that you can randomly get the tokens for any line by line number (start indexing at
0).

Your program should then instantiate a StackMachine class and it should then begin
executing operations one line at a time, dictated by the StackMachine CurrentLine property.
This should continue until the StackMachine CurrentLine property is equal to or greater than the
number of lines in the file (because the first line is index at zero and is line zero internally).

If at any time the StackMachine raises an IndexError your program should print the IndexError
message along with the line number that currently caused it with the following message: “Line
#: ‘<tokens>’ caused Invalid Memory Access.” For example: “Line 3: ‘pop’ caused Invalid
Memory Access”.

If any of the Execution(tokens) calls returns a non-None value, it should be
printed on its own line to STDOUT. If at anytime the CurrentLine property becomes negative,
print the following message: “Trying to execute invalid line: #” and quit. For example: “Trying to
execute invalid line: -5”


When your StackMachine stops running naturally (CurrentLine >= # of lines in input file) your
program should print: “Program terminated correctly” and quit.

just means when out of the damn loop
'''
