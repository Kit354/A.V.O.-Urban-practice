calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    print(tuple_)
    return


def is_contains(string, list_to_search):
    count_calls()
    lowercase_list = [s.lower() for s in list_to_search]
    if string.lower() in lowercase_list:
        print(True)
    else:
        print(False)
    return


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
