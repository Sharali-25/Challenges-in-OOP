class Roman:
    def __init__(self,num):
        self.num=num
    def convert(self):
        n=self.num
        roman= ""
        while n>=10:
            roman=roman+"x"
            n=n-10
        number=int(input("Enter a number: "))
        r=Roman(number)
        print("Roman numeral is:",r.converted)