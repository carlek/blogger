truncate_table_query = """
	mutation TruncateTable($tableName: String!) {
		truncateTable(tableName: $tableName) 
	}
"""

truncate_table_variables = \
[
	{"tableName": "post"},
	{"tableName": "postcomment"},
	{"tableName": "author"},
]

populate_database_query = """
	mutation PopulateDatabase {
		populateDatabase() 
	}
"""
