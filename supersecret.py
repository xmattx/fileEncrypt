from cryptography.fernet import Fernet
import argparse

# defining main class


class encDec:

    def __init__(self, fileName, decryption_key) -> None:
        self.fileName = fileName
        self.decryption_key = decryption_key

    # encrypt function
    def encrypt(fileName):
        key = Fernet.generate_key()
        _encryptor = Fernet(key)

        print(f"Do not lose this key! -> { key.decode() }")

        with open(fileName, "rb") as f:
            content = f.read()
            content = _encryptor.encrypt(content)

        with open(fileName, "w") as f:
            f.write(content.decode())

    # decrypt function
    def decrypt(fileName, decryptionKey):

        with open(fileName, "rb") as f:

            try:
                decryptionKey = Fernet(bytes(decryptionKey, "UTF-8"))
            except ValueError:
                print("Key seems to be in an uncorrect format")
                exit()

            content = f.read()
            content = decryptionKey.decrypt(content)

        with open(fileName, "wb") as f:
            f.write(content)


# parsing args
parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str,
                    dest="fileName", help="File to encrypt")
parser.add_argument("--encrypt", dest="encrypt",
                    action="store_true", help="Encrypt")
parser.add_argument("--decrypt", dest="decrypt",
                    action="store_true", help="Decrypt")
parser.add_argument("--key", dest="decryptionKey", help="Decryption key")
args = parser.parse_args()
fileName = args.fileName
encrypt = args.encrypt
decrypt = args.decrypt
decryptionKey = args.decryptionKey

# catching errors
if not encrypt and not decrypt:
    print("Please specify an Action! Use --encrypt or --decrypt")
    exit(1)

# main execution
if __name__ == "__main__":

    # if encrypting
    if encrypt:
        if not fileName:
            print("Please provide filename to encrypt using --filename")
            exit(1)
        else:
            prova = encDec.encrypt(fileName)

    # if decrypting
    if decrypt:
        if not fileName or not decryptionKey:
            print(
                "Please provide both decryption key and filename using --key and --filename!")
            exit(1)

        prova = encDec.decrypt(fileName, decryptionKey)
