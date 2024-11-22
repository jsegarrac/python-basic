from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
print(some_list)

name = r.get_full_name()

print(name)

for user in some_list:
    print (user.get_full_name()," ",user.get_email())

for user in some_list:
    print (user .get_picture())
    
    
'''
To generate a table with information about the users, we can write a function containing all desirable parameters. 
For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed.
We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
'''

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)

get_users()
df1 = pd.DataFrame(get_users())  
print(df1)