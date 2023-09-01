import socket

def scan_subdomains(domain):
    subdomains = []
    try:
        # Perform DNS query to get the list of subdomains
        for i in range(1, 11):  # Change the range to increase/decrease the number of subdomains to check
            subdomain = f"sub{i}.{domain}"
            try:
                # Resolve the subdomain's IP address
                ip_address = socket.gethostbyname(subdomain)
                subdomains.append((subdomain, ip_address))
            except socket.gaierror:
                continue
    except KeyboardInterrupt:
        pass
    return subdomains

def main():
    target_domain = input("Enter the target domain: ")
    print(f"Scanning subdomains of {target_domain}...")
    subdomains = scan_subdomains(target_domain)

    if subdomains:
        print("\nDiscovered subdomains:")
        for subdomain, ip_address in subdomains:
            print(f"{subdomain} - {ip_address}")
    else:
        print("No subdomains found.")

    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
