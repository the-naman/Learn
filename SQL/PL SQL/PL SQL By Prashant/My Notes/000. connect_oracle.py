import sys
from IPython import get_ipython

# Auto-load the SQL extension into the active notebook
get_ipython().run_line_magic('load_ext', 'sql')

# The exact connection configuration
conn_string = "CON_V_I_C_TSDG_SCHEMA_BOHNN:qOXP!U90EC17XYHNOJ7C6ZC2XJ6AWU@db.freesql.com:2484/?service_name=26ai_un3c1"

# Run the connection command silently
get_ipython().run_line_magic('sql', conn_string)
print("✨ Connected to Oracle DB successfully!")
