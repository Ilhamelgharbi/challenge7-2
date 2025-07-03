ch1 = input("Enter the first string: ")
ch2 = input("Enter the second string: ")
var1 =ch1.split()
var2 =ch2.split()
var3 = []
for i in range(len(var1)-1):
    for j in range(len(var2)-1):
        if var1[i] == var2[j]:
            var3.append(var1[i])
print("Common words found:", var3)
