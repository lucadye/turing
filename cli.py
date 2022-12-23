# Debug stuff:
def debug (text):
    if __name__[0:5] == 'debug':
        print(text)

print('''--------------------------------------
#####  #   #  ####   ###  #   #   ###
  #    #   #  #   #   #   ##  #  #
  #    #   #  ####    #   # # #  #  ##
  #    #   #  #  #    #   #  ##  #   #
  #     ###   #   #  ###  #   #   ###
--------------------------------------''')


# Modules:
import re
import clock


# Constants:
whitespaces = [' ', '\t' '\n']


# Gets the command string, formats it, then converts it into a list:
command = input('Command: ').lower()
debug(command)

# Command syntax:
# <type> <encode/decode> <key> <message(greedy)>

# Format the command into an array using Regex:
express = re.compile(r'^\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)$', re.IGNORECASE)
match = express.match(command)
command = []
command[0] = match.group(1)
command[1] = match.group(2)
command[2] = match.group(3)
command[3] = match.group(4)

# Command Tree:

# If the command starts with 'quit', print a message and close the program:
if command[0] == 'quit':
    print('Closing...')
    quit()

# If the command starts with 'help' or '?', print a list of commands and their functions:
elif command[0] == 'help' | 'help':
    if command[1] == 'clock':
        print('clock <encode/decode> <key> <message>')
    else:
        print('help <command>')
        print('? <command>')
        print('clock <encode/decode> <key> <message>')
# If the command starts with 'clock', Encode or Decode the provided message and key:
elif command[0] == 'clock':
    if command[1][0:2] == 'en':
        clock.encode(command[3], command[4])
    elif command[1][0:2] == 'de':
        clock.decode(command[3], command[4])
    else:
        print("Command 'clock' requires an encode/decode argument.")

# Else print an error message:
else:
    print("Command '%s' unknown. Type 'help' or '?' for a list of commands.", command[0])
    debug(command)