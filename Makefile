### DIRECTORIES ###
ROOT_DIR=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
BIN_DIR=${ROOT_DIR}/.bin

### DEPS ###
ARCH?=linux

### PYTHON ###
PYTHON_BIN_PATH=${BIN_DIR}/python/bin
YQ_BIN_PATH=${PYTHON_BIN_PATH}/yq

### HELM ###
#### HELM BINARY ###
HELM_VERSION?=v3.9.0
HELM_BIN=${BIN_DIR}/helm
#### HELM VARIABLES ####
NAMESPACE?=boilerplate
RELEASE?=api

define USAGE
BOILERPLATE API build system ⚙️

Commands:
	install   Install API dependencies.
	uninstall Remove API dependencies.
	printenv  Print environment variables.
	serve     Run app in dev environment.
	test      Run test on Api.
	doc       Create documentation.
	build     Build Docker image.
	push      Push Docker image.
	deploy    Install API on a Kubernetes cluster.
	undeploy  Uninstall API from Kubernetes cluster.
endef

# Pass defined Makefile vars to env
export

.PHONY: help printenv install uninstall serve test doc deploy build push

help:
	@echo "$$USAGE"

printenv:
	@printenv

install:
	@mkdir -p ${BIN_DIR} && cd ${BIN_DIR} && \
	python3 -m venv ./python && \
	echo "[+] Upgrading pip" && ${PYTHON_BIN_PATH}/pip install --upgrade pip wheel certifi setuptools && \
	echo "[+] Installing pip requirements" && ${PYTHON_BIN_PATH}/pip install  --quiet -r ${ROOT_DIR}/requirements.txt && \
	PATH=${PATH}:${BIN_DIR} && \
	echo "[+] Installation done, uninstall w/ 'make uninstall'"

uninstall:
	@rm -rf ${BIN_DIR}

serve:
	${PYTHON_BIN_PATH}/python3 -m flask run

test:
	${PYTHON_BIN_PATH}/python3 -m unittest

### DOCKER ###
### IMG NAME ###
IMG_NAME?=boilerplate_build
### IMG TAG ###
IMG_TAG?=boilerplate

build_wsgi :
	docker build -t ${IMG_TAG} .

deploy_serve_wsgi :
	docker run -d --name ${IMG_NAME} -p 8080:8080 ${IMG_TAG}
	echo "Type 'exit' to quit the terminal."
	docker exec -it ${IMG_NAME} bash

undeploy_wsgi :
	docker stop ${IMG_NAME}
	docker rm -f ${IMG_NAME}

### DOCKER ###
#### BASE IMAGE ####
IMG?=<img_tag>
#### IMAGE TAG ####
TAG:=$(shell { ${YQ_BIN_PATH} -r .appVersion ${ROOT_DIR}/charts/${NAMESPACE}/Chart.yaml || echo "none"; } 2>/dev/null)

build: # test
	docker build -t ${IMG}:${TAG} -t ${IMG}:latest .

push:
	docker push ${IMG} --all-tags

deploy:
	@${HELM_BIN} upgrade --install -n ${NAMESPACE} --create-namespace ${RELEASE} ${ROOT_DIR}/charts/${NAMESPACE} --set-string env=${ENV}

undeploy:
	@${HELM_BIN} uninstall -n ${NAMESPACE} ${RELEASE}
