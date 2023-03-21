#!/home/uthayamurthy/Development/SSS/venv/bin python3

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from essentials import *
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
        while True:
            try:
                query = input_query()
                print()
                command = get_primary_command(query)

                if command == 'exit':
                    break
                
                elif command == None:
                    continue

                elif command in ['select', 'desc', 'describe']:
                    cursor.execute(query)

                    column_names = [i[0] for i in cursor.description]
                    
                    data = cursor.fetchall()

                    if command == 'desc': t_title = 'Describe'
                    else: t_title = command.capitalize()

                    table = Table(title=f'[bold sky_blue3]{t_title} Query')
                    
                    for cname in column_names:
                        table.add_column(cname)
                    

                    for r in data:
                        l = list(r)
                        for a in l:
                            if isinstance(a, str):
                                continue
                            else:
                                l[l.index(a)] = str(a)
                        r = tuple(l)
                        table.add_row(*r)
                        # print(r)

                    console.print(table)
                
                elif command == 'show':
                    cursor.execute(query)
                    raw_data = cursor.fetchall()
                    data = '[bold cyan]'
                    for d in raw_data:
                        data += d[0] + '\n'
                    query = query.split()

                    console.print(Panel.fit(data, title='[bold dark_green]'+ query[1].upper().replace(';', '')))

                elif command == 'use':
                    cursor.execute(query)
                    query = query.split()
                    current_table = query[1].replace(";", "").strip().upper()
                    console.print(f'{success_emoji()} Using { current_table } ')
                    prompt_text = f'[bold dark_olive_green1]mysql[{current_table}]> '

                else:
                    cursor.execute(query)
                    data = cursor.fetchall()
                    for row in data:
                        print(row)
                    conn.commit()

                if command in ['insert', 'delete', 'update', 'alter']:
                    rows_affected = cursor.rowcount            
                    console.print(f'[bold green] Query Ok[/] {success_emoji()} , {rows_affected} rows affected.')                
                elif command in ['select', 'desc', 'describe']:
                    rows_set = cursor.rowcount            
                    console.print(f'[bold green] Query Ok[/] {success_emoji()} , {rows_set} rows in set.')
                else:
                    console.print(f'[bold green] Query Ok[/] {success_emoji()}')

            except Exception as e:
                console.print(f'{error_emoji()} [bold red] {e.args[1]}')