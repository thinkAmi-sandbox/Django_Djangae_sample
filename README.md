# Django_Djangae_sample
## How to use
1. create your Google App Engine application.
2. clone or download.
3. open `app.yaml`, change `application`'s value for your application.
4. `pip install -r requirements.txt`
5. `python manage.py --sandbox=remote migrate`
6. `python manage.py --sandbox=remote loaddata cultivar`
7. access `http://<your_app>.appspot.com/mysite/register`

　  
## Tested environment
- Windows10
- Python2.7.11
- Dango 1.8.7
- Djangae 0.9.2

　  
## License
Public Domain