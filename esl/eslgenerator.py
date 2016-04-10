# @Author: BingWu Yang <detailyang>
# @Date:   2016-04-06T21:18:58+08:00
# @Email:  detailyang@gmail.com
# @Last modified by:   detailyang
# @Last modified time: 2016-04-10T16:18:06+08:00
# @License: The MIT License (MIT)


import commands

from eslast import QueryStringNode, HeaderNode, BodyNode, ValueNode, ValueNode,\
    ShellNode

class ESLGenerator(object):
    def __init__(self, ast):
        self.ast = ast

    def to_curl(self):
        pass

    def to_go(self):
        pass

    def to_python(self):
        url = self.ast.left.url
        method = self.ast.method.name
        params = {}
        headers = {}
        body = {}
        for option in self.ast.right.options if self.ast.right else []:
            if isinstance(option.key, QueryStringNode):
                if isinstance(option.value, ValueNode):
                    params[option.key.key] = option.value.value
                elif isinstance(option.value, ShellNode):
                    params[option.key.key] = commands.getstatusoutput(option.value.value)[1]
            elif isinstance(option.key, HeaderNode):
                headers[option.key.key] = option.value.value
            elif isinstance(option.key, BodyNode):
                body[option.key.key] = option.value.value

        return '''
    params = {params}
    data = {data}
    headers = {headers}
    requests.{method}('{url}', params=params, data=data, body=body, headers=headers)
        '''.format(url=url, method=method.lower(), params=params, data=body, headers=headers)

    def to_node(self):
        pass
