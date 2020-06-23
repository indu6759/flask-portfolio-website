# flask-portfolio-website

Instllation Steps :

how to install flask:
https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask

create enviornment to run project independently
python -m env projectName
.\flask_website\Scripts\Activate.ps1 (for Windows)

pip install Flask

if error of restricted policy there then use command on powershell  :
Set-ExecutionPolicy Unrestricted -Force 


$env:FLASK_APP = "filename.py"
python -m flask run


debug mode on
$env:FLASK_ENV='development'

http://127.0.0.1:5000/ 

