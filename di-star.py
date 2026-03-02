rows = 5

# Upper pyramid
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))

# Lower inverted pyramid
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "* " * (i + 1))
