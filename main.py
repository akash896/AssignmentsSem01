
import hashlib
import hmac

sha256_hash = hashlib.sha256()


def print_hi(name):
    message = "I aash"
    key = 53613083175710875908100895016148967977859138703614866678397899532020804369136
    h = hmac.new(str(key).encode(), message.encode(), hashlib.sha256)
    print("hash before = ", h)
    print(h.hexdigest())
    # appended_message = message+sha256_hash.hexdigest()
    # print(appended_message)
    # print(appended_message[-64:])

if __name__ == '__main__':
    print_hi('PyCharm')
