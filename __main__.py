"""
	BREAKDOWN:
	'from' : typical package location operator
	'packagedirectory' : whatever your base package directory is, ie: 'superapp'
	'import' : package identifier operator
	'app_file' : the name of your mother file, ie: 'superapp' or 'thematrix'
"""
from packagedirectory import app_file
# also acceptable is:
# from . import app_file

"""
	BREAKDOWN:
	'__name__' : returns the file's namespace, ie: if "print(__name__)" was run in
			mamapackage/subdir/module.py, it would return "mamapackage.subdir.module"
			HOWEVER, if a package is run directly (aka: python -m mymodule), then
			"print(__name__)" would return the special value of "main".
	THEREFORE: this conditional is ensuring that this file is actually being run directly
	
	You can add this conditional to the end of module.py, ie:
			if __name__ == '__main__':
				run()
	and it will be ignored if it is run as a package (python -m module), but it will be
	executed if run from the actual file (python -m module.py)
"""
if __name__ == '__main__':
	app_file.run()
