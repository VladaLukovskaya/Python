def bracket_check():
    open = close = 0
    raw = input('Enter your raw: ')
    for symbol in raw:
        if symbol == '(':
            open += 1
        elif symbol == ')':
            close += 1
        else:
            print('Enter a bracket sequence.')
    if open <= close and raw[-1] == ')':  # need to check other variants
        print("Perfect! It's the bracket sequence.")
    else:
        print("I don't see a bracket sequence here.")


bracket_check()
