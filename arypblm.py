arr=[]
n=int(input("number of elements:"))
for i in range(n):
     element=int(input("enter element:"))
     arr.append(element)

def summation():
     total=0
     for elements in arr:
          total+=elements
     return total

def maximum():
     max_val=arr[0]
     for val in arr:
          if val>max_val:
               max_val=val
     return max_val

def minimum():
     min_val=arr[0]
     for val in arr:
          if val<min_val:
               min_val=val
     return min_val

def average():
     total=summation()
     avg=total/len(arr)
     return avg

def display():
     print("array elements:",end=" ")
     for elements in arr:
          print(elements,end=" ")
     print("\nsummation=",summation())
     print("\nmaximum=",maximum())
     print("\nminimum=",minimum())
     print("\naverage=",average())
display()