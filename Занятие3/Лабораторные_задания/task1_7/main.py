def student(nak=0, stip=10000, rash=10000, persent=5):
    month = 0
    total_money = nak
    while total_money >= 0:
        total_money = total_money + stip - rash
        rash += rash * (persent / 100)
        month +=1
    return month

if __name__ == "__main__":
    # Write your solution here
   print(student())
