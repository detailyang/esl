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
````
> esl http://httpbin.org/headers get --htest=1
200 ok
Content-Length: 174
Server: nginx
Connection: keep-alive
Access-Control-Allow-Credentials: true
Date: Sat, 16 Apr 2016 07:30:03 GMT
Access-Control-Allow-Origin: *
Content-Type: application/json
{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "Test": "1",
    "User-Agent": "python-requests/2.9.1"
  }
}
>
````

*esl-go*
````
> esl-go http://httpbin.org/headers get --habcdefgh=123 --qabcd=oiu

            url = "http://httpbin.org/headers?abcd=oiu"
            form := url.Values{}
            form.Add("abcdefgh", "123")
            client := &http.Client{}
            req, err := http.NewRequest("GET", url, strings.NewReader(form.Encode()))
            if err != nil {
                fmt.Println(err)
                return
            }

            req.Header.Add("abcdefgh", "123")
            resp, err := client.Do(req)
````

*esl-python*
````
> esl-python http://httpbin.org/headers get --habcdefgh=123 --qabcd=oiu

    params = {'abcd': 'oiu'}
    data = {}
    headers = {'abcdefgh': '123'}
    requests.get('http://httpbin.org/headers', params=params, data=data, body=body, headers=headers)

>
````

*esl-curl*
````
> esl-curl http://httpbin.org/headers get --habcdefgh=123 --qabcd=oiu

        curl -X GET -H "abcdefgh: 123"  "http://httpbin.org/headers?abcd=oiu"

>
````

Contributing
------------

To contribute to ESL, clone this repo locally and commit your code on a separate branch. 


Author
------

> GitHub [@detailyang](https://github.com/detailyang)     
   

License
-------

ESL is licensed under the [MIT] license.  
