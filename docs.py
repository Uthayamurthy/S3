# Contains the help text of S3 and a function to render it.
# Help Contents are hardcoded so that it is easier to make a portable executable without any data file.

from rich.markdown import Markdown

primary_help_md = """
# HELP - S3 (Simplified SQL Shell)

## Regular SQL Commands

Just type in your required SQL Command and press enter. 
Multiline SQL Statements are supported, just press enter and don't end the statement with semicolon ';' until you want to end it.

> Don't Forget Semicolon at the end of every statement.

For SQL Specific Documentation refer to :
1. MySQL Docs - https://dev.mysql.com/doc/
2. MariaDB Docs - https://mariadb.org/documentation/

## Shortcut SQL Commands

Shortcuts is a special feature of S3 that helps to dramatically reduce the length of the SQL statements that you type.

> Using Semicolons ';' to end shortcuts is not mandatory.

0. Set the Database that you wanna use (Obvious Stuff !!)

```
USE <DATABASE_NAME>
```

1. Set The Table for Shortcut Commands. (Not Mandatory, but Recommended)
It saves typing the table name everytime !
```
!t <table_name>
```

2. Use the Shortcuts !
Example Usage -

```
!s
```
Is Equivalent to running 
```
SELECT * FROM <table_name>;
```

Just see How much you need not type !

For more help about Shortcuts, refer to Shorcut Manual by -
```
help shortcuts;
```
## App Commands

### Exit
To exit the app, just type 
```
exit; 
```
and press enter.

### About

To know about the app, just type
```
about;
```
and press enter
"""

