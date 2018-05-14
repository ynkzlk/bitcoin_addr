from pybitcoin import *

# Generating Private Key
print("\n---- Generate Private Key ----")
private_key = BitcoinPrivateKey()
# print("Private key (Bin): ", private_key.to_bin())
print("Private key (Hex): ", private_key.to_hex())
print("Private key (WIF): ", private_key.to_wif())
# print("Private key (DER): ", private_key.to_der())
# print("Private key (PEM): ", private_key.to_pem())
print("Private Key (WIF) Length: ", len(private_key.to_wif()))

print("\n---- Generate Compressed Private Key ----")
compressed_private_key = BitcoinPrivateKey(private_key.to_hex() + '01')
print("Compressed Private key (Hex): ", compressed_private_key.to_hex())
print("Compressed Private key (WIF):", compressed_private_key.to_wif())
print("Compressed Private Key (WIF) Length: ", len(compressed_private_key.to_wif()))

# Generating Public Key from private key
print("\n---- Generate Public Key ----")
public_key = private_key.public_key()
print("Public key (Hex): ", public_key.to_hex())

# Generating Bitcoin Address from public key
print("\n---- Bitcoin Address ----")
print("Bitcoin Address(sha256): ", public_key.address())

print("Bitcoin Address (ripemd160): ", public_key.hash160())

print("Bitcoin Address (Hex): ", public_key.to_hex())


print("\n---- Private Key From Passphrase ----")
p_private_key = BitcoinPrivateKey.from_passphrase()
print('Passphrase:')
print(p_private_key.passphrase())
temp = p_private_key.passphrase()
p2_private_key = BitcoinPrivateKey.from_passphrase(temp)
print(p_private_key.to_hex() == p2_private_key.to_hex())
print("Private key (Hex): ", p_private_key.to_hex())
print("Private key (WIF): ", p_private_key.to_wif())
print("Compressed Private key (WIF):", BitcoinPrivateKey(p_private_key.to_hex() + '01').to_wif())

# Generating Public Key from private key
print("\n---- Generate Public Key ----")
p_public_key = p_private_key.public_key()
print("Public key (Hex): ", p_public_key.to_hex())










## LitecoinPublicKey

# l_private_key = LitecoinPrivateKey()
# print("Litecoin Private key (Hex): ", l_private_key.to_hex())
# print("Litecoin Private key (WIF): ", l_private_key.to_wif())
