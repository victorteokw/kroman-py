# kroman python package

Kroman is a Korean hangul romanization tool.

It's currently implemented as a command line utility, a ruby gem,
a python package, and a nodejs package. Editor plugins will be implemented.

This is the python package.

## Implementations

- [kroman command line tool](https://github.com/cheunghy/kroman)
- [kroman ruby gem](https://github.com/cheunghy/kroman-gem)
- [kroman python package](https://github.com/cheunghy/kroman-py)
- [kroman nodejs package](https://github.com/cheunghy/kroman-js)

## Installation

Install it with pip is recommended.

```
    $ pip install kroman
```

Or install it yourself as:
```
    $ python setup.py install
```

## Usage

``` python
kroman.parse("손목시계")
=> "son-mog-si-gye"
```


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/cheunghy/kroman-py.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
