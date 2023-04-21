# All necessary code to perform auto insert into a table.
# Seperate file for auto insert because it is quite big !

from faker import Faker
from random import randint, choice

# Default locale English-India
fake = Faker('en_IN')

 # Sets Locale for data generation.
def set_locale(locale):
    global fake
    fake = Faker(locale)

def auto_insert(squery, table):
    queries = []
    num = squery[1]
    if num.isdigit():
        num = int(num)
    else:
        raise Exception("The Number Of Inserts [second argument] should be a integer.")

    args = squery[2:]

    for i in range(num):
        data = parse_arg(args)
        queries.append(f'INSERT INTO {table} Values({data});')

    return queries 

# Takes in Argument and Return data that can be put into values.
# Used to process primary shorcut arguments
# Eg :
# name(m) num(10) date
#   ^      ^       ^
# Used to process these

def parse_arg(args):
    global fake

    data = ''
    
    for arg in args:
        arg = arg.lower()

        if arg.startswith('name'):
            if arg.find('(') == -1:
                data += f' "{fake.name()}",'
            else:
                int_args = get_int_arg(arg)
                if int_args[0] == 'm':
                    data += f'"{fake.name_male()}",'
                elif int_args[0] == 'f':
                    data += f' "{fake.name_female()}",'
                elif int_args[0] == 'nb':
                    data += f' "{fake.name_nonbinary()}",'
                else:
                    raise Exception('Invalid Argument for name.')
        
        elif arg.startswith('fname'):
            if arg.find('(') == -1:
                data += f' "{fake.first_name()}",'
            else:
                int_args = get_int_arg(arg)
                if int_args[0] == 'm':
                    data += f' "{fake.first_name_male()}",'
                elif int_args[0] == 'f':
                    data += f' "{fake.first_name_female()}",'
                elif int_args[0] == 'nb':
                    data += f' "{fake.first_name_nonbinary()}",'
                else:
                    raise Exception('Invalid Argument for fname.')

        elif arg.startswith('lname'):
            if arg.find('(') == -1:
                data += f' "{fake.last_name()}",'
            else:
                int_args = get_int_arg(arg)
                if int_args[0] == 'm':
                    data += f' "{fake.last_name_male()}",'
                elif int_args[0] == 'f':
                    data += f' "{fake.last_name_female()}",'
                elif int_args[0] == 'nb':
                    data += f' "{fake.last_name_nonbinary()}",'
                else:
                    raise Exception('Invalid Argument for lname.')

        elif arg.startswith('num') or arg.startswith('int'):
            if arg.find('(') == -1:
                data += f' {randint(0, 1000)},'
            else:
                int_args = get_int_arg(arg)
                if len(int_args) == 1: # Single Argument - Digits in Number
                    tp = int(int_args[0]) - 1 # ten power
                    data += f' {randint(10**tp, (10**(tp+1))-1)},'
                elif len(int_args) == 2: # Two Argument - Range of Number
                    data += f' {randint(int(int_args[0]), int(int_args[1]))},'
                else:
                    raise Exception('Invalid Argument for num.')
        
        elif arg.startswith('phone'):
            data += f' "{fake.phone_number()}",'
        
        elif arg.startswith('addr'):
            data += f' "{fake.address()}",'
        
        elif arg.startswith('city'):
            data += f' "{fake.city()}",'
        
        elif arg.startswith('country'):
            data += f' "{fake.country()}",'

        elif arg.startswith('pincode'):
            data += f' "{fake.postcode()}",'
        
        elif arg.startswith('aadhaar'): # Works on for Indian Locale.
            try:
                data += f' "{fake.aadhaar_id()}",'
            except:
                raise Exception('Random Aadhaar ID Can be created only for Indian Locale. Please set locale to en_IN.')
        
        elif arg.startswith('company'):
            data += f' "{fake.company()}",'
        
        elif arg.startswith('lang'):
            data += f' "{fake.language_name()}",'
        
        elif arg.startswith('bool'):
            booleans = ['true', 'false']
            data += f' {choice(booleans)},'
        
        elif arg.startswith('yn'):
            vals = ['yes', 'no']
            data += f' "{choice(vals)}",'
        
        elif arg.startswith('gender'):
            vals = ['male', 'female']
            data += f' "{choice(vals)}",'
        
        elif arg.startwith('null') or arg.startwith('none'):
            data += f' NULL,'
        else:
            data += f' "{arg}",'

    # Clean up
    data = data[:-1] # Remove the ',' at the end
    data = data.strip() # Remove whitespaces at the beginning and end
    return data

# Gets the internal arguments of an argument ;) 
# Eg : name(m)
#           ^
#       Gets this

def get_int_arg(arg):
    a = arg.split('(')
    args = a[1][:-1] # Ignores the ')'
    args = list(args.split(','))
    return args