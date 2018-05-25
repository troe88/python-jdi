Description
===========

Template project for web ui automation

===HTML====
pytest -m jdi_criticalPath --domain=qa --html=report_crtcl.html
pytest -m jdi_smoke --domain=qa --html=report_smoke.html

===JUNIT===
pytest -m jdi_criticalPath --domain=qa  --junitxml=junit/report_crpth.xml
pytest -m jdi_smoke --domain=qa  --junitxml=junit/report_smk.xml

===ALLURE==
-m jdi_criticalPath --domain=qa --alluredir=allure/critical
-m jdi_smoke  --domain=qa --alluredir=allure/smoke

allure generate ./smoke ./critical
allure generate ./smoke ./critical
allure open