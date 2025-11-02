def operation():
    str = input("Enter numbers separated by spaces. ex: 5 3 8 3 9.... : ")
    arr = str.split()
    arr = [int(x) for x in arr]
    print(sum(arr))
    print(sum(arr) / len(arr))
    print(max(arr))
    print(min(arr))
    uni_arr = set(arr)
    print(list(uni_arr))
    arr.sort()
    print(arr)
    arr.sort(reverse=True)
    print(arr)
    # even = map(lambda x: x % 2 == 0, arr)
    even = filter(lambda x: x % 2 == 0, arr)
    print(list(even))
    odd = filter(lambda x: x % 2 != 0, arr)
    print(list(odd))


operation()
