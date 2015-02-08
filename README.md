# Hexchat Click

Click links in Hexchat using your keyboard.

## Installation

Unix:
  Place hexchat_click.py in ~/.config/hexchat/addons/

Windows:
  Place hexchat_click.py in %APPDATA\Hexchat\addons\

Either restart Hexchat or use this command to load the module:
/py LOAD hexchat_click.py

## Usage

/click [regex]

Will search backwards in the plugin's history for the first link that matches
the regex. If you don't supply an argument, it'll simply open the last link
posted in your channel.

The plugin will start logging urls from all channels in memory. URLs from before
the plugin was loaded are not remembered, nor will URLs from previous sessions.

To search outside the scope of your current channel, use
/click -g [regex]

## Requirements

Hexchat:
  https://hexchat.github.io/

You will also need the Python plugin installed.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

8/2 - 2015 Initial commit

8/2 - 2015 Regex shenanigans

8/2 - 2015 Per-channel log

## Credits

Zeddy - Wrote the plugin

## License

        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
