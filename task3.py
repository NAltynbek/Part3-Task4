numbers = input ("Enter the list number: ").split(" ")
step = int(input ("Enter the step: "))

def cezar(list, steps):
    if steps > 0:
        for i in range(steps):
            lst.append(lst.pop(0))  
    elif steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.insert(0, lst.pop()) 
cezar(numbers,step)
print(numbers)  
