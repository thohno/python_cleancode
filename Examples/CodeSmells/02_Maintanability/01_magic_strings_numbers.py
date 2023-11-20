# Code smell
if line.startswith('Warning '):
    line = line[len('Warning '):]
    if line == 'Connection down!':
        connection.reconnect()
        while (not connection.connected):
            sleep(0.5)


# Better
warning_prefix = 'Warning '
connection_down_msg = 'Connection down!'
reconnect_wait = 0.5

if line.startswith(warning_prefix):
line = line[len(warning_prefix):]
if line == connection_down_msg:
    connection.reconnect()
    while (not connection.connected):
        sleep(reconnect_wait)


if __name__ == '__main__':
    pass
