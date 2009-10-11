# coding: utf-8

from unicodedata import name as uname
from unicodedata import category, normalize
from htmlentitydefs import codepoint2name

def columnize(seq, cols=4):
    ''' split sequence into a list of lists to display as columns
    
        >>> columnize(range(8), 4)
        [[0, 2, 4, 6], [1, 3, 5, 7]]

        >>> columnize(range(8), 2)
        [[0, 4], [1, 5], [2, 6], [3, 7]]

        >>> columnize(range(10), 3)
        Traceback (most recent call last):
          ...
        ValueError: Sequence length must be a multiple of the number of columns
    
    '''
    num_rows = len(seq) // cols
    if len(seq) % cols:
        raise ValueError('Sequence length must be a multiple of the number of columns')
    return [seq[i::num_rows] for i in xrange(num_rows)]
    
def rowize(seq, cols=4):    
    ''' split sequence into a list of lists to display as rows '''
    
    return [seq[i:i+cols] for i in range(0,len(seq),cols)]


class UnicodeChar(object):
    name = ''
    category = ''
    def __init__(self, codepoint):
        self.char = unichr(codepoint)
        self.hex = '%04x' % codepoint
        self.dec = codepoint
        self.entity = '&#x%x;' % codepoint
        try:
            self.name = uname(self.char)
            self.category = category(self.char)
        except ValueError:
            pass
    @property
    def html_entity(self):
        name = codepoint2name.get(self.dec)
        if name:
            return '&%s;' % name
        else:
            return ''

    @property
    def klass(self):
        return self.category[:1]
    @property
    def category_name(self):
        return categ_dict.get(self.category, '')

    def decompose(self):
        comp = [UnicodeChar(ord(c)) for c in normalize('NFKD',self.char)]
        return comp if len(comp) > 1 else []
        
    
categ_list = [
    ('Lu', 'Letter, uppercase'),
    ('Ll', 'Letter, lowercase'),
    ('Lt', 'Letter, titlecase'),
    ('Lm', 'Letter, modifier'),
    ('Lo', 'Letter, other'),
    ('Mn', 'Mark, nonspacing'),
    ('Mc', 'Mark, spacing combining'),
    ('Me', 'Mark, enclosing'),
    ('Nd', 'Number, decimal digit'),
    ('Nl', 'Number, letter'),
    ('No', 'Number, other'),
    ('Pc', 'Punctuation, connector'),
    ('Pd', 'Punctuation, dash'),
    ('Ps', 'Punctuation, open'),
    ('Pe', 'Punctuation, close'),
    ('Pi', 'Punctuation, initial quote (may behave like Ps or Pe depending on usage)'),
    ('Pf', 'Punctuation, final quote (may behave like Ps or Pe depending on usage)'),
    ('Po', 'Punctuation, other'),
    ('Sm', 'Symbol, math'),
    ('Sc', 'Symbol, currency'),
    ('Sk', 'Symbol, modifier'),
    ('So', 'Symbol, other'),
    ('Zs', 'Separator, space'),
    ('Zl', 'Separator, line'),
    ('Zp', 'Separator, paragraph'),
    ('Cc', 'Other, control'),
    ('Cf', 'Other, format'),
    ('Cs', 'Other, surrogate'),
    ('Co', 'Other, private use'),
    ('Cn', 'Other, not assigned (including noncharacters)'),
]

categ_dict = dict(categ_list)

# http://www.unicode.org/Public/5.1.0/ucd/Blocks.txt

