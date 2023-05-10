#!/usr/bin/env bash

set -e

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOTDIR="$(git -C "$SCRIPTDIR" rev-parse --show-toplevel)"

set -x

# see also ".mailmap" for how email addresses and names are deduplicated
cat > "${ROOTDIR}/AUTHORS" <<- EOF
	# File @generated by hack/generate-authors.sh. DO NOT EDIT.
	# This file lists all contributors to the repository.
	# See hack/generate-authors.sh to make modifications.
	# Contributors sorted by number of commits plus just
	# run it if your name is not present.

	$(git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
