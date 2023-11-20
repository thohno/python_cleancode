# Code smell
def read_log_file(log_file_path):
    # open logfile
    with open(log_file_path, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            print(line)  # print the line

# Better
def read_log_file_better(log_file_path):
    with open(log_file_path, "r") as fh:
        lines = fh.readlines()
    for line in lines:
        print(line)

if __name__ == '__main__':
    pass
