calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string),string.upper(),string.lower()


def is_contains(string, search_list):
    count_calls()
    for i in range(0, len(search_list)):
        search_list[i]=search_list[i].lower()
    if string.lower() in search_list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
