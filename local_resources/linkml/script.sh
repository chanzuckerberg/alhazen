
#!/bin/bash
gen-python sciknow.yaml > schema_python.py
gen-sqla sciknow.yaml > schema_sqla.py
gen-sqlddl --dialect postgresql --sqla-file alhazen/schema_sqla.py sciknow.yaml > schema.sql
python ../../alhazen/hacks/sqla_fixes.py
gen-erdiagram --format mermaid sciknow.yaml > schema.mermaid
cp schema_python.py ../../alhazen/
cp schema_sqla.py ../../alhazen/
#test -f /tmp/alhazen/sciknow.db && rm /tmp/alhazen/sciknow.db
#cat schema.sql | sqlite3 /tmp/alhazen/sciknow.db 