def show_nmap_help():
    print("\n=== Nmap Commands with Logic ===\n")

    commands = [
        # Basic Scans
        ("nmap <target>", "Default TCP scan (1000 common ports)."),
        ("nmap -p- <target>", "Scan all 65535 TCP ports."),
        ("nmap -sU <target>", "UDP scan."),
        ("nmap -sS <target>", "Stealth SYN scan."),
        ("nmap -sT <target>", "TCP connect scan (no raw sockets)."),
        ("nmap -sA <target>", "ACK scan (firewall rule detection)."),
        ("nmap -sW <target>", "Window scan (firewall mapping)."),
        ("nmap -sM <target>", "Maimon scan (rare stealth)."),

        # Service & OS Detection
        ("nmap -sV <target>", "Service version detection."),
        ("nmap -O <target>", "OS detection."),
        ("nmap -A <target>", "Aggressive scan: OS + services + scripts + traceroute."),
        ("nmap -sC <target>", "Run default NSE scripts."),
        ("nmap --script=vuln <target>", "Run vulnerability NSE scripts."),

        # Host Discovery
        ("nmap -sn <target/24>", "Ping sweep (host discovery only)."),
        ("nmap -Pn <target>", "Skip ping, scan even if host blocks ICMP."),
        ("nmap -PS22,80,443 <target>", "TCP SYN ping on specific ports."),
        ("nmap -PE <target>", "ICMP Echo request."),
        ("nmap -PP <target>", "ICMP Timestamp request."),
        ("nmap -PM <target>", "ICMP Netmask request."),

        # Timing & Performance
        ("nmap -T0 <target>", "Paranoid timing (very slow, avoid IDS)."),
        ("nmap -T4 <target>", "Aggressive timing (fast, may trigger IDS)."),
        ("nmap -T5 <target>", "Insane timing (very fast, very noisy)."),

        # Port Ranges
        ("nmap -p1-65535 <target>", "Scan all TCP ports."),
        ("nmap -p22,80,443 <target>", "Scan specific ports."),
        ("nmap -F <target>", "Fast scan (top 100 ports)."),

        # Output Options
        ("nmap -oN results.txt <target>", "Normal output to file."),
        ("nmap -oX results.xml <target>", "XML output."),
        ("nmap -oG results.gnmap <target>", "Grepable output."),
        ("nmap -oA results <target>", "Save in all formats (results.nmap/xml/gnmap)."),

        # Firewall & IDS Evasion
        ("nmap -D RND:10 <target>", "Decoy scan (hide source)."),
        ("nmap -S <IP> <target>", "Spoof source IP."),
        ("nmap -g 53 <target>", "Use specific source port (e.g. 53 for DNS)."),
        ("nmap --data-length 200 <target>", "Append random data to packets."),
        ("nmap --mtu 24 <target>", "Use specific packet size (MTU)."),

        # Advanced NSE usage
        ("nmap --script=http-title <target>", "Grab HTTP page titles."),
        ("nmap --script=ssl-cert <target>", "Fetch SSL certificate info."),
        ("nmap --script=ftp-anon <target>", "Check FTP anonymous login."),
        ("nmap --script=smb-vuln-ms17-010 <target>", "Check SMB EternalBlue vuln."),
    ]

    for cmd, logic in commands:
        print(f"{cmd}\n    # {logic}\n")
