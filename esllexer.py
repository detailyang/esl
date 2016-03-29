import ply.lex as lex


digit            = r'([0-9])'
nondigit         = r'([_A-Za-z])'
variable         = r'[a-zA-Z0-9\[\]-_]+'

class ESLLexer:
    # List of token names.   This is always required
    tokens = (
       'URL',
       'METHOD',
       'HEADER',
       'QUERYSTRING',
       'BODY'
    )


    # Regular expression rules for simple tokens
    t_URL = r'^[^ ]+'
    t_METHOD = r'(GET|get|POST|post|DELETE|delete|OPTIONS|options|CONNECT|connect)'
    t_HEADER = r'--h' + variable + r'=' + variable
    t_QUERYSTRING = r'--q' + variable + r'=' + variable
    t_BODY = r'--b' + variable + r'=' + variable

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: break
             print tok

m = ESLLexer()
m.build()           # Build the lexer
m.test("http://aasdfasdf.sdf.sdf get --habc=a --qdef=123a --basdf[]=sdfk")     # Test it
