email="nikil@gmail.com"
pwd=123456
otp=6666
cemail=input("Enter the email:")
cpwd=int(input("Enter the pwd:"))
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter otp:"))
    if(otp==cotp):
       print("login successfully")
    else:
       print("login failed due to incorrect otp")
elif(email!=cemail and pwd==cpwd and otp==cotp):
    print("login failed due to email")
elif(email==cemail and pwd!=cpwd and otp==cotp):
    print("login failed due to pwd")
elif(email==cemail and pwd==cpwd and otp!=cotp):
    print("login failed due to incorrect otp")
    
    