blocks = [
    (0x0000, 0x007F, 'Basic Latin'),
    (0x0080, 0x00FF, 'Latin-1 Supplement'),
    (0x0100, 0x017F, 'Latin Extended-A'),
    (0x0180, 0x024F, 'Latin Extended-B'),
    (0x0250, 0x02AF, 'IPA Extensions'),
    (0x02B0, 0x02FF, 'Spacing Modifier Letters'),
    (0x0300, 0x036F, 'Combining Diacritical Marks'),
    (0x0370, 0x03FF, 'Greek and Coptic'),
    (0x0400, 0x04FF, 'Cyrillic'),
    (0x0500, 0x052F, 'Cyrillic Supplement'),
    (0x0530, 0x058F, 'Armenian'),
    (0x0590, 0x05FF, 'Hebrew'),
    (0x0600, 0x06FF, 'Arabic'),
    (0x0700, 0x074F, 'Syriac'),
    (0x0750, 0x077F, 'Arabic Supplement'),
    (0x0780, 0x07BF, 'Thaana'),
    (0x07C0, 0x07FF, 'NKo'),
    (0x0900, 0x097F, 'Devanagari'),
    (0x0980, 0x09FF, 'Bengali'),
    (0x0A00, 0x0A7F, 'Gurmukhi'),
    (0x0A80, 0x0AFF, 'Gujarati'),
    (0x0B00, 0x0B7F, 'Oriya'),
    (0x0B80, 0x0BFF, 'Tamil'),
    (0x0C00, 0x0C7F, 'Telugu'),
    (0x0C80, 0x0CFF, 'Kannada'),
    (0x0D00, 0x0D7F, 'Malayalam'),
    (0x0D80, 0x0DFF, 'Sinhala'),
    (0x0E00, 0x0E7F, 'Thai'),
    (0x0E80, 0x0EFF, 'Lao'),
    (0x0F00, 0x0FFF, 'Tibetan'),
    (0x1000, 0x109F, 'Myanmar'),
    (0x10A0, 0x10FF, 'Georgian'),
    (0x1100, 0x11FF, 'Hangul Jamo'),
    (0x1200, 0x137F, 'Ethiopic'),
    (0x1380, 0x139F, 'Ethiopic Supplement'),
    (0x13A0, 0x13FF, 'Cherokee'),
    (0x1400, 0x167F, 'Unified Canadian Aboriginal Syllabics'),
    (0x1680, 0x169F, 'Ogham'),
    (0x16A0, 0x16FF, 'Runic'),
    (0x1700, 0x171F, 'Tagalog'),
    (0x1720, 0x173F, 'Hanunoo'),
    (0x1740, 0x175F, 'Buhid'),
    (0x1760, 0x177F, 'Tagbanwa'),
    (0x1780, 0x17FF, 'Khmer'),
    (0x1800, 0x18AF, 'Mongolian'),
    (0x1900, 0x194F, 'Limbu'),
    (0x1950, 0x197F, 'Tai Le'),
    (0x1980, 0x19DF, 'New Tai Lue'),
    (0x19E0, 0x19FF, 'Khmer Symbols'),
    (0x1A00, 0x1A1F, 'Buginese'),
    (0x1B00, 0x1B7F, 'Balinese'),
    (0x1B80, 0x1BBF, 'Sundanese'),
    (0x1C00, 0x1C4F, 'Lepcha'),
    (0x1C50, 0x1C7F, 'Ol Chiki'),
    (0x1D00, 0x1D7F, 'Phonetic Extensions'),
    (0x1D80, 0x1DBF, 'Phonetic Extensions Supplement'),
    (0x1DC0, 0x1DFF, 'Combining Diacritical Marks Supplement'),
    (0x1E00, 0x1EFF, 'Latin Extended Additional'),
    (0x1F00, 0x1FFF, 'Greek Extended'),
    (0x2000, 0x206F, 'General Punctuation'),
    (0x2070, 0x209F, 'Superscripts and Subscripts'),
    (0x20A0, 0x20CF, 'Currency Symbols'),
    (0x20D0, 0x20FF, 'Combining Diacritical Marks for Symbols'),
    (0x2100, 0x214F, 'Letterlike Symbols'),
    (0x2150, 0x218F, 'Number Forms'),
    (0x2190, 0x21FF, 'Arrows'),
    (0x2200, 0x22FF, 'Mathematical Operators'),
    (0x2300, 0x23FF, 'Miscellaneous Technical'),
    (0x2400, 0x243F, 'Control Pictures'),
    (0x2440, 0x245F, 'Optical Character Recognition'),
    (0x2460, 0x24FF, 'Enclosed Alphanumerics'),
    (0x2500, 0x257F, 'Box Drawing'),
    (0x2580, 0x259F, 'Block Elements'),
    (0x25A0, 0x25FF, 'Geometric Shapes'),
    (0x2600, 0x26FF, 'Miscellaneous Symbols'),
    (0x2700, 0x27BF, 'Dingbats'),
    (0x27C0, 0x27EF, 'Miscellaneous Mathematical Symbols-A'),
    (0x27F0, 0x27FF, 'Supplemental Arrows-A'),
    (0x2800, 0x28FF, 'Braille Patterns'),
    (0x2900, 0x297F, 'Supplemental Arrows-B'),
    (0x2980, 0x29FF, 'Miscellaneous Mathematical Symbols-B'),
    (0x2A00, 0x2AFF, 'Supplemental Mathematical Operators'),
    (0x2B00, 0x2BFF, 'Miscellaneous Symbols and Arrows'),
    (0x2C00, 0x2C5F, 'Glagolitic'),
    (0x2C60, 0x2C7F, 'Latin Extended-C'),
    (0x2C80, 0x2CFF, 'Coptic'),
    (0x2D00, 0x2D2F, 'Georgian Supplement'),
    (0x2D30, 0x2D7F, 'Tifinagh'),
    (0x2D80, 0x2DDF, 'Ethiopic Extended'),
    (0x2DE0, 0x2DFF, 'Cyrillic Extended-A'),
    (0x2E00, 0x2E7F, 'Supplemental Punctuation'),
    (0x2E80, 0x2EFF, 'CJK Radicals Supplement'),
    (0x2F00, 0x2FDF, 'Kangxi Radicals'),
    (0x2FF0, 0x2FFF, 'Ideographic Description Characters'),
    (0x3000, 0x303F, 'CJK Symbols and Punctuation'),
    (0x3040, 0x309F, 'Hiragana'),
    (0x30A0, 0x30FF, 'Katakana'),
    (0x3100, 0x312F, 'Bopomofo'),
    (0x3130, 0x318F, 'Hangul Compatibility Jamo'),
    (0x3190, 0x319F, 'Kanbun'),
    (0x31A0, 0x31BF, 'Bopomofo Extended'),
    (0x31C0, 0x31EF, 'CJK Strokes'),
    (0x31F0, 0x31FF, 'Katakana Phonetic Extensions'),
    (0x3200, 0x32FF, 'Enclosed CJK Letters and Months'),
    (0x3300, 0x33FF, 'CJK Compatibility'),
    (0x3400, 0x4DBF, 'CJK Unified Ideographs Extension A'),
    (0x4DC0, 0x4DFF, 'Yijing Hexagram Symbols'),
    (0x4E00, 0x9FFF, 'CJK Unified Ideographs'),
    (0xA000, 0xA48F, 'Yi Syllables'),
    (0xA490, 0xA4CF, 'Yi Radicals'),
    (0xA500, 0xA63F, 'Vai'),
    (0xA640, 0xA69F, 'Cyrillic Extended-B'),
    (0xA700, 0xA71F, 'Modifier Tone Letters'),
    (0xA720, 0xA7FF, 'Latin Extended-D'),
    (0xA800, 0xA82F, 'Syloti Nagri'),
    (0xA840, 0xA87F, 'Phags-pa'),
    (0xA880, 0xA8DF, 'Saurashtra'),
    (0xA900, 0xA92F, 'Kayah Li'),
    (0xA930, 0xA95F, 'Rejang'),
    (0xAA00, 0xAA5F, 'Cham'),
    (0xAC00, 0xD7AF, 'Hangul Syllables'),
    (0xD800, 0xDB7F, 'High Surrogates'),
    (0xDB80, 0xDBFF, 'High Private Use Surrogates'),
    (0xDC00, 0xDFFF, 'Low Surrogates'),
    (0xE000, 0xF8FF, 'Private Use Area'),
    (0xF900, 0xFAFF, 'CJK Compatibility Ideographs'),
    (0xFB00, 0xFB4F, 'Alphabetic Presentation Forms'),
    (0xFB50, 0xFDFF, 'Arabic Presentation Forms-A'),
    (0xFE00, 0xFE0F, 'Variation Selectors'),
    (0xFE10, 0xFE1F, 'Vertical Forms'),
    (0xFE20, 0xFE2F, 'Combining Half Marks'),
    (0xFE30, 0xFE4F, 'CJK Compatibility Forms'),
    (0xFE50, 0xFE6F, 'Small Form Variants'),
    (0xFE70, 0xFEFF, 'Arabic Presentation Forms-B'),
    (0xFF00, 0xFFEF, 'Halfwidth and Fullwidth Forms'),
    (0xFFF0, 0xFFFF, 'Specials'),
    (0x10000, 0x1007F, 'Linear B Syllabary'),
    (0x10080, 0x100FF, 'Linear B Ideograms'),
    (0x10100, 0x1013F, 'Aegean Numbers'),
    (0x10140, 0x1018F, 'Ancient Greek Numbers'),
    (0x10190, 0x101CF, 'Ancient Symbols'),
    (0x101D0, 0x101FF, 'Phaistos Disc'),
    (0x10280, 0x1029F, 'Lycian'),
    (0x102A0, 0x102DF, 'Carian'),
    (0x10300, 0x1032F, 'Old Italic'),
    (0x10330, 0x1034F, 'Gothic'),
    (0x10380, 0x1039F, 'Ugaritic'),
    (0x103A0, 0x103DF, 'Old Persian'),
    (0x10400, 0x1044F, 'Deseret'),
    (0x10450, 0x1047F, 'Shavian'),
    (0x10480, 0x104AF, 'Osmanya'),
    (0x10800, 0x1083F, 'Cypriot Syllabary'),
    (0x10900, 0x1091F, 'Phoenician'),
    (0x10920, 0x1093F, 'Lydian'),
    (0x10A00, 0x10A5F, 'Kharoshthi'),
    (0x12000, 0x123FF, 'Cuneiform'),
    (0x12400, 0x1247F, 'Cuneiform Numbers and Punctuation'),
    (0x1D000, 0x1D0FF, 'Byzantine Musical Symbols'),
    (0x1D100, 0x1D1FF, 'Musical Symbols'),
    (0x1D200, 0x1D24F, 'Ancient Greek Musical Notation'),
    (0x1D300, 0x1D35F, 'Tai Xuan Jing Symbols'),
    (0x1D360, 0x1D37F, 'Counting Rod Numerals'),
    (0x1D400, 0x1D7FF, 'Mathematical Alphanumeric Symbols'),
    (0x1F000, 0x1F02F, 'Mahjong Tiles'),
    (0x1F030, 0x1F09F, 'Domino Tiles'),
    (0x20000, 0x2A6DF, 'CJK Unified Ideographs Extension B'),
    (0x2F800, 0x2FA1F, 'CJK Compatibility Ideographs Supplement'),
    (0xE0000, 0xE007F, 'Tags'),
    (0xE0100, 0xE01EF, 'Variation Selectors Supplement'),
    (0xF0000, 0xFFFFF, 'Supplementary Private Use Area-A'),
    (0x100000, 0x10FFFF, 'Supplementary Private Use Area-B'),
]

block_firsts = dict( [(first, (last, title)) for first, last, title in blocks] )

if __name__=='__main__':
    import doctest
    doctest.testmod()
    