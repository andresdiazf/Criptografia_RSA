# Libreriafroms
from sympy import randprime, isprime
from math import gcd
from sympy import mod_inverse


def generate_rsa_keys():

    # Paso 1: Elegir dos números primos distintos p y q
    p = randprime(100, 1000)
    q = randprime(100, 1000)

    while q == p:
        q = randprime(100, 1000)

    # Paso 2: Calcular n = p * q
    n = p * q

    # Paso 3: Calcular la función totiente φ(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)

    # Paso 4: Elegir un entero e tal que 1 < e < φ(n) y gcd(e, φ(n)) = 1
    e = randprime(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = randprime(1, phi_n)

    # Paso 5: Determinar d como d ≡ e⁻¹ (mod φ(n))
    d = mod_inverse(e, phi_n)

    # Paso 6: Retornar la clave pública (e, n) y la clave privada (d, n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# Generar y mostrar las claves RSA
public_key, private_key = generate_rsa_keys()

print("Clave pública:", public_key)
print("Clave privada:", private_key)
