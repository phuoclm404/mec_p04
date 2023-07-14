log = []


def data(data):
    global log
    log.append(data)


def print_log():
    global log
    for i in log:
        print(i)
    log = []
