def count_words(text):
    words = text.split()
    return len(words)

def count_each_character(text):
    counts = {}
    for char in text:
        if char.lower() in counts:
            counts[char.lower()] += 1
        else:
            counts[char.lower()] = 1
    return counts

def sort_character_counts(counts):
    sorted_counts = []
    for count in counts:
        sorted_counts.append({"char": count, "num": counts[count]})
    sorted_counts.sort(reverse=True, key=lambda x: x["num"])
    return sorted_counts
