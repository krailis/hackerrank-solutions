def capitalize(string):
    words = string.split(" ")
    upper = []
    for item in words:
        if (item.isalnum()):
            if (item[0].isalpha()):
                str_list = list(item)
                str_list[0] = str_list[0].upper()
                item_new = "".join(str_list)
                upper.append(item_new)
            else:
                upper.append(item)
        else:
            upper.append(item)
    return " ".join(upper)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
