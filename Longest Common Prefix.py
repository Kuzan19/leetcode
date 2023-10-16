def prefix(list_string: list):
    prefix = list_string[0]
    i = 1
    while i < len(list_string):
        if list_string[i].startswith(prefix):
            i += 1
        else:
            prefix = prefix[:-1]
    return prefix


if __name__ == "__main__":
    print(prefix(["c","acc","ccc"]))

