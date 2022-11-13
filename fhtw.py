# -*- coding: utf-8 -*-
"""
    pygments.styles.fhtw
    ~~~~~~~~~~~~~~~~~~~~~~~

    Corporate style of the UAS Technikum Wien.

"""

from pygments.style import Style
from pygments.token import Token, Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Text

RegExp = Token.RegExp


class FhtwStyle(Style):
    """
    Corporate style of UAS Technikum Vienna.
    """
    default_style = ''

    styles = {
        Text:                   '#111111',
        Token.Vue.Class:        'bold #45B784',
        Token.Vue.Attribute:    'bold #45B784',
        # Token.Vue.Directive:    '#4EC9B0',
        # Token.Vue.Instance:     '#4EC9B0',
        Token.Vue.Directive:    '#45B784',
        Token.Vue.Instance:     '#45B784',
        # Token.Vue.Instance:     '#35495D',

        RegExp:                 '#F33838',
        RegExp.String:          '#F33838',
        RegExp.Slash:           'bold #F33838',
        # RegExp.Special:         'bold #b5cea8',
        # RegExp.Special:         '#95be98',
        # RegExp.Special:         '#81888D',
        RegExp.Special:         '#fe9178',
        RegExp.Escape:          '#ce9178',
        RegExp.Modifier:        'bold #F33838',
        # RegExp.Groups:          '#909090',
        RegExp.Groups:          '#71787D',

        Whitespace:             '#bbbbbb',

        Comment:                'italic #71787D',
        Comment.Preproc:        'noitalic #008080',
        Comment.Special:        'noitalic bold',

        String:                 '#FC10B4',
        String.Char:            '#800080',
        String.Backtick:        '#FC10B4',
        String.Interpol:        '#034369',
        String.Regex:           '#ff0000',

        Number:                 '#0000FF',

        Keyword:                'bold #08649A',
        Keyword.Reserved:       'bold #C50A8C',
        # Keyword.Reserved:       'bold #08649A',

        Operator:               '#C50A8C',
        Operator.Word:          'bold',

        Name.Function:          '#8BB124',
        Name.Label:             '#A0A000',
        Name.Attribute:         '#0E82C6',
        Name.Tag:               'bold #08649A',
        Name.Other:             '#0E82C6',
        # Name.Builtin:           'bold #4ec9b0',
        Name.Builtin:           '#38b89e',

        Generic.Heading:        '#999999',
        Generic.Subheading:     '#aaaaaa',
        Generic.Deleted:        'bg:#ffdddd #000000',
        Generic.Inserted:       'bg:#ddffdd #000000',
        Generic.Error:          '#aa0000',
        Generic.Emph:           'italic',
        Generic.Strong:         'bold',
        Generic.Prompt:         '#555555',
        Generic.Output:         '#888888',
        Generic.Traceback:      '#aa0000',

        Error:                  'bg:#e3d2d2 #a61717'
    }
