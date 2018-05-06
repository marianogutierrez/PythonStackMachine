
class StackMachine:
    def __init__(self):
        self.currentline = 1 # public
        self.__stack = [] # indication for private
        self.__memory = {} # far easier as a dictionary

    def Execute(self,toks): # takes in a list
    # some loop to check what it is and then to
        for i in range(0,len(toks)):
            tok = toks[i]
            if tok == 'push': # is the item in the list "push?"
                self.__stack.append(int(toks[i+1])) # push the number onto the stack
                self.currentline = self.currentline + 1
                #i = i + 1; # increment the counter because we have consumed the number
            elif tok == 'pop': # ONLY TIME SOMETHING IS RETURNED
                if not self.__stack: # If the stack is empty, then you cannot pop
                    raise IndexError("Invalid Memory Access")
                    return
                val = int(self.__stack.pop())
                self.currentline = self.currentline + 1
                return val
            elif tok == 'add':
                if len(self.__stack) < 2:
                    raise IndexError("Invalid Memory Access")
                    return
                val1 = self.__stack.pop() # note we have strings here
                num1 = int(val1)
                val2 = self.__stack.pop()
                num2  = int(val2)
                result = num1 + num2
                self.__stack.append(result)
                self.currentline = self.currentline + 1
            elif tok == 'sub':
                if len(self.__stack) < 2:
                    raise IndexError("Invalid Memory Access")
                    return
                val1 = self.__stack.pop()
                num1 = int(val1)
                val2 = self.__stack.pop()
                num2 = int(val2)
                result = num1 - num2
                self.__stack.append(result)
                self.currentline = self.currentline + 1
            elif tok == 'mul':
                if len(self.__stack) < 2:
                    raise IndexError("Invalid Memory Access")
                    return
                val1 = self.__stack.pop()
                num1 = int(val1)
                val2 = self.__stack.pop()
                num2 = int(val2)
                result = num2 * num1
                self.__stack.append(result)
                self.currentline = self.currentline + 1
            elif tok == 'div':
                if len(self.__stack) < 2:
                    raise IndexError("Invalid Memory Access")
                    return
                val1 = self.__stack.pop()
                num1 = int(val1)
                val2 = self.__stack.pop()
                num2 = int(val2)
                result = num1 / num2
                self.__stack.append(result)
                self.currentline = self.currentline + 1
            elif tok == 'mod':
                if len(self.__stack) < 2:
                    raise IndexError("Invalid Memory Access")
                    return
                val1 = self.__stack.pop()
                num1 = int(val1)
                val2 = self.__stack.pop()
                num2 = int(val2)
                result = num1 % num2
                self.__stack.append(result)
                self.currentline = self.currentline + 1
            elif tok == "skip":
                    if  len(self.__stack) < 2 :
                        raise IndexError("Invalid Memory Access")
                        return
                    val1 = self.__stack.pop()
                    val2 = self.__stack.pop()
                    if val1 == 0:
                        #self.currentline = 0
                        num2 = int(val2)
                        self.currentline = num2
            elif tok == "save":
                if not self.__stack: # if the stack is empty well... cant do much
                    raise IndexError("Invalid Memory Access")
                    return
                memIdx = int(toks[i+1]) # where are we are going to save the val at the top of the stack?
                #if memIdx not in self.__memory: # dictionary
                    #raise IndexError("Invalid Memory access")
                val1 = self.__stack.pop()
                num1 = int(val1)
                #self.__memory.insert(val1,memIdx) # insert rather than append handles this problem
                self.__memory[memIdx] = num1
                self.currentline = self.currentline + 1
                #i = i + 1 # increment
            elif tok == "get": # get from the memory location index
                if not self.__memory: # cant get anything if the nothing was ever saved
                    raise IndexError("Invalid Memory Access")
                    return
                memIdx = int(toks[i+1]) # the number that follows the get command
                if memIdx not in self.__memory: # check if the key was in the dictionary
                    raise IndexError("Invalid Memory Access")
                    return
                result = self.__memory[memIdx]
                self.__stack.append(result) # Now, slap it onto the stack
                self.currentline = self.currentline + 1
                #i = i + 1 #increment


    '''
    The Execute(tokens) function should accept a list of tokens that has previously been Tokenized
and Parsed correctly. The Execute function will then perform the operation defined in the list of
tokens as specified by the operation. (Not all operations will return a value, some will):

• push # -- Pushes the number onto the stack. Returns None.
• pop -- Pops the top of the stack. Returns the popped value.
• add -- Pops two values off the stack, adds them pushes the result. Returns None.
• sub -- Pops two, subtracts the second from the first, pushes result. Returns None.
• mul -- Pops two, multiples, pushes result. Returns None.
• div -- Pops two, divides the first by the second, pushes result. Returns None.
• mod -- Pops two, remainder of first divided by second, pushes result. Returns None.
• skip -- Pops two, if the first value is ZERO, changes the CurrentLine property by the
second value. If the first value is not zero, nothing extra occurs. Returns None.
• save # -- Pops one, saves that value for future retrival. Returns None.

• get # -- Pops zero. Gets a previously saved value and pushes it on the stack. A saved
value may be gotten multiple times. For example, if the top of the stack is 3, and the
‘save 1’ operation occurs, the 3 is popped off the stack and saved to some ancillary
memory (probably a list). Then whenever a ‘get 1’ operation is executed that value of 3
is pushed onto the stack until the value stored in memory 1 is replaced with a different
‘save 1’ operation. (You can think about this as hard array access if you like… because
that’s what memory really is). Returns None.

Whenever the Execute(tokens) function finishes executing the operation specified by the
tokens, the property CurrentLine is incremented by 1.
If, at any time, your program attempts to pop a value that doesn’t exist, or get a value that
has not previously been saved, raise an IndexError with the message “Invalid Memory
Access”.
    '''
