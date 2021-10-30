if __name__ == "__main__":
    # Write your solution here



#``INPUT:{"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}```
# OUTPUT: [{'Наука':88,'Язык':77},{'Наука':89,'Язык':78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]```

    def create_dict(item):
        print(item)
        return None

    def task(dict_):
        n = map(create_dict, dict_.values())


        return list(n)

    print(task({"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}))