def find_match(original_intcode):
    for i in range(100):
        for j in range(100):
            copy_intcode = [x for x in original_intcode]
            copy_intcode[1] = i
            intcode[2] = j
            current_index = 0

            while intcode[current_index] != 99:
                if copy_intcode[current_index] == 1:
                    copy_intcode[copy_intcode[current_index + 3]] = copy_intcode[copy_intcode[current_index + 1]] + \
                                                                    copy_intcode[copy_intcode[current_index + 2]]
                if copy_intcode[current_index] == 2:
                    copy_intcode[copy_intcode[current_index + 3]] = copy_intcode[copy_intcode[current_index + 1]] * \
                                                                    copy_intcode[copy_intcode[current_index + 2]]

                current_index += 4

            if copy_intcode[0] == desired_output:
                print(100 * copy_intcode[1] + copy_intcode[2])
                return


with open('day2_input', 'r') as f:
    intcode = [int(x) for x in (f.readline().split(','))]
    desired_output = 19690720
    found_match = False

    find_match(intcode)



