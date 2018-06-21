def find_substrings(s, start, results, result, end):
    if start == end:
        print(result)
        return

    find_substrings(s, )

def main(s):
    results = Set([])
    result = []
    find_substrings(s, 0, results, result, len(s))