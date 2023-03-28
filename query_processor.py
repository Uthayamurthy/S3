# Query Processor - Parses and Runs Queries.

from essentials import *
from rich.table import Table
from rich.table import Table
from rich.panel import Panel
from shortcuts import ShortcutProcessor

class QueryProcessor:

    def __init__(self, cursor, console, conn):
        self.cursor = cursor
        self.console = console
        self.change_in_prompt = False
        self.sp = ShortcutProcessor()
        self.conn = conn
        self.curr_table = None

    def parse(self, query): # Parses and Executes the Query
        nes = False # Non Executable Shortcut
        s_ack = None

        if self.sp.check_shortcuts(query):
            sc = self.sp.process_shortcuts(query)
            nes = sc[0]
            query = sc[1]
            s_ack = sc[2]

        self.command = get_primary_command(query)

        if nes == True:
            pass

        elif self.command in ['select', 'desc', 'describe']:
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
                if raw_data.index(d) != len(raw_data) - 1:
                    data += d[0] + '\n'
                else: # Avoid new line character in the last item.
                    data += d[0]
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
            print('Else Executed !')
            print(query)
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            for row in data:
                print(row)
            self.conn.commit()
        
        self.acknowledge_query(s_ack)

    def acknowledge_query(self, s_ack=None): # Acknowleges Successful Queries.
        if s_ack != None:
            self.console.print(f'[bold green] {s_ack} [/] {success_emoji()}')
        elif self.command in ['insert', 'delete', 'update', 'alter']:
            rows_affected = self.cursor.rowcount            
            self.console.print(f'[bold green] Query Ok[/] {success_emoji()} , {rows_affected} rows affected.')                
        elif self.command in ['select', 'desc', 'describe']:
            rows_set = self.cursor.rowcount            
            self.console.print(f'[bold green] Query Ok[/] {success_emoji()} , {rows_set} rows in set.')
        elif self.command == 'use':
            print()
        else:
            self.console.print(f'[bold green] Query Ok[/] {success_emoji()}')