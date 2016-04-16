# esl

ESL derived from EVA Shell. It's used to parse options and generate abstract syntax tree. Also it can be used to send HTTP request or trasnform to `curl`、`golang` and `python` code

Table of Contents
-----------------

  * [Install](#Install)
  * [Usage](#Usage)
  * [Contributing](#contributing)
  * [License](#license)
  * [Author](#Author)


Requirements
------------
* Jinja2
* MarkupSafe
* ply
* Pygments
* requests

Usage
------------
At first install the esll from pypi with `pip install esl`

*esl*
`esl http://httpbin.org/headers`

*esl-go*
`esl-go http://httpbin.org/headers`

*esl-python*
`esl-python http://httpbin.org/headers`

*esl-curl*
`esl-curl http://httpbin.org/headers`

Contributing
------------

To contribute to ESL, clone this repo locally and commit your code on a separate branch. 


Author
------

> GitHub [@detailyang](https://github.com/detailyang)     
   

License
-------

ESL is licensed under the [MIT] license.  
