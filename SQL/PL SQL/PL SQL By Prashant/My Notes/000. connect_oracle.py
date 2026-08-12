import oracledb


def get_connection():
    """Initializes a secure connection profile and returns active stream objects."""
    params = oracledb.ConnectParams(
        user="CON_V_I_C_TSDG_SCHEMA_BOHNN",
        password="qOXP!U90EC17XYHNOJ7C6ZC2XJ6AWU",
        host="://freesql.com",
        port=1521,
        service_name="free",
        protocol="tcps"
    )
    connection = oracledb.connect(params=params)
    cursor = connection.cursor()
    cursor.callproc("dbms_output.enable")
    return connection, cursor


def fetch_output(cursor):
    """Fetches and displays the console log lines from the database engine."""
    status = cursor.var(oracledb.NUMBER)
    line = cursor.var(oracledb.STRING)
    while True:
        cursor.callproc("dbms_output.get_line", [line, status])
        if status.getvalue() != 0:
            break
        print(line.getvalue())
