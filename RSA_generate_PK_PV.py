import rsa

pk, pv = rsa.newkeys(1024)
pem_pk = pk.save_pkcs1("PEM")
pem_pv = pv.save_pkcs1("PEM")

print(pem_pk.decode())
print(pem_pv.decode())
