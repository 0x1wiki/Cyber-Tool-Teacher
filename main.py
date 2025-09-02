from nmap_help import show_nmap_help
from sqlmap_help import show_sqlmap_help

print("=== Cybersecurity Tools Help (by 0x1) ===")
print("1. Nmap")
print("2. SQLMap")

choice = input("Select tool: ")

if choice == "1":
    show_nmap_help()
elif choice == "2":
    show_sqlmap_help()
else:
    print("Invalid choice")
