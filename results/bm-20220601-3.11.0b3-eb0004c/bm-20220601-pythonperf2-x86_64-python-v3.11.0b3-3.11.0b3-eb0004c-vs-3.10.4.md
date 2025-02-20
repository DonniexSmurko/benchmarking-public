
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                             |
| chameleon      | 9.62 ms                                                      | 7.60 ms: 1.27x faster                                            |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.20x faster                                           |
| html5lib       | 96.3 ms                                                      | 71.0 ms: 1.36x faster                                            |
| tornado_http   | 151 ms                                                       | 119 ms: 1.27x faster                                             |
| Geometric mean | (ref)                                                        | 1.27x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.9 ms: 1.48x faster                                            |
| nbody          | 132 ms                                                       | 93.0 ms: 1.42x faster                                            |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.31x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 156 ms: 1.23x faster                                             |
| regex_dna      | 261 ms                                                       | 219 ms: 1.19x faster                                             |
| regex_v8       | 26.0 ms                                                      | 24.3 ms: 1.07x faster                                            |
| regex_effbot   | 2.99 ms                                                      | 3.05 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.11x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 319 us: 1.42x faster                                             |
| xml_etree_process    | 77.6 ms                                                      | 55.9 ms: 1.39x faster                                            |
| unpickle_pure_python | 318 us                                                       | 238 us: 1.33x faster                                             |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                            |
| xml_etree_generate   | 94.1 ms                                                      | 80.2 ms: 1.17x faster                                            |
| json_dumps           | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                            |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                             |
| pickle_list          | 4.11 us                                                      | 3.92 us: 1.05x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 153 ms: 1.04x faster                                             |
| pickle               | 10.1 us                                                      | 9.80 us: 1.03x faster                                            |
| unpickle_list        | 4.73 us                                                      | 4.58 us: 1.03x faster                                            |
| pickle_dict          | 29.5 us                                                      | 31.3 us: 1.06x slower                                            |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                            |
| python_startup_no_site | 7.32 ms                                                      | 7.70 ms: 1.05x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                            |
| django_template | 52.0 ms                                                      | 41.4 ms: 1.26x faster                                            |
| genshi_text     | 31.7 ms                                                      | 26.3 ms: 1.20x faster                                            |
| genshi_xml      | 63.5 ms                                                      | 60.1 ms: 1.06x faster                                            |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf2-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.20 ms: 1.79x faster                                            |
| pyflate                 | 731 ms                                                       | 441 ms: 1.66x faster                                             |
| logging_silent          | 165 ns                                                       | 99.3 ns: 1.66x faster                                            |
| raytrace                | 491 ms                                                       | 304 ms: 1.62x faster                                             |
| go                      | 264 ms                                                       | 166 ms: 1.59x faster                                             |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.58x faster                                             |
| bench_mp_pool           | 7.10 ms                                                      | 4.52 ms: 1.57x faster                                            |
| scimark_monte_carlo     | 109 ms                                                       | 69.5 ms: 1.56x faster                                            |
| richards                | 73.9 ms                                                      | 49.2 ms: 1.50x faster                                            |
| scimark_lu              | 164 ms                                                       | 110 ms: 1.49x faster                                             |
| float                   | 109 ms                                                       | 73.9 ms: 1.48x faster                                            |
| chaos                   | 108 ms                                                       | 73.6 ms: 1.47x faster                                            |
| spectral_norm           | 138 ms                                                       | 96.8 ms: 1.42x faster                                            |
| nbody                   | 132 ms                                                       | 93.0 ms: 1.42x faster                                            |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.42x faster                                             |
| crypto_pyaes            | 119 ms                                                       | 84.5 ms: 1.40x faster                                            |
| xml_etree_process       | 77.6 ms                                                      | 55.9 ms: 1.39x faster                                            |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                           |
| hexiom                  | 9.54 ms                                                      | 7.00 ms: 1.36x faster                                            |
| async_tree_none         | 698 ms                                                       | 513 ms: 1.36x faster                                             |
| html5lib                | 96.3 ms                                                      | 71.0 ms: 1.36x faster                                            |
| thrift                  | 1.23 ms                                                      | 909 us: 1.35x faster                                             |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                            |
| unpickle_pure_python    | 318 us                                                       | 238 us: 1.33x faster                                             |
| async_tree_memoization  | 822 ms                                                       | 617 ms: 1.33x faster                                             |
| pprint_safe_repr        | 1.03 sec                                                     | 774 ms: 1.33x faster                                             |
| async_generators        | 419 ms                                                       | 318 ms: 1.32x faster                                             |
| pprint_pformat          | 2.12 sec                                                     | 1.61 sec: 1.32x faster                                           |
| unpack_sequence         | 59.7 ns                                                      | 45.4 ns: 1.31x faster                                            |
| deepcopy_memo           | 49.2 us                                                      | 37.7 us: 1.31x faster                                            |
| logging_simple          | 9.24 us                                                      | 7.16 us: 1.29x faster                                            |
| tornado_http            | 151 ms                                                       | 119 ms: 1.27x faster                                             |
| pycparser               | 1.66 sec                                                     | 1.31 sec: 1.27x faster                                           |
| chameleon               | 9.62 ms                                                      | 7.60 ms: 1.27x faster                                            |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.03 ms: 1.27x faster                                            |
| django_template         | 52.0 ms                                                      | 41.4 ms: 1.26x faster                                            |
| scimark_fft             | 359 ms                                                       | 286 ms: 1.26x faster                                             |
| logging_format          | 9.94 us                                                      | 7.95 us: 1.25x faster                                            |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                             |
| gunicorn                | 1.15 ms                                                      | 931 us: 1.23x faster                                             |
| aiohttp                 | 1.18 ms                                                      | 958 us: 1.23x faster                                             |
| regex_compile           | 191 ms                                                       | 156 ms: 1.23x faster                                             |
| sqlalchemy_declarative  | 188 ms                                                       | 154 ms: 1.22x faster                                             |
| docutils                | 3.41 sec                                                     | 2.83 sec: 1.20x faster                                           |
| genshi_text             | 31.7 ms                                                      | 26.3 ms: 1.20x faster                                            |
| json_loads              | 30.3 us                                                      | 25.2 us: 1.20x faster                                            |
| sqlglot_normalize       | 147 ms                                                       | 123 ms: 1.19x faster                                             |
| regex_dna               | 261 ms                                                       | 219 ms: 1.19x faster                                             |
| sqlglot_optimize        | 70.1 ms                                                      | 59.4 ms: 1.18x faster                                            |
| sqlite_synth            | 2.96 us                                                      | 2.51 us: 1.18x faster                                            |
| dulwich_log             | 80.5 ms                                                      | 68.4 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                       | 810 ms: 1.17x faster                                             |
| xml_etree_generate      | 94.1 ms                                                      | 80.2 ms: 1.17x faster                                            |
| deepcopy                | 457 us                                                       | 390 us: 1.17x faster                                             |
| sqlalchemy_imperative   | 22.9 ms                                                      | 19.6 ms: 1.17x faster                                            |
| nqueens                 | 114 ms                                                       | 97.6 ms: 1.16x faster                                            |
| sqlglot_transpile       | 2.69 ms                                                      | 2.32 ms: 1.16x faster                                            |
| dask                    | 478 ms                                                       | 414 ms: 1.16x faster                                             |
| flaskblogging           | 4.37 ms                                                      | 3.82 ms: 1.15x faster                                            |
| json                    | 5.94 ms                                                      | 5.20 ms: 1.14x faster                                            |
| sqlglot_parse           | 2.24 ms                                                      | 1.97 ms: 1.14x faster                                            |
| sympy_expand            | 603 ms                                                       | 531 ms: 1.14x faster                                             |
| deepcopy_reduce         | 3.91 us                                                      | 3.48 us: 1.13x faster                                            |
| bench_thread_pool       | 1.14 ms                                                      | 1.01 ms: 1.12x faster                                            |
| sympy_integrate         | 28.1 ms                                                      | 25.2 ms: 1.11x faster                                            |
| pathlib                 | 21.3 ms                                                      | 19.2 ms: 1.11x faster                                            |
| coroutines              | 30.6 ms                                                      | 27.9 ms: 1.10x faster                                            |
| sympy_str               | 358 ms                                                       | 327 ms: 1.09x faster                                             |
| pylint                  | 562 ms                                                       | 515 ms: 1.09x faster                                             |
| sympy_sum               | 193 ms                                                       | 177 ms: 1.09x faster                                             |
| meteor_contest          | 142 ms                                                       | 131 ms: 1.08x faster                                             |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                            |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                             |
| create_gc_cycles        | 1.80 ms                                                      | 1.68 ms: 1.07x faster                                            |
| regex_v8                | 26.0 ms                                                      | 24.3 ms: 1.07x faster                                            |
| mypy2                   | 466 ms                                                       | 438 ms: 1.06x faster                                             |
| json_dumps              | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                            |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                             |
| telco                   | 7.14 ms                                                      | 6.75 ms: 1.06x faster                                            |
| genshi_xml              | 63.5 ms                                                      | 60.1 ms: 1.06x faster                                            |
| mdp                     | 2.95 sec                                                     | 2.81 sec: 1.05x faster                                           |
| asyncio_tcp             | 787 ms                                                       | 751 ms: 1.05x faster                                             |
| pickle_list             | 4.11 us                                                      | 3.92 us: 1.05x faster                                            |
| xml_etree_parse         | 160 ms                                                       | 153 ms: 1.04x faster                                             |
| pickle                  | 10.1 us                                                      | 9.80 us: 1.03x faster                                            |
| unpickle_list           | 4.73 us                                                      | 4.58 us: 1.03x faster                                            |
| generators              | 57.0 ms                                                      | 56.0 ms: 1.02x faster                                            |
| regex_effbot            | 2.99 ms                                                      | 3.05 ms: 1.02x slower                                            |
| comprehensions          | 27.3 us                                                      | 28.3 us: 1.04x slower                                            |
| python_startup_no_site  | 7.32 ms                                                      | 7.70 ms: 1.05x slower                                            |
| pickle_dict             | 29.5 us                                                      | 31.3 us: 1.06x slower                                            |
| gc_traversal            | 3.46 ms                                                      | 4.03 ms: 1.16x slower                                            |
| Geometric mean          | (ref)                                                        | 1.22x faster                                                     |

Benchmark hidden because not significant (2): unpickle, fannkuch
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
