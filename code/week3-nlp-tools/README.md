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

**Polyglot**

[https://polyglot.readthedocs.io/en/latest/

Could not install, running into problems with installing the icu dependencies.

**spaCy**

[https://spacy.io/](https://spacy.io/)

```bash
$> pip install spacy
$> python -m spacy download en_core_web_sm
```

**Gensim**

https://pypi.org/project/gensim/

](https://spacy.io/)

```bash
$> pip install gensim
$> python -m spacy download en_core_web_sm
```

Many if the links on the PyPI pages are broken, for a simple example see [https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-auto-examples-core-run-core-concepts-py](https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-auto-examples-core-run-core-concepts-py).

