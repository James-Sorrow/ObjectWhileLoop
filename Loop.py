class Loop:
    def __init__(self,iterations,func,arg=None):
        self.func = func
        self.iterations = iterations
        self.current = 0
        self._arg = arg
        self._iteration_finished:bool = False

    @property
    def arg(self):
        return self._arg
    
    @arg.setter
    def arg(self,arg):
        self._arg = arg

    def __iter__(self):
        return self
    
    @property
    def iteration_finished(self):
        return self._iteration_finished
    
    def __next__(self):
        self._iteration_finished = False
        if self.current < self.iterations:
            if self.arg != None:
                result = self.func(self.arg)
            else:
                result = self.func()
            self.current += 1
        else:
            raise StopIteration
        self._iteration_finished = True
        return result
        
    def manual_next(self):
        self._iteration_finished = False
        if self.current < self.iterations:
            if self.arg != None:
                result = self.func(self.arg)
            else:
                result = self.func()
            self.current += 1
        else:
            raise StopIteration
        self._iteration_finished = True
        return result
    
    async def async_manual_next(self):
        self._iteration_finished = False
        if self.current < self.iterations:
            if self.arg != None:
                result = self.func(self.arg)
            else:
                result = self.func()
            self.current += 1
        else:
            raise StopIteration
        self._iteration_finished = True
        return result