
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: darwin-arm64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 166 ms: 1.03x slower                                                  |
| chameleon      | 4.55 ms                                                             | 5.09 ms: 1.12x slower                                                 |
| docutils       | 1.47 sec                                                            | 1.54 sec: 1.05x slower                                                |
| html5lib       | 34.8 ms                                                             | 36.7 ms: 1.05x slower                                                 |
| tornado_http   | 71.5 ms                                                             | 76.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                               | 1.06x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                             | 52.0 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                              | 281 ms: 1.00x slower                                                  |
| nbody          | 65.5 ms                                                             | 74.3 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.45 ms: 1.07x faster                                                 |
| regex_compile  | 76.6 ms                                                             | 78.0 ms: 1.02x slower                                                 |
| regex_dna      | 151 ms                                                              | 162 ms: 1.07x slower                                                  |
| regex_v8       | 16.1 ms                                                             | 17.5 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 2.63 us                                                             | 2.52 us: 1.04x faster                                                 |
| xml_etree_parse      | 106 ms                                                              | 101 ms: 1.04x faster                                                  |
| pickle_dict          | 17.9 us                                                             | 17.6 us: 1.01x faster                                                 |
| pickle_list          | 2.83 us                                                             | 2.82 us: 1.00x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                             | 69.8 ms: 1.01x slower                                                 |
| pickle               | 7.17 us                                                             | 7.26 us: 1.01x slower                                                 |
| xml_etree_generate   | 48.2 ms                                                             | 48.8 ms: 1.01x slower                                                 |
| json_loads           | 16.0 us                                                             | 16.6 us: 1.03x slower                                                 |
| json_dumps           | 7.59 ms                                                             | 7.85 ms: 1.04x slower                                                 |
| unpickle             | 9.66 us                                                             | 10.1 us: 1.04x slower                                                 |
| xml_etree_process    | 35.0 ms                                                             | 36.9 ms: 1.06x slower                                                 |
| unpickle_pure_python | 158 us                                                              | 176 us: 1.11x slower                                                  |
| pickle_pure_python   | 198 us                                                              | 229 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                             | 9.29 ms: 1.08x faster                                                 |
| python_startup         | 12.3 ms                                                             | 15.9 ms: 1.29x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 8.55 ms: 1.02x slower                                                 |
| genshi_text     | 15.3 ms                                                             | 15.7 ms: 1.02x slower                                                 |
| genshi_xml      | 29.9 ms                                                             | 30.9 ms: 1.03x slower                                                 |
| django_template | 21.1 ms                                                             | 22.7 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 58.4 ms                                                             | 43.4 ms: 1.34x faster                                                 |
| python_startup_no_site  | 10.1 ms                                                             | 9.29 ms: 1.08x faster                                                 |
| unpack_sequence         | 33.5 ns                                                             | 31.3 ns: 1.07x faster                                                 |
| regex_effbot            | 2.63 ms                                                             | 2.45 ms: 1.07x faster                                                 |
| pathlib                 | 28.3 ms                                                             | 26.5 ms: 1.07x faster                                                 |
| unpickle_list           | 2.63 us                                                             | 2.52 us: 1.04x faster                                                 |
| xml_etree_parse         | 106 ms                                                              | 101 ms: 1.04x faster                                                  |
| bench_mp_pool           | 43.8 ms                                                             | 42.0 ms: 1.04x faster                                                 |
| float                   | 53.0 ms                                                             | 52.0 ms: 1.02x faster                                                 |
| pickle_dict             | 17.9 us                                                             | 17.6 us: 1.01x faster                                                 |
| logging_format          | 3.77 us                                                             | 3.73 us: 1.01x faster                                                 |
| logging_simple          | 3.49 us                                                             | 3.47 us: 1.01x faster                                                 |
| generators              | 28.6 ms                                                             | 28.5 ms: 1.00x faster                                                 |
| pickle_list             | 2.83 us                                                             | 2.82 us: 1.00x faster                                                 |
| chaos                   | 49.4 ms                                                             | 49.2 ms: 1.00x faster                                                 |
| pidigits                | 281 ms                                                              | 281 ms: 1.00x slower                                                  |
| sympy_sum               | 86.0 ms                                                             | 86.3 ms: 1.00x slower                                                 |
| gc_traversal            | 2.41 ms                                                             | 2.43 ms: 1.01x slower                                                 |
| scimark_fft             | 200 ms                                                              | 201 ms: 1.01x slower                                                  |
| xml_etree_iterparse     | 69.2 ms                                                             | 69.8 ms: 1.01x slower                                                 |
| raytrace                | 207 ms                                                              | 209 ms: 1.01x slower                                                  |
| meteor_contest          | 73.3 ms                                                             | 74.2 ms: 1.01x slower                                                 |
| pickle                  | 7.17 us                                                             | 7.26 us: 1.01x slower                                                 |
| xml_etree_generate      | 48.2 ms                                                             | 48.8 ms: 1.01x slower                                                 |
| async_generators        | 195 ms                                                              | 198 ms: 1.01x slower                                                  |
| mako                    | 8.42 ms                                                             | 8.55 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.25 ms: 1.02x slower                                                 |
| create_gc_cycles        | 722 us                                                              | 735 us: 1.02x slower                                                  |
| regex_compile           | 76.6 ms                                                             | 78.0 ms: 1.02x slower                                                 |
| mdp                     | 1.54 sec                                                            | 1.57 sec: 1.02x slower                                                |
| sqlglot_normalize       | 171 ms                                                              | 175 ms: 1.02x slower                                                  |
| genshi_text             | 15.3 ms                                                             | 15.7 ms: 1.02x slower                                                 |
| flaskblogging           | 2.42 ms                                                             | 2.49 ms: 1.03x slower                                                 |
| 2to3                    | 161 ms                                                              | 166 ms: 1.03x slower                                                  |
| async_tree_none         | 285 ms                                                              | 294 ms: 1.03x slower                                                  |
| genshi_xml              | 29.9 ms                                                             | 30.9 ms: 1.03x slower                                                 |
| json_loads              | 16.0 us                                                             | 16.6 us: 1.03x slower                                                 |
| json_dumps              | 7.59 ms                                                             | 7.85 ms: 1.04x slower                                                 |
| spectral_norm           | 72.5 ms                                                             | 75.1 ms: 1.04x slower                                                 |
| unpickle                | 9.66 us                                                             | 10.1 us: 1.04x slower                                                 |
| hexiom                  | 4.73 ms                                                             | 4.93 ms: 1.04x slower                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                             | 65.3 ms: 1.04x slower                                                 |
| pylint                  | 271 ms                                                              | 283 ms: 1.04x slower                                                  |
| sympy_str               | 151 ms                                                              | 158 ms: 1.05x slower                                                  |
| docutils                | 1.47 sec                                                            | 1.54 sec: 1.05x slower                                                |
| sympy_expand            | 243 ms                                                              | 256 ms: 1.05x slower                                                  |
| html5lib                | 34.8 ms                                                             | 36.7 ms: 1.05x slower                                                 |
| dulwich_log             | 29.7 ms                                                             | 31.3 ms: 1.05x slower                                                 |
| xml_etree_process       | 35.0 ms                                                             | 36.9 ms: 1.06x slower                                                 |
| sympy_integrate         | 11.5 ms                                                             | 12.1 ms: 1.06x slower                                                 |
| deepcopy_memo           | 26.3 us                                                             | 27.8 us: 1.06x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                             | 49.2 ms: 1.06x slower                                                 |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.69 ms: 1.06x slower                                                 |
| deepcopy                | 224 us                                                              | 239 us: 1.07x slower                                                  |
| regex_dna               | 151 ms                                                              | 162 ms: 1.07x slower                                                  |
| tornado_http            | 71.5 ms                                                             | 76.5 ms: 1.07x slower                                                 |
| sqlite_synth            | 1.28 us                                                             | 1.38 us: 1.07x slower                                                 |
| fannkuch                | 260 ms                                                              | 279 ms: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.05 us: 1.07x slower                                                 |
| json                    | 2.77 ms                                                             | 2.98 ms: 1.07x slower                                                 |
| django_template         | 21.1 ms                                                             | 22.7 ms: 1.08x slower                                                 |
| pprint_safe_repr        | 463 ms                                                              | 499 ms: 1.08x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                             | 33.6 ms: 1.08x slower                                                 |
| pprint_pformat          | 946 ms                                                              | 1.02 sec: 1.08x slower                                                |
| thrift                  | 431 us                                                              | 467 us: 1.08x slower                                                  |
| async_tree_memoization  | 338 ms                                                              | 367 ms: 1.09x slower                                                  |
| coroutines              | 17.7 ms                                                             | 19.3 ms: 1.09x slower                                                 |
| bench_thread_pool       | 474 us                                                              | 516 us: 1.09x slower                                                  |
| comprehensions          | 16.1 us                                                             | 17.5 us: 1.09x slower                                                 |
| regex_v8                | 16.1 ms                                                             | 17.5 ms: 1.09x slower                                                 |
| go                      | 109 ms                                                              | 119 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                              | 587 ms: 1.10x slower                                                  |
| pycparser               | 695 ms                                                              | 767 ms: 1.10x slower                                                  |
| unpickle_pure_python    | 158 us                                                              | 176 us: 1.11x slower                                                  |
| chameleon               | 4.55 ms                                                             | 5.09 ms: 1.12x slower                                                 |
| async_tree_io           | 707 ms                                                              | 794 ms: 1.12x slower                                                  |
| crypto_pyaes            | 51.8 ms                                                             | 58.2 ms: 1.12x slower                                                 |
| nbody                   | 65.5 ms                                                             | 74.3 ms: 1.14x slower                                                 |
| deltablue               | 2.81 ms                                                             | 3.23 ms: 1.15x slower                                                 |
| pickle_pure_python      | 198 us                                                              | 229 us: 1.15x slower                                                  |
| pyflate                 | 309 ms                                                              | 360 ms: 1.16x slower                                                  |
| richards                | 32.2 ms                                                             | 37.7 ms: 1.17x slower                                                 |
| scimark_sor             | 82.9 ms                                                             | 99.5 ms: 1.20x slower                                                 |
| logging_silent          | 68.0 ns                                                             | 82.2 ns: 1.21x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                             | 1.41 ms: 1.26x slower                                                 |
| dask                    | 226 ms                                                              | 290 ms: 1.28x slower                                                  |
| python_startup          | 12.3 ms                                                             | 15.9 ms: 1.29x slower                                                 |
| sqlglot_parse           | 956 us                                                              | 1.24 ms: 1.30x slower                                                 |
| scimark_lu              | 72.2 ms                                                             | 93.8 ms: 1.30x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.05x slower                                                          |

Benchmark hidden because not significant (3): nqueens, telco, gunicorn
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, asyncio_tcp, mypy2
