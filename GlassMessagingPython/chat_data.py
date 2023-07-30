# coding=utf-8

from random import randint
from random import shuffle
import chat_formatter
import utilities

import participant_config

# source: https://www.keithv.com/software/enronmobile/
# FIXME: remove hard to pronounce names, marks, ...
MESSAGES_TESTING_SHORT = [
    "Thursday works better for me.",
    "Pressure to finish my review.",
    "I have never worked with her.",
    "Hope you guys are doing fine.",
    "I am glad she likes her tree.",
    "I would like to attend if so.",
    "She has absolutely everything.",
    "I hope you are feeling better.",
    "Call me to give you a heads up.",
    "Has anyone else heard anything?",
    "I would be glad to participate.",
    "There will be plenty of others.",
    "I will call you in the morning.",
    "Can we have them until we move?",
    "Do we need to worry about this?",
    "Thanks for the quick turnaround.",
    "He loves everything about rocks.",
    "Thank you for your prompt reply.",
    "Could you see where this stands?",
    "Is this the only time available?",
    "Please call tomorrow if possible.",
    "They are more efficiently conducted.",
    "Do they have some conflicts here?",
    "I changed that in previous draft.",
    "I think that is the right answer.",
    "I wanted to go drinking with you.",
    "We need to talk about this month.",
    "We are waiting on the cold front.",
    "We can have a drink and catch up.",
    "I will catch up with you tomorrow.",
    "I am waiting until she comes home.",
    "What number should he call you on?",
    "I think those are the right dates.",
    "I have a high table in my office. ",
    "Hope your trip to Florida was good.",
    "I have been to many baseball games.",
    "Are you going to join us for lunch?",
    "Should systems manage the migration?",
    "Hopefully this can wait until Monday.",
    "I am out of town on business tonight.",
    "I hope he is having a fantastic time.",
    "No employment claims for gas or power.",
    "I worked on the grade level promotion.",
    "Do you still need me to sign anything?",
    "Tell her to get my expense report done.",
    "That would likely be an expensive option.",
    "I agree since I am at the bank right now.",
]

MESSAGES_TESTING_LONG = [
    "James should be there, so I can tell him where to get the schedules.",
    "We have attached conditions to our commitment, that I like to preserve.",
    "Unless you can think of a reason why not make it simple to process?",
    "What is the name of the website where all of this information resides?",
    "He is reading and hearing brief discussions, about noise in the market.",
    "Let's make sure we have all bases covered and telephone tree in place.",
    "I asked what he would do, but the person I talked to didn't know.",
    "I will try and arrange to sit down and look at the most recent numbers.",
    "Did you add the sections about the new rules, that we want for employees?",
    "Just send the package to Kevin as we need backup and not presentations.",
    "I do not believe that we are in violation of any transfer restrictions.",
    "Can you please print the attachment and give them for the meeting today?",
    "Yes, but it will take me another day or more for the announcement.",
    "If so, send me an email, and I will come up with a solution before I leave.",
    "Generally he does not like these, but I am OK if he wants to let them.",
    "If she want, she could use a photo album or scrapbook for her story.",
    "Can you send me an invitation in Outlook, for the two meetings on Monday?",
    "I have never seen such courage and strength in an uncertain environment.",
    "No other major projects underway that are impacted by environmental damage.",
    "Hey, I have several contracts which the bankers want early tomorrow.",
    "I will forward it tomorrow to make him aware that something is coming.",
    "An increase in the fee for this important market chain is the deal.",
    "Cash is king for now and we need the pricing to get the rest of the cash.",
    "They mentioned that today is the deadline for the 4th amendment.",
    "If we agree to do so, then our records should reflect that service date.",
    "You have to be careful not to lose historical data for rate purposes.",
    "Can you talk to the appropriate commercial people and get them to decide?",
    "I will need you to correct your language on the gas bill for tomorrow.",
    "I think he will be done at his current offer, do you want to give him more?",
    "Was it an actual downgrade or just that they would not agree to do so?",
    "Please call help desk and ask her to fax a copy of the executed guarantee.",
    "We are waiting on the higher ups to fill us in, on what we are negotiating.",
    "I have not heard from anyone about the expected transition time frame.",
    "I am out of office this week and will be unable to fill out questionnaire.",
    "Today we are going to practice and then we will catch our flight home.",
    "I may try to call you a bit later on storage but we did not see that deal.",
    "We may need more logins if there are multiple people required to schedule.",
    "I talked to them last night, and we are on for Christmas dinner with them.",
    "I would still like to discuss status of the program when you are available.",
    "And also, can you start planning to have infinity up and running on day one?",
    "I think she should not work here, as she obviously was not happy.",
    "However let's wait and see if we can get one more draft done for Wednesday.",
    "It is enough to say all of these will be taken care before it funds.",
    "I have been thinking about them for several weeks yet failed to recover.",
    "I know it is our core business, but it might be quicker than selling Brazil.",
    "Jim should call with a phone number so I don't have to come over there.",
    "Probably need additional review by someone now, given the current situation.",
    "Since this is the first time we received this form I just wanted to confirm.",
    "I will see if we can incorporate some of this in the changes we are proposing.",
    "You have approval to submit a request to the cash committee via this.",
    "Besides Friday and Monday afternoons I do not have any other time off.",
]

