#Task 1

def get_age_category(age):
    if age < 18:
        return "Minor"
    elif age>=18 and age<=64:
        return "Adult"
    else:
        return "Senior"
    
 #Task 2
"""
num = int(input("Enter Number : "))

for i in range (10):
    print(" %s x %s = %s"%(num,i,num*i))
"""
#Task 3

def square_list(numbers):
    result = []
    for i in range(len(numbers)):
        print(numbers[i]*numbers[i])
    

print(square_list([1,2,3,4]))