# Results

- fork: python
- version: 3.12.0a3+
- commit hash: [e47b139](https://github.com/python/cpython/commit/e47b139)
- commit date: 2023-01-08T21:53:56-05:00
- ref: e47b13934b2eb50914e4

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230108-linux-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20230108-linux-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.md)
- [plot](bm-20230108-linux-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20230108-linux-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.md)
- [plot](bm-20230108-linux-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513537515)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230108-pythonperf2-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20230108-pythonperf2-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.md)
- [plot](bm-20230108-pythonperf2-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20230108-pythonperf2-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.md)
- [plot](bm-20230108-pythonperf2-x86_64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450722)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.md)
- [plot](bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.png)

### vs. 3.11.0

- 1.09x faster
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.md)
- [plot](bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494505186)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.md)
- [plot](bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.md)
- [plot](bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.png)

