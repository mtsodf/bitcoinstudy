import hashlib
import binascii

def int2hex(n):
    h = hex(n)[2:]

    h = (8-len(h)) * '0' + h

    return h


def hashHexString(s):
    binString = binascii.unhexlify(s)

    return hashlib.sha256(binString).hexdigest()





with open("data/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.block") as blockfile:
    with open("data/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.nonce") as noncefile:
        blockdata = blockfile.read().strip()
        nonce = noncefile.read()

        print "Nonce = ", nonce

        noncehex = int2hex(int(nonce))

        blocknonce = blockdata + nonce

        print hashHexString(blocknonce)



