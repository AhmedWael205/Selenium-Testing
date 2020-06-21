Requirements:
    download chrome selenium driver and firefox selenium driver and add them to your path variable
    install selenium, pytest, pytest-ordering, ddt
    if you are in windows you can just enter: bats\install.cmd

Running Tests:
    To run login tests: bats\login_tests.cmd
    To run register courses tests:
        bats\register_courses_tests.cmd 1  --> To run one test case
        bats\register_courses_tests.cmd 2  --> To run two test case
        bats\register_courses_tests.cmd 3  --> To run all test cases in testdata.csv
    To run login tests and test cases in testdata.csv: bats\all_tests.cmd
