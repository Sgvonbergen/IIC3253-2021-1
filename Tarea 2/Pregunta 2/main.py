def miller_rabin(n, k):

    return False


def generar_primo(l):

    return 2


def alg_ext_euclides(a, b):

    return 1, 1, 1


def exp_mod(a, b, n):
    if b == 0:
        return 1
    binary_b = bin(b)[2:]
    r = 1
    for i in range(len(binary_b)):
        r = (r * r) % n
        if binary_b[i] == "1":
            r = (r * a) % n
    return r


def inverso(a, n):

    return 1


def generar_clave(l):

    return l


def enc(m):

    return m


def dec(m):

    return m


print(exp_mod(3, 7, 13))