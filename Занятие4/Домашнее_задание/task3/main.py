if __name__ == "__main__":
    # Write your solution here



#``INPUT:{"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}```
# OUTPUT: [{'Наука':88,'Язык':77},{'Наука':89,'Язык':78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]```

    def create_dict(key, item):
        m = (map(lambda i: {key: i},  item))
        return list(m)

    def sep_list(dict1, dict2):
        return dict1 | dict2

    def task(dict_):
        n = list(map(create_dict, dict_, dict_.values()))
        m = map(sep_list, n[0], n[1])

        return list(m)

    print(task({"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}))