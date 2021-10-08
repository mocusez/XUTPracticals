def main():
    email_to_name = {}
    email = input_email()
    while email != "":
        name = format_name(email)
        print("Is your name {}? (Y/n) ".format(name), end="")
        if not judge_input():
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ").title()
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


#  A silly solution
# def format_name(email: str):
#     email = email.title().split("@")[0]
#     temp = list(email)
#     result = []
#     for char in temp:
#         if char == ".":
#             char = " "
#         result.append(char)
#     return "".join(result)


def format_name(email: str):
    prefix = email.title().split("@")[0]
    result = prefix.split(".")
    return "".join(result)


def judge_input():
    result = input().upper()
    if result != "" and result != "Y":
        return None
    return True


def input_email():
    email = input("Email: ")
    while email != "":
        if "@" in email:
            return email
        else:
            print("Invalid Email!")
            email = input("Email: ")
    if email == "":
        print("Invalid Email!")
        email = input_email()
    return email


main()
