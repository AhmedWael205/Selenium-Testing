
IF EXIST geckodriver.log DEL geckodriver.log
IF EXIST automation.log DEL automation.log

py.test -s -v tests\home\login_tests.py  --browser chrome --private True --url https://courses.letskodeit.com
pause
