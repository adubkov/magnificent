## MagnificentHealthcheck

To start magnificent monitoring daemon please execute:

```
magnificent_healthcheck http://localhost:12345 --interval 1 -r 1 -f 2 --daemon
```

On Mac it will writing logs to `/Users/{{ USER }}/Library/Logs/MagnificentHealthcheck/`
On Linux it will writing logs to `/var/logs/MagnificentHealthcheck/`

I didn't implement stopping mechanism. It should be just a function to find pid and kill the prcoess.

I would add this function to setup.py as entrypoint.
Also there were not time for tests, but I could add them easily with more time.

### Usage
```
$ magnificent_healthcheck -h
usage: magnificent_healthcheck [-h] [-i INTERVAL] [-r RISE] [-f FAIL]
                               [--daemon] [-D]
                               url

positional arguments:
  url                   URL to check

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        Interval of checking URL. Default: 5
  -r RISE, --rise RISE  Tests pass before rise. Default: 2
  -f FAIL, --fail FAIL  Tests failed before fail. Default: 3
  --daemon              Run process as a daemon. Default: False
  -D, --debug           Change verbosity level to DEBUG. Default: False
```
