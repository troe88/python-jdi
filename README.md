Description
===========

Template project for web ui automation

## HTML
pytest -m jdi_criticalPath --domain=qa --html=report_crtcl.html
pytest -m jdi_smoke --domain=qa --html=report_smoke.html

## JUNIT
pytest -m jdi_criticalPath --domain=qa  --junitxml=junit/report_crtcl.xml
pytest -m jdi_smoke --domain=qa  --junitxml=junit/report_smoke.xml

## ALLURE
pytest -m jdi_criticalPath --domain=qa --alluredir=allure/critical
pytest -m jdi_smoke --domain=qa --alluredir=allure/smoke

allure generate ./allure/smoke ./allure/critical --clean
allure open

## ALLURE PARALLEL
pytest  -m jdi --alluredir=allure/all -n 2 --dist=loadscope
allure generate ./allure/all --clean
