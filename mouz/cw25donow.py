def FindIt(s , f):
    return "Not found" if s.find(f) == -1 else s.find(f)

print(FindIt("littlepony", "pony"))
print(FindIt("littlepony", "xyz"))