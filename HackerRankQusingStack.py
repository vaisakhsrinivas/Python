firstq = []
secondq = []

def enqueue(d):
    firstq.append(d)

def dequeue():
    if (not secondq):
        while(firstq):
            secondq.append(firstq.pop())
    if (secondq):
        return secondq.pop()
    return None

def printtop():
    p = dequeue()
    print(p)
    secondq.append(p)


for _ in range (int(input())):
    option = input()
    if option[0] is "1":
        enqueue(int(option[2:]))
    elif option[0] is "2":
        dequeue()
    elif option[0] is "3":
        printtop()