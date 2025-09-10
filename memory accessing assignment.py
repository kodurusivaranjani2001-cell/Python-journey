# 1
num=[1,3,5,"pen",4,"item","index","pop","set.default","defaultdict()"]
print(len(num))
print(num[-1:-6:-1])
#2
num=[0,1,2,3,4,5,6,7,8,9]
print(num[::2])
sqrs = [x**2 for x in num]
print(sqrs)
# 3 last 3 elements
print(num[-1:-4:-1])
# 4 
print(num[:])
num1=num.copy()
print("num1",num1.copy())
# 5 
list1=[1,2,4]
list2=[3,5,4]
print(list1==list2)
# 6
bag= [["bag1","books","id"],["money","change","slip"]]
print(bag[1][2])
#7
sre="hello world"
print([ char for char in sre ])
# 8
list1 = [1,3,"str","c","job","set: no",5.4]
#print([x for x in list if isinstance(x, float)])
print(list1[2:-1])
# 9 
#list1=[1,2,3]
#list2=[3,4,5,5]
#print(list2[ : ])
# 10
#list = ["s:2","h:3"]

# set questiond
#11
set={10,20,30,20,10}
# 12
if 20 in set:
    print("20 in the set")
print(set.issubset(({10,20})))
#15
str="hell0"
#print(str.set())
# 16
list1 = {1,3,5,5}
list2= {1,5,3,5}
print(list1.intersection(list2))
print(list1 .difference(list2))
print(list1-list2)

#19
bag=[{"books","pen","id"}]
for item in bag:
    print(item)
# 20 frozen set

# dictionary questions
#21
d ={"name":"ram","age":37,"job":"it"}
print(d["name"])
print(d["age"])
print(d["job"])
#22
print(d.get("name"))
#23
dt={"name":("ram","shyam"),"age":(12,34),"job":("it","hr")}
print(dt)
print(dt["job"].index("it"))
print(dt["name"][1])
# find is not a method of dictionary
#25
print(enumerate(dt.items())) # y not output
#26
did ={"school":[{"1st cls":"10 s"},{"2 nd clss":" 16 s"}]}
print(did["school"][0]["1st cls"])

# 27
squared={1,2,4,5,6}
squared={ x : x*x for x in range(1, 6)}
print(squared)
# 28
num={"1","2","3"}
squares={"1","4","9"}
print(zip(num,squares))
list1=[1,2,3]
list2=["a","b","c"]
total=list(zip(list1,list2))
print(total)
