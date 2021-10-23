def task_(str_):
    split_str = str_.split()
    max_list = []
    revers_list = []
    max_len = 1
    for s in split_str:
        if len(s) > max_len:
            max_list.clear()
            max_list.append(s)
            max_len = len(s)
        elif len(s) == max_len:
            max_list.append(s)
        else:
            continue
    if len(max_list) > 1:
        for s in max_list:
            revers_list.append(s[::-1])
        return max_list, revers_list
    else:
        s = max_list[0]
        return s[::-1]

if __name__ == "__main__":
    # Write your solution here
   print(task_('Люблю тебя Петра творенье Люблю твой строгий стройный вид'))
