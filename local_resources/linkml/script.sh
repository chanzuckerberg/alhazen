
gen-python ./local_resources/linkml/sciknow.yaml > alhazen/schema_python.py
gen-sqla ./local_resources/linkml/sciknow.yaml > alhazen/schema_sqla.py
gen-sqlddl --dialect sqlite --sqla-file alhazen/schema_sqla.py --use-foreign-keys ./local_resources/linkml/sciknow.yaml > alhazen/schema.sql