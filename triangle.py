class rectangle :

    def __init__(self,length,breadth):
        self.length = length     
        self.breadth = breadth

    def info(self):            
        print("length of rectangle is:",self.length)            
        print("breadth of rectangle is:",self.breadth)                       

    def area(self):
        return (self.length*self.breadth)
                        
    def perimeter(self):
        return(2*self.length+2*self.breadth)

        

l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))

r1=rectangle(l , b)                    
print("rectangle details:")                    
r1.info()                    
print("")                    
print("area of rectangle is:",r1.area())
print("")
print("perimeter of rectangle is:",r1.perimeter())


                






