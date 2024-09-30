#You can start installing your packages
---
These commands is used to manage pip packages.

1. Installing a package:

through python command:
```
python -m pip install package-name

```
or by directly using the pip command:
```
pip install package-name
```
2. Installing a package using specific version
by giving the == followed by the version number after the package name.

```
pip install package-name==2.6.9

```
3. Upgrading a package

```
pip install --upgrade package-name

````
4. Uninstalling a package
```
pip uninstall package-name

```
5. Showing the details of a package
```
pip show package-name

```
6. Listing all packages installed in your environment
```
pip list

```
7. Exporting installed packages to requirement.txt file
```
pip freeze > requirement.txt

```
This will create a file called requirement.txt. That file contains a list of the packages you installed in your virtual environment (venv).

8. Installing packages from exported requirement.txt
```
pip install -r requirement.txt

``
This will run pip install package-name repeatedly as many the packages listed in requirement.txt.