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

while True:
    # Gets the command string, formats it, then converts it into a list:
    command = input('Command: ').lower()
    debug(command)

    # Command syntax:
    # <type> <encode/decode> <key> <message(greedy)>

    # Format the command into an array using Regex:
    express = re.compile(r'^\s*(\S*)\s*(\S*)\s*(\S*)\s*(.*)$', re.IGNORECASE)
    match = express.match(command)
    command = ['', '', '', '']
    command[0] = match.group(1)
    command[1] = match.group(2)
    command[2] = match.group(3)
    command[3] = match.group(4)

    # Command Tree:

    # If the command is blank, prompt the user again.
    if command[0] == '':
        print("Type 'help' or '?' for a list of commands.\n")
        continue
    # If the command starts with 'quit', print a message and close the program:
    if command[0] == 'quit':
        print('Closing...')
        quit()

    # If the command starts with 'help' or '?', print a list of commands and their functions:
    elif (command[0] == 'help') | (command[0] == '?'):
        if command[1] == 'clock':
            print('clock <encode/decode> <key> <message>')
        else:
            print('help <command>')
            print('? <command>')
            print('clock <encode/decode> <key> <message>')
    # If the command starts with 'clock', Encode or Decode the provided message and key:
    elif command[0] == 'clock':
        if command[1][0:2] == 'e':
            if command[2] == '':
                print("Command 'clock' requires a key argument.")
            else:
                if command[3] == '':
                    print("Command 'clock' requires a message argument.")
                else:
                  print(clock.encode(command[2], command[3]))
        elif command[1][0:2] == 'd':
            if command[2] == '':
                print("Command 'clock' requires a key argument.")
            else:
                if command[3] == '':
                    print("Command 'clock' requires a message argument.")
                else:
                  print(clock.decode(command[2], command[3]))
        else:
            print("Command 'clock' requires an encode/decode argument.")

    # Else print an error message:
    else:
        print("Command '%s' unknown. Type 'help' or '?' for a list of commands.", command[0])
        debug(command)

    print('')
    continue