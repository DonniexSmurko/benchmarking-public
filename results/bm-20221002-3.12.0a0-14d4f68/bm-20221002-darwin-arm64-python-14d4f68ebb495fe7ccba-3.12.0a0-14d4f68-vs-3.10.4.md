
# Results vs. 3.10.4

- fork: python
- ref: 14d4f68ebb495fe7ccba
- machine: darwin-arm64
- commit hash: 14d4f68
- commit date: 2022-10-02
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.69 ms: 1.24x faster                                                 |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| html5lib       | 44.2 ms                                                | 35.8 ms: 1.24x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.1 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.3 ms: 1.43x faster                                                 |
| float          | 72.4 ms                                                | 56.1 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.4 ms: 1.28x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                 |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps           | 8.40 ms                                                | 6.13 ms: 1.37x faster                                                 |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.25x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.6 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.9 ms: 1.11x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.56 us: 1.05x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| unpickle             | 9.89 us                                                | 9.75 us: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.02x slower                                                 |
| pickle               | 7.35 us                                                | 7.55 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.06 ms: 1.31x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.16 ms: 1.24x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.14 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.3 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.83 ms: 1.82x faster                                                 |
| logging_silent          | 119 ns                                                 | 71.7 ns: 1.67x faster                                                 |
| richards                | 51.4 ms                                                | 33.2 ms: 1.55x faster                                                 |
| scimark_lu              | 109 ms                                                 | 72.3 ms: 1.51x faster                                                 |
| raytrace                | 325 ms                                                 | 216 ms: 1.51x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 52.2 ms: 1.50x faster                                                 |
| nbody                   | 93.3 ms                                                | 65.3 ms: 1.43x faster                                                 |
| async_tree_none         | 400 ms                                                 | 283 ms: 1.42x faster                                                  |
| go                      | 165 ms                                                 | 118 ms: 1.41x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.6 ms: 1.40x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 732 ms: 1.39x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.13 ms: 1.37x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.00 ms: 1.36x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.17 ms: 1.34x faster                                                 |
| python_startup          | 11.9 ms                                                | 9.06 ms: 1.31x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 73.0 ms: 1.31x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.9 ms: 1.31x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 55.4 ms: 1.31x faster                                                 |
| tornado_http            | 91.5 ms                                                | 70.1 ms: 1.31x faster                                                 |
| thrift                  | 580 us                                                 | 446 us: 1.30x faster                                                  |
| float                   | 72.4 ms                                                | 56.1 ms: 1.29x faster                                                 |
| mako                    | 10.5 ms                                                | 8.14 ms: 1.29x faster                                                 |
| pyflate                 | 453 ms                                                 | 353 ms: 1.28x faster                                                  |
| pycparser               | 916 ms                                                 | 713 ms: 1.28x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 383 ms: 1.28x faster                                                  |
| regex_compile           | 96.4 ms                                                | 75.4 ms: 1.28x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.1 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 530 ms: 1.26x faster                                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.06 ms: 1.26x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.68 us: 1.26x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.25x faster                                                  |
| logging_format          | 4.97 us                                                | 3.97 us: 1.25x faster                                                 |
| scimark_sor             | 126 ms                                                 | 101 ms: 1.25x faster                                                  |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.16 ms: 1.24x faster                                                 |
| html5lib                | 44.2 ms                                                | 35.8 ms: 1.24x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.69 ms: 1.24x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.23 ms: 1.23x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.3 ms: 1.23x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.23x faster                                                |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.2 ms: 1.22x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.82 ms: 1.22x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 496 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| deepcopy_memo           | 34.4 us                                                | 28.5 us: 1.21x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 454 us: 1.20x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.4 ms: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                 |
| fannkuch                | 317 ms                                                 | 270 ms: 1.18x faster                                                  |
| deepcopy                | 281 us                                                 | 240 us: 1.17x faster                                                  |
| async_generators        | 234 ms                                                 | 201 ms: 1.17x faster                                                  |
| pylint                  | 307 ms                                                 | 265 ms: 1.16x faster                                                  |
| scimark_fft             | 230 ms                                                 | 199 ms: 1.16x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.06 us: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.6 ms: 1.14x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 47.6 ms: 1.14x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.13x faster                                                  |
| generators              | 32.7 ms                                                | 29.2 ms: 1.12x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 64.9 ms: 1.11x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.3 ms: 1.11x faster                                                 |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 34.1 ns: 1.10x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                 |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 85.9 ms: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.09x faster                                                |
| 2to3                    | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| telco                   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                 |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.56 us: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.5 ms: 1.04x faster                                                 |
| unpickle                | 9.89 us                                                | 9.75 us: 1.01x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.46 us: 1.01x faster                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.02x slower                                                 |
| pickle                  | 7.35 us                                                | 7.55 us: 1.03x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 41.9 ms: 1.06x slower                                                 |
| coverage                | 42.0 ms                                                | 53.5 ms: 1.27x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (2): pidigits, meteor_contest
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221002-3.12.0a0-14d4f68/bm-20221002-darwin-arm64-python-14d4f68ebb495fe7ccba-3.12.0a0-14d4f68.json: mypy
