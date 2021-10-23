def task(str1, str2, k):
    if str1[0:k] == str2[0:k]:
        return "ДА"
    else:
        return  "НЕТ"



if __name__ == "__main__":

    print(task('LLLL', 'L444', 2))

