# Essential Functions

def check_query_end(query):
    query = query.strip()
    
    if query == '' or query == ' ':
        return True
    
    if query.endswith(';'):
        return True
    else:
        return False

def get_primary_command(query):
    
    if query == '' or query == ' ':
        query = None
        return query
    
    x = query.split(' ')

    if len(x) == 1:
        return x[0].replace(';', '').lower()
    else:
        return x[0].lower()