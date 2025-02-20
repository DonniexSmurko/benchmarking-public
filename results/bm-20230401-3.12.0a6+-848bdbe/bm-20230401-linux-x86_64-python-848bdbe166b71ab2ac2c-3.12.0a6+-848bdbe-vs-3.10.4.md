
# Results vs. 3.10.4

- fork: python
- ref: 848bdbe166b71ab2ac2c
- machine: linux-x86_64
- commit hash: 848bdbe
- commit date: 2023-04-01
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.55 ms: 1.39x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                 |
| html5lib       | 86.4 ms                                                             | 61.5 ms: 1.40x faster                                                  |
| tornado_http   | 129 ms                                                              | 91.8 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                               | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 86.7 ms: 1.68x faster                                                  |
| float          | 110 ms                                                              | 74.7 ms: 1.47x faster                                                  |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                               | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.31x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 21.8 ms: 1.15x faster                                                  |
| regex_dna      | 213 ms                                                              | 202 ms: 1.05x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.64 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                               | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 289 us: 1.58x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 201 us: 1.49x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.62 ms: 1.42x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 56.1 ms: 1.33x faster                                                  |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 81.3 ms: 1.17x faster                                                  |
| unpickle             | 15.0 us                                                             | 13.4 us: 1.12x faster                                                  |
| pickle_list          | 4.73 us                                                             | 4.24 us: 1.11x faster                                                  |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                              | 102 ms: 1.10x faster                                                   |
| unpickle_list        | 4.94 us                                                             | 4.99 us: 1.01x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 31.6 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.83 ms: 1.60x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.52 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.0 ms: 1.47x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 21.5 ms: 1.42x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 47.0 ms: 1.37x faster                                                  |
| django_template | 45.8 ms                                                             | 34.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.5 ms: 2.57x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.24 ms: 2.25x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                   |
| logging_silent          | 169 ns                                                              | 96.1 ns: 1.76x faster                                                  |
| scimark_sor             | 198 ms                                                              | 113 ms: 1.75x faster                                                   |
| richards                | 74.2 ms                                                             | 43.6 ms: 1.70x faster                                                  |
| nbody                   | 146 ms                                                              | 86.7 ms: 1.68x faster                                                  |
| raytrace                | 470 ms                                                              | 284 ms: 1.66x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                              | 67.1 ms: 1.62x faster                                                  |
| pyflate                 | 671 ms                                                              | 417 ms: 1.61x faster                                                   |
| go                      | 226 ms                                                              | 140 ms: 1.61x faster                                                   |
| python_startup          | 14.1 ms                                                             | 8.83 ms: 1.60x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 73.8 ms: 1.58x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 289 us: 1.58x faster                                                   |
| hexiom                  | 9.50 ms                                                             | 6.03 ms: 1.58x faster                                                  |
| spectral_norm           | 150 ms                                                              | 95.2 ms: 1.58x faster                                                  |
| chaos                   | 106 ms                                                              | 67.7 ms: 1.56x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 43.2 ns: 1.52x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 201 us: 1.49x faster                                                   |
| deepcopy_memo           | 51.8 us                                                             | 35.0 us: 1.48x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.0 ms: 1.47x faster                                                  |
| float                   | 110 ms                                                              | 74.7 ms: 1.47x faster                                                  |
| scimark_lu              | 160 ms                                                              | 110 ms: 1.46x faster                                                   |
| sqlglot_parse           | 2.07 ms                                                             | 1.44 ms: 1.44x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.31 us: 1.44x faster                                                  |
| logging_simple          | 8.21 us                                                             | 5.76 us: 1.43x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.62 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.73 ms: 1.42x faster                                                  |
| genshi_text             | 30.4 ms                                                             | 21.5 ms: 1.42x faster                                                  |
| html5lib                | 86.4 ms                                                             | 61.5 ms: 1.40x faster                                                  |
| tornado_http            | 129 ms                                                              | 91.8 ms: 1.40x faster                                                  |
| chameleon               | 9.13 ms                                                             | 6.55 ms: 1.39x faster                                                  |
| scimark_fft             | 425 ms                                                              | 306 ms: 1.39x faster                                                   |
| pprint_pformat          | 1.98 sec                                                            | 1.43 sec: 1.39x faster                                                 |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.38x faster                                                 |
| pprint_safe_repr        | 953 ms                                                              | 695 ms: 1.37x faster                                                   |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                 |
| genshi_xml              | 64.3 ms                                                             | 47.0 ms: 1.37x faster                                                  |
| async_tree_none         | 713 ms                                                              | 526 ms: 1.36x faster                                                   |
| django_template         | 45.8 ms                                                             | 34.0 ms: 1.35x faster                                                  |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                  |
| xml_etree_process       | 74.8 ms                                                             | 56.1 ms: 1.33x faster                                                  |
| coroutines              | 31.8 ms                                                             | 23.9 ms: 1.33x faster                                                  |
| 2to3                    | 336 ms                                                              | 253 ms: 1.33x faster                                                   |
| thrift                  | 1.04 ms                                                             | 782 us: 1.33x faster                                                   |
| deepcopy                | 438 us                                                              | 331 us: 1.32x faster                                                   |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.27 ms: 1.32x faster                                                  |
| regex_compile           | 177 ms                                                              | 135 ms: 1.31x faster                                                   |
| mypy2                   | 432 ms                                                              | 332 ms: 1.30x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 658 ms: 1.30x faster                                                   |
| fannkuch                | 485 ms                                                              | 376 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.80 us                                                             | 2.98 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 742 ms: 1.27x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 51.6 ms: 1.27x faster                                                  |
| sqlglot_normalize       | 135 ms                                                              | 106 ms: 1.26x faster                                                   |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                 |
| nqueens                 | 98.8 ms                                                             | 79.8 ms: 1.24x faster                                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                   |
| bench_thread_pool       | 954 us                                                              | 790 us: 1.21x faster                                                   |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 63.7 ms: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                                  |
| sympy_expand            | 540 ms                                                              | 461 ms: 1.17x faster                                                   |
| xml_etree_generate      | 94.9 ms                                                             | 81.3 ms: 1.17x faster                                                  |
| json                    | 5.41 ms                                                             | 4.68 ms: 1.16x faster                                                  |
| sympy_str               | 328 ms                                                              | 285 ms: 1.15x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 21.8 ms: 1.15x faster                                                  |
| comprehensions          | 27.3 us                                                             | 23.8 us: 1.14x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.63 us: 1.13x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.12x faster                                                  |
| unpickle                | 15.0 us                                                             | 13.4 us: 1.12x faster                                                  |
| djangocms               | 36.3 us                                                             | 32.5 us: 1.12x faster                                                  |
| pickle_list             | 4.73 us                                                             | 4.24 us: 1.11x faster                                                  |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 17.8 ms: 1.11x faster                                                  |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.11x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.50 sec: 1.10x faster                                                 |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                              | 102 ms: 1.10x faster                                                   |
| regex_dna               | 213 ms                                                              | 202 ms: 1.05x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.51 ms: 1.02x faster                                                  |
| async_generators        | 420 ms                                                              | 416 ms: 1.01x faster                                                   |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| unpickle_list           | 4.94 us                                                             | 4.99 us: 1.01x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.52 ms: 1.13x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.64 ms: 1.13x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 31.6 us: 1.14x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 4.07 ms: 1.16x slower                                                  |
| dask                    | 437 ms                                                              | 514 ms: 1.18x slower                                                   |
| coverage                | 70.6 ms                                                             | 98.0 ms: 1.39x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.29x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
