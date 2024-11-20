def categorize_age(age):
    res='';
    if age >= 1 and age <= 5:res='1_5'
    elif age >= 6 and age <= 10:res='6_10'
    elif age > 10 and age <= 20:res='11_20'
    elif age > 21 and age <= 30:res='21_30'
    elif age > 31 and age <= 45:
        res='30_45'
    elif age > 46 and age <= 60:
        res='46_60'
    else:res='61+'
    return res

print(categorize_age(1))
print(categorize_age(7))
print(categorize_age(14))
print(categorize_age(29))
print(categorize_age(35))
print(categorize_age(55))
print(categorize_age(65))
