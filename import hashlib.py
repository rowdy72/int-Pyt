import hashlib

def generate_hash(data):
    result = hashlib.sha256(data.encode()).hexdigest()
    return result 

data1 ="Blockchain Technology"
data2 ="blockchain technology"

hash1 = generate_hash(data1)
hash2 = generate_hash(data2)

print("Data 1:" , data1)
print("SHA-256 Hash:" , hash1)
print("\nData 2:", data2 )
print("SHA-256 Hash:", hash2)

if hash1 != hash2:
    print("\nHashes are diffrent due to small change in input!")