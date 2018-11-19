
notes = {}


def listener():
    firstcom_str = 'Add'
    secondcom_str = 'List'
    thirdcom_str = 'Show'
    print (firstcom_str + ' or ' + secondcom_str + ' or ' + thirdcom_str)
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
        else:
            print ("Ooops, something went wrong...")


if __name__ == "__main__":
    listener()
