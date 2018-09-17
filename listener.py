def listener():
    listener_str = raw_input('Enter command:')
    if listener_str == "Echo":
        print ('You use right command!')
    else:
        print ("Ooops, something went wrong...")


if __name__ == "__main__":
    listener()
