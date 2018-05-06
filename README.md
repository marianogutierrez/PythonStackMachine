Mariano Gutierrez
margutierrez75@gmail.com

Included Files:
prog4_1.py
prog4_2.py
prog4_3.py

The purpose of this program was to practice tokenization and parsing as done in
program 2. The difference being was to approcah the problem in a pythonic way.

Notes on prog4_1:
    This part of the program made extenisve use of list comprehsnsions and some 
    of pythons helpful syntax not avaliable in other lanauges. For example, list
    comprehensions with the use of "in" were used to greatly simplify checking
    to see if the given tokens were indeed valid. Thus, simplifying the tokenization
    and parsing process. Besides that, the program is of the same functionality and purpose and was the C++
    program in prog2_2. 
    
Notes on prog4_2:
    This program implments a simple stack machine with
    an ancillary stack and dictionary for "memory." It is a behemoth of if-else if. 
    The purpose was to feed the program  a list of already Tokenized and Parsed tokens, 
    so that it can execute in a stack machine like fashion. 
    The stack is used to hold numerical values, and dictionary is used 
    to serve as the computers "memory." By using a dictionary, the commands for
    "get #idx in memory" and "save idx" were greatly simplified, as the error checking to 
    see if the index was valid was easy to implement. In addition, anytime anything
    is requested to be popped of the stack, error checking ensures that the stack
    is of length 2 or is at least not empty. 

Notes on prog4_3:
    This program serves as a driver for the two programs above. It reads a file with
    code that the stack machine can understand, and begins to execute it.
    The process is like this:
    1) Clean up the code in the text file, by rmeoving incidental white space and tab
    characters.
    2) Tokenize the file line by line
    3) Parse the file line by line.
    4) Execute the instructions. If the "pop" command is detected, then the output is
    printed to standard out. Otherwise, the instruction continues as normal.
    If aat anytime the users skip command for an unconditional jump occurs and produces
    a negative line, an error is raised. An error is also raised whenever memory attemped to
    be accessed is invalid, i.e. the memory in the stack machine instantiated does memory
    in the nedex requested a.k.a a null access. 
    
    
    
    
