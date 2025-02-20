
# Results vs. 3.11.0

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 162 ms: 1.01x slower                                                  |
| docutils       | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                                |
| html5lib       | 34.8 ms                                                             | 33.8 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                               | 1.00x faster                                                          |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                             | 52.8 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                              | 281 ms: 1.00x slower                                                  |
| nbody          | 65.5 ms                                                             | 66.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                               | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.20 ms: 1.20x faster                                                 |
| regex_compile  | 76.6 ms                                                             | 75.5 ms: 1.01x faster                                                 |
| regex_dna      | 151 ms                                                              | 171 ms: 1.13x slower                                                  |
| regex_v8       | 16.1 ms                                                             | 19.8 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                              | 102 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                             | 67.3 ms: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                             | 17.6 us: 1.01x faster                                                 |
| json_loads           | 16.0 us                                                             | 15.9 us: 1.01x faster                                                 |
| unpickle_pure_python | 158 us                                                              | 157 us: 1.01x faster                                                  |
| pickle_list          | 2.83 us                                                             | 2.81 us: 1.00x faster                                                 |
| pickle               | 7.17 us                                                             | 7.15 us: 1.00x faster                                                 |
| pickle_pure_python   | 198 us                                                              | 199 us: 1.00x slower                                                  |
| xml_etree_process    | 35.0 ms                                                             | 35.2 ms: 1.01x slower                                                 |
| unpickle_list        | 2.63 us                                                             | 2.65 us: 1.01x slower                                                 |
| json_dumps           | 7.59 ms                                                             | 7.68 ms: 1.01x slower                                                 |
| unpickle             | 9.66 us                                                             | 9.87 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.00x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                             | 9.78 ms: 1.03x faster                                                 |
| python_startup         | 12.3 ms                                                             | 12.1 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                               | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 8.21 ms: 1.03x faster                                                 |
| genshi_text     | 15.3 ms                                                             | 15.1 ms: 1.01x faster                                                 |
| django_template | 21.1 ms                                                             | 21.2 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                             | 30.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                             | 2.20 ms: 1.20x faster                                                 |
| unpack_sequence         | 33.5 ns                                                             | 32.0 ns: 1.05x faster                                                 |
| deltablue               | 2.81 ms                                                             | 2.69 ms: 1.05x faster                                                 |
| async_tree_memoization  | 338 ms                                                              | 323 ms: 1.05x faster                                                  |
| dask                    | 226 ms                                                              | 217 ms: 1.04x faster                                                  |
| sympy_sum               | 86.0 ms                                                             | 82.6 ms: 1.04x faster                                                 |
| xml_etree_parse         | 106 ms                                                              | 102 ms: 1.04x faster                                                  |
| logging_format          | 3.77 us                                                             | 3.65 us: 1.03x faster                                                 |
| nqueens                 | 62.4 ms                                                             | 60.6 ms: 1.03x faster                                                 |
| pathlib                 | 28.3 ms                                                             | 27.5 ms: 1.03x faster                                                 |
| html5lib                | 34.8 ms                                                             | 33.8 ms: 1.03x faster                                                 |
| python_startup_no_site  | 10.1 ms                                                             | 9.78 ms: 1.03x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                             | 67.3 ms: 1.03x faster                                                 |
| scimark_monte_carlo     | 46.5 ms                                                             | 45.3 ms: 1.03x faster                                                 |
| sympy_integrate         | 11.5 ms                                                             | 11.2 ms: 1.03x faster                                                 |
| mako                    | 8.42 ms                                                             | 8.21 ms: 1.03x faster                                                 |
| sympy_str               | 151 ms                                                              | 148 ms: 1.02x faster                                                  |
| logging_simple          | 3.49 us                                                             | 3.41 us: 1.02x faster                                                 |
| coroutines              | 17.7 ms                                                             | 17.3 ms: 1.02x faster                                                 |
| deepcopy_memo           | 26.3 us                                                             | 25.8 us: 1.02x faster                                                 |
| python_startup          | 12.3 ms                                                             | 12.1 ms: 1.02x faster                                                 |
| regex_compile           | 76.6 ms                                                             | 75.5 ms: 1.01x faster                                                 |
| pickle_dict             | 17.9 us                                                             | 17.6 us: 1.01x faster                                                 |
| pprint_safe_repr        | 463 ms                                                              | 457 ms: 1.01x faster                                                  |
| genshi_text             | 15.3 ms                                                             | 15.1 ms: 1.01x faster                                                 |
| generators              | 28.6 ms                                                             | 28.3 ms: 1.01x faster                                                 |
| go                      | 109 ms                                                              | 108 ms: 1.01x faster                                                  |
| sympy_expand            | 243 ms                                                              | 241 ms: 1.01x faster                                                  |
| pprint_pformat          | 946 ms                                                              | 937 ms: 1.01x faster                                                  |
| async_generators        | 195 ms                                                              | 193 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                                |
| sqlite_synth            | 1.28 us                                                             | 1.27 us: 1.01x faster                                                 |
| scimark_sor             | 82.9 ms                                                             | 82.2 ms: 1.01x faster                                                 |
| json_loads              | 16.0 us                                                             | 15.9 us: 1.01x faster                                                 |
| asyncio_tcp             | 651 ms                                                              | 648 ms: 1.01x faster                                                  |
| unpickle_pure_python    | 158 us                                                              | 157 us: 1.01x faster                                                  |
| async_tree_io           | 707 ms                                                              | 703 ms: 1.01x faster                                                  |
| pickle_list             | 2.83 us                                                             | 2.81 us: 1.00x faster                                                 |
| float                   | 53.0 ms                                                             | 52.8 ms: 1.00x faster                                                 |
| async_tree_none         | 285 ms                                                              | 283 ms: 1.00x faster                                                  |
| pickle                  | 7.17 us                                                             | 7.15 us: 1.00x faster                                                 |
| scimark_fft             | 200 ms                                                              | 200 ms: 1.00x faster                                                  |
| gc_traversal            | 2.41 ms                                                             | 2.41 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                              | 281 ms: 1.00x slower                                                  |
| create_gc_cycles        | 722 us                                                              | 724 us: 1.00x slower                                                  |
| pickle_pure_python      | 198 us                                                              | 199 us: 1.00x slower                                                  |
| telco                   | 3.40 ms                                                             | 3.41 ms: 1.00x slower                                                 |
| 2to3                    | 161 ms                                                              | 162 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.21 ms: 1.01x slower                                                 |
| mdp                     | 1.54 sec                                                            | 1.55 sec: 1.01x slower                                                |
| chaos                   | 49.4 ms                                                             | 49.7 ms: 1.01x slower                                                 |
| xml_etree_process       | 35.0 ms                                                             | 35.2 ms: 1.01x slower                                                 |
| django_template         | 21.1 ms                                                             | 21.2 ms: 1.01x slower                                                 |
| unpickle_list           | 2.63 us                                                             | 2.65 us: 1.01x slower                                                 |
| fannkuch                | 260 ms                                                              | 262 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 173 ms: 1.01x slower                                                  |
| nbody                   | 65.5 ms                                                             | 66.1 ms: 1.01x slower                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                             | 63.3 ms: 1.01x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                             | 1.93 us: 1.01x slower                                                 |
| json_dumps              | 7.59 ms                                                             | 7.68 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                              | 541 ms: 1.01x slower                                                  |
| spectral_norm           | 72.5 ms                                                             | 73.4 ms: 1.01x slower                                                 |
| richards                | 32.2 ms                                                             | 32.6 ms: 1.01x slower                                                 |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.37 ms: 1.01x slower                                                 |
| deepcopy                | 224 us                                                              | 227 us: 1.02x slower                                                  |
| json                    | 2.77 ms                                                             | 2.82 ms: 1.02x slower                                                 |
| meteor_contest          | 73.3 ms                                                             | 74.7 ms: 1.02x slower                                                 |
| dulwich_log             | 29.7 ms                                                             | 30.3 ms: 1.02x slower                                                 |
| genshi_xml              | 29.9 ms                                                             | 30.5 ms: 1.02x slower                                                 |
| unpickle                | 9.66 us                                                             | 9.87 us: 1.02x slower                                                 |
| pyflate                 | 309 ms                                                              | 316 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                             | 31.9 ms: 1.02x slower                                                 |
| pylint                  | 271 ms                                                              | 277 ms: 1.02x slower                                                  |
| logging_silent          | 68.0 ns                                                             | 69.6 ns: 1.02x slower                                                 |
| gunicorn                | 1.12 ms                                                             | 1.15 ms: 1.03x slower                                                 |
| raytrace                | 207 ms                                                              | 212 ms: 1.03x slower                                                  |
| hexiom                  | 4.73 ms                                                             | 4.88 ms: 1.03x slower                                                 |
| pycparser               | 695 ms                                                              | 717 ms: 1.03x slower                                                  |
| aiohttp                 | 1.05 ms                                                             | 1.09 ms: 1.03x slower                                                 |
| bench_thread_pool       | 474 us                                                              | 499 us: 1.05x slower                                                  |
| comprehensions          | 16.1 us                                                             | 17.5 us: 1.09x slower                                                 |
| crypto_pyaes            | 51.8 ms                                                             | 56.5 ms: 1.09x slower                                                 |
| regex_dna               | 151 ms                                                              | 171 ms: 1.13x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                             | 1.33 ms: 1.19x slower                                                 |
| sqlglot_parse           | 956 us                                                              | 1.17 ms: 1.22x slower                                                 |
| regex_v8                | 16.1 ms                                                             | 19.8 ms: 1.23x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (8): bench_mp_pool, chameleon, scimark_lu, xml_etree_generate, thrift, mypy2, flaskblogging, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage
