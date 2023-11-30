
def boyer_moore_search(haystack, needle):
    if not haystack or not needle:
        return []

    m, n = len(needle), len(haystack)
    if m > n:
        return []

    indices = []

    bad_char_table = {needle[i]: max(1, m - 1 - i) for i in range(m - 1)}

    i = 0
    while i <= n - m:
        j = m - 1

        while j >= 0 and needle[j] == haystack[i + j]:
            j -= 1

        if j < 0:
            indices.append(i)

            i += m
        else:
            bad_char_shift = bad_char_table.get(haystack[i + j], m)
            i += bad_char_shift

    return indices