shortcuts_help_md = """
# SHORCUT MANUAL - S3 (Simplified SQL Shell)

Shortcuts is a special feature of S3 that helps to dramatically reduce the length of the SQL statements that you type. Shortcuts is currently only available for a handful of SQL Commandd.

> Using Semicolons ';' to end shortcuts is not mandatory. Also, Shortcuts are NOT CASE SENSITIVE (even the arguments !).  

## Beware about arguments of Shortcuts.

***Arguments that have multiple things seperated by commas SHOULD NOT have spaces between them. It will either not work or produce Unintended [Absurd !] results.***

## Set Table Shortcut
**Usage-**  
Just
```
!t <Table_Name>
```
That's It !

## Show Shortcut
**Usage -**
```
!sh <arg1>
```
- arg1 [optional] - Table or Database, **Default - t**  
**Values -**  
**d**: database  
**t**: tables  

## Select Shortcut
**Usage-**
```
!s <arg1> <arg2>
```
- arg1 [optional] - Set the fields you want to retrieve, * is default, field names are comma-seperated **with no spaces** between them.
- arg2 [optional] - Set Table name, use this if you haven't set the table using !t or you want to just overide it. 

## Describe Shortcut
**Usage-**
```
!d <arg1>
```
- arg1 [optional] - Set Table name, use this if you haven't set the table using !t or you want to just overide it.

## Insert Shortcut
**Usage-**
```
!i <arg1> <arg2> <arg3>
```
- arg1 [Mandatory] - Set the values to insert into the table. Values are comma-seperated **with no spaces** between them.
- arg2 [Optional] - Set the field names into which the command needs to be inserted. Field names are comma-seperated **with no spaces** between them.
- arg3 [Optional] - Set Table name, use this if you haven't set the table using !t or you want to just overide it.

## Auto Insert Shorcut
Definetely, one of the coolest feature of S3, very useful if you want to insert a bunch of random values super-quickly into your database !
It uses the **Faker** Library and **Python's Random Library** to generate data according to your requirements !
> Prior !t usage is mandatory.
**Usage-**
```
!ai <arg1> **args
```
> Run !d before you use autoinsert to avoid errors in using this feature.

- arg1 [Mandatory] - Set the number of entries you want to insert.
- **args - Set the Data Type that you want to insert into this field.

Example usage of Auto-Insert -
```
!ai 5 num(2) name(nb) num(20000, 30000) phone addr bool yn gender null
```

### Supported Data Types for Auto Insert -
> For the arguments of the datatypes, use parenthesis '()' and arguments are comma-seperated **with no spaces** between them.
#### Name
**Datatype - String (Char, Varchar, whatever you wanna call it !)**  
Generates Random Person Names based on locale.
1. Full Name
```
name(arg1) 
```
- arg1 [optional] - Set the gender for name. **Default-Random**
**Values -**  
**m**: male  
**f**: female  
**nb**: non-binary
2. First Name
```
fname(arg1) 
```
- arg1 [optional] - Same as Full Name

3. Last Name
```
lname(arg1) 
```
- arg1 [optional] - Same as Full Name

> If you use name and lname, fname then they won't match !

#### Number
**Datatype - Integer**  
Number Datatype is slightly special, in the sense, different number of argument will yield different results.  
1. With 0 Arguments
Will Generate  A Random Integer between 0 and 1000.
```
num
```
2. With 1 Argument
Argument is taken as the number of digits. 
```
num(3)
```
A 3 digit number is generated.

3. With 2 Arguments
Arguments are taken as the range from which the digits should be generated. 
```
num(100,500)
```
This will generate a number between 100 and 500  
Again, **No Spaces** between the comma seperated arguments or else it will produce insanely absurd results !!  
***So, Don't Do This* !**
```
num(100, 500)
```
> You can also use '**int**' instead of '**num**' in all the above commands.

#### Date
**Datatype - Date**  
Generates a date in default SQL Format.
```
date(arg1,arg2)
```
- arg1 [optional] - Set the Starting Year. **Default-1970**
- arg2 [optional] - Set the Ending Year. **Deafult-Present-Year**

#### Date Of Birth
**Datatype - Date**  
Generates a date of birth in default SQL date Format.
```
dob(arg1,arg2)
```
- arg1 [optional] - Set the Minimum Age. **Default-0**
- arg2 [optional] - Set the Maximum Age. **Deafult-115**

#### Color
**Datatype - String**  
Generates a random color name.
```
color
```
> **colour** can also be used instead of **color**

#### Phone Number
**Datatype - String**  
Generates a phone number based on locale.
```
phone
```

#### Address
**Datatype - String**  
Generates a random address based on locale.
```
addr
```

#### City
**Datatype - String**  
Generates a random city name according to locale.
```
city
```

#### Country
**Datatype - String**  
Generates a random country name.
```
country
```

#### Pincode
**Datatype - String**  
Generates a random pincode [or postcode] according to the locale.
```
pincode
```

#### Boolean Values
**Datatype - Bool**  
Generates Either True or False.
```
bool
```

#### Yes or No
**Datatype - String**  
Generates Yes or No
```
yn
```

#### Gender
**Datatype - String**  
Generates Male or Female
```
gender
```

#### Null
**Datatype - Null**  
Sets the field to null.
```
null
```
> Even **'none'** can be used instead of **'null'**

#### Aadhaar Number (Only for Indian Locale)
**Datatype - String**  
Generates a random aadhaar number
```
aadhaar
```

#### Company
**Datatype - String**  
Generates a random company name.
```
company
```

#### Language Name
**Datatype - String**  
Generates a random language name.
```
language
```

#### In All Other Cases
Incase you do this -
```
!ai 10 num(2) name num(1) abc addr
```
Here **abc** is not a datatype. So **abc** will be considered as the default value for all the 4th field of 10 rows.
> Only String Values are supported for Default Value. Incase you enter a number, it will be converted into a string. So don't use this with a field of number datatype.

## Set Shortcut Locale
**Default Locale is en_IN [India]** 
```
!l <locale>
```
Example -
```
!l en_US
```
> For Supported Locale types refer to Faker Documentations(https://faker.readthedocs.io/en/master/locales.html) .

"""


about_md = """
# ABOUT - S3 (Simplified SQL Shell)
## Author - R Uthaya Murthy (https://github.com/Uthayamurthy)
## Source - https://github.com/Uthayamurthy/S3
## License - MIT License

***S3 is a SQL Shell for MariaDB and MySQL.
It comes with a Colorful CLI (emojis too !) and has shortcuts that can help to greatly shorten your SQL Commands.***
> Primarily Intended For Educational Purposes Only. 

To Know More About Licensing Terms, Run -
```
about license;
```
"""

license_md = """
# License - S3 (Simplified SQL Shell)
## MIT License

> Copyright (c) 2023 R Uthaya Murthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def app_help(typ='gen'):
    global primary_help_md, shortcuts_help_md
    if typ == 'gen':
        return Markdown(primary_help_md)
    elif typ == 'shortcuts':
        return Markdown(shortcuts_help_md)

def app_about(typ='gen'):
    global about_md, license_md
    if typ == 'gen':
        return Markdown(about_md)
    elif typ == 'license':
        return Markdown(license_md)