def remove_whitespace(str_):
    n_srt = str_.split()
    s = ' '.join(n_srt)
    return s

if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
