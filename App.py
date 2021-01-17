import createKeys
import encryptData
import decryptData


class App:
    @staticmethod
    def KeysCreation():
        createKeys.KeyGeneration()

    @staticmethod
    def DataEncryption(message):
        encryptData.Encryption(message)

    @staticmethod
    def DataDecryption():
        decryptData.Decryption()


# App.KeysCreation()
#App.DataEncryption("Heelllo My Name is Abhisht from App.py!!!")
App.DataDecryption()
