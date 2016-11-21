arr=[]
word=input()
while word !=(''):
    s=word[0:2]+word[3: ]
    arr.insert(0,s)
    word=input()
print(arr)
