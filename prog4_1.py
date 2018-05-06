def __isNumber(num): # written outside of the class. Python does not allow static methods by default
    try:
        int(num) # string is an integer, unless an exception is raised
        return True
    except ValueError:
        return False # note syntatical convention for true and false

def __isValid(tok):
    validTokens = ["push" , "pop" ,"add" ,"sub" , "mul" ,"div", "mod", "skip", "save", "get"]
    return tok in validTokens or __isNumber(tok) # isNumber has to be second or else breaks

# Takes in input string
# returns the list of the valid tokens , otherwise raise error unexpected token <token>
# return the first invalid token
def Tokenize(str):
    toks = [x for x in str.split(' ') if len(x) > 0]
    invalid = [x for x in toks if not __isValid(x)]
    goodTokens = [x for x in toks if __isValid(x)]
    if len(goodTokens) != len(str.split(' ')): # Are the amount of good tokens equivalent to the amount passed thru?
        raise ValueError("Unexpected token: " + invalid[0]) # first invalid token
    return goodTokens # list of good tokens has been returned

'''
 *  The following tokens must appear by themselves on a single line: pop, add, sub, mul, div, mod, skip
 *  Any other line  that contains a single token is invalid.
 *  The following tokens must appear on a single line of two tokens, in the correct order: push <int>  save <int> get <int> Any other input is invalid.
'''

def __twopart(cmds): # takes in a list
    twoPartCmds = ["push", "save", "get"]
    if(cmds[0]) in twoPartCmds: # Was the first part a two part cmds?
        if __isNumber(cmds[1]): # ok, but is the second part a number?
          return True
        else:
          raise ValueError("second token in two part command is not a number")
    else:
        raise ValueError("Failed to provide permissable two part command")


def __onepart(cmd):
    onePartCmds = ["pop","add","sub","mul","div","mod","skip"]
    if (cmd[0]) in onePartCmds:
        return True
    else:
        raise ValueError("Not a one part command.")


# takes the list! of the tokens that have already been tokenized
# the function will then parse as given the rules as prog2_3 and raise the parse error whenn needed
def Parse(tokenList):
    #if(len(tokens.split(' ')) == 2): # may not be needed
    if(len(tokenList) == 2): # length of the LIST
        __twopart(tokenList)
    else:
        __onepart(tokenList)
