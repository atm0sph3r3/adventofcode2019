def find_match(intcode, noun, verb):
    copy_intcode = [x for x in intcode]
    copy_intcode[1] = noun
    intcode[2] = verb
    current_index = 0

    while intcode[current_index] != 99:
        if copy_intcode[current_index] == 1:
            copy_intcode[copy_intcode[current_index + 3]] = copy_intcode[copy_intcode[current_index + 1]] + \
                                                            copy_intcode[copy_intcode[current_index + 2]]
        if copy_intcode[current_index] == 2:
            copy_intcode[copy_intcode[current_index + 3]] = copy_intcode[copy_intcode[current_index + 1]] * \
                                                            copy_intcode[copy_intcode[current_index + 2]]

        current_index += 4

    return copy_intcode

