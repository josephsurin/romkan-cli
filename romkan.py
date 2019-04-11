#!/usr/bin/env python
from romkan import to_katakana, to_hiragana, to_kana, to_hepburn, to_kunrei, to_roma
conv_types = {
    'to_katakana': to_katakana,
    'to_hiragana': to_hiragana,
    'to_kana': to_kana,
    'to_hepburn': to_hepburn,
    'to_kunrei': to_kunrei,
    'to_roma': to_roma
}
import argparse

parser = argparse.ArgumentParser(description='romaji-kana converter based on soimort\'s romkan module')
parser.add_argument('-t', '--type', 
        help='Type of conversion: to_katakana, to_hiragana, to_kana, to_hepburn, to_kunrei, to_roma')
parser.add_argument('string', type=str,
        help='String to convert (either in romaji or kana)')

args = parser.parse_args()
conv_str = args.string
if args.type:
    if args.type in conv_types:
        conv_type = conv_types[args.type]
    else:
        print(args.type, 'is not a valid conversion type!')
        exit()
else:
    conv_type = conv_types['to_hiragana'] if 65 <= ord(conv_str[0]) <= 122 else conv_types['to_roma']

print(conv_type(conv_str))

