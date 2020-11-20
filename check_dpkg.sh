#!/bin/bash

PACKAGE=miller

if [[ ! $(dpkg -l ${PACKAGE}) ]] ; then
  echo "${PACKAGE} is not installed, installing now."
  sudo apt-get install ${PACKAGE} -y
else
  echo "${PACKAGE} is installed."
fi

