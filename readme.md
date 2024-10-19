# SIMPLE-FASTAPI (IN WINDOWS)

* Create a git repo "simple-fastapi"
* In powershell git clone  
* create one files ```dockerfile```
* Copy ```main.py``` and ```requirements.txt``` file

* On Windows power shell run this command

```python -m venv .venv
.venv/scripts/activate
```

* INstall dependencies
```pip install -r requirements.txt```

* RUN
  ```uvicorn main:app --host 0.0.0.0 --port 8000 --reload```
