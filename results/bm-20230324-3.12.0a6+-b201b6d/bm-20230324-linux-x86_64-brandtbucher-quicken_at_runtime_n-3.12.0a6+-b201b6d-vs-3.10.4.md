
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: b201b6d
- commit date: 2023-03-24
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 253 ms: 1.33x faster                                                         |
| chameleon      | 9.13 ms                                                             | 6.51 ms: 1.40x faster                                                        |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                       |
| html5lib       | 86.4 ms                                                             | 62.6 ms: 1.38x faster                                                        |
| tornado_http   | 129 ms                                                              | 91.6 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.6 ms: 1.65x faster                                                        |
| float          | 110 ms                                                              | 74.4 ms: 1.48x faster                                                        |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                               | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 136 ms: 1.31x faster                                                         |
| regex_v8       | 24.9 ms                                                             | 21.3 ms: 1.17x faster                                                        |
| regex_dna      | 213 ms                                                              | 202 ms: 1.06x faster                                                         |
| regex_effbot   | 3.22 ms                                                             | 3.41 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                               | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 294 us: 1.55x faster                                                         |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.49x faster                                                         |
| json_dumps           | 13.7 ms                                                             | 9.73 ms: 1.41x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 56.5 ms: 1.32x faster                                                        |
| json_loads           | 29.3 us                                                             | 24.5 us: 1.19x faster                                                        |
| xml_etree_generate   | 94.9 ms                                                             | 81.1 ms: 1.17x faster                                                        |
| pickle_list          | 4.73 us                                                             | 4.20 us: 1.13x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                              | 99.9 ms: 1.11x faster                                                        |
| xml_etree_parse      | 164 ms                                                              | 148 ms: 1.11x faster                                                         |
| unpickle             | 15.0 us                                                             | 13.9 us: 1.08x faster                                                        |
| unpickle_list        | 4.94 us                                                             | 4.92 us: 1.00x faster                                                        |
| pickle               | 10.2 us                                                             | 10.5 us: 1.03x slower                                                        |
| pickle_dict          | 27.8 us                                                             | 31.7 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.65 ms: 1.63x faster                                                        |
| python_startup_no_site | 5.80 ms                                                             | 6.34 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.22x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                                        |
| django_template | 45.8 ms                                                             | 33.9 ms: 1.35x faster                                                        |
| genshi_text     | 30.4 ms                                                             | 22.5 ms: 1.35x faster                                                        |
| genshi_xml      | 64.3 ms                                                             | 48.5 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                               | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.1 ms: 2.60x faster                                                        |
| deltablue               | 7.30 ms                                                             | 3.26 ms: 2.24x faster                                                        |
| asyncio_tcp             | 922 ms                                                              | 509 ms: 1.81x faster                                                         |
| scimark_sor             | 198 ms                                                              | 111 ms: 1.78x faster                                                         |
| logging_silent          | 169 ns                                                              | 96.5 ns: 1.75x faster                                                        |
| richards                | 74.2 ms                                                             | 44.2 ms: 1.68x faster                                                        |
| raytrace                | 470 ms                                                              | 284 ms: 1.65x faster                                                         |
| spectral_norm           | 150 ms                                                              | 91.1 ms: 1.65x faster                                                        |
| nbody                   | 146 ms                                                              | 88.6 ms: 1.65x faster                                                        |
| python_startup          | 14.1 ms                                                             | 8.65 ms: 1.63x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 67.4 ms: 1.61x faster                                                        |
| go                      | 226 ms                                                              | 141 ms: 1.60x faster                                                         |
| chaos                   | 106 ms                                                              | 66.9 ms: 1.58x faster                                                        |
| crypto_pyaes            | 117 ms                                                              | 73.8 ms: 1.58x faster                                                        |
| pyflate                 | 671 ms                                                              | 427 ms: 1.57x faster                                                         |
| hexiom                  | 9.50 ms                                                             | 6.06 ms: 1.57x faster                                                        |
| pickle_pure_python      | 457 us                                                              | 294 us: 1.55x faster                                                         |
| deepcopy_memo           | 51.8 us                                                             | 34.4 us: 1.50x faster                                                        |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.49x faster                                                         |
| unpack_sequence         | 65.6 ns                                                             | 44.4 ns: 1.48x faster                                                        |
| float                   | 110 ms                                                              | 74.4 ms: 1.48x faster                                                        |
| scimark_lu              | 160 ms                                                              | 109 ms: 1.47x faster                                                         |
| mako                    | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                                        |
| sqlglot_parse           | 2.07 ms                                                             | 1.44 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                             | 1.73 ms: 1.42x faster                                                        |
| json_dumps              | 13.7 ms                                                             | 9.73 ms: 1.41x faster                                                        |
| tornado_http            | 129 ms                                                              | 91.6 ms: 1.41x faster                                                        |
| chameleon               | 9.13 ms                                                             | 6.51 ms: 1.40x faster                                                        |
| pprint_pformat          | 1.98 sec                                                            | 1.42 sec: 1.39x faster                                                       |
| scimark_fft             | 425 ms                                                              | 308 ms: 1.38x faster                                                         |
| html5lib                | 86.4 ms                                                             | 62.6 ms: 1.38x faster                                                        |
| logging_format          | 9.07 us                                                             | 6.58 us: 1.38x faster                                                        |
| pycparser               | 1.53 sec                                                            | 1.12 sec: 1.37x faster                                                       |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                       |
| pprint_safe_repr        | 953 ms                                                              | 700 ms: 1.36x faster                                                         |
| logging_simple          | 8.21 us                                                             | 6.05 us: 1.36x faster                                                        |
| django_template         | 45.8 ms                                                             | 33.9 ms: 1.35x faster                                                        |
| genshi_text             | 30.4 ms                                                             | 22.5 ms: 1.35x faster                                                        |
| async_tree_none         | 713 ms                                                              | 527 ms: 1.35x faster                                                         |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.17 ms: 1.35x faster                                                        |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.33x faster                                                        |
| 2to3                    | 336 ms                                                              | 253 ms: 1.33x faster                                                         |
| genshi_xml              | 64.3 ms                                                             | 48.5 ms: 1.33x faster                                                        |
| xml_etree_process       | 74.8 ms                                                             | 56.5 ms: 1.32x faster                                                        |
| coroutines              | 31.8 ms                                                             | 24.1 ms: 1.32x faster                                                        |
| deepcopy                | 438 us                                                              | 333 us: 1.31x faster                                                         |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                                        |
| async_tree_memoization  | 853 ms                                                              | 651 ms: 1.31x faster                                                         |
| regex_compile           | 177 ms                                                              | 136 ms: 1.31x faster                                                         |
| thrift                  | 1.04 ms                                                             | 795 us: 1.30x faster                                                         |
| mypy2                   | 432 ms                                                              | 335 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed | 944 ms                                                              | 740 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                             | 51.6 ms: 1.27x faster                                                        |
| fannkuch                | 485 ms                                                              | 384 ms: 1.26x faster                                                         |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                       |
| deepcopy_reduce         | 3.80 us                                                             | 3.04 us: 1.25x faster                                                        |
| sqlglot_normalize       | 135 ms                                                              | 108 ms: 1.25x faster                                                         |
| nqueens                 | 98.8 ms                                                             | 80.6 ms: 1.23x faster                                                        |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.21x faster                                                         |
| bench_thread_pool       | 954 us                                                              | 794 us: 1.20x faster                                                         |
| dulwich_log             | 76.3 ms                                                             | 63.6 ms: 1.20x faster                                                        |
| json_loads              | 29.3 us                                                             | 24.5 us: 1.19x faster                                                        |
| regex_v8                | 24.9 ms                                                             | 21.3 ms: 1.17x faster                                                        |
| xml_etree_generate      | 94.9 ms                                                             | 81.1 ms: 1.17x faster                                                        |
| sympy_integrate         | 24.3 ms                                                             | 20.8 ms: 1.17x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.1 ms: 1.17x faster                                                        |
| json                    | 5.41 ms                                                             | 4.65 ms: 1.16x faster                                                        |
| sympy_expand            | 540 ms                                                              | 467 ms: 1.16x faster                                                         |
| comprehensions          | 27.3 us                                                             | 23.7 us: 1.15x faster                                                        |
| sqlite_synth            | 2.97 us                                                             | 2.60 us: 1.14x faster                                                        |
| sympy_str               | 328 ms                                                              | 288 ms: 1.14x faster                                                         |
| pickle_list             | 4.73 us                                                             | 4.20 us: 1.13x faster                                                        |
| djangocms               | 36.3 us                                                             | 32.5 us: 1.12x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                              | 99.9 ms: 1.11x faster                                                        |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.11x faster                                                         |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                                        |
| xml_etree_parse         | 164 ms                                                              | 148 ms: 1.11x faster                                                         |
| sympy_sum               | 185 ms                                                              | 168 ms: 1.10x faster                                                         |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                                        |
| mdp                     | 2.75 sec                                                            | 2.55 sec: 1.08x faster                                                       |
| unpickle                | 15.0 us                                                             | 13.9 us: 1.08x faster                                                        |
| regex_dna               | 213 ms                                                              | 202 ms: 1.06x faster                                                         |
| telco                   | 6.67 ms                                                             | 6.48 ms: 1.03x faster                                                        |
| async_generators        | 420 ms                                                              | 409 ms: 1.03x faster                                                         |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                         |
| unpickle_list           | 4.94 us                                                             | 4.92 us: 1.00x faster                                                        |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.03x slower                                                        |
| regex_effbot            | 3.22 ms                                                             | 3.41 ms: 1.06x slower                                                        |
| python_startup_no_site  | 5.80 ms                                                             | 6.34 ms: 1.09x slower                                                        |
| gc_traversal            | 3.53 ms                                                             | 3.93 ms: 1.11x slower                                                        |
| pickle_dict             | 27.8 us                                                             | 31.7 us: 1.14x slower                                                        |
| dask                    | 437 ms                                                              | 515 ms: 1.18x slower                                                         |
| coverage                | 70.6 ms                                                             | 96.3 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.29x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
