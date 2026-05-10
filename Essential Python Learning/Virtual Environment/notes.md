## What is Virtual Environment
A virtual environment in Python is an isolated directory tree that contains a specific Python interpreter and its own independent set of installed packages, separate from other projects and the system-wide Python installation. 

This isolation is a crucial practice for Python development, primarily to prevent conflicts between different projects that might require different versions of the same library.

Creating a Python virtual environment allows us to manage dependencies separately for different projects, preventing conflicts and maintaining cleaner setups. With Python’s venv module, We can create isolated environments that use different versions of libraries or Python itself.

## Create a Virtual Environment and Run It.
- Open the Terminal or Windows Powershell in the following directory where we wish to create the Environment.
- Then run the following Command:
```shell
python3 -m venv .venv 
```
- Here `.venv` is the name of the Environment (It can be anything)
- Then to activate the **Virtual Environment** run the following command
```shell
.venv\Scripts\activate.bat
```

## How to Create and Use requirements.txt File

A `requirements.txt` file is used within a Python virtual environment to manage project dependencies, allowing for reproducible and consistent project setups across different machines.

The typical workflow involves creating and activating a virtual environment, installing necessary packages, generating the `requirements.txt` file to record dependencies, and using that file to install those dependencies elsewhere. 

To Create `requirements.txt` we can use following commands:
```bash
pip freeze > requirements.txt
```
This will automatically create text file naming requirements.txt where all the packages/dependencies installed within the Environment will be mentioned along with their version.


### Important References:
1. https://realpython.com/python-virtual-environments-a-primer/