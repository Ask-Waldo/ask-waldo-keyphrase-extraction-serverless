from dependencies.keybert import KeyBERT

keybert = KeyBERT(model="average_word_embeddings_glove.6B.300d")


def extract_keyphrases(event, context):
    """
    Input should contain an "input_text" attribute
    containing the string that needs to be processed.
    """
    input_text = event['data']['input_text']

    config = _parse_config(input_text)

    keywords_raw = keybert.extract_keywords(**config)

    keywords = {
        "keywords": []
    }

    for keyword_raw in keywords_raw:
        keyword = {
            "string": keyword_raw[0],
            "score": keyword_raw[1]
        }

        keywords["keywords"].append(keyword)

    return keywords


def _parse_config(input_text):
    return {
        "docs": input_text,
        "keyphrase_ngram_range": (
            1,
            2
        ),
        "stop_words": None,
        "use_mmr": False,
        "use_maxsum": False,
        "top_n": 25,
        "diversity": 0.7,
        "nr_candidates": 50,
    }
