# romkan-cli
Simple romaji&lt;->kana converter CLI utility based on soimort's romkan

## Usage

```
usage: romkan [-h] [-t TYPE] string

romaji-kana converter based on soimort's romkan module

positional arguments:
  string                String to convert (either in romaji or kana)

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  Type of conversion: to_katakana, to_hiragana, to_kana,
                        to_hepburn, to_kunrei, to_roma
```

See https://github.com/soimort/python-romkan for more information.