MESSAGES_TRAINING = [
    "Are you feeling better?",
    "Do not forget the wood.",
    "What is the cost issue?",
    "Did you differ from me?",
    "Or are you going to be tied up with dinner?",
    "Wednesday is definitely a hot chocolate day.",
    "Are you getting all the information you need?",
    "Where do you want to meet to walk over there?",
    "I do not have the distraction of taking care of a small child.",
]

CONVERSATION_NAMES = [
    'Peter',
    'Nancy',
    'John',
    'Linda',

    'Susie',
    'Betty',
    'Tony',
    'Jack',

    'Lily',
    'Kelly',
    'Robin',
    'Vivian',

    'Tom',
    'Frank',
    'Dan',
    'Richard',
]

TOTAL_CONVERSATION_COUNT = len(CONVERSATION_NAMES)

prev_conversation_index = None
random_conversation_id_list = []


def _get_random_conversation_id():
    global prev_conversation_index, random_conversation_id_list

    if prev_conversation_index is None or len(
            random_conversation_id_list) != TOTAL_CONVERSATION_COUNT:
        prev_conversation_index = -1
        random_conversation_id_list = list(range(TOTAL_CONVERSATION_COUNT))
        shuffle(random_conversation_id_list)

    prev_conversation_index += 1
    if prev_conversation_index >= TOTAL_CONVERSATION_COUNT:
        prev_conversation_index = 0

    return random_conversation_id_list[prev_conversation_index]


# return sender_id, receiver_id
def get_random_sender_receiver(texting_task):
    if texting_task == participant_config.TEXTING_TASK_VIEW:
        sender_id = _get_random_conversation_id()
        receiver_id = None
    elif texting_task == participant_config.TEXTING_TASK_REPLY:
        sender_id = _get_random_conversation_id()
        receiver_id = None
    elif texting_task == participant_config.TEXTING_TASK_MULTI:
        sender_id = None
        receiver_id = _get_random_conversation_id()
    else:
        print(f'Error: Unsupported texting task: {texting_task}')
        sender_id = None
        receiver_id = None

    return sender_id, receiver_id


def get_empty_message():
    return chat_formatter.get_new_message(None, None, utilities.get_current_millis(), '')


SEQUENCE_FILE_TEST_MESSAGE = 'sequence_test_messages.json'
MAX_AGE_OF_SAVED_DATA_MINUTES = 120


def _get_message_history_file(participant, length):
    return f'data/{utilities.get_date()}/{participant}/_{participant}_{length}_{SEQUENCE_FILE_TEST_MESSAGE}'


# return message_id, message_content
def _get_next_testing_message(participant, length):
    message_history_file = _get_message_history_file(participant, length)
    order, index = utilities.read_order_data(message_history_file, MAX_AGE_OF_SAVED_DATA_MINUTES)

    message_list = []
    if length == participant_config.MESSAGE_LENGTH_SHORT:
        message_list = MESSAGES_TESTING_SHORT
    elif length == participant_config.MESSAGE_LENGTH_LONG:
        message_list = MESSAGES_TESTING_LONG
    else:
        print(f'Error: Unsupported message length: {length}, {participant}')

    tot_message_count = len(message_list)

    if order is None or index is None:
        order = list(range(tot_message_count))
        shuffle(order)
        index = 0

    index += 1
    if index > tot_message_count:
        index = 0

    utilities.save_order_data(message_history_file, order, index)
    message_id = order[index]

    return message_id, message_list[message_id]


