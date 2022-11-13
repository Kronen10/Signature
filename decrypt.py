import rsa

# Открытие файла-ключа и возврат данных ключа
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Открытие файла открытого ключа и загрузка ключа
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey.key'))

message = file_open('message.txt')
signature = file_open('signature_file')

# Проверка подписи
try:
    rsa.verify(message,signature,pubkey)
    print("Проверка успешна, подпись подтверждена")

except:
    print("ВНИМАНИЕ!!! Подпись не может быть проверена")
