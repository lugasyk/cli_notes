
notes = {}


def listener():
    firstcom_str = 'Add'
    secondcom_str = 'List'
    thirdcom_str = 'Show'
    fourth_str = 'Help'
    print (firstcom_str + ' or ' + secondcom_str + ' or ' + thirdcom_str + ' or ' + fourth_str)
    while True:
        listener_str = raw_input('Enter command: ')
        if listener_str.startswith('Add'):
            index = len(notes)
            text = raw_input('')
            notes[index] = text
            print(notes[index])
        elif listener_str == "List":
            print notes
        elif listener_str.startswith('Show'):
            index = int(raw_input(''))
            print notes.get(index)
        elif listener_str.startswith('Update'):
            index = int(raw_input(''))
            text = raw_input('')
            notes[index] = text
        elif listener_str.startswith('Help'):
            command = raw_input('')
            if command == 'Add':
                print ("This command helps you to add new notes.")
            elif command == 'Show':
                print ("This command shows the text of a note by an index.")
            elif command == 'List':
                print ("This command shows the list of notes with indexes.")
            elif command == 'Update':
                print ("This command updates the text of a note by an index.")
            elif command == 'Help':
                print ("This command shows the description of the each command.")
        else:
            print ("Ooops, something went wrong...")


if __name__ == "__main__":
    listener()
