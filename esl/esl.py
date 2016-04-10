# @Author: BingWu Yang <detailyang>
# @Date:   2016-04-09T19:24:11+08:00
# @Email:  detailyang@gmail.com
# @Last modified by:   detailyang
# @Last modified time: 2016-04-10T15:31:51+08:00
# @License: The MIT License (MIT)


from eslgenerator import ESLGenerator
from eslyacc import parse

ast = parse("/api/cmdb/peoples/ post --qhost_ip=$(ifconfig eth0) --qhost_name=bj-sdf --hContent-Type=abcd --bslkjsdf=123")     # Test it
generator = ESLGenerator(ast)
generator.to_python()
