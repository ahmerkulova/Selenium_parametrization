# Task for review [PyTest - parametrization, configuration, plugins Step 9](https://stepik.org/lesson/237240/step/9) (Stepik)

Task description:
1. Create GitHub repository with conftest.py and test_items.py files
2. Add code to conftest.py that reads the command line language option
3. Implement launching tests with language specified by user
4. Browser must be declared in 'browser' fixture and ised in tests as parameter
5. In test_items.py, write a test checking 'add to cart' button availability at http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
6.Test must be run with language parameter, which executes the command: pytest --language=es test_items.py and succeeds
