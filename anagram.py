'''write a program to check whether the given input is satisfying the condition of anagram
test case-1
input 1-listen
input 2-silent
output-true
test case-2
i1=space
i2=racer
output-flase'''

str1='silent'
str2='listen'
n=len(str1)
m=len(str2)
sortn=sorted(str1)
sortm=sorted(str2)
if n==m:
    if sortn==sortm:
       print("its anagram")
    else:
        print("not anagram")
else:
    print("if length differs its not anagram")

    
    
    
    
    
    