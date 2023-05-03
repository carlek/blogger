edit_author_query = '''
	mutation EditAuthor($id: Int!, $username: String, $email: String, $password: String) {
		editAuthor(id: $id, username: $username, email: $email, password: $password) {
			username
			email
			password
			createdAt
			updatedAt
		}
	}
'''

edit_author_variables = \
	[
		{'id': 1, 'password': 'new_password_1'},
		{'id': 2, 'username': 'new_username_2'},
		{'id': 3, 'email': 'new_email_3'},
		{'id': 4, 'username': 'new_username_4', 'password': 'new_password_4'},
		{'id': 5, 'username': 'new_username_5', 'email': 'new_email_5', 'password': 'new_password_5'},
	]

