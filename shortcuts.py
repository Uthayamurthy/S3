# Converts Shortcuts into valid SQL Code.

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
            return (True, '', f'Set Shortcut Table to {self.table}')
        
        elif squery.startswith('!sh'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                return (False, 'SHOW TABLES;', None)
            elif len(squery) == 2:
                if squery[1].lower() == 'd':
                    return (False, 'SHOW DATABASES;', None)
                elif squery[1].lower() == 't':
                    return (False, 'SHOW TABLES;', None)
                else:
                    raise Exception('Invalid Argument for show shortcut')

        elif squery.startswith('!s'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                return (False, f'SELECT * FROM {self.table};', None)
            elif len(squery) == 2:
                return (False, f'SELECT {squery[1]} FROM {self.table};', None)
            elif len(squery) == 3:
                return (False, f'SELECT {squery[1]} FROM {squery[2]};', None)
        
        elif squery.startswith('!d'):
            squery = list(squery.split(' '))
            if len(squery) == 1:
                return (False, f'DESC {self.table}', None)
            elif len(squery) == 2:
                return (False, f'DESC {squery[1]}', None)

        else:
            raise Exception('Invalid Shortcut, please try again.')