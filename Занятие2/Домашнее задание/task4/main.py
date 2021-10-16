if __name__ == "__main__":
    list_= [12,5,4,98,32,1,58,32,90,8] #list(range(10))
    max_ = 0
    max_index = 0
    for index, curr in enumerate(list_):
        if max_ <= curr:
            max_ = curr
            max_index = index
    list_[0], list_[max_index] = list_[max_index], list_[0]

    print(list_)
