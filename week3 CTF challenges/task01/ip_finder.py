import ipaddress

ip_input = input("Enter an IP address: ")

try:
    ip = ipaddress.ip_address(ip_input)

    print("\n✅ Valid IP address")

    # Private or Public
    if ip.is_private:
        print("🔒 Private IP")
    else:
        print("🌍 Public IP")

    # Class
    first_octet = int(ip_input.split(".")[0])

    if 1 <= first_octet <= 127:
        print("Class: A")
    elif 128 <= first_octet <= 191:
        print("Class: B")
    elif 192 <= first_octet <= 223:
        print("Class: C")
    elif 224 <= first_octet <= 239:
        print("Class: D")
    else:
        print("Class: E")

    # Subnet (simple)
    network = ipaddress.ip_network(ip_input + "/24", strict=False)
    print("Subnet:", network)

except ValueError:
    print("❌ Invalid IP address")