# NLP Tools



## Installation

You don't have to do this, but using a virtual environment may be a good idea, I for one intend to use one or several for this class:

```bash
$> python -m venv /Applications/ADDED/python/env/nlp-tools
$> source /Applications/ADDED/python/env/nlp-tools/bin/activate
(nlp-tools) $>
```

On windows this is advertized to be something like:

```windows
c:\Python35\python -m venv c:\path\to\myenv
c:\path\to\myenv\bin/activate
```

(See [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) and [https://packaging.python.org/tutorials/installing-packages/](https://packaging.python.org/tutorials/installing-packages/)).

You can use any path you like, I tend to put it somewhere out of the way and not in the current directory. Once you activate the environment your prompt changes and you can get out of the environment with `deactivate`. I am in the `week3-nlp-tools` directory and I like to put a shortcut to the environment in that directory, both to save me some typing and to remind me that I am supposed to use the nlp-tool environment.

```bash
$> ln -s /Applications/ADDED/python/env/nlp-tools/bin/activate venv
$> source venv
```

(I am not sure how this works on Windows).

Note that I sourced the environment twice. That's no problem and it does not get you into environments inside of environments. You can activate a thousand of them and still exit with only one deactivate.

Instructions below are for Mac/Unix, but will in general be the same for windows because typically all that is needed ar Python package installs.



**NLTK**

[http://www.nltk.org/install.html](http://www.nltk.org/install.html)

Install nltk and numpy. The latter is optional for NLTK, but sooner rather than later you will need it.

```bash
$> pip install nltk	
$> pip install numpy
```

If you don't do this in the environment you may want to consider using the `--user` option. The example on the NLTK site also uses the `-U` option which upgrades all packages to the newest version.

Check the installation and download data if you want:

```bash
$> python	
>>> import nltk
>>> nltk.download()
```



**TextBlob**

[https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/)

Install TextBlob and its corpora:

```bash
$> pip install textblob
$> python -m textblob.download_corpora
```

TextBlob uses NLTK. You may note that installation and downloading is rather quick if you already have NLTK and its corpora installed. The data downloaded are: brown, punkt, wordnet, averaged_perceptron_tagger, conll2000 and movie_reviews.

Check the installation with the code listed at the top of [https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/).



**Polyglot**

[https://polyglot.readthedocs.io/en/latest/

This may be a hard one and any problems most likely are with having ICU (International Components for Unicod) installed properly. The instructions above just do a pip install of polyglot and an apt-get install of numpy, and I think it forgets to mention to also pip install the pyicu package.

For me, installing pyicu always ended in dependency tears, but the following is what seems to work for at least some people (taken from [https://dzone.com/articles/python-polyglot-modulenotfounderror-no-module-name](https://dzone.com/articles/python-polyglot-modulenotfounderror-no-module-name)):

```bash
$> brew uninstall --ignore-dependencies icu4c
$> brew install icu4c
$> export ICU_VERSION=67.1
$> export PYICU_INCLUDES=/usr/local/Cellar/icu4c/67.1/include
$> export PYICU_LFLAGS=-L/usr/local/Cellar/icu4c/67.1/lib
$> pip install pyicu
$> pip install pycld2
$> pip install morfessor
```

After this you can start python and check polyglot by trying the language detection module as described in  [https://polyglot.readthedocs.io/en/latest/Detection.html](https://polyglot.readthedocs.io/en/latest/Detection.html). 

<u>Polyglot with Docker</u>

What eventually worked for me is to use Docker. Try these instructions if you have Docker installed, they are a simplified version of the instructions at [https://forum.codeselfstudy.com/t/how-to-install-and-run-the-polyglot-package-python-in-docker/2031](https://forum.codeselfstudy.com/t/how-to-install-and-run-the-polyglot-package-python-in-docker/2031). 

First create a directory `polyglot` (or any other name you want to use) and add two files: `Dockerfile` and `requirements.txt`. The contents of the `Dockerfile` should be

```dockerfile
FROM continuumio/anaconda3

RUN apt-get update && apt-get install -qq -y \                                                                            
    build-essential libpq-dev vim --no-install-recommends

COPY ./ ./app
WORKDIR ./app

RUN pip install -r requirements.txt
```

And the contents of `requirements.txt` should be

```
numpy
pycld2
morfessor
pyicu
polyglot
flask
Flask-Cors
gunicorn
```

After this you build a Docker image:

```bash
$> cd polyglot
$> docker build -t polyglot .
```

This will take a little while (5-15 minutes), but after that you can open a Docker container and you will have access to polyglot:

```bash
$> docker run --rm -it polyglot bash
```

You will end up in a bash shell on the container with a somewhat different prompt then you are used to:

```
(base) root@88dc22938688:/app# 
```

You can start python and check the language detection as described in  [https://polyglot.readthedocs.io/en/latest/Detection.html](https://polyglot.readthedocs.io/en/latest/Detection.html). 



**spaCy**

[https://spacy.io/](https://spacy.io/)

```bash
$> pip install spacy
$> python -m spacy download en_core_web_sm
```

Try spaCy with the code listed on [https://spacy.io/](https://spacy.io/)

