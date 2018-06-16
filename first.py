def print_lines(fname, should_strip=True):
    f = open(file=fname, mode='r')
    num_lines = 0
    for line in f.readlines():
        num_lines = num_lines + 1
        if should_strip:
            print(line.strip())
        else:
            print(line)
    return num_lines


num_lines_printed = print_lines('./input.txt', should_strip=False)
print('Printed ' + str(num_lines_printed) + ' lines')

num_lines_printed = print_lines('./input.txt')
print('Printed ' + str(num_lines_printed) + ' lines')