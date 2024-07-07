import argparse

def main():
    global String

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help = "String to convert to raw bytes for payload")
    parser.add_argument("-b", "--bytes", help = "Bytes to convert to string for payload")
    args = parser.parse_args()
    
    if (args.string): 
        output = toBytes(args.string)
        print("Outputted: " + output)
    elif (args.bytes):
        output = toString(args.bytes)
        output = repr(output)
        print("Outputted: " + str(output[2:len(str(output))-1]))
    else:
        print("No arguments inputted, try -s or -b!")

def toBytes(String):
    byteSeq = String.encode('utf-8')
    hexSeq = ''.join([f"\\x{byte:02X}" for byte in byteSeq])
    
    return hexSeq

def toString(StringOfBytes):
    StringOfBytes = StringOfBytes.replace('\\', '')
    StringOfBytes = StringOfBytes.replace('x', '')

    hexPairs = [StringOfBytes[i:i+2] for i in range(0, len(StringOfBytes), 2)]

    byteSeq = bytes(int(pair, 16) for pair in hexPairs)
    return byteSeq

if __name__ == '__main__':
    String = ""
    main()