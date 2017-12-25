#!Python
"""
This module defines common utilities such as logging functions
and datetime formatting.
"""

__author__ = 'mramirez'

# Required modules
from datetime import datetime
import os, shutil

# Logging Utilities
def logger(log_path, msg):
    """
    Logs a message using MSG + \\n format
    """
    with open(log_path, 'a+') as f:
        f.write(msg + '\n')

def logger_date(log_path, msg):
    """
    Logs a message using YYYY-MM-DD + MSG + \\n format
    """
    with open(log_path, 'a+') as f:
        f.write(datetime.now().strftime('%Y-%m-%d') + '\t' + msg + '\n')
        
def logger_datetime(log_path, msg):
    """
    Logs a message using YYYY-MM-DD HH:MM:SS + MSG + \\n format
    """
    with open(log_path, 'a+') as f:
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t\t' + msg + '\n')
        
def logger_empty_line(log_path, custom_message=''):
    """
    Logs a message using \\n + MSG format
    """
    with open(log_path, 'a+') as f:
        f.write('\n' + custom_message)


# Top-Level Directory/File Utilities
def remove_dir_file(item, verbose=False):
    """
    Attempts to remove a file or directory for a given path (relative or absolute) and 
    returns a message string with the result for such action if verbose is enabled
    """
    if item.is_file():
        try:
            os.remove(item.path)
            if verbose:
                return 'File removed:\t' + item.name
        except:
            if verbose:
                return 'File error:\t\t' + item.name
    elif item.is_dir():
        try:
            shutil.rmtree(item.path)
            if verbose:
                return '*Dir removed:\t' + item.name
        except:
            if verbose:
                return '*Dir error:\t\t' + item.name
    else:
        if verbose:
            return '*** Incorrect argument ***'

def get_num_dirs_files(path='.'):
    """
    Scans path and returns number of directories and files in tuple format 
    (dirs, files)
    """
    num_dirs = 0
    num_files = 0
    for item in os.scandir(path):
        if item.is_file():
            num_files += 1
        elif item.is_dir():
            num_dirs += 1
        else:
            pass
    return num_dirs, num_files

def create_logDirs(path, logpath=False, *pargs):
    """
    Creates directory tree path if not in place already. Also, returns logpath
    if enabled. Need to set logpath=True and provide strftime <format> as well as
    _<logname> parameters
    """
    os.makedirs(path) if not os.path.isdir(path) else None
    if logpath:
        return os.path.join(path, datetime.now().strftime('{}'.format(pargs[0])) + '_{}'.format(pargs[1]))


# Top-Level Module Testing
if __name__ == '__main__':
    log_path = 'LoggerDemo.txt'
    os.remove(log_path) if os.path.isfile(log_path) else None
    print('** Logger Demo File <' + log_path + '> Created **')
    logger(log_path, 'This line corresponds to the logger() definition')
    logger(log_path, 'It uses the following format: MSG + \\n')
    logger_empty_line(log_path, '<< This line corresponds to logger_empty_line(): It creates a blank line w/ a custom message as an option')
    logger_empty_line(log_path, '\n')
    logger_date(log_path, 'This line corresponds to the logger_date() definition')
    logger_date(log_path, 'It uses the followign format: YYYY-MM-DD + MSG + \\n')
    logger_empty_line(log_path)
    logger_datetime(log_path, 'This line corresponds to the logger_datetime() definition')
    logger_datetime(log_path, 'It uses the following format: YYYY-MM-DD HH:MM:SS + MSG + \\n')
