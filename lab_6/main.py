def rabin_karp(haystack, needle):
    if not haystack or not needle:
        return []

    def hash_str(s):
        h = 0
        for char in s:
            h = (h * 256 + ord(char)) % 101
        return h

    len_haystack = len(haystack)
    len_needle = len(needle)

    hash_needle = hash_str(needle)

    indices = []

    hash_window = hash_str(haystack[:len_needle])

    for i in range(len_haystack - len_needle + 1):
        if hash_window == hash_needle:
            if haystack[i:i + len_needle] == needle:
                indices.append(i)

        if i < len_haystack - len_needle:
            hash_window = (hash_window * 256 - ord(haystack[i]) * (256 ** len_needle) + ord(haystack[i + len_needle])) % 101

    return indices

haystack = "ababcababcabcabc"
needle = "abc"
result = rabin_karp(haystack, needle)
print("Індекси входжень:", result)