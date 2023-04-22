#!/home/uthayamurthy/Development/SSS/venv/bin python3

from rich.console import Console
from rich.prompt import Prompt
from essentials import *
from query_processor import QueryProcessor
from shortcuts import ShortcutProcessor
import pymysql as pym
import pyfiglet
import readline
from sys import exit

console = Console()

head = pyfiglet.figlet_format("S 3", font="3-d")
subhead = pyfiglet.figlet_format("Simplified SQL Shell", font="bubble")
author = pyfiglet.figlet_format("Copyright (C) 2023 R Uthaya Murthy", font="digital")
console.print(f'[bold deep_sky_blue4]{head}')
console.print(f'[bold cyan3]{subhead}')
console.print(f'[bold cyan1]{author}')

connected = False

console.print('[bold bright_blue]:warning: Default Values in brackets, just press enter to use them. \n')

while connected == False:
    try:
        host = Prompt.ask('[bold blue]Enter Host Address', default='localhost')
        print()
        port = int(Prompt.ask('[bold blue]Enter Port', default='3306'))
        print()
        uname = Prompt.ask('[bold blue]Enter Username', default='root')
        print()
        passwd = Prompt.ask('[bold blue]Enter Password [/] [bold dark_goldenrod](:warning: Don\'t worry if you can\'t see it )', password=True)
        print()
        try:
            conn = pym.connect(host=host, user=uname, password=passwd, port = port)
            connected = True
        except Exception as e:
            console.print(f'{error_emoji()} [bold red] {e.args[1]}')
    except KeyboardInterrupt:
                print()
                user_ack = Prompt.ask('[bold red]Do you want to quit ?', default='y')
                print()
                if user_ack.lower() == 'y':
                    console.print(f'{error_emoji()} [bold blue] Bye !')
                    exit()
    
current_table = None
prompt_text = 'mysql> '

def input_query():
    global prompt_text

    query = input('\u001b[33;1m' + prompt_text + '\u001b[0m') # Using input instead of rich's prompt to avoid blankline bug

    if ShortcutProcessor.check_shortcuts(query) == False: # If not shortcut, then keep asking input until ';' is encountered. 
        while check_query_end(query) == False:

            if not query.endswith(' '):
                query += ' '
            query += input('\u001b[33;1m' + ' '*6 + '->' + '\u001b[0m')
    
    return query

with conn:
    with conn.cursor() as cursor:
        console.print(f'\n[bold green]Connected [/]{success_emoji()}\n')
        console.print(f'[dark_sea_green]Unsure of what to do ? Just type [/dark_sea_green][bold green] help; [/bold green][dark_sea_green] and press Enter ![/dark_sea_green]')
        console.print(f'[dark_sea_green]Want to exit S3 ? Just type [/dark_sea_green][bold green] exit; [/bold green][dark_sea_green] and press Enter ![/dark_sea_green]\n')
        Q = QueryProcessor(cursor, console, conn)
        while True:
            try:
                query = input_query()
                command = get_primary_command(query)

                if command == 'exit':
                    print()
                    user_ack = Prompt.ask('[bold red]Do you want to quit ?', default='y')
                    print()
                    console.print(f'{error_emoji()} [bold blue] Bye !')
                    if user_ack.lower() == 'y':                    
                        exit()
                
                elif command == None:
                    continue

                else:
                    Q.parse(query)
                    if Q.change_in_prompt:
                        Q.change_in_prompt == False
                        prompt_text = Q.new_prompt
                        
            except Exception as e:
                try:
                    console.print(f'{error_emoji()} [bold red] {e.args[1]}')
                except:
                    console.print(f'{error_emoji()} [bold red] {e}')
            
            except KeyboardInterrupt:
                print()
                user_ack = Prompt.ask('[bold red]Do you want to quit ?', default='y')
                print()
                if user_ack.lower() == 'y':                    
                    console.print(f'{error_emoji()} [bold blue] Bye !')
                    exit()