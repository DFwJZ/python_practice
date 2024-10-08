def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)

    lps = compute_lps(pattern)

    i = j = 0
    results = []

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == M:
            results.append(i - j)
            j = lps[j - 1]
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return results

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"Pattern found at indices: {kmp_search(text, pattern)}")