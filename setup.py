# @Author: BingWu Yang <detailyang>
# @Date:   2016-03-30T20:27:36+08:00
# @Email:  detailyang@gmail.com
# @Last modified by:   detailyang
# @Last modified time: 2016-04-10T17:30:50+08:00
# @License: The MIT License (MIT)


from setuptools import setup, find_packages

setup(
    name = 'esl',
    version = '0.1.1',
    keywords = ('esl', 'eva-shell-language'),
    description = 'eva shell language for eva-shell',
    license = 'MIT License',
    install_requires = [
        'ply>=3.8',
        'requests>=2.9.1'
    ],
    entry_points={
        'console_scripts': [
            'esl-python = esl:eslpython',
            'esl-go = esl:eslgo',
            'esl = esl:esl'
        ],
    },
    author = 'detailyang',
    author_email = 'detailyang@gmail.com',

    packages = find_packages(),
    platforms = 'any',
)
