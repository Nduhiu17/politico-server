source virtual/bin/activate
export SECRET_KEY='your-secret-key-comes-here'
export JWT_SECRET_KEY='your-secret-key-comes-here'
export DATABASE_URL="postgres://yourusername:yourpassword@localhost:5432/your-db-name"

python manage.py server