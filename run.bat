pytest -s -v -m "sanity" --html=./reports/Reports.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./reports/Reports.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./reports/Reports.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./reports/Reports.html testCases/ --browser chrome