# coding=utf-8


import pandas as pd
import numpy as np
import Levenshtein
import utilities


# input: data directory
def get_data_directory(participant, date):
    return f'data/{date}/{participant}'


# input: related to stimuli response
def get_message_info_file_name_prefix(participant, session):
    return f'{participant}_{session}_message_info'


COLUMN_MESSAGE_TYPE = 'type'
COLUMN_MESSAGE_SERVER_TIME = 'server_time'
COLUMN_MESSAGE_ID = 'message_id'
COLUMN_MESSAGE_SENDER = 'sender'
COLUMN_MESSAGE_CONTENT = 'content'
COLUMN_MESSAGE_TIME = 'time'
COLUMN_MESSAGE_DATA = 'data'

EVENT_TYPE_START = 'start'
EVENT_TYPE_STOP = 'stop'
EVENT_TYPE_CLIENT = 'client'
EVENT_TYPE_SERVER = 'server'
EVENT_TYPE_ANNOTATION = 'a1'


# output: converted files
def get_message_summary_output_file(participant, session, date):
    return f'data/{date}/{participant}/{participant}_{session}_summary.csv'


def read_csv_file_with_header(csv_file):
    return pd.read_csv(csv_file, header=0)


def get_array_without_none(array):
    return [item for item in array if item is not None]


def get_value(df_column, row):
    return df_column[row]


# return data_frame from message_info file
def get_message_info_data_frame(participant, session, date):
    data_directory = get_data_directory(participant, date)
    message_info_files = utilities.read_file_names(data_directory, '.csv',
                                                   get_message_info_file_name_prefix(participant,
                                                                                     session))
    return read_csv_file_with_header(message_info_files[0])


def get_nearest_row(row, possible_nearest_rows):
    nearest_row = None

    # next_candidate = (row + 1) or (row + 2)
    next_candidate = row + 1
    if next_candidate not in possible_nearest_rows:
        next_candidate += 1

    while next_candidate in possible_nearest_rows:
        nearest_row = next_candidate

        next_candidate += 1

    # print(f'Nearest row: {row}: {nearest_row}')
    return nearest_row


