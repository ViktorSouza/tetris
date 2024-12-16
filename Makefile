.PHONY: all doc tests clean

all:
	doxygen
	cd src && python -m pytest

doc:
	doxygen

tests:
	cd src && python -m pytest

clean:
clean:
	-rmdir /s /q html
	-rmdir /s /q latex
	-cd src && rmdir /s /q .pytest_cache

