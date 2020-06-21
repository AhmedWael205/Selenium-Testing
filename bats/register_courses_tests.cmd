IF EXIST automation.log DEL automation.log
IF EXIST geckodriver.log DEL geckodriver.log

IF %1=="" ECHO Add an argument 1 or 2 or 3

IF %1==1 py.test -s -v tests\courses\register_courses_tests.py --browser chrome --private true

IF %1==2 py.test -s -v tests\courses\register_courses_multiple_data_set.py --browser chrome --private true

IF %1==3 py.test -s -v tests\courses\register_courses_csv_data.py --browser chrome --private true

PAUSE