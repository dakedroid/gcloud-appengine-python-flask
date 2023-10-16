# google-app-engine-flask-example
Working through [Building a Python 3 App on App Engine tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app)

TLDR: require an `app.yaml` then `gcloud services enable cloudbuild.googleapis.com` and finally `gcloud app deploy`. To view the app run `gcloud app browse` and to close and delete `gcloud projects delete MY-PROJ-ID`

# docker
Test app in docker
```
# Build
docker build -t test-flask-app .
# Run
docker run -p 5000:5000 test-flask-app:latest
```

## References
- https://medium.com/@dmahugh_70618/deploying-a-flask-app-to-google-app-engine-faa883b5ffab

## Local dev
Run locally and dev:
* `python3 -m venv venv`
* `source venv/bin/activate`
* `(venv) $ pip install -r requirements.txt`
* `(venv) $ python3 app.py`
