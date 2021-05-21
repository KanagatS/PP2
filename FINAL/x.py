n = int(input())
d, total = {}, 0

for _ in range(n):
    name, score = input().split()
    total += int(score)

    d[name] = d.get(name, int(score)) + int(score)
    
    # if not d.get(name):
    #     d[name] = int(score)
    # else:
    #     d[name] += int(score)

for key, value in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(key, str(value / total * 100) + '%', sep=' ', end='\n')
