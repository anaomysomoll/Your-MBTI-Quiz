user_data = {} #where user ID and their states coming in, short term memory

def init_user(user_id):
    #Create a fresh state entry for a user. Called on /start and reset.
    user_data[user_id] = { #Sets a nested dictionary
        'question_index': 0,        # which question they're on
        'scores': {                 #The nested dictionary, each dimension starts at 0
            'E': 0, 'I': 0,
            'S': 0, 'N': 0,
            'T': 0, 'F': 0,
            'J': 0, 'P': 0,
        },
        'current_state': 'INTRO',   # tracks quiz stage: INTRO / QUESTION_LOOP / RESULT
        'answers': [],              ##Empty list that will grow as user answers question.
    }


def get_user_state(user_id):
    """Return the user's data dict, or None if they haven't started yet."""
    return user_data.get(user_id)


def next_question(user_id):
    """Advance the question index by 1."""
    if user_id in user_data:
        user_data[user_id]['question_index'] += 1


def update_score(user_id, dimension, value=1):
    """Add `value` to the given MBTI dimension score (e.g. 'E', 'I', 'T'...)."""
    if user_id in user_data:
        user_data[user_id]['scores'][dimension] += value


def record_answer(user_id, answer_label):
    """Store the raw answer label (e.g. 'Agree') in the answers list."""
    if user_id in user_data:
        user_data[user_id]['answers'].append(answer_label)


def reset_user(user_id):
    """ Reuse init_user — single source of truth for the default state structure."""
    init_user(user_id)