# a father has 3 children

father={"son1":"house1","son2":"house2","daughter":"land"}

#property=("house1","house2","land")
#fathersettlement=()
for i, j in father.items():
    print(" settlement",i,j)

#else:
   # print("pending")
          

#fatherearned=("house1","house2","land")
#fatherfamily={"son1":"ram","son2":"balu","daughter":"sita"}
#fathersettlement[]

#for i ,j in fatherfamily.items():
  #  print("settlement",(fatherfamily).upadate({fatherfamily}))
 #   fathersettlement.update(fatherfamily)
#print(fathersettlement)
              
              

fatherearned=("house1","house2","land")

fatherfamily={"happy":"equally shared","son1":"house1","son2":"house2","daughter":"land"}

fathersettlement={}
# track already given properties
given_properties = set()

# first pass : collect who already got something
for person,property_given in fatherfamily.items():
    
    if property_given != "equally shared":
        print(f"{person} got {property_given} → settlement needed")
        given_properties.add(property_given)
# remaining properties for "equally shared
remaining_properties = list(set(fatherearned) - given_properties)

# second pass: build final settlement mapping
for person, propert_given in fatherfamily.items():
    if property_given=="equally shared":
        fathersettlement[person]=remaining_properties
    else:
        fathersettlement[person]=property_given
    

for person, props in fathersettlement.items():
    print(f"{person} : {props}")
          

    
