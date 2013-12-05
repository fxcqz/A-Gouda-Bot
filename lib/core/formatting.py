import ast
import os.path

formats = {
'black': '\x1b[30m', 
'red': '\x1b[31m', 'green': '\x1b[32m',
'yellow': '\x1b[33m',
'blue': '\x1b[34m',
'purple': '\x1b[35m',
'cyan': '\x1b[36m',
'black_bg': '\x1b[40m', 
'red_bg': '\x1b[41m', 'green': '\x1b[32m',
'yellow_bg': '\x1b[43m',
'blue_bg': '\x1b[44m',
'purple_bg': '\x1b[45m',
'cyan_bg': '\x1b[46m',
'bold': '\x1b[1m',
'underline': '\x1b[4m',
'flash': '\x1b[5m',
'clear': '\x1b[0m'}
tag_left = "["
tag_right = "]"

def fmat(string, fmat):
    return str(formats[fmat] + string + '\x1b[0m')

def fmatTags(string):
    return_string = string
    for tag, ctrl_code in formats:
        return_string = return_string.replace(tag_left + tag + tag_right, ctrl_code)
    return return_string
