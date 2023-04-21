# shortcuts.py : Converts Shortcuts into valid SQL Code.

# Even Shortcut returns a tuple.
# (nes, query, s_ack, bulk)

from auto_insert import auto_insert, set_locale

class ShortcutProcessor:

    def __init__(self):
        self.table = None

    @staticmethod
    def check_shortcuts(squery):
        if squery.startswith('!'):
            return True
        else:
            return False

    
    def process_shortcuts(self, squery):
        squery = squery.replace(';', '')
        squery = squery.strip()

        if squery.startswith('!t'):
            squery = list(squery.split(' '))
            if len(squery) < 2:
                raise Exception('Expected a table name.')

            self.table = squery[1]
            return (True, '', f'Set Shortcut Table to {self.table}', False)
        
        elif squery.startswith('!sh'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                return (False, 'SHOW TABLES;', None, False)
            elif len(squery) == 2:
                if squery[1].lower() == 'd':
                    return (False, 'SHOW DATABASES;', None, False)
                elif squery[1].lower() == 't':
                    return (False, 'SHOW TABLES;', None, False)
                else:
                    raise Exception('Invalid Argument for show shortcut')

        elif squery.startswith('!s'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                return (False, f'SELECT * FROM {self.table};', None, False)
            elif len(squery) == 2:
                return (False, f'SELECT {squery[1]} FROM {self.table};', None, False)
            elif len(squery) == 3:
                return (False, f'SELECT {squery[1]} FROM {squery[2]};', None, False)
        
        elif squery.startswith('!d'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                return (False, f'DESC {self.table}', None, False)
            elif len(squery) == 2:
                return (False, f'DESC {squery[1]}', None, False)
        
        elif squery.startswith('!ai'):
            squery = list(squery.split(' '))
            queries = auto_insert(squery, self.table)
            return (True, queries, f'Executed {len(queries)} Auto Insert Queries', True)

        elif squery.startswith('!i'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                raise Exception('Insufficient Arguments. Expected more arguments for insert shortcut.')
            elif len(squery) == 2:
                return (False, f'INSERT INTO {self.table} Values({squery[1]});', None, False)
            elif len(squery) == 3:
                return (False, f'INSERT INTO {self.table}({squery[2]}) Values({squery[1]});', None, False)
            elif len(squery) == 4:
                return (False, f'INSERT INTO {squery[3]}({squery[2]}) Values({squery[1]});', None, False)
        
        elif squery.startswith('!l'):
            squery = list(squery.split(' '))
            if len(squery) < 2:
                raise Exception('Expected a locale name.')

            locale = squery[1]
            set_locale(locale)
            return (True, '', f'Set Shortcut locale to {locale}', False)

        else:
            raise Exception('Invalid Shortcut, please try again.')