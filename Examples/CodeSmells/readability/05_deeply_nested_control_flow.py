# Code smell
if (files_are_valid):
    for line in file_content:
        if line.startswith('Warning '):
            line = line[len('Warning '):]
            if line == 'Connection down!':
                connection.reconnect(
                while (not connection.connected):
                    sleep(0.5)
            elif line == 'System not ready!':
                sleep(2)
            elif line == 'Invalid command!':
                raise Exception('Invalid command sent.')
            else:
                print(line)
        else:
            print(line)

# Better
if (files_are_valid):
    for line in file_content:
        process_line(line)

def process_line(line):
    if line.startswith('Warning '):
        warning = line[len('Warning '):]
        process_warning(warning)
    else:
        print(line)

def process_warning(warning):
    if warning == 'Connection down!':
        reconnect_and_wait()
    elif warning == 'System not ready!':
        sleep(2)
    elif warning == 'Invalid command!':
        raise Exception('Invalid command sent.')
    else:
        print(warning)

def reconnect_and_wait():
    connection.reconnect()
    while (not connection.connected):
        sleep(0.5)


if __name__ == '__main__':
    pass
