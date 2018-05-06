class StackMachine:
    def __init__(self):
        self.currentline = 0 # public
        self.__stack = [] # indication for private
        self.__memory = {} # far easier as a dictionary

    def Execute(self,toks): # takes in a list
    # some loop to check what it is and then to
        for i in range(0,len(toks)):
            tok = toks[i]
            if tok == 'push': # is the item in the list "push?"
                self.__stack.append(int(toks[i+1])) # push the number onto the stack
                self.currentline = self.currentline + 1
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
                    if int(val1) == 0:
                        num2 = int(val2)
                        self.currentline = self.currentline +1 + num2 # plus 1 to compensate
                    else:
                        self.currentline = self.currentline + 1 
            elif tok == "save":
                if not self.__stack: # if the stack is empty well... cant do much
                    raise IndexError("Invalid Memory Access")
                    return
                memIdx = int(toks[i+1]) # where are we are going to save the val at the top of the stack?
                val1 = self.__stack.pop()
                num1 = int(val1)
                self.__memory[memIdx] = num1
                self.currentline = self.currentline + 1
            elif tok == "get": # get from the memory location index
                if not self.__memory: # cant get anything if the nothing was ever saved
                    raise IndexError("Invalid Memory Access")
                    return
                memIdx = int(toks[i+1]) # the number that follows the get command
                if memIdx not in self.__memory: # check if the key was in the dictionary
                    raise IndexError("Invalid Memory Access")
                    return
                result = int(self.__memory[memIdx])
                self.__stack.append(result) # Now, slap it onto the stack
                self.currentline = self.currentline + 1
