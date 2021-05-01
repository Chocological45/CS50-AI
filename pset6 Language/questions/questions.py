import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    data = dict()

    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path) and file.endswith(".txt"):
            with open(path, "r", encoding='utf-8') as f:
                data[file] = f.read()

    return data


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = nltk.corpus.stopwords.words('english')
    words.extend(string.punctuation)
    tokens = nltk.word_tokenize(document.lower())
    filtered_tokens = [word for word in tokens if word not in words]

    return filtered_tokens


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()

    words = set(word for word_list in documents.values() for word in word_list)

    # Get the number of documents
    num_doc = len(documents)

    for word in words:
        # Get a count of the number of documents with the word from words
        count = 0
        for vocab in documents.values():
            if word in vocab:
                count += 1

        # Compute the idf values from data gathered
        idfs[word] = math.log(num_doc / count)

    # Return idfs dictionary
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_scores = dict()

    for file in files:
        tf_scores[file] = 0
        for word in query:
            tf_scores[file] += files[file].count(word) * idfs[word]

    # Sort the scores into ranks
    tf_ranks = sorted(tf_scores.items(), key=lambda a: a[1], reverse=True)
    tf_ranks = [key for key, value in tf_ranks]

    # Return the first n values from the sorted values
    return tf_ranks[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    # Top sentences scores
    ts_scores = dict()

    # Iterate for all the items in the dictionary
    for sentence, words in sentences.items():
        queried_words = query.intersection(words)

        # Initialize a new idf score
        idf = 0
        # Calculate the idf score
        for word in queried_words:
            idf += idfs[word]

        # Total number of words in query
        total_wq = sum(map(lambda a: a in queried_words, words))

        # Query term density = total number of words in query / number of words
        qtd = total_wq / len(words)

        ts_scores[sentence] = {'idf': idf, 'qtd': qtd}

    # Sort the scores into a ranking
    ts_ranks = sorted(ts_scores.items(), key=lambda a: (a[1]['idf'], a[1]['qtd']), reverse=True)
    ts_ranks = [idf for idf, qtd in ts_ranks]

    # Return the first n values
    return ts_ranks[:n]







if __name__ == "__main__":
    main()
