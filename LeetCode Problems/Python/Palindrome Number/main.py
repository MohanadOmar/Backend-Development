def isPalindrome(x):
    list = []

    for i in str(x):
        list.append(i)

    reversed_list = list[::-1]

    if list == reversed_list:
        print("True")
    else:
        print("False")


isPalindrome(121)