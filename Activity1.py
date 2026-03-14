class A:
    def __init__(self,a):
        self.a= a 
    def __check__(self, other):
        if(self.a<other.a):
            return "obj1 is less than obj2"
        else:
            return "obj2 is less than obj1"
    def __equal__(self, other):
        if(self.a==other.a):
            return " both are equal"
        else:
            return " not equal"

obj1=A(2)
obj2=A(3)
print("passed values:",obj1.a,obj2.a)
print(obj1 < obj2)
ob=A(4)
ob2=A(4)
print("passed value:",ob.a,ob2.a)
print(ob==ob2)