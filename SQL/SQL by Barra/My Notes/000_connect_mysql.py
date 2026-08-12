import os
from IPython import get_ipython


def connect_mysql():
    """Reads credentials from your file and establishes/refreshes the MySQL connection."""
    ip = get_ipython()
    if ip is None:
        return

    try:
        # 1. Read your secure credentials file
        credentials_file = r"E:\Study\Github\Sec\Secrets\MySQL DB Credentials\MySQLConnectionString.txt"

        if not os.path.exists(credentials_file):
            print(f"⚠️ Connection File Missing at: {credentials_file}")
            return

        with open(credentials_file, "r", encoding="utf-8") as f:
            connection_string = f.read().strip()

        # 2. Initialize or reload the JupySQL engine extension framework
        try:
            ip.run_line_magic("load_ext", "sql")
        except:
            # If already loaded, force-refresh it to clear stale sessions
            ip.run_line_magic("reload_ext", "sql")

        # 3. Authenticate and connect
        ip.run_line_magic("sql", connection_string)
        print("⚡ MySQL connection initialized successfully!")

    except Exception as e:
        print(f"❌ MySQL connection failed: {e}")


# Register the function into the notebook's global memory space
ip = get_ipython()
if ip is not None:
    ip.user_ns['connect_mysql'] = connect_mysql

# Automatically run the connection sequence when this script is called
connect_mysql()
