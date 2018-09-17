notes = {}

def listener():
    firstcom_str = 'Add'
    secondcom_str = 'List'
    thirdcom_str = 'Show'
    print (firstcom_str + ' or ' + secondcom_str + ' or ' + thirdcom_str)
    listener_str = raw_input('Enter command: ')
    if listener_str.startswith('Add'):
        index = len(notes)
        notes[index] = listener_str
        print(notes[index])
        print str.replace("You've inter:", " ", )
    elif listener_str == "List":
        print notes
    elif listener_str == "Show":
        print
    else:
        print ("Ooops, something went wrong...")


if __name__ == "__main__":
    listener()