def process_participant_session(participant, session, date=None):
    if date is None:
        date = utilities.get_date()

    print(f'Participant: {participant}, session: {session}, date: {date}')
    # message info data
    data_frame_message_info = get_message_info_data_frame(participant, session, date)
    # print(data_frame_message_info.shape)
    event_count = data_frame_message_info.shape[0]  # = number of events

    ori_event_type = data_frame_message_info[COLUMN_MESSAGE_TYPE]
    ori_server_time = data_frame_message_info[COLUMN_MESSAGE_SERVER_TIME]
    ori_message_id = data_frame_message_info[COLUMN_MESSAGE_ID]
    ori_message_sender = data_frame_message_info[COLUMN_MESSAGE_SENDER]
    ori_message_content = data_frame_message_info[COLUMN_MESSAGE_CONTENT]
    ori_message_time = data_frame_message_info[COLUMN_MESSAGE_TIME]
    ori_message_data = data_frame_message_info[COLUMN_MESSAGE_DATA]

    # identify start, stop, annotations, client, server
    start_rows = ori_event_type[ori_event_type == EVENT_TYPE_START].index
    stop_rows = ori_event_type[ori_event_type == EVENT_TYPE_STOP].index
    annotation_rows = ori_event_type[ori_event_type == EVENT_TYPE_ANNOTATION].index

    client_rows = ori_event_type[ori_event_type == EVENT_TYPE_CLIENT].index
    client_message_count = len(client_rows)
    server_rows = ori_event_type[ori_event_type == EVENT_TYPE_SERVER].index
    server_message_count = len(server_rows)

    print(
        f'client messages: {client_message_count}, server messages: {server_message_count}, annotations: {len(annotation_rows)}, start : {len(start_rows)}, stop : {len(stop_rows)}')

    start_stop_gap_millis = int(get_value(ori_server_time, stop_rows[-1])) - int(
        get_value(ori_server_time, start_rows[-1]))
    print(f'Time Gap between last stop and start (s): {start_stop_gap_millis / 1000}')

    if server_message_count != client_message_count:
        print('Error: unmatched messages')
        return

    ## reformat data

    # data ordering: start, (client, <annotation?>, server) * n, stop
    # note: first message of client (start chat) and last message of server (stop message) must be discarded
    new_row_count = 1 + server_message_count - 1  # ('start-stop' row + total server messages - last server message)

    # FIXME: Hack to support "none"
    if new_row_count == 0:
        print("\n[WARNING] Server row count is 0. So adding a new row to support start-stop annotations\n")
        new_row_count = 1

    server_type = [None] * new_row_count
    server_message_time = [None] * new_row_count
    server_message_user = [None] * new_row_count
    server_message_content = [None] * new_row_count
    server_message_data = [None] * new_row_count

    annotation_type = [None] * new_row_count
    annotation_time = [None] * new_row_count

    client_type = [None] * new_row_count
    client_message_time = [None] * new_row_count
    client_message_user = [None] * new_row_count
    client_message_content = [None] * new_row_count
    client_message_data = [None] * new_row_count
    client_message_time_diff = [None] * new_row_count

    # set data related to 'start'/'stop' row
    server_type[0] = EVENT_TYPE_START
    server_message_time[0] = get_value(ori_server_time, start_rows[0])
    client_type[0] = EVENT_TYPE_STOP
    client_message_time[0] = get_value(ori_server_time, stop_rows[0])

    current_row = 1

    # set data related to messages (exclude first client and last server messages)
    for current_server_row in server_rows:
        if current_row >= new_row_count:
            break
        # print(current_row, new_row_count)

        server_type[current_row] = EVENT_TYPE_SERVER
        server_message_time[current_row] = get_value(ori_message_time, current_server_row)
        server_message_user[current_row] = get_value(ori_message_sender, current_server_row)
        server_message_content[current_row] = get_value(ori_message_content, current_server_row)
        server_message_data[current_row] = get_value(ori_message_data, current_server_row)

        nearest_annotation_row = get_nearest_row(current_server_row, annotation_rows)
        # print(f'current row: {current_row}, current_server_row:{current_server_row}, nearest_annotation_row:{nearest_annotation_row}, annotation_rows:{annotation_rows}')
        if nearest_annotation_row is not None:
            annotation_type[current_row] = get_value(ori_event_type, nearest_annotation_row)
            annotation_time[current_row] = get_value(ori_server_time, nearest_annotation_row)

        nearest_client_row = get_nearest_row(current_server_row, client_rows)
        # print(f'current row: {current_row}, current_server_row:{current_server_row}, nearest_client_row:{nearest_client_row}, client_rows:{client_rows}')
        client_type[current_row] = EVENT_TYPE_CLIENT
        client_message_time[current_row] = get_value(ori_message_time, nearest_client_row)
        client_message_user[current_row] = get_value(ori_message_sender, nearest_client_row)
        client_message_content[current_row] = get_value(ori_message_content, nearest_client_row)
        client_message_data[current_row] = get_value(ori_message_data, nearest_client_row)
        client_message_time_diff[current_row] = int(client_message_time[current_row]) - int(
            get_value(ori_server_time, nearest_client_row))

        current_row += 1

    # calculate results
    server_client_name_diff = [None] * new_row_count
    server_client_content_diff = [None] * new_row_count
    server_client_time_diff = [0] * new_row_count
    annotation_client_time_diff = [None] * new_row_count

    for current_row in range(new_row_count):
        if server_message_user[current_row] != client_message_user[current_row]:
            if server_message_user[current_row] == "None" and server_message_content[
                current_row] is not None:  # special case for instruction
                intended_sender = utilities.get_first_text_inside_parentheses_without_parentheses(
                    server_message_content[current_row]).strip()
                print(
                    f'Changing "server_message_user" from [{server_message_user[current_row]}] to [{intended_sender}]')
                server_message_user[current_row] = intended_sender

            server_client_name_diff[current_row] = 1 - Levenshtein.ratio(
                server_message_user[current_row], client_message_user[current_row])
        else:
            server_client_name_diff[current_row] = 0

        if server_message_content[current_row] is not None:
            server_text = utilities.get_text_without_parentheses_text(
                server_message_content[current_row]).strip().lower()
            client_text = client_message_content[current_row].strip().lower()
            server_client_content_diff[current_row] = 1 - Levenshtein.ratio(server_text,
                                                                            client_text)
        #             print(server_text, client_text, server_client_content_diff[current_row])
        else:
            server_client_content_diff[current_row] = None

        server_client_time_diff[current_row] = int(client_message_time[current_row]) - int(
            server_message_time[current_row])

        if annotation_time[current_row] is not None:
            annotation_client_time_diff[current_row] = int(client_message_time[current_row]) - \
                                                       int(annotation_time[current_row]) - \
                                                       client_message_time_diff[current_row]
        else:
            annotation_client_time_diff[current_row] = None

    print_stats(server_client_time_diff, client_message_time_diff, annotation_client_time_diff,
                server_client_name_diff, server_client_content_diff)

    csv_data = {'server_type': server_type,
                'server_message_time': server_message_time,
                'server_message_user': server_message_user,
                'server_message_content': server_message_content,
                'server_message_data': server_message_data,
                'annotation_type': annotation_type,
                'annotation_time': annotation_time,
                'client_type': client_type,
                'client_message_time': client_message_time,
                'client_message_user': client_message_user,
                'client_message_content': client_message_content,
                'client_message_data': client_message_data,
                'client_message_time_diff': client_message_time_diff,

                'server_client_name_diff': server_client_name_diff,
                # = sever sender's name != client sender's name
                'server_client_content_diff': server_client_content_diff,
                # = server sent message != client replied message
                'server_client_time_diff': server_client_time_diff,
                # = sever sent time - client replied time
                'annotation_client_time_diff': annotation_client_time_diff,
                # = annotation added time - client replied time
                }
    # print(csv_data)
    converted_file_name = get_message_summary_output_file(participant, session, date)
    pd.DataFrame(data=csv_data).to_csv(converted_file_name)
    print(f'Summary data is written to [{converted_file_name}]\n\n')


