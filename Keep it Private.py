class myClass:
    
    _privateVar = 27
    
    def __privMeth(self):
        print("I'm inside class myClass")
        
    def hello(self):
        print(f"Private Variable Value: ",myClass.__privateVar)
        
foo = myClass()

#print(foo.__privateVar)
#foo.__privMeth

foo.hello()