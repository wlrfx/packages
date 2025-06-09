#!/bin/sh -l

# Exit on error
set -e

API_LOGIN="$1"
API_USERNAME="$2"
API_TOKEN_CONTENT="$3"
COPR_REPO_NAME="$4"
PKGNAME="$5"

echo "Publishing $PKGNAME"

mkdir -p "$HOME/.config"
# To generate a new token: https://copr.fedorainfracloud.org/api/.
echo "[copr-cli]" >> "$HOME/.config/copr"
echo "login = $API_LOGIN" >> "$HOME/.config/copr"
echo "username = $API_USERNAME" >> "$HOME/.config/copr"
echo "token = $API_TOKEN_CONTENT" >> "$HOME/.config/copr"
echo "copr_url = https://copr.fedorainfracloud.org" >> "$HOME/.config/copr"

cd "COPR/$PKGNAME"

# Download RPM Spec sources
spectool -g "./$PKGNAME.rpkg.spec"

# Submit the build to copr
rpkg -v copr-build -w "$COPR_REPO_NAME"
