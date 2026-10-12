default: pytest

pytest:
	PYTHONDONTWRITEBYTECODE=1 pytest --color=yes
