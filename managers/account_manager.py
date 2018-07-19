#Functions and queries for update the database as requested from the API

def create_user(user_name, email, password):
	conn = psycopg2.connect("dbname=gsl_twitter")
	cur = conn.cursor()

	sql_add = """
		INSERT INTO accounts (user_name, email, password)
		VALUES('%s', '%s', '%s');
		"""%(user_name, email, password)
	cur.execute(sql_add)
	conn.commit()