training_message_id = -1


def _get_next_training_message():
    global training_message_id

    if training_message_id == -1:
        shuffle(MESSAGES_TRAINING)

    training_message_id += 1
    if training_message_id > len(MESSAGES_TRAINING):
        training_message_id = 0

    return training_message_id, MESSAGES_TRAINING[training_message_id]


def get_random_message(platform, texting_task, participant, texting_length, is_training):
    if is_training:
        message_id, message = _get_next_training_message()
    else:
        message_id, message = _get_next_testing_message(participant, texting_length)

    sender_id, receiver_id = get_random_sender_receiver(texting_task)

    if receiver_id is None:
        modified_message = message
    else:
        modified_message = f'[{get_conversation_name(receiver_id)}] {message}'

    if sender_id is None:
        message = chat_formatter.get_new_message(None, None, utilities.get_current_millis(),
                                                 modified_message)
    else:
        message = chat_formatter.get_new_message(get_platform_conversation_id(platform, sender_id),
                                                 f'{get_conversation_name(sender_id)}',
                                                 utilities.get_current_millis(),
                                                 modified_message)

    message['message_id'] = message_id
    return message


def get_custom_message(message_content, platform):
    sender_id = 0
    return chat_formatter.get_new_message(get_platform_conversation_id(platform, sender_id),
                                          get_conversation_name(sender_id),
                                          utilities.get_current_millis(),
                                          message_content)


def get_init_user_conversation():
    return chat_formatter.get_new_user_conversation("Me", [])


def get_init_conversations(platform):
    return [chat_formatter.get_new_conversation(get_platform_conversation_id(platform, x),
                                                f'{get_conversation_name(x)}',
                                                f'{get_conversation_name(x)}',
                                                []) for x in range(TOTAL_CONVERSATION_COUNT)]


def get_init_messages(platform):
    introductions = [
        chat_formatter.get_new_message(get_platform_conversation_id(platform, x),
                                       f'{get_conversation_name(x)}',
                                       utilities.get_current_millis(),
                                       f'Hi, I am {get_conversation_name(x)}.',
                                       True) for x in range(TOTAL_CONVERSATION_COUNT)]
    greetings = [
        chat_formatter.get_new_message(get_platform_conversation_id(platform, x),
                                       f'{get_conversation_name(x)}',
                                       utilities.get_current_millis(),
                                       'Nice to meet you!'
                                       , True) for x in range(TOTAL_CONVERSATION_COUNT)]
    return introductions + greetings


def get_conversation_name(conversation_id):
    return CONVERSATION_NAMES[conversation_id]


PLATFORM_GLASS_CONVERSATION_IDS = [x for x in range(TOTAL_CONVERSATION_COUNT)]

# Note: these are specific to the selected telegram bot (map name with id)
PLATFORM_PHONE_CONVERSATION_IDS = [
    -708515257,
    -623569996,
    -753912170,
    -618194111,

    -689721398,
    -732990650,
    -711610574,
    -714815789,

    -758255738,
    -737681540,
    -607621996,
    -637440928,

    -772797900,
    -640942293,
    -698550954,
    -646192119,
]


def get_platform_conversation_id(platform, conversation_id):
    if platform == participant_config.PLATFORM_GLASS:
        return PLATFORM_GLASS_CONVERSATION_IDS[conversation_id]
    elif platform == participant_config.PLATFORM_PHONE:
        return PLATFORM_PHONE_CONVERSATION_IDS[conversation_id]
    else:
        print("Error: Undefined platform")
        return None


def get_conversation_name_by_platform_id(platform_conversation_id):
    if platform_conversation_id is None:
        print('Error: Empty conversation id for platform!')
        return None

    platform_id = int(platform_conversation_id)
    if platform_id in PLATFORM_GLASS_CONVERSATION_IDS:
        return get_conversation_name(
            PLATFORM_GLASS_CONVERSATION_IDS.index(platform_id))
    if platform_id in PLATFORM_PHONE_CONVERSATION_IDS:
        return get_conversation_name(
            PLATFORM_PHONE_CONVERSATION_IDS.index(platform_id))

    print(f'Error: platform id [{platform_id}] not found')
    return None
