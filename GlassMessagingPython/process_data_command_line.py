# coding=utf-8

# command line interface
# command format: python3 process_raw_data.py -p <PARTICIPANT_ID> -s <SESSION_ID>

import optparse
import participant_config
from process_data import process_participant_session
import traceback
import sys


def get_testing_sessions(participant):
    sessions = participant_config.get_all_sessions(participant)
    return [x for x in sessions if not participant_config.is_training(participant, x)]


def process_participant(participant):
    sessions = get_testing_sessions(participant)

    for session in sessions:
        try:
            process_participant_session(participant, session)
        except Exception:
            print("Error in data processing")
            traceback.print_exc(file=sys.stdout)


parser = optparse.OptionParser()
parser.add_option("-p", "--participant", dest="participant")
parser.add_option("-s", "--session", dest="session")
parser.add_option("-d", "--date", dest="date")

options, args = parser.parse_args()

# print options
# print args
_participant = options.participant
_session = options.session
_date = options.date

if _session is None:
    process_participant(_participant)
else:
    process_participant_session(_participant, _session, _date)
