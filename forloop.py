list=['a','e','i','o','u']
word=input("Enter the word")
count=0
for i in list:
    if i  in word:
        count+=1
print(count)

