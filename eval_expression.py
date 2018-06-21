def evaluate_exp(expression):
    print("expression=",expression)
    result = 0
    stack = []
    for i in range(len(expression)):
        val = expression[i]
        print("val =", val)
        if stac'':
            print("hitting condition blank")
            result = int(str(result) + stack.pop())
        elif val == '*':
            result = result * int(stack.pop())
        elif val == '+':
            result = result + int(stack.pop())
        else:
            stack.append(val)

    return result

def generate_exp(s, target, exp, index):
    results = []

    if (index == len(s)):
        result = eval(exp)
        if (result == target):
            return exp
        return None

    for i in range(index, len(s)):
        result1 = generate_exp(s, target, exp + '' + s[i], i + 1)
        result2 = generate_exp(s, target, exp + '+' + s[i], i + 1)
        result3 = generate_exp(s, target, exp + '*' + s[i], i + 1)

        if result1: results.append(''.join(map(str,result1)))
        if result2: results.append(''.join(map(str,result2)))
        if result3: results.append(''.join(map(str,result3)))

    return results

def generate_all_expressions(s, target):
    results = generate_exp(s, target, s[0], 1)
    print(results)


generate_all_expressions("222", 44)

print(evaluate_exp("1""2"))