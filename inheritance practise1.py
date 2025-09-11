# legacy money ---> cash,property, gold
class legacymoney:
    #  value of money family members known :wife son
    # outsider see what value money--> property
    houses=3
    worths="10 cr"
    def __init__(self,gold):
        self.houses={"hyderabad":"2 cr","bangalore":"4 cr"}
        self.cash=5000000
        self.gold=gold
        print(self.houses,self.cash,self.gold)
    @staticmethod
    def outsiders():
        print(legacymoney.houses,legacymoney.worths)

venkat=legacymoney("1kg")
suresh=legacymoney("2 kg")

# your money ---> salary
class companymoney:
    working="infosys"
    salary="70000"

    def __init__(self,designation,performance,challenge,workoverload):
        self.designation=designation
        self.performance=performance
        self.challenge=challenge
        self.workoverload=workoverload
        print(self.designation,self.performance,self.challenge, self.workoverload)
    def display(self):
        print(self.designation,self.performance)

venkat=companymoney("se","good","mentoring",True)
venkat.display()
# fiture money --> salary, legacy money USING INERTANCE

class futuremoney(legacymoney,companymoney):

    def __init__(self,houses,worths):
        companymoney.__init__(self,"se","good","mentoring",True)
        self.houses=houses
        self.worths=worths
        print("futuremoney")

venkat=futuremoney(1,"2 cr")
print(venkat.houses)
venkat.display()
    


        
        
    
    
    
    
        
        
    
