
#!/bin/bash
gen-python sciknow.yaml > schema_python.py
gen-sqla sciknow.yaml > schema_sqla.py
gen-sqlddl --dialect sqlite --sqla-file alhazen/schema_sqla.py --use-foreign-keys sciknow.yaml > schema.sql
gen-erdiagram --format mermaid sciknow.yaml > schema.mermaid
mv schema_python.py ../../alhazen/
mv schema_sqla.py ../../alhazen/
test -f /tmp/alhazen/sciknow.db && rm /tmp/alhazen/sciknow.db
cat schema.sql | sqlite3 /tmp/alhazen/sciknow.db 