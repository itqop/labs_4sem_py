def is_tr(str_in):
    temp_ch = [0, 0]
    for i in range(len(str_in[1])):
        if str_in[0][i] >= str_in[1][i] and temp_ch[0] != -1:
            temp_ch[0] += 1
        else:
            temp_ch[0] = -1
        if str_in[1][i] >= str_in[0][i] and temp_ch[1] != -1:
            temp_ch[1] += 1
        else:
            temp_ch[1] = -1
    return temp_ch.index(max(temp_ch)) + 1 if max(temp_ch) != -1 else False


def all_var(str_l):
    temp = [None, None]
    for i in range(2):
        temp[i] = "".join(sorted(map(str, str_l[i])))
    return is_tr(temp)


# n = list(map(str, input().split(" ")))
# print(all_var(n))


from itertools import zip_longest, islice


def to_int_keys_best(l):
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]



def suffix_array_best(s):
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    return line


def suffixArray(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort(key=lambda x: x[0])
    for s in suffixes:
        yield s[1]


def con(s):
    if len(s) % 2 == 0:
        if s[:len(s) // 2] == s[len(s) // 2:]:
            return s
    else:
        if s[:len(s) // 2] == s[len(s) // 2:-1]:
            return s[:-1]
        if s[1:len(s) // 2] == s[len(s) // 2:]:
            return s[1:]


ans = []
for i in suffixArray("abcabcabc"):
    for j in range(i, len("abcabcabc")):
        a = con("abcabcabc"[i:j])
        if a != None and a != "":
            ans.append(a) if ans.count(a) == 0 else None
print(ans)
"""

string3 = "babad"
q = 0
k = 0
q2 = []
f = 0
for i in range(len(string3) - 1):
    for b in range(i + 1, len(string3)):
        if string3[i] == string3[b]:
            o = i
            p = b
            k = 1
            while o != b:
                if string3[o] == string3[p]:
                    o += 1
                    p -= 1
                    k += 1
                else:
                    break
            if k == 1 + (b - i):
                q2.append(string3[i:b + 1])

q = len(max(q2))

for i in range(len(q2)):
    if len(q2[i]) == q:
        print(q2[i]
              )
"""