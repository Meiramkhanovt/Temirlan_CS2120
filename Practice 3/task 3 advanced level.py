def check_pass(password):
    a=int(0)
    if (len(password)==8):
        if any(c for c in password if c.islower()):
            if any(c for c in password if c.isupper()):
                if '-' in password or '*' in password or '#' in password:{
                 print('Your password is perfect')
                }
                else:{
                    print('Password has no such elements like "*-#')
                 }
            else:{
                print('Password has no any uppercase characters')
            }
        else:{
        print('Password has no any lowercase characters')
        }
    
    else:{
        print('Password has less than 8 characters or more')
    }
    
check_please=input('Please enter your password: ')
check_pass(check_please)