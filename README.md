# tokinazer

A minimal byte-level **Byte Pair Encoding (BPE)** tokenizer in pure Python, with no dependencies.

Text is first converted to UTF-8 bytes (IDs 0–255). Training then repeatedly finds the most frequent adjacent pair of IDs and replaces it with a new ID (256, 257, …) until the requested vocabulary size is reached. Because it works on bytes, it handles any text, including Arabic and emoji.

## Usage

```python
from tokenizer import train, build_vocab, encode, decode

merges = train("aaabdaaabac", vocab_size=259)
vocab = build_vocab(merges)

ids = encode("aaabdaaabac", merges)
print(ids)                 # [258, 100, 258, 97, 99]
print(decode(ids, vocab))  # aaabdaaabac
```

## API

| Function | Description |
| --- | --- |
| `word(text)` | Convert text to a list of UTF-8 byte IDs. |
| `get_stats(ids)` | Count occurrences of each adjacent pair of IDs. |
| `merge(ids, pair, new_id)` | Replace every occurrence of `pair` in `ids` with `new_id`. |
| `train(text, vocab_size)` | Learn merges from `text`; returns a `{pair: new_id}` dict in merge order. |
| `build_vocab(merges)` | Build the `{id: bytes}` lookup table used for decoding. |
| `encode(text, merges)` | Turn text into token IDs by applying the learned merges in order. |
| `decode(ids, vocab)` | Turn token IDs back into text. |
