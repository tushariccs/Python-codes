anime = ["naruto","onepiece","jujutsu kaisen","shinchan"]

is_there = False

for series in anime:
    if series == "naruto":
        is_there = True
        break
    
    
if is_there:
    print("Naruto is in anime")
else:
    print("Naruto is not in anime")
    
    
if "naruto" not in anime:
    print("Naruto is not in anime")
else:
    print("Naruto is in anime")    