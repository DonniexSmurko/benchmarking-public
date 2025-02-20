# Results

- fork: python
- version: 3.12.0a2+
- commit hash: [594de16](https://github.com/python/cpython/commit/594de16)
- commit date: 2022-11-28T01:49:10-05:00
- ref: 594de165bf2f21d6b28e

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16.json)

### vs. 3.10.4

- 1.32x faster \*
- missing benchmarks: asyncio_tcp, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md)
- [plot](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md)
- [plot](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513536837)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16.json)

### vs. 3.10.4

- 1.24x faster
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md)
- [plot](bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md)
- [plot](bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450236)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md)
- [plot](bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.png)

### vs. 3.11.0

- 1.09x faster
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md)
- [plot](bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494504555)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16.json)

### vs. 3.10.4

- 1.18x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md)
- [plot](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x slower
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md)
- [plot](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.png)

