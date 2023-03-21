# Query Processor - Parses and Runs Queries.

from essentials import *
from rich.table import Table
from rich.table import Table
from rich.panel import Panel

class QueryProcessor:

    def __init__(self, cursor, console):
        self.cursor = cursor
        self.console = console
        self.change_in_prompt = False

    def parse(self, query): # Parses and Executes the Query
        self.command = get_primary_command(query)

        if self.command in ['select', 'desc', 'describe']:
            self.cursor.execute(query)

            column_names = [i[0] for i in self.cursor.description]
            
            data = self.cursor.fetchall()

            if self.command == 'desc': t_title = 'Describe'
            else: t_title = self.command.capitalize()

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

            self.console.print(table)

        elif self.command == 'show':
            self.cursor.execute(query)
            raw_data = self.cursor.fetchall()
            data = '[bold cyan]'
            for d in raw_data:
                data += d[0] + '\n'
            query = query.split()

            self.console.print(Panel.fit(data, title='[bold dark_green]'+ query[1].upper().replace(';', '')))

        elif self.command == 'use':
            self.cursor.execute(query)
            query = query.split()
            current_db = query[1].replace(";", "").strip().upper()
            self.console.print(f'{success_emoji()} [bold spring_green3] Using { current_db } ')
            self.change_in_prompt = True
            self.new_prompt = f'mysql[{current_db}]> '

        else:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            for row in data:
                print(row)
            self.conn.commit()
        
        self.acknowledge_query()

    def acknowledge_query(self): # Acknowleges Successful Queries.
        if self.command in ['insert', 'delete', 'update', 'alter']:
            rows_affected = self.cursor.rowcount            
            self.console.print(f'[bold green] Query Ok[/] {success_emoji()} , {rows_affected} rows affected.')                
        elif self.command in ['select', 'desc', 'describe']:
            rows_set = self.cursor.rowcount            
            self.console.print(f'[bold green] Query Ok[/] {success_emoji()} , {rows_set} rows in set.')
        elif self.command == 'use':
            print()
        else:
            self.console.print(f'[bold green] Query Ok[/] {success_emoji()}')