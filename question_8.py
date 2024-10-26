def dict_checker(dict, n):
    value = []
    for key, values in dict.items():
        if  values > n:
            value.append(key)
    return value
thisdict = {
  "brand": 20,
  "model": 0,
  "year": 44,
  "schot": 32
}
n = 4
results = dict_checker(thisdict,n)
print(results)