# S3 - Simplified SQL Shell
## S3 is a user-friendly, cross-platform SQL Shell which features **colourful text** and **emojis**. Along with its visually engaging interface, S3 is packed with helpful features, including **convinient shortcuts**, making it easy to manage your databases and execute SQL Queries. **Primarily Intended for Educational Purposes**  

![](https://github.com/Uthayamurthy/S3/blob/main/demo/S3_quick_demo.gif)  

> ## Also have a Look at the longer [Demo Video](https://drive.google.com/file/d/1Y3TuhlDBqaXAJxNWRDDgZP7lIiGiyo2I/view)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Supported Platforms
### - Any Linux Distro (Tested on OpenSUSE Tumbleweed)
### - Windows (Tested on Windows 10, should work in Windows 11 as well)

> Mac Users can try the Source Install Method and Let me know, if it works. I just can't support it, because I don't have one. 

# Installation

##  Prerequisite
It is assumed that you have already installed SQL Server in your pc (Obvious Stuff, right?)  
In case you haven't then install it from
- https://dev.mysql.com/downloads/installer/ [For Windows, Mysql]
- https://opensource.com/article/20/10/mariadb-mysql-linux [For Linux, MySql or MariaDB]

Or Follow any [working] Tutorial that you find online.

## Binary Install Linux -
> Though S3 will work from any terminal emulator, **Gnome Terminal is Recommended** as I have Tested it there and it works. Kde Konsole seems to not render the Emojis Properly.

1. Go to [Releases Page](https://github.com/Uthayamurthy/S3/releases/) and Download the S3-1.0.0-Linux-Any-x86_64.zip file. [or the latest version]
2. Extract it.
3. Give the install.sh file permissions to execute by -
```
chmod +x install.sh
```
4. Run install.sh file by -
```
./install.sh
```
Now you should be able to run S3 in your terminal from anywhere.
Just type -
```
S3
```
and press enter !

> Alternatively, you can use S3 file as a portable binary without installing it, just give it permissions to execute (**chmod +x S3**) and run it by **./S3**

## Binary Install Windows[10/11] -

> The launch of portable binary file can be slow, [probably] because it has to uncompress before startup.

### Step 0 - Install Windows Terminal

*Although S3 will work with CMD.exe in Windows, Windows terminal will ensure that the rendering of the text is fine and not messed up. Further, Emojis are absent in CMD.exe.*

- Install Windows Terminal by following - https://learn.microsoft.com/en-us/windows/terminal/install
- Set CMD as the default profile.

### Using Setup File(**Recommended**) -
> Windows Terminal is a Mandatory Requirement for this method.

You can Install S3 using a Setup File, just like how you will install any other program (and ofcourse use it like any typical windows program.)
1. Go to [Releases Page](https://github.com/Uthayamurthy/S3/releases/) and Download the S3-1.0.0-Windows-Setup-x86_64.zip file. [or the latest version]
2. Extract it.
3. Double Click and Run S3_Setup.exe
4. Follow the Instructions and you're Done !

### Using Portable Binary
This allows you to double click and run the file without actually installing it.

1. Go to [Releases Page](https://github.com/Uthayamurthy/S3/releases/) and Download the S3-1.0.0Windows-Portable-x86_64.zip file.[or the latest version]
2. Extract it.
3. Double CLick and Run Run_S3.bat if you are using windows terminal or start S3 by running S3.exe diretly (will run through CMD.exe). 

## Source Install (Works for Linux, Windows, [Maybe] for Mac) -
Don't Do This, Until you know what you are doing !
1. Navigate to your desired directory and create a Virtual Environment.
```
python3 -m venv venv
```
2. Activate it
- Linux
```
source venv/bin/activate
```
- Windows
```
venv\Scripts\activate
```
3. Install the required libraries.
```
pip install pyinstaller rich Faker pyfiglet PyMySQL PyMySQL[rsa]
```
4. Clone this repo and go it's directory
```
git clone https://github.com/Uthayamurthy/S3
cd S3
```
5. Create the binary file 
```
pyinstaller --collect-all pyfiglet --icon=S3/icon.ico -F main.py
```
Now, in the dist directory, you will find the executable (named **main** or **main.exe**)

# Basic Usage

## Regular SQL Commands

Just type in your required SQL Command and press enter. 
Multiline SQL Statements are supported, just press enter and don't end the statement with semicolon ';' until you want to end it.

> Don't Forget Semicolon at the end of every statement.

For SQL Specific Documentation refer to :
1. MySQL Docs - https://dev.mysql.com/doc/
2. MariaDB Docs - https://mariadb.org/documentation/

## Shortcut SQL Commands

Shortcuts is a special feature of S3 that helps to dramatically reduce the length of the SQL statements that you type.They always start with **!** .

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

If you are not convinced, look at this -
```
!ai 15 num(4) name dob(7, 18) addr phone
```
Is equivalent to running
```
Insert INTO <Table_Name> <random_4_digit_number> <random_name> <random_dob> <random_addr> <random_phone_no>
.
.
.
15 Times !!
```
So 15 lines into just one !

For more help about Shortcuts, refer to the
Shorcut Manual.

## App Commands

### Help 
To access internal help menu, just type
```
help;
```
and press enter.

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

# Shortcut Manual

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