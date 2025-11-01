
names = list()
names = ['hanna','alex','abel','yakob','mikcky']
        #  - 5        -4    -3   -2      -1
#negtive indexing
print(names[-3])
print(len(names))
print(names[4])

#unpacking 
first,second,third,*fourth=names
print(fourth)


#slicing
print(names[1:4])
new_list=names[2:3]
print(new_list)

#by negtive print alex and abel
print(names[-4:-2])

#modify list
names[2]='sami'
print(names)

print('hanna' in names)#true
print('sami' not in names)#false
# adding 
names.append('abdu')#add to the end
print(names)

#insert item at specific position
names.insert(1,'dawit')
print(names)

#remove item
names.remove('mikcky')
print(names)

#pop item
popped_item=names.pop()#remove last item
print(popped_item)
print(names)

#clear list
#names.clear()
#print(names)

#copy list
new_list1 = names.copy()
print(new_list1)

del names[3]


# list joining
numbers =[45,54,8,9]
numbers.extend(names)
new_list2= numbers + names
print(new_list2)

print(new_list.count)

print(names.index('alex'))

# reversing a list
names.reverse()
print(names)

#sorting a list
names.sort()
print(names)

# function class loop tuble dixtrioes 

