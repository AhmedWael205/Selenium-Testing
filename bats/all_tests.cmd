
IF EXIST automation.log DEL automation.log
IF EXIST geckodriver.log DEL geckodriver.log

py.test -s -v tests\test_suite_demo.py --browser chrome --private True
PAUSE