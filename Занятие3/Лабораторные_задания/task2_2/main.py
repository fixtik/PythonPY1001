def poly(str_):
    if str_ == str_[::-1]:
        return "YES"
    else:
        return 'NO'

if __name__ == "__main__":
    # Write your solution here
    print(poly('ПОТОП'))
