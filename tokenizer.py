def word(text):
    return list(text.encode("utf-8"))


def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(ids, pair, new_id):
    out = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
            out.append(new_id)
            i += 2
        else:
            out.append(ids[i])
            i += 1
    return out


def train(text, vocab_size):
    ids = word(text)
    merges = {}
    for new_id in range(256, vocab_size):
        stats = get_stats(ids)
        if not stats:
            break
        pair = max(stats, key=stats.get)
        ids = merge(ids, pair, new_id)
        merges[pair] = new_id
    return merges


def build_vocab(merges):
    vocab = {i: bytes([i]) for i in range(256)}
    for (a, b), new_id in merges.items():
        vocab[new_id] = vocab[a] + vocab[b]
    return vocab


def encode(text, merges):
    ids = word(text)
    for pair, new_id in merges.items():
        ids = merge(ids, pair, new_id)
    return ids


def decode(ids, vocab):
    return b"".join(vocab[i] for i in ids).decode("utf-8", errors="replace")
