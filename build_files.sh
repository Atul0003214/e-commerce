echo "install requirements"
pip install -r requirements.txt

echo "start migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

python3.9 manage.py collectstatic --noinput --clear

