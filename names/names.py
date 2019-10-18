import time

start_time = time.time()

f = open('names\\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names\\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Using Dictionary Reducing the time complexity from O(n*2) to o(n)
first_dict = {}
for name1 in names_1:
    first_dict[name1] = name1

for name2 in names_2:
    try: 
        if first_dict[name2] == name2:
            duplicates.append(name2)
        
    except KeyError:
        pass

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

