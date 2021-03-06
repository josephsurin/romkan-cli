# romkan-cli
Simple romaji&lt;->kana converter CLI utility based on soimort's romkan

## Installation

```
sudo curl https://raw.githubusercontent.com/josephsurin/romkan-cli/master/romkan.py -o /usr/local/bin/romkan
sudo chmod a+rx /usr/local/bin/romkan
```

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

## Examples

```
> romkan にんじゃ
ninja
> romkan ninja
にんじゃ
> romkan ninzya
にんじゃ
> romkan ニンジャ
ninja
> romkan -t to_kunrei ニンジャ
ninzya
```

See https://github.com/soimort/python-romkan for more information.
