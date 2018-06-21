def pow(dblbase, ipower):
    result = 1.0
    if ipower == 0:
        return result
    if (ipower < 0):
        return (1 / pow(dblbase, -ipower))

    result = pow(dblbase, int(ipower / 2))
    if (ipower % 2):
        return result * result * dblbase
    return result * result

print(pow(10.0, 3))
print(pow(10.0, 3))