
class UnexpectedRightParen(StandardError):
    """unexpected )"""

def tokenize(source_code):
    """Convert a string into a list of tokens"""
    delimiters = '();'
    for delimiter in delimiters:
        source_code = source_code.replace(delimiter, ' '+delimiter+' ')
    return source_code.split()

def interactive_reader(prompt1 = '-->', prompt2 = '...'):
    """Return tokenized expression, ignoring comments and line breaks"""
    prompt = prompt1
    open_parens = 0 # pending (, not yet closed
    tokens = []
    while True:
        lin = raw_input(prompt+' ')
        raw_tokens = tokenize(lin)
        for pos, token in enumerate(raw_tokens):
            if token == ';':
                break
            elif token == '(':
                open_parens += 1
            elif token == ')':
                open_parens -= 1
                if open_parens < 0:
                    raise UnexpectedRightParen()
            tokens.append(token)
        if open_parens == 0:
            return tokens
        prompt = prompt2

if __name__=='__main__':
    num_expr = 0
    while True:
        num_expr += 1
        try:
            print interactive_reader()
        except UnexpectedRightParen:
            print '*** UNEXPECTED )'
        except KeyboardInterrupt:
            print
            continue
        except EOFError:
            print
            raise SystemExit
        print '-'*40


"""

"""