Description
===========

Template project for web ui automation

===========

pytest -m jdi_criticalPath --domain=qa --html=report_crtcl.html
pytest -m jdi_smoke --domain=qa --html=report_smoke.html

-m jdi_criticalPath --domain=qa --html=report_crtcl.html --alluredir=allure/critical
-m jdi_smoke  --domain=qa --html=report_smk.html  --junitxml=junit/report_smk.xml --alluredir=allure/smoke

allure generate ./smoke ./critical