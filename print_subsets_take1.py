s = 'abc'

def recur(s, prefix, out):
    if len(s) == 0:
        out.append(prefix)
        return
    if len(s) > 0:
        recur(s[1:], prefix+s[0], out)
        recur(s[1:], prefix, out)
    return out

print (recur(s, '', []))