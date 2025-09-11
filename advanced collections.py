from collections import Counter,defaultdict,deque
from itertools import combinations,permutations
from functools import lru_cache
import heapq
# Example usage of Counter
arr=[1,2,2,4,3,3,5,32,4]
freq = Counter(arr)
print(freq)

lists= [122,334,44,22,333]
transform=Counter(lists)
print("transform",transform)

bag=["bottle","pen","id","pen"]
bag_count=Counter(bag)
print(bag_count)

bag={"bottle","pen","id","pen"}
bag_count=Counter(bag)
print( " set bag",bag_count)
 
# Example usage of defaultdict
df= [{"a":[1]},{"b":[2]}]
print("my own data",df)

dd = defaultdict(list)
dd["a"].append(1)
dd["b"].append(2)
dd["a"].append(3)
print(dd)
print("default dict",dd)

# print( deque - sliding window / double-ended queue)
dq =deque([1,2,3])
dq.appendleft(0)  # Add to the left end
dq.append(4)    # Add to the right end
print(dq)
dq.pop()
print(dq)
print(dq.popleft())
print(dq)

# heapq -priority queue , min heap operations
min_heap =[]
heapq.heappush(min_heap,5)
heapq.heappush(min_heap,1)
heapq.heappush(min_heap,3)
print("james bond",min_heap)

print("before pop",min_heap)
print(heapq.heappop(min_heap))
print("after pop",min_heap)
print(heapq.heappop(min_heap))
print("after pop again",min_heap)

print("heapq is fast ")
print(" heapq value",min_heap)
print(heapq.heappop(min_heap))
print("after pop again", min_heap)

print("venkat",heapq.nlargest(3,[5,1,8,3]))
print("venkat",heapq.nsmallest(2,[5,1,8,3]))
print("venkat",heapq.nlargest(2, [5, 1, 8, 3], key=lambda x: x % 2))

# Example usage of combinations and permutations 
comb = list(combinations([1,2,3],2))
perm = list(permutations([1,2],2))
print("combinations",comb)
print("permutations",perm)

# enumerate - get index and value in loop
for idx, val in enumerate(['a',3,"str","c"]):
    print(idx,val)
    print(Counter([val]))

# zip -combine two oe more iterables
names=['a','b','c']
scores=[10,20,30]
gift=['pencil','pen','book']
zipped=list(zip(names,scores,gift))
print(zipped)

# 
mathruns=[5,6,7]
player=["venki","ramesh","suresh"]
for player, run in zip(player, mathruns):
    print(f"{player} scored {run} runs")
 
 # sorted(keys=...)-custom sort
nums = [5,6,1,3,2]
newarr=sorted(nums)
print("sort",newarr)

venkat = lambda x: print(x)
venkat("hello world")
venkat(5)

people = [{"name": "a","age":34},{"name":"b","age":20}]
sorted_people =sorted(people,key=lambda x:x["age"])
print("sorted people by age",sorted_people)

# lru_cache - memoization for expensive function calls
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
print(fib(10))

     
# bitwise operations &,|,^ for set/bitmask logic
a=0b1010
b=0b1100
print(a&b)
print(a|b)
print(a^b)

    
user={"name":"venkat","age":30,"skills":["python","sql"]}  
backup=user.copy()
print("user backup", backup)
user.setdefault("profession","Engineer")
print(user)
print(user["profession"])

list=[12,45,665,43,56,12 , 45]
list1=Counter(list)
print(list1)

runs = {2,3,245,3,2,4,5,3}
print(runs)

runs=[1,4,2,5,3,6,3,2]
print(set(runs))

def fibonacci(n):
    if n <= 1:
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)
terms = 10
for i in range (terms):
    print(fibonacci(i), end=" ")


def fibonacci_series(terms):
    a, b = 0, 1
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_series(8)
