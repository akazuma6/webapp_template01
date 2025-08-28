クローンした後
python -m venv venv
venv\Scripts\activate　or source venv/bin/activate
pip install -r requirements.txt
# データベースに反映
python manage.py migrate
python manage.py runserver
