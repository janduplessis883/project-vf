install:
	@pip install -e .
	@echo "🌵 pip install -e . successfull!"

clean:
	@rm -f */version.txt
	@rm -f .DS_Store
	@rm -f .coverage
	@rm -rf */.ipynb_checkpoints
	@rm -Rf build
	@rm -Rf */__pycache__
	@rm -Rf */*.pyc
	@echo "🧽 Cleaned up successfully!"

all: install clean

app:
	@streamlit run inforcast/app.py

git_merge:
	$(MAKE) clean
	$(MAKE) lint
	@python vf/automation/git_merge.py
	@echo "👍 Git merge (master) successfull!"

git_push:
	$(MAKE) clean
	$(MAKE) lint
	@python vf/automation/git_push.py
	@echo "👍 Git push (branch) successfull!"

test:
	@pytest -v tests

# Specify package name
lint:
	@black vf/
