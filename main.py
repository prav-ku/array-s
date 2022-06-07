# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele) # adding the element
     
print(lst)

arr = lst;    
temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
#Displaying elements of the array after sorting    
   
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ")


#Mean
import statistics
lst = []
 

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele)
     
print(lst)
x = statistics.mean(lst)
print("Mean is :", x)


#Median
import statistics
lst = []
 

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele)
     
print(lst)
x = statistics.median(lst)
print("Median is :", x)

#Standard Deviation
import statistics
lst = []
 

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
 
    lst.append(ele)
     
print(lst)
x = statistics.stdev(lst)
print("Standard Deviation is :", x)


