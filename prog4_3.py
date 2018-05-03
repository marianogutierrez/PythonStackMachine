import sys
from prog4_2.py import StackMachine
from prog4_1.py import Tokenize
from prog4_1.py import Parse

if __name__ == "__main__":
    main()

def main():
    print("Assignment #4-3, Mariano Gutierrez, margutierrez75@gmail.com\n")
    with open(sys.argv[1],mode = 'r') as f: # file resource will auto close once out of scope mode is set to read
        code = [x.strip() for x in f.readlines()] # strip off trailing or additonal white space
        fileLines = len(code) # code alread has the length so we are good to go
        fileLines = len(f.readlines) # can also do this
        code = [x for x in code if len(x) > 0]  # ok ensure that we dont have blanks inputted
        goodTokens = [Tokenize(x) for x in code] # just tokenize everything 
        # needs to be split to get correct

        # Tokenization process complete. Onward to Parsing
        for line in f:
            parse(line) # parse line by line

        # Parsing complete

        machine = StackMachine() # instantiate new machine; no need to use the 'new' keyword
        #execution process begins

        while(machine.__currentline <= filelines)
            if(machine.__currentline < 0) # if at anytime current line proprty becomes zero
                print("Trying to execute an invalid line: " + machine.__currentline)
            try:
                for i in range (0,len(goodTokens))
                    machine.Execute(goodTokens) # process the tokens but not line by line..?
            except IndexError("Line " + machine.__line + goodTokens[i])

        # Nothing broke
    print("Program terminated correctly")
    return 0

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


    '''
    # tokenize and parse all lines of the file
    # Tokenize first before parsing
    # a list structure then is used
    # start indexing at zero
    #instantiate stack machine
    # execute instructions line by line as determined by
    # the current line property UNTILL cline property
    # is equal or greater than the numer of lines in
    # the file
    # currentLine >= # lines in file program should prpint
    "Program terminated correctly" and quit
    If at any time the the line becomes negative print
    "Trying to execute an invalid line: # " and quick
    '''
