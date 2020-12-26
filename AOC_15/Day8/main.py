print(sum(len(s.strip()) - len(eval(s.strip())) for s in open("input").readlines()))
print(sum(2 + s.count("\\") + s.count('"') for s in open("input").readlines()))
