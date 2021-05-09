def bracket_check():
    open_bracket = close_bracket = 0
    raw = input('Enter your raw: ')
    for symbol in raw:
        if symbol == '(':
            open_bracket += 1
        elif symbol == ')':
            close_bracket += 1
        else:
            print('Enter a bracket sequence.')
    if open_bracket <= close_bracket and raw[-1] == ')':  # need to check other variants
        print("Perfect! It's the bracket sequence.")
    else:
        print("I don't see a bracket sequence here.")
