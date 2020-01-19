input_min = 357253
input_max = 892942
matches = 0


def num_matches(number):
    found_duplicate = False
    number_repeating = 1
    previous = -1
    number_as_str = str(number)

    for index in range(len(number_as_str)):
        num = int(number_as_str[index])
        if num < previous:
            return False

        if num == previous:
            number_repeating += 1
        elif number_repeating == 2:
            found_duplicate = True
        else:
            number_repeating = 1

        previous = num

    return found_duplicate or number_repeating == 2


for i in range(input_min, input_max+1):
    if num_matches(i):
        matches += 1

print(matches)

