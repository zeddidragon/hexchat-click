__module_name__ = "hexchat_click"
__module_version__ = "1.0"
__module_description__ = "Click links with your keyboard"

import re
import hexchat
import webbrowser

NEW_TAB=2

user_defined_url_regex = hexchat.get_pluginpref('link_clicker_url_regex')

url_history = []
url_regex = user_defined_url_regex or ".*[:\/\/.|.*\..*]*"

usage = """
    Usage: /click <regex>, opens the first url match back in plugin's log
"""

def set_url_regex(args, *_):
    url_regex = args[1]
    hexchat.set_pluginpref('link_clicker_url_regex', url_regex)

def log_urls(args, *_):
    for word in args[1].split():
        if re.match(url_regex, word):
            url_history.append(word) 

def click_link(args, *_):
    regex = args[1] if len(args) > 1 else ''

    for url in reversed(url_history):
        if re.match(".*%s.*" % regex, url):
            webbrowser.open_new_tab(url) 
            return hexchat.EAT_ALL

    print("Unable to find urls matching '%s'" % regex)
    return hexchat.EAT_ALL


hexchat.hook_command('click', click_link, help=usage)

logged_events = [
    "Your Message", "Your Action", "Channel Message", "Channel Action",
    "Channel Action Hilight", "Channel Msg Hilight", "Channel Notice",
    "Private Message", "Private Message to Dialog", "Private Action",
    "Private Action to Dialog", "Motd", "Topic", "Topic Change",
    "Topic Creation", "Private Message", "Part with Reason", "Quit",
    "You Part with Reason"
]
for event in logged_events:
    hexchat.hook_print(event, log_urls)
 
print("Link Clicker loaded")
