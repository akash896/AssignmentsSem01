
import hashlib
sha256_hash = hashlib.sha256()


def print_hi(name):
    message = "I aash"
    sha256_hash.update(message.encode())
    appended_message = message+sha256_hash.hexdigest()
    print(appended_message)
    print(appended_message[-64:])

if __name__ == '__main__':
    print_hi('PyCharm')
