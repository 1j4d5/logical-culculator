def display_buf_message(buffed_messages):
    for messages in buffed_messages:
        if isinstance(messages, tuple):
            # If it's a tuple, treat it as a formatted message
            print("\n".join(messages))
        elif isinstance(messages, list):
            # If it's a list, treat it as a normal array
            print(messages)
        else:
            # Otherwise, just print the message
            print(messages)


def start_div(num_plus_signs, middle_text):
    divider = ("+" * (num_plus_signs - 1))
    middle_padding = int((num_plus_signs - len(middle_text)) / 2)
    return "|{}|".format(divider), "|{}|".format("~" * middle_padding + middle_text + "~" * middle_padding), "|{}|".format(divider)


def sub_div(num_plus_signs, middle_text):
    num_plus_signs = num_plus_signs-1
    divider = "-" * num_plus_signs
    middle_padding = int((num_plus_signs - len(middle_text)) / 2)
    return "|"+"~" * middle_padding + middle_text + "~" * middle_padding + "|", "|"+divider+"|"


def starting_menu():
    display_buf_message([start_div(100, " Welcome to Logical calculator ")])


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return num1 / num2


def mul(num1, num2):
    return num1 * num2


def option_showcase_simplify(method, alias):
    showcase = "   | {} |   ".format(method+"      ->       "+alias)
    display_buf_message([sub_div(100, showcase)])


def start_menu():
    display_buf_message([sub_div(100, "Options")])


def options_menu(data):
    for option in data:
        method, alias = option
        option_showcase_simplify(method, alias)


def options_showcase():
    options_menu([("+", "1"), ("-", "2"), ("×", "3"), ("÷", "4")])


def menu():
    start_menu()
    options_showcase()


def starting_screen():
    starting_menu()
    menu()


def error(text):
    print("ERROR: "+text)


def asking_proses_method():
    while(True):
        method = str(input("Enter Preferred Option: "))
        if method == "1":
            return "1"
        elif method == "2":
            return "2"
        elif method == "3":
            return "3"
        elif method == "4":
            return "4"
        else:
            error("You can only select method between 1 to 4")


def asking_proses_numbers(stage):
    while (True):
        try:

            return int(input("Enter Your Preferred "+stage+" Number: "))
        except:
            error("you can only enter numbers not strings and the number cannot be empty")


def validate(stage, prefix):
    if prefix == "divopt1":
        if stage[0] == 0:
            error("cannot be divided by 0")
            return False
        else:
            return True
    if prefix == "divopt2":
        if stage[1] == 0 and stage[0] == 0:
            error("results is unknown")
            return False
        else:
            return True


def processor(method, int1, int2):
    result = None  # Initialize result with a default value

    if method == "1":
        result = add(int1, int2)
    elif method == "2":
        result = sub(int1, int2)
    elif method == "3":
        result = mul(int1, int2)
    elif method == "4":
        if validate((int2,), "divopt1"):
            if validate((int1, int2), "divopt2"):
                result = div(int1, int2)
        else:
            result = None  # Handle the case where validation fails

    return result


def proses():
    method = asking_proses_method()
    first_int = asking_proses_numbers("first")
    sec_int = asking_proses_numbers("second")
    result = processor(method, first_int, sec_int)

    if result is not None:
        print("Result:", result)


def system():
    starting_screen()
    proses()


def friendlizer():
    system()
    while(True):
        if input("Want to try again: (y/n)") == "y":
            system()
        else:
            print("i hope u enjoyed :)")
            return 0


def final():
    friendlizer()


def start():
    final()


def run():
    start()


run()
