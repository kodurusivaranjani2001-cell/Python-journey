#  hospital and patients
class Patients:
    def __init__(self,problem,ward,patient_num):
        self.problem=problem
        self.ward=ward
        self.patient_num=patient_num

class Hospital:
    def __init__(self):
        self.patients=[]
    
    def admit_patient(self,patient):
        self.patients.append(patient)
        print(f"{patient.patient_num} with prob {patient.problem} admits in {patient.ward}")
        
    def discharge_patient(self,patient_num):
        for patient in self.patients:
            if patient.patient_num== patient_num:
                print(f"patient gud {patient.patient_num} discharge from ward{patient.ward}")
                
            else:
                print(f"no patient is found with patient num {patient_num}")
    def list_patients(self):
        if not self.patients:
            print("no patients are admitted")
        else:
            for patient in self.patients:
                print(f"  patients list is {patient.patient_num} : {patient.ward}")
                           
my_hospital=Hospital()        
p1=Patients("heart",1,"pn 12")
p2=Patients("fever",4,"pn 45")              
my_hospital.admit_patient(p1)
my_hospital.discharge_patient(34)  
my_hospital.list_patients()    

#  school and teachers
class Teachers:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
        
class School:
    def __init__(self):
        self.teachers=[]
    def add_teachers(self,teacher):
        self.teachers.append(teacher)
        print(f"{teacher.name} teaches {teacher.subject}")
    def list_teachers(self):
        if not self.teachers:
            print("no teachers in the school")
        else:
            print("teachers in the school")
            for teacher in self.teachers:
                print(f"{teacher.name} teaches {teacher.subject}")
                
my_school=School()        
t1=Teachers("mam1","eng")
t2=Teachers("mam2","maths")
my_school.add_teachers(t1)
my_school.add_teachers(t2)
my_school.list_teachers()
            
## restaurent and menu items
class menu_items:
    def __init__(self,item_name,cost,quantity_sold=0):
        self.item_name=item_name
        self.cost=cost
        self.quantity_sold=quantity_sold
class Restaurant:
    def __init__(self):
        self.items=[]
    def add_items(self,item):
        self.items.append(item)        
        print(f"{item.item_name} cost is {item.cost}")
    def remove_item(self,cost):
        for item in  self.items:
            if item.cost==cost:
                self.items.remove(item)
                print(f"remove {item.item_name} with cost {cost}")
                return
            
        print( f"no item is   available with that {cost}" )
    def total_revenue(self):
        total = 0
        #self.quantity=quantity

        for item in self.items:
            total += item.cost * item.quantity_sold
        print(total)
        return
        
item1=menu_items("maggie",100,20)
item2=menu_items("biryani",250,15)
menu=Restaurant()
menu.add_items(item1)
menu.add_items(item2)
menu.remove_item(250)
menu.total_revenue()
# university and course

class course:
    def __init__(self,name,students):
        self.name=name
        self.students=students

    def __str__(self):
        return f"{self.name} and {self.students}"
class university:
    def __init__(self):
        self.courses=[]
    def add_courses(self,course):
        self.courses.append(course)
    def total_students(self):
        total=0
        for course in self.courses:
            total=total+course.students
        print(total)
        
c=university()
c1=course("eng",30)
c2=course("mat",40)
c.add_courses(c1)
c.add_courses(c2)
for course in c.courses:
    print(course)
        
c.total_students()

# zoo and animals
    

class animals:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
        
    
class zoo:
    def __init__(self):
        self.animals=[]
    def add_animal(self,animal):
        self.animals.append(animal)
        print(f"added:{animal.name}")

    def remove_animal(self,name):
        for animal in self.animals:
            if animal.name==name:
                self.animals.remove(animal)
                print(f"remove animal {animal.name}")
                return
            
        print("no animal name found",{name})

    def list_all(self):
        print("all animals in zoo")
        for animal in self.animals:
            if not self.animals:
                print("no animals")
            else:
                print("animals in zoo",{animal.name})
                 
an1=animals("monkey")
an2=animals("zebra")
z=zoo()
z.add_animal(an1)
z.add_animal(an2)
z.remove_animal("monkey")
z.remove_animal("lion")
z.list_all()
            
        
# smart home automation
class device:
    def __init__(self,name):
        self.name=name
        self.is_on=False
    def turn_on(self):
        self.is_on=True
        print(f"{self.name} is now on")
    def turn_off(self):
        self.is_on=False
        print(f"{self.name} is now off")
    def status(self):
        return f"{self.name}:{'on' if self.is_on else 'off'}"

class smarthome:
    def __init__(self):
        self.devices=[] # store devices objects
    def add_device(self,device):
        self.devices.append(device)
        print(f"added device: {device.name}")

    def turn_off_all_devices(self):
        if not self.devices:
            print("no devices in smarthome")
        else:
            print("turning of all devices")
            for device in self.devices:
                device.turn_off()

    def list_devices(self):
        if not self.devices:
            print("no devices connnected")
        else:
            print("devices in smarthome:")
            for device in self.devices:
                print(device.status())
                
    def turn_on_all_devices(self):
        if not self.devices:
            print("No devices in the SmartHome")
        else:
            print("Turning on all devices...")
            for device in self.devices:
                device.turn_on()
    def control_device(self, name, action):       # Control a specific device by name
        for device in self.devices:               # Look through all devices
            if device.name.lower() == name.lower():   # Case-insensitive match
                if action.lower() == "on":            # If action is "on"
                    device.turn_on()                  # turn it ON
                elif action.lower() == "off":         # If action is "off"
                    device.turn_off()                 # turn it OFF
                else:
                    print("Invalid action! Use 'on' or 'off'.")  # Guard against typos
                return                               # Stop after handling one matching device
        print(f"No device named '{name}' found.")     # If loop ended, device wasn't found          

home=smarthome()
light=device("light")

fan=device("fan")
ac=device("ac")
home.add_device(light)
home.add_device(fan)

home.add_device(ac)

light.turn_on()
fan.turn_on()
home.list_devices()

home.turn_off_all_devices()
home.list_devices()

home.turn_on_all_devices()
home.list_devices()
home.control_device("Light", "on") # Find "Light" and turn it ON
home.control_device("AC", "on")    # Find "AC" and turn it ON
home.control_device("Fan", "off")  # Find "Fan" and ensure it's OFF
home.control_device("TV", "on")    # Try to control a non-existent device -> 








