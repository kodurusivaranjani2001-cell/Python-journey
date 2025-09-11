class interview:
    def __init__(self,resume,formal_dress):
        self.resume=resume
        self.formal_dress=formal_dress

    def company1(self,name,time,round1,round2):
        self.name=name
        self.time=time
        self.round1=round1
        self.round2=round2
       # print(self.name,self.time,self.round1,self.round2)
    def snacks(self,snack,tea):
        self.snack=snack
        self.tea=tea
        print(self.snack,self.tea)

#day=interview()  so we cant give instance variables before inheritance and polymorphism i.e,after inheritance and polymorphism are calling 

#day.snacks("samosa","tea")

class interview2(interview):

    def __init__(self,resume,formal_dress):
        super().__init__(resume,formal_dress)


    def company2(self,name,time,round1,round2):
        super().company1(name,time,round1,round2)
    
    def display(self):
        print("Resume:", self.resume, "Formal Dress:", self.formal_dress)
        print("Interview:", self.name, self.time, self.round1, self.round2)
        
    def snacks(self,snack):
        self.snack=snack
        print("only snack given:",self.snack)

        
        
day=interview2("strong resume","yes")
day.company1("sita","9 am"," round one cleared","we will maill u the result of round2")
day.display()
day.snacks("samosa")



