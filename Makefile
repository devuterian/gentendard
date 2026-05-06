.PHONY: vendor build clean hooks

hooks:
	sh scripts/install-hooks.sh

vendor:
	sh scripts/fetch_vendor.sh

build: vendor
	python3 scripts/build_gentendard.py

clean:
	rm -rf dist build-release

package:
	sh scripts/package_release.sh
