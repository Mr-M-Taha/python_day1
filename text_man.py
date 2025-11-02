def str_pattern_analizer():
    str = input("write a string:")
    print(len(str))
    str_no_space = str.replace(" ", "")
    print(len(str_no_space))
    print(len(str.split(" ")))

    dict = {}

    for char in str:
        dict[char] = dict.get(char, 0) + 1
    print(dict)

    if str == str[::-1]:
        print("yes palindrome")
    else:
        print("not palindrome")

    reversed_str = list(reversed(list(str)))
    print(reversed_str)


str_pattern_analizer()
