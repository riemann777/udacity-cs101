#### search.py ####

def lucky_search(wcorpus, keyword):
    pages = wcorpus.lookup(keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if wcorpus.page_rank(candidate) > wcorpus.page_rank(best_page):
                best_page = candidate
    return best_page

def quicksort_pages(pages, wcorp):
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = wcorp.page_rank(pages[0])
        worse = []
        better = []
        for page in pages[1:]:
            if wcorp.page_rank(page) <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort_pages(better, wcorp) + [pages[0]] + quicksort_pages(worse, wcorp)
            
def ordered_search(wcorp, keyword):
    pages = wcorp.lookup(keyword)
    return quicksort_pages(pages, wcorp)