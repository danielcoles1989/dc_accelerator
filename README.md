# dc_accelerator
Repo for Data Science Accelerator

Gravty data [metadata](https://www.cepii.fr/DATA_DOWNLOAD/gravity/doc/Gravity_documentation.pdf).

TO FINISH

## Instruction for installation
Made using python 3.13.

An enviroment manager is recommended for this project to avoid dependency issues.

### Reqs
Depending on your operating sytem create a new python venv 
```python3 -m venv venv ```

Activate your new venv
```source venv/bin/activate```

Windows users may need to check the venv/Scripts/ folder instead.

Install reqs
```pip install -r requirements.txt```

### Download data
run data_download.py
```python data_download.py```

### How to run notebook
Notebook outputs are saved so you don't need to run any cells. But if you want to change things all notebooks should run in order if you've downloaded the data correctly. NOTE: notebook.ipynb must be fully ran before notebook_ml.ipynb since the first notebook creates a filtered dataframe used by the second notebook.

### NOTES

- Written on a machine with 16gb RAM, 8c/16th. Dataset is large.
