__module_name__ = "hexchat_click"
__module_version__ = "1.0"
__module_description__ = "Click links with your keyboard"

import re
import hexchat
import webbrowser
from collections import defaultdict

user_defined_url_regex = hexchat.get_pluginpref('link_clicker_url_regex')

global_url_history = []
url_history = defaultdict(lambda: defaultdict(list))
url_regex = user_defined_url_regex or ".*:\/\/.*"

usage = """
    Usage: /click <regex>, opens the first url match back in plugin's log.
    Configure: /click -set_url_regex <new regex>
"""

logged_events = [
    "Your Message", "Your Action", "Channel Message", "Channel Action",
    "Channel Action Hilight", "Channel Msg Hilight", "Channel Notice",
    "Private Message", "Private Message to Dialog", "Private Action",
    "Private Action to Dialog", "Motd", "Topic", "Topic Change",
    "Topic Creation", "Private Message", "Part with Reason", "Quit",
    "You Part with Reason"
]

def set_url_regex(new_regex):
    url_regex = new_regex
    hexchat.set_pluginpref('link_clicker_url_regex', url_regex)

def log_urls(args, *_):
    server = hexchat.get_info('server')
    channel = hexchat.get_info('channel')
    for word in args[1].split():
        if re.match(url_regex, word):
            global_url_history.append(word)
            url_history[server][channel].append(word) 

def search_link(regex, arr):
    for url in reversed(arr):
        if re.match(".*%s.*" % regex, url):
            return webbrowser.open_new_tab(url) 

    print("Unable to find urls matching '%s'" % regex)

def try_arg(args, i):
    return args[i] if len(args) > i else ''

def controller(args, *_):
    if try_arg(args, 1) == "-set_url_regex":
        set_url_regex(try_arg(args, 2))
    elif try_arg(args, 1) == "-g":
        search_link(try_arg(args, 2), global_url_history)
    else:
        server = hexchat.get_info('server')
        channel = hexchat.get_info('channel')
        search_link(try_arg(args, 1), url_history[server][channel])

    return hexchat.EAT_ALL

hexchat.hook_command('click', controller, help=usage)

for event in logged_events:
    hexchat.hook_print(event, log_urls)
 
print("Hexchat Click loaded")
