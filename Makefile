# Variables
GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}
SRC_DIR := ./src
LINE_LENGTH := 120


run_docker:
	docker-compose build && docker-compose up -d

format:
	black $(SRC_DIR)/* --line-length=$(LINE_LENGTH) --skip-string-normalization
	isort $(SRC_DIR)/* --line-length=$(LINE_LENGTH) --multi-line=0
	flake8 $(SRC_DIR)/* --max-line-length=$(LINE_LENGTH)

# Create a new release
# Usage: make release
release:
	@echo "Input version[$(shell git describe --abbrev=0 --tags --always)]:"
	@read INPUT_VERSION; [[ ! -z $$INPUT_VERSION ]] \
		|| INPUT_VERSION=`git describe --abbrev=0 --tags --always` \
		&& echo "__version__ = '$$INPUT_VERSION'" > `pwd`/src/__init__.py \
		&& echo "Creating a new release version: $$INPUT_VERSION" \
		&& git add `pwd`/src/__init__.py \
		&& git commit -m "new version $$INPUT_VERSION" \
		&& git tag "$$INPUT_VERSION" \
		&& git push origin "$$INPUT_VERSION" \
		&& git push origin -u "$(shell git rev-parse --abbrev-ref HEAD)"

clean-pyc:
	find . -name "__pycache__" -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

requirements:
	@pipenv lock
