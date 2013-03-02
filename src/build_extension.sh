#! /bin/bash

REPO_NAME=autopagerize
ADDON_SDK_URL='https://ftp.mozilla.org/pub/mozilla.org/labs/jetpack/jetpack-sdk-latest.zip'
ADDON_SDK_NAME=jetpack-sdk-latest.zip

pushd $REPO_NAME
git pull origin master
popd
curl -L -o $ADDON_SDK_NAME $ADDON_SDK_URL
unzip -q $ADDON_SDK_NAME
pushd $(ls -d addon-sdk-* | head -n 1)
source bin/activate
popd
pushd $REPO_NAME
cfx xpi
popd
deactivate
rm -rf $ADDON_SDK_NAME addon-sdk-*
mv $REPO_NAME/*.xpi ./
