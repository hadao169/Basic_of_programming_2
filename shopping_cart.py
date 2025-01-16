set1 = {"apple", "bread", "milk", "eggs", "bananas", "chocolate"}
set2 = {"milk", "bread", "cheese", "oranges", "chocolate", "yogurt"}

# def shopping_cart(set1:set, set2:set):
#   sameItems = set()
#   diffItems = set()
#   for item1 in list(set1):
# 			if item1 in set2:
# 				sameItems.add(item1)
# 				set1.remove(item1)
# 				set2.remove(item1)
#   diffItems = set1.union(set2)

#   print("Similar items: ", sameItems)
#   print("Different items:", diffItems)
# shopping_cart(set1, set2)

sameItems = set()
x1 = set1.intersection(set2)
x2 = set1.difference(set2)
x3 = set2.difference(set1)
for i in x2:
  sameItems.add(i)
for i in x3:
  sameItems.add(i)

print("Same items: ", sameItems)
print("Different items: ", x1)

