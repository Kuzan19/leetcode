def prefix(list_string: list):
    """Поиск максимального префикса строки"""
    i = 0
    char_list = []
    while True:
        for n in list_string:
            if not char_list:
                char_list.append(n[i])
                continue
            if n[i] not in char_list:
                return char_list
            else:
                continue
        i += 1



if __name__ == "__main__":
    print(prefix(["flower", "flow", "flight"]))

