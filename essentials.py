# Essential Functions

import random

error_emojis = ['unamused', 'slightly_frowning_face', 'worried', 'face_with_raised_eyebrow', 'fearful_face', 'yawning_face', 'astonished_face', 'anxious_face_with_sweat', 'anguished_face', 'cold_face', 'confused_face', 'pensive_face', 'dizzy_face', 'hot_face']
success_emojis = ['partying_face', 'thumbs_up', 'slightly_smiling_face', 'laughing', 'grinning_face', 'grinning_face_with_smiling_eyes', 'grinning_face_with_big_eyes', 'smiling_face_with_smiling_eyes', 'smiling_face_with_sunglasses', 'smiling_face_with_halo', 'winking_face', 'nerd_face']

def success_emoji():
    return f':{random.choice(success_emojis)}:'

def error_emoji():
    return f':{random.choice(error_emojis)}:'


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