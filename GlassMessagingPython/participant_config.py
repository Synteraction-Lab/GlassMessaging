# coding=utf-8


PLATFORM_GLASS = 'glass'
PLATFORM_PHONE = 'phone'
PLATFORM_NONE = 'none'

PRIMARY_TASK_WALKING = 'walking'
PRIMARY_TASK_COMMUTING = 'commuting'
PRIMARY_TASK_EATING = 'eating'

TEXTING_TASK_NONE= 'text_none'
TEXTING_TASK_VIEW = 'text_view'
TEXTING_TASK_REPLY = 'text_reply'
TEXTING_TASK_MULTI = 'text_multi'

MESSAGE_LENGTH_SHORT = "short"
MESSAGE_LENGTH_LONG = "long"
MESSAGE_LENGTH_NONE = "none"

# training vs testing
MESSAGE_GAP_TRAINING = 20
MESSAGE_GAP_TESTING = 45

MESSAGE_COUNT_TRAINING = 8
MESSAGE_COUNT_TESTING = 10


def is_training(participant, session):
    return int(session) < 0


def get_all_sessions(participant):
    session_data = CONFIG[participant]
    return list(session_data.keys())


def get_platform(participant, session):
    return CONFIG[participant][session]['platform']


def get_primary_task(participant, session):
    return CONFIG[participant][session]['primary_task']


def get_texting_task(participant, session):
    return CONFIG[participant][session]['texting_task']


def get_message_count(participant, session):
    return CONFIG[participant][session]['message_count']


def get_message_gap(participant, session):
    return CONFIG[participant][session]['message_gap']


def get_message_length(participant, session):
    return CONFIG[participant][session]['message_length']


CONFIG = {
    'p0': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': 10,
            'message_gap': 15,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_REPLY,
            'message_count': 10,
            'message_gap': 15,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': 10,
            'message_gap': 15,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_REPLY,
            'message_count': 10,
            'message_gap': 15,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': 10,
            'message_gap': 15,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    
    'p1400': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_COMMUTING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
    },
    
    'p1321': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1322': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1323': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1324': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },

    'p1305': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1306': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1307': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1308': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },

    'p1309': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1310': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1311': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1312': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },

    'p1313': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1314': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1315': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1316': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },

    'p1317': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1318': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1319': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
    'p1320': {
        '0': {
            'platform': PLATFORM_NONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_NONE,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_NONE,
        },

        '-1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '-2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TRAINING,
            'message_gap': MESSAGE_GAP_TRAINING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },

        '1': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '2': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_SHORT,
        },
        '3': {
            'platform': PLATFORM_PHONE,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
        '4': {
            'platform': PLATFORM_GLASS,
            'primary_task': PRIMARY_TASK_WALKING,
            'texting_task': TEXTING_TASK_MULTI,
            'message_count': MESSAGE_COUNT_TESTING,
            'message_gap': MESSAGE_GAP_TESTING,
            'message_length': MESSAGE_LENGTH_LONG,
        },
    },
}
