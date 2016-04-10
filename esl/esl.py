# @Author: BingWu Yang <detailyang>
# @Date:   2016-04-09T19:24:11+08:00
# @Email:  detailyang@gmail.com
# @Last modified by:   detailyang
# @Last modified time: 2016-04-10T16:02:47+08:00
# @License: The MIT License (MIT)


from eslgenerator import ESLGenerator
from eslyacc import parse
import requests
import sys
from eslast import QueryStringNode, HeaderNode, BodyNode, ValueNode, ValueNode,\
    ShellNode

def esl():
    _map = {
        'GET': requests.get,
        'POST': requests.post,
        'DELETE': requests.delete,
        'PUT': requests.put
    }
    ast = parse(' '.join(sys.argv[1:]))
    url = ast.left.url
    method = ast.method.name
    params = {}
    headers = {}
    body = {}
    for option in ast.right.options:
        if isinstance(option.key, QueryStringNode):
            if isinstance(option.value, ValueNode):
                params[option.key.key] = option.value.value
            elif isinstance(option.value, ShellNode):
                params[option.key.key] = commands.getstatusoutput(option.value.value)[1]
            elif isinstance(option.key, HeaderNode):
                headers[option.key.key] = option.value.value
            elif isinstance(option.key, BodyNode):
                body[option.key.key] = option.value.value
    try:
        r = _map[method](url, data=body, params=params, headers=headers)
        print(r.text)
    except requests.exceptions.MissingSchema as e:
        print(e)

def eslgo():
    pass

def eslpython():
    ast = parse(' '.join(sys.argv[1:]))
    generator = ESLGenerator(ast)
    print(generator.to_python())

def eslcurl():
    pass
