source virtual/bin/activate
export SECRET_KEY='your-secret-key-comes-here'
export DATABASE_URL="postgres://yourusername:yourpassword@localhost:5432/your-test-db-name"

python manage.py server