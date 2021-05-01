import os
import random
import copy
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_dist = dict()

    # Check if there are any links in the page
    # If not then assume all pages with equal probability
    if len(corpus[page]) == 0:
        for link in corpus:
            prob_dist[link] = 1 / len(corpus)

        return prob_dist

    for link in list(corpus.keys()):
        prob_dist[link] = (1 - damping_factor) / len(list(corpus.keys()))

    for link in corpus[page]:
        prob_dist[link] = prob_dist[link] + damping_factor / len(corpus[page])

    # Return the probability dictionary
    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = dict()
    for page in corpus:
        page_rank[page] = float(0)

    curr_page = random.choice(list(corpus.keys()))

    for _ in range(1, n):
        # Get current model
        prob_dist = transition_model(corpus, curr_page, damping_factor).items()
        # Format model
        prob_dist = list(zip(*prob_dist))

        # Get the pages and weights
        pages = prob_dist[0]
        weights = prob_dist[1]

        # Calculate the page rankings
        curr_page = random.choices(population=pages, weights=weights)[0]
        page_rank[curr_page] = page_rank[curr_page] + 1/n

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = dict()

    for page in corpus:
        page_ranks[page] = 1 / len(corpus)

    # Initialize condition for
    condition = True
    while condition:
        curr_ranks = copy.deepcopy(page_ranks)
        for page in corpus:
            # Calculate the sum of the current page ranks, PR(i) / number of links present NumLinks(i)
            sum_i = float(0)
            for i in curr_ranks:
                if page in corpus[i]:
                    sum_i += curr_ranks[i] / len(corpus[i])

                if not corpus[i]:
                    sum_i += curr_ranks[i] / len(corpus)

            # Calculate the page rank values
            page_ranks[page] = ((1 - damping_factor) / len(corpus)) + damping_factor * sum_i

            # Make sure to repeat loop until no PageRank value changes by more than 0.001
            # current ranks - new page ranks > 0.001
            condition = (abs(curr_ranks[page] - page_ranks[page]) > 0.001) or False

    return page_ranks


if __name__ == "__main__":
    main()
