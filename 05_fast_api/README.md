# FastAPI
FastAPI framework, high performance, easy to learn, fast to code, ready for production

## Step 1: Install FastAPI and Uvicorn

You can also install it part by part.

This is what you would probably do once you want to deploy your application to production:

```Python
pip install fastapi
```

Also install uvicorn to work as the server:

```Python
pip install "uvicorn[standard]"
```
Or install everything in one go:

```Python
pip install "fastapi[all]"
```

## Step 2: Run one of the scripts

```Python
# Activate your virtual environment
demo_apps/Scripts/activate

# Run a script
python .\GET_health_check.py

# Successful run
INFO:     Started server process [4332]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## Step 3: Open Swagger API Docs

You can now navigate to the API docs:

![alt text](https://fastapi.tiangolo.com/img/tutorial/metadata/image02.png "FastAPI Docs")