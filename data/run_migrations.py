import psycopg2

def run():
	# get all migrations and run new ones

	conn = psycopg2.connect("dbname=gsl_twitter")
	cur = conn.cursor()

	# Actually use a migration for this
	sql_create = """
		CREATE TABLE accounts (
		user_name VARCHAR(50) PRIMARY KEY,
		email VARCHAR(50) NOT NULL,
		password VARCHAR(50) NOT NULL);
	"""
	cur.execute(sql_create)
	conn.commit()


if __name__ == '__main__':
    manager.run()