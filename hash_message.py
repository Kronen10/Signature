#Этот файл подписывает файл закрытым ключом владельца и
#проверяет подпись с помощью открытого ключа владельца
import rsa


# Открытие файла-ключа и возврат данных ключа
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Откройте файл закрытого ключа и загрузите ключ
privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))

#Откройте файл секретного сообщения и верните данные в переменную
message = file_open('message.txt')
hash_value = rsa.compute_hash(message, 'SHA-512')  

# Подпись сообщения закрытым ключом владельца
signature = rsa.sign(message, privkey, 'SHA-512')

s = open('signature_file','wb')
s.write(signature)


print(signature)
print(len(signature))

print(len(hash_value) * 8)  # для проверки размера хэша

