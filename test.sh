source virtual/bin/activate
export SECRET_KEY='set-your-secret-key-here'
export JWT_SECRET_KEY='set-your-jwt_secret-key-here'
export DATABASE_URL='postgres://nduhiu:password@localhost:5432/politico_test'

pytest --cov-report term-missing --cov=app