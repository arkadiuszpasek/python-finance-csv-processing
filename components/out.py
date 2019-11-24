attributes = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "white": "\033[37m",
    "gray": "\033[90m",
}

def set_print(color):
    print(attributes[color],end="")

def set_print_reset():
    print(attributes["reset"],end="")

def print_colored(str,color):
    print("%s%s%s" % (attributes[color],str,attributes["reset"]))

def get_color_string(str,color):
    return attributes[color] + str + attributes["reset"]

def print_table(table):
    print_first_row(table[0])

    for row in table[1:]:
        print_row(row)

def print_first_row(row):
    print("{}{: <10}  {: <25}  {: <25}  {: <20}  {: <10}  {: <10}{}".format(attributes["magenta"],*row,attributes["reset"]))

def print_row(row):
    print("{}{: <10}  ".format(attributes["cyan"],row[0]), end="")
    print("{}{: <25}  ".format(attributes["reset"],row[1]), end="")
    print("{}{: <25}  ".format(attributes["reset"],row[2]), end="")
    print("{}{: <20}  ".format(attributes["reset"],row[3]), end="")
    
    if row[4].startswith("-"):
        row[4] = row[4][1:]
        set_print("red")
    else:
        set_print("green")

    print("{: <10}  ".format(row[4]),end="")
    print("{}{: <10}{}".format(attributes["cyan"],row[5],attributes["reset"]))
