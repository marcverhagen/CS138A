# Flask assignment solution

Requirements:

```bash
$> pip install spacy flask flask_restful
$> python -m spacy download en_core_web_sm
```

To run the code:

```bash
$> python app.py
```

Accessing the API:

```bash
$> curl http://127.0.0.1:5000/api
$> curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```

To access the website point your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

