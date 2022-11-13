import rsa

# создание публичного и приватного ключей
(pubkey, privkey) = rsa.newkeys(1024)

# запись публичного ключа в файл
with open('publickey.key', 'wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))

# запись приватного ключа в файл
with open('privatekey.key', 'wb') as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))


#PEM(Privacy-Enhanced Mail) - файл почтового сертификата с улучшенной конфиденциальностью
#pkcs1 - стандарт криптографии с открытым ключом
