# Write your solution here:

def sort_by_seasons(items: list):
    def seasons(item):
        return item["seasons"]
    return sorted(items, key=seasons)