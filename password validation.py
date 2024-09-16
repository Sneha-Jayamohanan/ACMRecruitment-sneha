import re
import sys
pattern=r'^.*(?=.{8})(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*_]).*$'
password=input("Enter Password: ")
result=re.findall(pattern,password)
password_r = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]
sym=["!","@","#","$","%","^","&","_","*","1","2","3","4","5","6","7","8","9","0"]


if password in password_r:
    print("error")
    sys.exit()
    
    
    
if password[0] in sym:
    print("error")
    sys.exit()
    
    
    

if result:
    print("Password is valid ")

else:
    print("Password is invalid")
        
    