def print_stats(server_client_time_diff, client_message_time_diff, annotation_client_time_diff,
                server_client_name_diff, server_client_content_diff):
    if len(server_client_time_diff) > 1:
        print(f'Total server duration (s): {server_client_time_diff[0] / 1000}\n'
              f'Avg message send time (s): {np.mean(get_array_without_none(client_message_time_diff[1:])) / 1000}\n'
              f'Avg server-client time (s): {np.mean(get_array_without_none(server_client_time_diff[1:])) / 1000}\n'
              f'Avg annotation-client time (s): {np.mean(get_array_without_none(annotation_client_time_diff[1:])) / 1000}\n'
              f'Avg wrong sender (%): {np.mean(get_array_without_none(server_client_name_diff[1:])) * 100}\n'
              f'Avg wrong text (%): {np.nanmean(get_array_without_none(server_client_content_diff[1:])) * 100}\n'
              )
    else:
        print(f'Total server duration (s): {server_client_time_diff[0] / 1000}\n')

# print(Levenshtein.ratio("Hi, how are you?","Hi, how are you?"))
# print(Levenshtein.ratio("Hi, how are you?",'Hi, how are you?'))
# print(Levenshtein.ratio("Hi, how are you?","Hi, how are you"))
# print(Levenshtein.ratio("Hi, how are you?","hi, how are you?"))
# print(Levenshtein.ratio("Hi, how are you?","hi how are you"))
# print(Levenshtein.ratio("Hi, how are you?","Hi, how are"))
