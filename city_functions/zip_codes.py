import json

def zip_code_count(city_list):
    for i, city in enumerate(city_list):
        pass

    return i


def dup_check(city_list):
    dup = False
    dup_zips = []
    city_dict = {}
    dup_ct = 0
    city_list_copy = city_list
    for i, city in enumerate(city_list):
        z_0 = city["postal_code"]
        for j, c in enumerate(city_list_copy):
            if i != j:
                if z_0 == c["postal_code"]:
                    dup_ct += 1
                    city_dict = c
                    dup_zips.append(city_dict)


    return {"duplicates": dup, "duplicate_count": dup_ct, "zips": dup_zips}

with open('us_zips.json', 'r') as j:
    data = json.load(j)
    num_cities = zip_code_count(data)
    duplicates = dup_check(data)

print(num_cities)
for dup in duplicates['zips']:
    print(dup['city'], end=' ')
    print(dup['state_code'], end=' ')
    print(dup['postal_code'])
    
    