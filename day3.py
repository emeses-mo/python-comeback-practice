#Task 1
def list_stats(numbers):
    s= sum(numbers)
    ma= max(numbers)
    mi= min(numbers)
    nums= {
        "sum": s,
        "max": ma,
        "min":mi
    }
    return nums

#Task2
from collections import Counter
sentence =""
words = sentence.split()

counts= {}

for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1


#Task3
def get_evens(numbers):
    evens = []
    for number in numbers:
        if number%2 == 0:
            evens.append(number)
        else:
            pass
    return evens
e=[1,2,3,4,5,6]
print(get_evens(e))
