def student(stipends=10000, rash=12000, persent=3):
    total_need = 0
    n = 10
    for i in range(1,n+1):
        total_need += rash
        rash += rash * (persent / 100)
    return total_need - stipends * n


if __name__ == "__main__":
    # Write your solution here
   print(round(student()))
