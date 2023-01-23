from WhileObjects import While

#Custom while loop overriding step function's calc interface
class customLoop(While):

    def step(self):
        if self.op == "<" or self.op == "<=":
            if not self.isFinished():
                self.calc += self.i
                self.i += self.increment
        elif self.op == ">" or self.op == ">=":
            if not self.isFinished():
                self.calc += self.i
                self.i -= self.increment            
        return self.i

#Instantiating the custom loop and getting finished calculation
loop = customLoop(i=0,end=10)
while not loop.isFinished():
    loop.step()

print(loop.calc)
