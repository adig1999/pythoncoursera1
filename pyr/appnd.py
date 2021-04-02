def appendsums(lst):
    i=0
    while i<25:
        l=len(lst)
        sum=lst[l-1]+lst[l-2]+lst[l-3]
        lst.append(sum)
        i+=1

sum_three = [0, 1, 2]
appendsums(sum_three)
print (sum_three[20])
