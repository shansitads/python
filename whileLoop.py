#digit extractor -> sum of digits
n = 132
sum = 0
print("\noriginal number: "+str(n))

while not n == 0:
    sum += n%10
    n = int(n/10)

print("sum of digits: "+ str(sum))