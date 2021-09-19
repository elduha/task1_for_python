def permutation(chars):
    if len(chars) == 1:
        return chars
    perms = permutation(chars[1:])
    char = chars[0]
    res = []
    for perm in perms:
        for i in range(len(perm)+1):
            res.append(perm[:i]+ char +perm[i:])
    return res
print(permutation('abc'))