import os
from config import CLIENT_ID, CLIENT_SECRET, CLIENT_SCOPES, TOKEN_PATH, TOKEN_FILE, RESULT_LINK
from O365 import Account,FileSystemTokenBackend
from multiprocessing import Lock, Process, Queue, current_process
import queue
import time
import sys

from datetime import date

today = date.today()
print("Today's date:", today)
print("Today's date:", today)
