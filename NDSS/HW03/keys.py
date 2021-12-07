from secp256k1 import curve,scalar_mult
import random

print("Basepoint:\t", curve.g)

aliceSecretKey  = random.randrange(1, curve.n)
alicePublicKey = scalar_mult(aliceSecretKey, curve.g)

bobSecretKey  = random.randrange(1, curve.n)
bobPublicKey = scalar_mult(bobSecretKey, curve.g)

print("\nAlice\'s secret key:\t", aliceSecretKey)
print("Alice\'s public key:\t", alicePublicKey)
print("\nBob\'s secret key:\t", bobSecretKey)
print("Bob\'s public key:\t", bobPublicKey)

print("==========================")

sharedSecret1 = scalar_mult(bobSecretKey, alicePublicKey)
sharedSecret2 = scalar_mult(aliceSecretKey, bobPublicKey)

print("==========================")
print("Alice\'s shared key:\t", sharedSecret1)
print("Bob\'s shared key:\t", sharedSecret2)

print("\n==========================")
print("abG: \t", (sharedSecret1[0]))

res=(aliceSecretKey*bobSecretKey) % curve.n

res=scalar_mult(res, curve.g)

print("(ab)G \t", (res[0]))