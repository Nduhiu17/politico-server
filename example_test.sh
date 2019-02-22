source virtual/bin/activate
export SECRET_KEY='set-your-secret-key-here'
export JWT_SECRET_KEY='set-your-jwt_secret-key-here'
export DATABASE_URL='postgres://yourusername:yourpassword@localhost:5432/your_test_db_name'

pytest --cov-report term-missing --cov=app