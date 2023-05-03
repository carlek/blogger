edit_author_query = '''
		"mutation EditAuthor($id: Int!, $username: String!, $email: String!, $password: String!) {
  			editAuthor(id: $id, username: $username, email: $email, password: $password) {
  				username
    			email
    			password
    			createdAt
    			updatedAt
			}
		}"
'''
edit_author_variables = '''
		"id": 1, 
		"username": "new_username", 
		"email": "new_email@example.com", 
		"password": "new_password"
	}
}
'''

edit_author = f'{"query": {edit_author_query}, "variables": {edit_author_variables} }'

