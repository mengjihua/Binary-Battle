# 快速幂求模逆元（费马小定理，MOD 是质数）
def mod_inv(a, mod):
    return pow(a, mod - 2, mod)