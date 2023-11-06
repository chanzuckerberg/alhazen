#!/bin/bash
gen-python sciknow_dev.yaml > schema_python_dev.py
gen-sqla sciknow_dev.yaml > schema_sqla_dev.py
gen-sqlddl --dialect sqlite --sqla-file schema_sqla_dev.py --use-foreign-keys sciknow_dev.yaml > schema_dev.sql
gen-erdiagram --format mermaid sciknow_dev.yaml > schema_dev.mermaid
test -f sciknow_dev.db && rm sciknow_dev.db
cat schema_dev.sql | sqlite3 $PWD/sciknow_dev.db