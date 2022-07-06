#Following are the conditions while writing an email.
#a-z Only small alphabets are used.
#0-9 All digits can occur
#._ These characters can come only 1 time
#. A dot should must be placed ar 2 or 3 position from Last.

import re
email_verification="^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

#Taking input from user

enter_email=input("Please enter your email:")

if re.search(email_verification,enter_email):
    print("Right Email entered")
 
else:
    print("Wrong Email")
    
