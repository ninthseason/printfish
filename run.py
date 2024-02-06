import threading

# state:
# 0: _/$
# 1: <
# 2: >
# 3: <>
# 4: ><
# 5: <><
# 6: ><>

state_machine = {
    0: {'<': 1, '>': 2},
    1: {'>': 3},
    2: {'<': 4},
    3: {'<': 5},
    4: {'>': 6},
    5: {'_': 0},
    6: {'_': 0},
}
current_state = 0

mutex = threading.Lock()
cv = threading.Condition()


def left_printer():
    # always print '<'
    global current_state
    while True:
        cv.acquire()
        while current_state not in [0, 2, 3]:
            cv.wait()
        print('<', end='')
        current_state = state_machine[current_state]['<']
        cv.notify_all()
        cv.release()


def right_printer():
    # always print '>'
    global current_state
    while True:
        cv.acquire()
        while current_state not in [0, 1, 4]:
            cv.wait()
        print('>', end='')
        current_state = state_machine[current_state]['>']
        cv.notify_all()
        cv.release()


def dash_printer():
    # always print '_'
    global current_state
    while True:
        cv.acquire()
        while current_state not in [5, 6]:
            cv.wait()
        print('_', end='')
        current_state = state_machine[current_state]['_']
        cv.notify_all()
        cv.release()


if __name__ == '__main__':
    threading.Thread(target=left_printer).start()
    threading.Thread(target=right_printer).start()
    threading.Thread(target=dash_printer).start()
