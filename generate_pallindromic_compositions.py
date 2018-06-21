def generate_pallindromes(s, result, midpoint):
    print ("entering: midpoint =", midpoint)
    if (midpoint < 0 or midpoint == len(s)):
        print(result)
        return

    start = midpoint
    end = midpoint

    while s[start] == s[end]:
        start = start - 1
        end = end + 1

        if start < 0:
            break
        if end >= len(s):
            break

    result = result + "|" + s[start+1 : end]
    print("===",result)
    generate_pallindromes(s, result, midpoint - 1)
    generate_pallindromes(s, result, midpoint + 1)


def generate_palindromic_decompositions(s):
    results = ""
    midpoint = int(len(s)/2)

    generate_pallindromes(s, results, midpoint )

generate_palindromic_decompositions("abba")