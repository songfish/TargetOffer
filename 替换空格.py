# 替换空格
def replaceSpace(s):
    s_list = list(s)
    print(s_list)
    result = []
    for data in s_list:
        if data == ' ':
            result.append('%20')
        else:
            result.append(data)
    return "".join(result)


def replaceSpace2(s):
    s = list(s)
    length = len(s)
    for i in range(length):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)


def replaceSpace3(s):
    blank_num = 0
    for i in s:
        if i == ' ':
            blank_num += 1
    new_length = len(s) + 2 * blank_num
    new_str = new_length * [None]
    i = len(s) - 1
    j = new_length - 1
    while 0 <= i <= j:
        if s[i] == ' ':
            new_str[j-2:j+1] = ['%', '2', '0']
            j -= 3
            i -= 1
        else:
            new_str[j] = s[i]
            i -= 1
            j -= 1
        # print(new_str)
    return ''.join(new_str)


h = replaceSpace3('We are Happy')
print(h)
