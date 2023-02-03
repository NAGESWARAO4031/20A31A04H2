text='nikil'
index=0
for i in text:
    print("text[",index,"]=",i)
    index+1
    
text='india is great'
print(text.title())
print(text.swapcase())


text='India Is Great'
print(text.split())

#enumerate
str='hello to you'
print(list(enumerate(str)))n