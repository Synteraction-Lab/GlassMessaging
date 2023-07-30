# coding=utf-8

def get_new_user_conversation(user, conversations):
    return {
        'user': user,
        'conversations': conversations
    }


def get_new_conversation(id, name, icon, messages):
    return {
        'id': id,
        'name': name,
        'icon': icon,
        'messages': messages,
    }


def get_new_message(conversation_id, sender, time, content, read=False):
    return {
        'conversation_id': conversation_id,
        'sender': sender,
        'time': time,
        'content': content,
        'read': read,
    }
