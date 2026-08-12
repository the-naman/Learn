import oracledb
import sys
import os

# 1. Path to your external secure credentials text file
secrets_path = r"E:\Study\Github\Sec\Secrets\Orace DB Credentials\OracleConnectionString.txt"

# 2. Check if we are running inside an active Jupyter Notebook environment
shell = sys.modules.get('IPython') and sys.modules['IPython'].get_ipython()

if shell:
    try:
        # Load and parse credentials dynamically from your secure text file
        creds = {}
        if os.path.exists(secrets_path):
            with open(secrets_path, "r") as f:
                for line in f:
                    if "=" in line:
                        k, v = line.strip().split("=", 1)
                        # Clean out quotes if you left them in the text file
                        creds[k.strip()] = v.strip().replace(
                            '"', '').replace("'", "")
        else:
            raise FileNotFoundError(
                f"Secrets file not found at path: {secrets_path}")

        # Assemble the internal driver configuration block safely
        params = oracledb.ConnectParams(
            user=creds.get("user"),
            password=creds.get("password"),
            host=creds.get("host"),
            port=int(creds.get("port", 1521)),
            service_name=creds.get("service_name"),
            protocol=creds.get("protocol", "tcps")
        )

        # Establish connection channel using the dynamic parameters
        connection = oracledb.connect(params=params)
        cursor = connection.cursor()

        # Define the clean %%plsql cell command shortcut
        def plsql(line, cell):
            try:
                cursor.callproc("dbms_output.enable")
                cursor.execute(cell)

                status = cursor.var(oracledb.NUMBER)
                db_line = cursor.var(oracledb.STRING)

                while True:
                    cursor.callproc("dbms_output.get_line", [db_line, status])
                    if status.getvalue() != 0:
                        break
                    print(db_line.getvalue())
            except Exception as e:
                print(f"❌ Oracle Error: {e}")

        # Register the shortcut directly into the notebook system space cleanly
        shell.register_magic_function(
            plsql, magic_kind='cell', magic_name='plsql')
        print("✨ Permanent %%plsql registered from secrets file! Session is live.")
    except Exception as e:
        print(f"❌ Connection setup failed: {e}")


# To start from any notebook
# %run "000. connect_oracle.py"

# to check connection is established correctly or not?

# %%plsql
# DECLARE
#     v_msg VARCHAR2(100) := 'Brilliant! Your database setup is officially complete.';
# BEGIN
#     DBMS_OUTPUT.PUT_LINE(v_msg);
# END;
