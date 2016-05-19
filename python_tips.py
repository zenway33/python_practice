#Non-Programmer's Tutorial for Python 3

#打印文件
print("Hello world!")
print("2 + 2 is", 2 + 2)
print(22 / 7)

print("Something's rotten in the state of Denmark.")
print("                -- Shakespeare")

#for 迭代
for i in [1, 2, 3]:
    print(i)

#dict

obj = {"a": 123, "b": 456}
for k in obj:
    print(k)

for k,v in obj.items():
    print("%s = %s" %(k, v))

#list
#列表求和
list = [2, 4, 6, 8]
sum = 0
for num in list:
    sum = sum + num

print("The sum is:", sum)

#找到列表相同的数据
list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
list.sort()
prev = None
for item in list:
    if prev == item:
        print("Duplicate of", prev, "found")
    prev = item


#range
range(1, 10)

list(range(1, 10))

i = range(1, 10)
for count in i:
    print(count)

#File io

# Write a file
with open("test.txt", "wt") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)



