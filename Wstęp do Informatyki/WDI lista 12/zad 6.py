def is_onp(w):
    number_counter = 0
    for i in w:
        if i == "*" or i == "+":
            if number_counter < 2:
                return False
            else:
                number_counter -= 1
        else:
            number_counter += 1
    return number_counter == 1
