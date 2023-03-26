
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 168 ms: 1.04x slower                                   |
| chameleon      | 4.55 ms                                                             | 4.51 ms: 1.01x faster                                  |
| docutils       | 1.47 sec                                                            | 1.51 sec: 1.03x slower                                 |
| html5lib       | 34.8 ms                                                             | 36.7 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                               | 1.02x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 60.6 ms: 1.08x faster                                  |
| pidigits       | 281 ms                                                              | 280 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                               | 1.03x faster                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                             | 16.1 ms: 1.00x faster                                  |
| regex_dna      | 151 ms                                                              | 152 ms: 1.00x slower                                   |
| regex_compile  | 76.6 ms                                                             | 77.0 ms: 1.01x slower                                  |
| regex_effbot   | 2.63 ms                                                             | 2.71 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.24 ms: 1.22x faster                                  |
| xml_etree_parse      | 106 ms                                                              | 97.8 ms: 1.08x faster                                  |
| unpickle_pure_python | 158 us                                                              | 151 us: 1.05x faster                                   |
| pickle_pure_python   | 198 us                                                              | 194 us: 1.02x faster                                   |
| pickle_dict          | 17.9 us                                                             | 18.0 us: 1.01x slower                                  |
| pickle_list          | 2.83 us                                                             | 2.87 us: 1.02x slower                                  |
| json_loads           | 16.0 us                                                             | 16.3 us: 1.02x slower                                  |
| unpickle_list        | 2.63 us                                                             | 2.68 us: 1.02x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                             | 70.7 ms: 1.02x slower                                  |
| pickle               | 7.17 us                                                             | 7.45 us: 1.04x slower                                  |
| xml_etree_process    | 35.0 ms                                                             | 37.0 ms: 1.06x slower                                  |
| xml_etree_generate   | 48.2 ms                                                             | 52.0 ms: 1.08x slower                                  |
| Geometric mean       | (ref)                                                               | 1.01x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                             | 10.3 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                               | 1.01x slower                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 7.40 ms: 1.14x faster                                  |
| genshi_text     | 15.3 ms                                                             | 14.9 ms: 1.03x faster                                  |
| genshi_xml      | 29.9 ms                                                             | 29.4 ms: 1.02x faster                                  |
| django_template | 21.1 ms                                                             | 21.9 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                               | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                              | 462 ms: 1.41x faster                                   |
| json_dumps              | 7.59 ms                                                             | 6.24 ms: 1.22x faster                                  |
| mako                    | 8.42 ms                                                             | 7.40 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 2.84 ms: 1.13x faster                                  |
| xml_etree_parse         | 106 ms                                                              | 97.8 ms: 1.08x faster                                  |
| nbody                   | 65.5 ms                                                             | 60.6 ms: 1.08x faster                                  |
| deltablue               | 2.81 ms                                                             | 2.62 ms: 1.07x faster                                  |
| hexiom                  | 4.73 ms                                                             | 4.42 ms: 1.07x faster                                  |
| scimark_fft             | 200 ms                                                              | 189 ms: 1.06x faster                                   |
| generators              | 28.6 ms                                                             | 27.1 ms: 1.05x faster                                  |
| unpickle_pure_python    | 158 us                                                              | 151 us: 1.05x faster                                   |
| chaos                   | 49.4 ms                                                             | 47.2 ms: 1.05x faster                                  |
| async_tree_memoization  | 338 ms                                                              | 326 ms: 1.04x faster                                   |
| genshi_text             | 15.3 ms                                                             | 14.9 ms: 1.03x faster                                  |
| richards                | 32.2 ms                                                             | 31.5 ms: 1.02x faster                                  |
| pycparser               | 695 ms                                                              | 680 ms: 1.02x faster                                   |
| pickle_pure_python      | 198 us                                                              | 194 us: 1.02x faster                                   |
| logging_silent          | 68.0 ns                                                             | 66.6 ns: 1.02x faster                                  |
| create_gc_cycles        | 722 us                                                              | 710 us: 1.02x faster                                   |
| genshi_xml              | 29.9 ms                                                             | 29.4 ms: 1.02x faster                                  |
| deepcopy_memo           | 26.3 us                                                             | 26.0 us: 1.01x faster                                  |
| scimark_lu              | 72.2 ms                                                             | 71.4 ms: 1.01x faster                                  |
| chameleon               | 4.55 ms                                                             | 4.51 ms: 1.01x faster                                  |
| unpack_sequence         | 33.5 ns                                                             | 33.3 ns: 1.01x faster                                  |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.23 ms: 1.00x faster                                  |
| regex_v8                | 16.1 ms                                                             | 16.1 ms: 1.00x faster                                  |
| pidigits                | 281 ms                                                              | 280 ms: 1.00x faster                                   |
| mdp                     | 1.54 sec                                                            | 1.54 sec: 1.00x faster                                 |
| bench_thread_pool       | 474 us                                                              | 475 us: 1.00x slower                                   |
| deepcopy                | 224 us                                                              | 224 us: 1.00x slower                                   |
| regex_dna               | 151 ms                                                              | 152 ms: 1.00x slower                                   |
| regex_compile           | 76.6 ms                                                             | 77.0 ms: 1.01x slower                                  |
| meteor_contest          | 73.3 ms                                                             | 73.8 ms: 1.01x slower                                  |
| gc_traversal            | 2.41 ms                                                             | 2.43 ms: 1.01x slower                                  |
| spectral_norm           | 72.5 ms                                                             | 73.1 ms: 1.01x slower                                  |
| pickle_dict             | 17.9 us                                                             | 18.0 us: 1.01x slower                                  |
| json                    | 2.77 ms                                                             | 2.81 ms: 1.01x slower                                  |
| dulwich_log             | 29.7 ms                                                             | 30.2 ms: 1.02x slower                                  |
| pickle_list             | 2.83 us                                                             | 2.87 us: 1.02x slower                                  |
| json_loads              | 16.0 us                                                             | 16.3 us: 1.02x slower                                  |
| unpickle_list           | 2.63 us                                                             | 2.68 us: 1.02x slower                                  |
| async_tree_none         | 285 ms                                                              | 290 ms: 1.02x slower                                   |
| telco                   | 3.40 ms                                                             | 3.46 ms: 1.02x slower                                  |
| xml_etree_iterparse     | 69.2 ms                                                             | 70.7 ms: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                              | 546 ms: 1.02x slower                                   |
| python_startup_no_site  | 10.1 ms                                                             | 10.3 ms: 1.02x slower                                  |
| sympy_integrate         | 11.5 ms                                                             | 11.8 ms: 1.02x slower                                  |
| docutils                | 1.47 sec                                                            | 1.51 sec: 1.03x slower                                 |
| sympy_expand            | 243 ms                                                              | 250 ms: 1.03x slower                                   |
| sympy_str               | 151 ms                                                              | 156 ms: 1.03x slower                                   |
| deepcopy_reduce         | 1.91 us                                                             | 1.97 us: 1.03x slower                                  |
| sympy_sum               | 86.0 ms                                                             | 88.6 ms: 1.03x slower                                  |
| sqlglot_normalize       | 171 ms                                                              | 177 ms: 1.03x slower                                   |
| regex_effbot            | 2.63 ms                                                             | 2.71 ms: 1.03x slower                                  |
| sqlalchemy_declarative  | 62.6 ms                                                             | 64.6 ms: 1.03x slower                                  |
| pprint_pformat          | 946 ms                                                              | 980 ms: 1.04x slower                                   |
| pprint_safe_repr        | 463 ms                                                              | 480 ms: 1.04x slower                                   |
| django_template         | 21.1 ms                                                             | 21.9 ms: 1.04x slower                                  |
| pickle                  | 7.17 us                                                             | 7.45 us: 1.04x slower                                  |
| sqlglot_optimize        | 31.2 ms                                                             | 32.4 ms: 1.04x slower                                  |
| fannkuch                | 260 ms                                                              | 271 ms: 1.04x slower                                   |
| coverage                | 58.4 ms                                                             | 60.8 ms: 1.04x slower                                  |
| 2to3                    | 161 ms                                                              | 168 ms: 1.04x slower                                   |
| async_tree_io           | 707 ms                                                              | 740 ms: 1.05x slower                                   |
| html5lib                | 34.8 ms                                                             | 36.7 ms: 1.05x slower                                  |
| bench_mp_pool           | 43.8 ms                                                             | 46.2 ms: 1.06x slower                                  |
| crypto_pyaes            | 51.8 ms                                                             | 54.8 ms: 1.06x slower                                  |
| logging_simple          | 3.49 us                                                             | 3.69 us: 1.06x slower                                  |
| xml_etree_process       | 35.0 ms                                                             | 37.0 ms: 1.06x slower                                  |
| sqlite_synth            | 1.28 us                                                             | 1.36 us: 1.06x slower                                  |
| logging_format          | 3.77 us                                                             | 3.99 us: 1.06x slower                                  |
| go                      | 109 ms                                                              | 116 ms: 1.06x slower                                   |
| coroutines              | 17.7 ms                                                             | 18.8 ms: 1.06x slower                                  |
| scimark_sor             | 82.9 ms                                                             | 88.0 ms: 1.06x slower                                  |
| thrift                  | 431 us                                                              | 460 us: 1.07x slower                                   |
| raytrace                | 207 ms                                                              | 222 ms: 1.07x slower                                   |
| xml_etree_generate      | 48.2 ms                                                             | 52.0 ms: 1.08x slower                                  |
| comprehensions          | 16.1 us                                                             | 17.8 us: 1.11x slower                                  |
| pyflate                 | 309 ms                                                              | 343 ms: 1.11x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                             | 1.25 ms: 1.11x slower                                  |
| sqlglot_parse           | 956 us                                                              | 1.07 ms: 1.12x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                             | 52.1 ms: 1.12x slower                                  |
| async_generators        | 195 ms                                                              | 267 ms: 1.37x slower                                   |
| dask                    | 226 ms                                                              | 327 ms: 1.45x slower                                   |
| Geometric mean          | (ref)                                                               | 1.02x slower                                           |

Benchmark hidden because not significant (7): tornado_http, pathlib, python_startup, float, unpickle, nqueens, mypy2
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint