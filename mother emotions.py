
# mother two children --> son,daughter

mother={"son":"venkat","daughter":"ramya"}
#mother activity
#affection& love
#step1 -- happy
#step2 -- living for you
#step -- emotional separated without 1hr

# let u visit a temple son is missing 
plan="ganesha "
time="9am"
family=("husband","mother","son1","daughter")
print("missing son",family[2])
worry=[]


if family[2] == "son1":
    worry.append(family[1])
    worry.append(family[0])
    

print(worry)
#outcome of data from tuple to list in above code
    
#cooking

preparedvegbiryani={"rice":"2cup","carrot":"100 gm","beans":"100gm"}
stove=("empty1","rice cooker","milk","empty2")

ricecooker = []

for i,j in preparedvegbiryani.items():
    print("item added",i,j)
    ricecooker.append(j)

print(ricecooker)

# outcome from one dictionary to list in above code

#cleaning house,cloths,dressing

#struggles & worries

presentlife={"husband":"salaried employees","house expences":1000,"suppor":5000,"habbits":"drinking"}
worries={}

if presentlife["husband"]=="salaried employees":
    happy="smiling"
    print(happy)
elif presentlife["husband"]=="idle" and presentlife["habbits"]=="drinking" :
    worries.update({"house concerns":presentlife["house expences"]})
    worries.update({"fight":"2 hours"})

print(worries)

#data copied from one dictionary to anther worries dictionary
























