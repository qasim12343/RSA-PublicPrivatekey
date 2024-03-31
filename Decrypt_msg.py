import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes

private_key_pem = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1Z2jVrc/TiJfS
cHnJqGh8mhCOTX2Pu5ChAs4/5bvfA5tnrTS+KsxhDauyCqNegvsX2zXL+sTnq1Ly
B6QjmzqsTqLehtCMCEwdnQzvm7EbP+sh2DBqnjal85n2mqV69xmeyCEvniFPm8vk
ophNkW5VE3AaZj73YUuHlQMdOZ4zi0vjRhnfVvaMWVB4x7j0h7Wc8D7JVR05Lp5+
lmhj/NflDQuAXCXYfIHvQS/5GKQ6PNoEkqYLVfw1UjUWH9ttmpF/kjT9CAwR0XwW
mTorDqvSX6LUiKDy29IcPx6oYfm6mF2agwdRQKcutR1Y26m6cgn/WZvHLPo2Fo3S
X9CfpowPAgMBAAECggEADE0hDqMU6EnSIyWYb08vGAqp278v0rrhPGHrKD8acILs
m2kN82VbQFZD0d98ePDAjpDBbah+3hzqk4S8IeP+ubzdY4yt1gkhVugVqVFGqcvk
VIJgtMzaH4J3lYGi03Cv4+oQrLYi7nnop4OfzgbHfhfC2YTHI/xiOaVRCul41mgw
R82Vi9rglqqQYCxdOR54s84pH2+/8UlSolYC90j7yotjhu0oEbl1v+r8pVwEZx9d
WI0AhQK5mZriRPDbd1cQ9/OFzuIot9GKFABWgGUbdHF3qdqb8vdY/24+AROXimqp
WAOIuszVDODIE1IrmLqEChwv0IORIVz3XSi+xdL7YQKBgQDq5kh1+EK8Ao/a3WJn
0o8LZS0YJDqxQPeDAAuvTH0hBNEiBo34rD6cnL4DTjPsBLCWNjh6gOeZy8I/Jnej
PBVZTlm1JVuuZfWwW+7AT1KmihxhqeQ3kmnTLoUMlI3mP4sLveYYz/S+SCWlWVOw
snjTLsMjkTaDgMzRR4C1xCCl7wKBgQDFsvL7j0RIbYOVdS5g766KFAlpi8FfoXfZ
THJ5ROS3xtlqU5WcJyvFdwdwMopfVoUpiLpTXQGabpqE3Fy5ykiELhTxadM7nomN
rZq2L0g+/RNGMq5yLRgC72wDCzOYZoYeZHfyGvDir8As3hjofsFXprTekgeclihG
YXK/MlOb4QKBgQCp5HR0HmLl6FRzT7tkq/2ZmEvNMibhHMPnk5jf6Mp3nyxDF8qH
GM0QKK2lZmJXSe0ON5kRwTnBGoYbdo8BGOu389seES8GK+hO7a74mGaG3U05tc7C
ArtXakYAm1EmPr8qduZ8+6tgFH5l4P2OxwZsd13b06NB6V453yVQUdHrMQKBgBdR
fhtx0IoCcMzGH4xLePjMWDfcxhgzgWFeBPqMx7VtfONvrGvYqu8FlRkEvRF1sQsv
F1sR00iV1x/opf87/sWoccvvwXx8vJi7a04l0Y2saAOVosHQ08400zagsZs+LH+V
NhiWWOdD95TTNXjmyoM+JINEEiXECEgU4mXu17HBAoGBANIjbcxBOcR32iZwo80R
AxvpbyTwFKao/xZ2N1j6dt2VTbgUD0YcoFLKgIfnY1W/vl941dTiKuEkoDismBcy
bZC6aCbDFdEibJnIDcUkHyd1wy+mnO2qPRPJU8ABOut9oc5U2ybqJriBAff9uR8B
4qtoY+SpIFZF2MUncAD+vwih
-----END PRIVATE KEY-----
"""
private_key = serialization.load_pem_private_key(
    private_key_pem.encode(), password=None, backend=default_backend()
)

public_key_pem = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtWdo1a3P04iX0nB5yaho
fJoQjk19j7uQoQLOP+W73wObZ600virMYQ2rsgqjXoL7F9s1y/rE56tS8gekI5s6
rE6i3obQjAhMHZ0M75uxGz/rIdgwap42pfOZ9pqlevcZnsghL54hT5vL5KKYTZFu
VRNwGmY+92FLh5UDHTmeM4tL40YZ31b2jFlQeMe49Ie1nPA+yVUdOS6efpZoY/zX
5Q0LgFwl2HyB70Ev+RikOjzaBJKmC1X8NVI1Fh/bbZqRf5I0/QgMEdF8Fpk6Kw6r
0l+i1Iig8tvSHD8eqGH5uphdmoMHUUCnLrUdWNupunIJ/1mbxyz6NhaN0l/Qn6aM
DwIDAQAB
-----END PUBLIC KEY-----
"""

public_key = serialization.load_pem_public_key(
    public_key_pem.encode(), backend=default_backend()
)


# Encrypt a message
# message = "sabdjh"

# ciphertext = public_key.encrypt(
#     message.encode(),
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )

# print(ciphertext)

cipher64 = input()

decoded_cipher = base64.b64decode(cipher64.encode('utf-8'))
# Decrypt the ciphertext using the private key
plaintext = private_key.decrypt(
    decoded_cipher,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted message: ", plaintext.decode())
