# TEE RATKAISUSI TÄHÄN:

def sort_by_ratings(items: list):
    def rating(item):
        return item["rating"]
    return sorted(items, key=rating, reverse=True)