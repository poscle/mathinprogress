length = int(input("How long?"))
arr = [0]*length
for i in range(length):
    arr[i] = int(input("Input number"))
evencount = 0
oddcount = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        evencount+=1
    else:
        oddcount+=1
print("Even count:", evencount)
print("Odd count:", oddcount)