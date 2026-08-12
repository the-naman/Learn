import oracledb
from IPython.core.magic import register_cell_magic
import sys


def get_connection():
    """Initializes a secure connection profile and returns active stream objects."""
    params = oracledb.ConnectParams(
        user="CON_V_I_C_TSDG_SCHEMA_BOHNN",
        password="qOXP!U90EC17XYHNOJ7C6ZC2XJ6AWU",
        host="db.freesql.com",
        port=2484,
        service_name="26ai_un3c1",
        protocol="tcps"
    )


# Global connection variables
connection = None
cursor = None


def init_magic():
    """Establishes connection and hooks the %%plsql cell command directly into Jupyter."""
    global connection, cursor
    try:
        if connection is None:
            connection = oracledb.connect(params=params)
            cursor = connection.cursor()

        # Register a clean, zero-boilerplate cell handler shortcut
        @register_cell_magic
        def plsql(line, cell):
            try:
                cursor.callproc("dbms_output.enable")
                cursor.execute(cell)

                # Automatically extract and dump server text buffers onto screen
                status = cursor.var(oracledb.NUMBER)
                db_line = cursor.var(oracledb.STRING)

                while True:
                    cursor.callproc("dbms_output.get_line", [db_line, status])
                    if status.getvalue() != 0:
                        break
                    print(db_line.getvalue())
            except Exception as e:
                print(f"❌ Oracle Error: {e}")

        # Register it cleanly into the active notebook space
        get_ipython().register_magic_function(
            plsql, magic_kind='cell', magic_name='plsql')
        print("✨ Permanent %%plsql cell magic registered! Session is live.")
    except Exception as e:
        print(f"❌ Connection setup failed: {e}")


# Automatically fire the configuration when the file is loaded
init_magic()
