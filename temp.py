def dfs2(neutral_set, start=[]):
    if not start:
        start = neutral_set.pop()
    U = {start}
    V = {start}
    while U:
        current_node = U.pop()
        for n in neighbours(current_node, neutral_set):
            if n not in V:
                U.add(n)
                V.add(n)
    return V

def choose_random(n, neutral_set):
    l = len(neutral_set)
    total = set()
    while len(total) < n:
        total.add(neutral_set[random.randint(0, l-1)])
    return total



unique_phaenotypes_int = np.unique(GPmap)

    
# Die zugehörigen Genotypen finden
total = list(np.zeros(50))
j = 0
for i in unique_phaenotypes_int:
    if i != 67108864:
        genotypys_weird_format = np.where(GPmap==i)
        total[j] = list(zip(*genotypys_weird_format))
        j = j + 1

