.PHONY: install lint clean

###############################################################
# GLOBALS                                                     #
###############################################################
REQUIREMENTS=requirements.txt

###############################################################
# COMMANDS                                                    #
###############################################################
# Install dependencies
install:
	pip install --upgrade pip
	pip install -r $(REQUIREMENTS)

# Style the code
lint:
	@echo ">>> black files"
	black .
	@echo ">>> linting files"
	flake8

# Clean the code
clean:
	rm -rf $(MODEL_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
