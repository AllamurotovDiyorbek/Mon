a=['a','e','o','u','i']
letters=["h", "e", "l", "l", "o", "w", "O", "r", "l", "d"]
count=0
for son in letters:
    if son.upper() in a and son.lower() in a:
        count+=1
print(count)
