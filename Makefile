.PHONY: verify test
verify: test
	python3 scripts/check_report.py
	python3 scripts/check_docs.py
	python3 scripts/check_release.py
test:
	python3 -m unittest discover -s tests -v
