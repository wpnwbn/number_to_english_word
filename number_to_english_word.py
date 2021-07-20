import re
with open("english.txt", "r") as f:
    words = list(map(lambda x: x[:-1], f.readlines()))

def ceil(number):
    return (number // 1) + bool(number % 1)

# Digit-Letter Code
DLC = {
        '0' : '[sxz]',
        '1' : '[td]',
        '2' : '[n]',
        '3' : '[m]',
        '4' : '[r]',
        '5' : '[l]',
        '6' : '(sh|ch|j|g)',
        '7' : '[ckgq]',
        '8' : '[fv]',
        '9' : '[pb]',
        }

# Separators
sep = "[aehiouwy]*"

BLUE = '\033[95m'
ENDC = '\033[0m'

while True:
    print(BLUE + "Input number: " + ENDC, end='')

    number = list(map(lambda x: DLC[x], input()))
    regex = sep + f"{sep}".join(number) + sep

    # Matched words
    match = []

    for word in words:
        x = re.fullmatch(regex, word)
        if x: match.append(x.group())

    # Number of columns that will be displayed
    columns = 10

    # Rows are chosen so that:
    # (rows * columns) > len(match)
    rows = int(ceil(len(match) / columns))

    tmp_table = []
    for i in range(columns):
        tmp_table.append(match[i * rows : (i + 1) * rows])

    # Adding empty spaces for tmp_table to be matrix, to not get IndexError when dealing with the last rows
    for i in range(len(tmp_table)):
        if len(tmp_table[i]) < rows:
            tmp_table[i] += [''] * (rows - len(tmp_table[i]))

    # Tranposing matrix:
    # [ 1 2 ]     [ 1 3 5 ]
    # [ 3 4 ] --> [ 2 4 6 ]
    # [ 5 6 ]
    # so that the words will be shown sorted by columns, not rows
    table = [[tmp_table[i][j] for i in range(columns)] for j in range(rows)]

    # Printing final table
    for i in range(rows):
        for j in range(columns):
            print("{:12}".format(table[i][j]), end="")
        print()
    print()
