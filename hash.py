import random

def custom_hash(message):
    random.seed(message)  # Seed the random number generator with the message
    hash_value = random.randint(0, 2**16 - 1)  # Generate a random 16-bit hash value
    return hash_value

message = input("Enter the message: ")

hash_value = custom_hash(message)

print("Original Message:", message)
print("Hash value:", hash_value)

# Simulate receiver computing the hash again
received_message = input("Enter the received message: ")
received_hash_value = custom_hash(received_message)

print("Received Message:", received_message)
print("Received Hash value:", received_hash_value)

# Verify integrity
if received_hash_value == hash_value:
    print("Integrity: The message has not been modified.")
else:
    print("Integrity: The message has been modified.")