n1 = input("Enter a name: ").lower()
n2 = input("Enter another name: ").lower()

def calculate_love_score(n1,n2):
    t = 0
    l = 0
    for i in n1:
        if i in "true":
            t += 1
        elif i in "love":
            l += 1
            
    for j in n2:
        if j in "true":
            t += 1
        elif j in "love":
            l += 1

    print(str(t)+str(l))
    
calculate_love_score(n1,n2)
