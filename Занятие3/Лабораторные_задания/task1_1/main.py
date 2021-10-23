MAX_VALUE = 500

def main():
    sum_ = 0
    i = 1
    while sum_ <= MAX_VALUE:
       if sum_ + i ** 2 > MAX_VALUE:
           return i, sum_
       sum_ += i **2
       i += 1
    return i, sum_


if __name__ == "__main__":
   print(main())