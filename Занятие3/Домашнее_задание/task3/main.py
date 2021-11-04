# def task_(str_):
#     split_str = str_.split()
#     max_list = []
#     max_len = 1
#     for s in split_str:
#         if len(s) > max_len:
#             max_list.clear()
#             max_list.append(s)
#             max_len = len(s)
#         elif len(s) == max_len:
#             max_list.append(s)
#         else:
#             continue
#     if len(max_list) > 1:
#         return max_list
#     else:
#         return max_list[0]

def task_(str_ :str):
    max_len = len(max(str_.split(), key=lambda x: len(x)))
    return [item for item in str_.split() if len(item) == max_len]



if __name__ == "__main__":
    # Write your solution here
   print(task_('Люблю       тебя Петра творенье творенbе Люблю твой строгий стройный вид'))
