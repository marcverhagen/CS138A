"""ner.py

Run spaCy NER over an input string and insert XML tags for each entity.

"""

import io
import spacy

nlp = spacy.load("en_core_web_sm")


def entity_markup(text: str) -> str:
    entities = nlp(text).ents
    starts = {e.start_char: e.label_ for e in entities}
    ends = {e.end_char: True for e in entities}
    buffer = io.StringIO()
    for p, char in enumerate(text):
        if p in ends:
            buffer.write('</entity>')
        if p in starts:
            buffer.write('<entity class="%s">' % starts[p])
        buffer.write(char)
    markup = buffer.getvalue()
    return '<markup>%s</markup>' % markup


if __name__ == '__main__':

    text = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")

    print(entity_markup(text))
