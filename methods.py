text="  hello World 123! "
# lower() --convert to lowercase
print("lower:",text.lower())
# upper() -- convert to uppercase
print("upper:",text.upper())
# tilte() -- capitalize eafirsth word
print("Title",text.title())
# strip() -- romve leading trailing whitespaces
stripped=text.strip()
print("stripped:",stripped)
# replace(a,b) -- replace substring
print("replace 'world' by 'university':",text.replace("World","University"))
# find()
print(stripped.find("University"))
print(text.index("123"))
words=["apple","banana","orange"]
vowels="aeiouAEIOU"
for word in words:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    if count > 0:
        print(f"{word}: contains {count} vowels")
# Check if each word starts with a vowel
for word in words:
    if word[0] in vowels:
        print(f" {word} first letter starts with a vowels")
# split() -- split string into list
sentence="   we love   python"
print(sentence.split())
# strip() -- remove leading and trailing whitespaces
print(sentence.strip())
#str.startwith() -- ccheck if a string starts with a specific substring or prefix
file="report"
print(file.startswith("rep"))
#str.endswith()-- check if a string ends with a specific substring or substring
print(file.endswith("port"))
# list.append()-- add an item to end of the list
fruits =["apple","banana"]
fruits.append("orange")
print(fruits)
#list.sort() -- sort elements in ascending order
nums=[5,6,3]
nums.sort()
print(nums)
#list.pop() -- remove and return item at index (default last)
tasks=["code","review","test"]
print(tasks.pop())
#list.count() -- count occurences of an item in a list 
letters = ["a", "b","a","c"]
print(letters.count(letters[0]))
print(letters.count("a"))

# dict methods
# dict.get() -- safely get value by key , return None if not found
emp = {"name": "Alice","role":"Engineer"}
print(emp.get("name"))
print(emp.get("age"))
print(emp.get("role"))
#dict.items() -- iterate over key-value pairs for key,val in emp.items():
for key , val in emp.items():
    print(" emp dict " ,key,val)
#dict.keys() -- get all keys in a dictionary
print("emp keys:",emp.keys())
# dict .values() -- get all values of the dictionary
print("emp values:",emp.values())
#dict.update() -- merger or upadate a new dictionary
emp.update({"age": 30 ,"location": "nyc"})
print(emp)
# dict.pop() -- remove key and return its value
print(emp.pop("role"))
print(emp)


 #set methods
 
# set.add() -- add an element to the set
skills={"python","sql"}
skills.add("docker")
print(sorted(skills))
# set.intersection (): common elements between sets 
a={1,2,3}
b={2,3,4}
print(a.intersection (b))
print(a & b)
# set.union (): combine elemnets from two sets
print(a.union(b))
print(a|b)
#set.difference(): elements in set a not in b 
print(a.difference(b))
print(a-b)
# set.symmetric_difference():elements in either set but not both 
print(a.symmetric_difference(b))
print(a^b)
# set.issubset(): check if set a is a sub set of b
print(a.issubset(b))
print(a <= b)
# set.issuperset(): check if set a is a superset of b
print(b.issuperset(a))
print(b >= a)
# set.pop(): remove and return an arbitrary element from the set
B={1,3,5,4}
print(B.pop())
# set.remove(): remove a specific element from the set
B={1,3,5,4}
B.remove(4)
print(B)
# set.clear(): remove all elements from the set
a.clear()
print(a,"after clear")
# str.isalpha() -- check if all characters are alphabetic
print("Hello".isalpha())
print("Hello123".isalpha())