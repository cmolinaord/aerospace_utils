.PHONY: count_lines

USER_PATH=`python -m site --user-site`

all:
	@echo "Run 'make install_local' for install package in your user python path"
	@echo "Run 'make uninstall' for uninstallation"

install_local:
	mkdir -p $(USER_PATH)
	cp *.py $(USER_PATH)

uninstall:
	rm -rf $(USER_PATH)

count_lines:
	cat *.py | wc -l
