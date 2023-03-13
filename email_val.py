import re

email_type = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'aol.com', 'protonmail.com',
              'mybusiness.com', 'mycompany.com', 'iiti.ac.in']

# user input
inp_email = input('Eneter your email id')

try:
    for i in email_type:
        # using regex for checking the pattern
        #     pattern='[a-zA-Z]+[\.]?\w+[@]'

        val_email = re.search('^[a-zA-Z]+[\.]?\w+[@]', inp_email).group()
        # iterating through different email type to check the validation
        if (val_email + i) == inp_email:
            print('yes its a valid email id')
            break
    else:
        print('wrong email')

except:
    print('please check your email and try again')
