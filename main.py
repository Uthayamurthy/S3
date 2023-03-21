#!/home/uthayamurthy/Development/SSS/venv/bin python3

from rich.console import Console
from rich.prompt import Prompt
from essentials import *
from query_processor import QueryProcessor
import pymysql as pym
try:
    import readline
except:
    import pyreadline3 as readline

console = Console()

connected = False

while connected == False:
    host = Prompt.ask('[bold blue]Enter Host Address', default='localhost')
    print()
    uname = Prompt.ask('[bold blue]Enter Username', default='root')
    print()
    passwd = Prompt.ask('[bold blue]Enter Password [/] [bold dark_goldenrod](:warning: Don\'t worry if you can\'t see it )', password=True)
    print()
    try:
        conn = pym.connect(host=host, user=uname, password=passwd)
        connected = True
    except Exception as e:
        console.print(f'{error_emoji()} [bold red] {e.args[1]}')
    
current_table = None
prompt_text = 'mysql> '

def input_query():
    global prompt_text

    query = input('\u001b[33;1m' + prompt_text + '\u001b[0m') # Using input instead of rich's prompt to avoid blankline bug

    while check_query_end(query) == False:

        if not query.endswith(' '):
            query += ' '
        query += input('\u001b[33;1m' + ' '*6 + '->' + '\u001b[0m')
    
    return query

with conn:
    with conn.cursor() as cursor:
        console.print(f'\n[bold green]Connected [/]{success_emoji()} \n')
        print()
        Q = QueryProcessor(cursor, console)
        while True:
            try:
                query = input_query()
                print()
                command = get_primary_command(query)

                if command == 'exit':
                    break
                
                elif command == None:
                    continue

                else:
                    Q.parse(query)
                    if Q.change_in_prompt:
                        Q.change_in_prompt == False
                        prompt_text = Q.new_prompt
                        
            except Exception as e:
                console.print(f'{error_emoji()} [bold red] {e.args[1]}')