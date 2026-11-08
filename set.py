#collection of unordered items.
#elements must be unique and are immutable.


collection={"suryajeet","surya","sms"}
print(collection)

print(len(collection))
print(type(collection))

collection.add("maurya")
print(collection)
print(collection.clear())
print(collection)

set1={1,2,5,4,8,7}
set2={8,5,7,9,6,4}
print(set1.union(set2))
print(set1.intersection(set2))
