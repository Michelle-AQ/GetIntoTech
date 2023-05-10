address_parts = [1, "High Street", "Townsville", "Greater London", "XX123"]

address = ""

for item in address_parts:
    address =  address + str(item)+ " "

print(address)
# strings are immutable

concatenated_address = ", ".join(address_parts)
print(concatenated_address)
