list=['Mango','Apple','Banana','Grapes','Orange']
print("Length of the list is: ",len(list))
print("First Element:", list[0])

print("Last Element:", list[-1])

list.append('Pineapple')
print("Updated list:", list)

list.remove('Orange')
print("Updated list:", list)

list.sort()
print("Sorted list:", list)

list.pop(2)
print("Updated list:", list)

list= list[:3]
print("Sliced list:", list )


