import intcode

desired_output = 19690720

with open('day2_input', 'r') as f:
    input_intcode = [int(x) for x in (f.readline().split(','))]
    found_match = False

    for i in range(100):
        if found_match:
            break
        for j in range(100):
            new_intcode = intcode.find_match(input_intcode, i, j)

            if new_intcode[0] == desired_output:
                print(100 * new_intcode[1] + new_intcode[2])
                break
