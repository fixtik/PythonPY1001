if __name__ == "__main__":
    list_= [12,5,4,98,32,1,58,32,90,8] #list(range(10))
    max_index = list_.index(max(list_))
    list_[0], list_[max_index] = list_[max_index], list_[0]

    print(list_)
