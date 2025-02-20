
# Results vs. 3.11.0

- fork: brandtbucher
- ref: fold_slices
- machine: linux-x86_64
- commit hash: 39619f9
- commit date: 2023-04-06
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 250 ms: 1.03x faster                                                |
| chameleon      | 6.52 ms                                                             | 6.49 ms: 1.00x faster                                               |
| docutils       | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                              |
| html5lib       | 64.0 ms                                                             | 61.2 ms: 1.05x faster                                               |
| tornado_http   | 96.7 ms                                                             | 90.9 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 86.6 ms: 1.12x faster                                               |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                |
| float          | 76.0 ms                                                             | 73.6 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                               | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 134 ms: 1.02x faster                                                |
| regex_v8       | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                               |
| regex_effbot   | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                               |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                               | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.53 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                |
| json_loads           | 26.2 us                                                             | 24.1 us: 1.09x faster                                               |
| xml_etree_parse      | 162 ms                                                              | 150 ms: 1.08x faster                                                |
| pickle_pure_python   | 307 us                                                              | 290 us: 1.06x faster                                                |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.05x faster                                                |
| unpickle             | 13.2 us                                                             | 13.5 us: 1.02x slower                                               |
| xml_etree_process    | 54.1 ms                                                             | 56.2 ms: 1.04x slower                                               |
| pickle_dict          | 30.9 us                                                             | 32.6 us: 1.05x slower                                               |
| xml_etree_generate   | 76.5 ms                                                             | 80.9 ms: 1.06x slower                                               |
| pickle_list          | 4.03 us                                                             | 4.35 us: 1.08x slower                                               |
| pickle               | 9.79 us                                                             | 10.9 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                               | 1.02x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                               |
| python_startup_no_site | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.6 ms: 1.09x faster                                               |
| genshi_text     | 21.8 ms                                                             | 21.0 ms: 1.04x faster                                               |
| django_template | 32.9 ms                                                             | 33.4 ms: 1.02x slower                                               |
| mako            | 9.82 ms                                                             | 10.1 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.2 ms: 2.52x faster                                               |
| asyncio_tcp             | 888 ms                                                              | 500 ms: 1.77x faster                                                |
| json_dumps              | 12.5 ms                                                             | 9.53 ms: 1.32x faster                                               |
| mypy2                   | 422 ms                                                              | 335 ms: 1.26x faster                                                |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                |
| unpack_sequence         | 49.5 ns                                                             | 43.9 ns: 1.13x faster                                               |
| nbody                   | 96.7 ms                                                             | 86.6 ms: 1.12x faster                                               |
| sqlglot_parse           | 1.36 ms                                                             | 1.23 ms: 1.11x faster                                               |
| coroutines              | 26.3 ms                                                             | 23.7 ms: 1.11x faster                                               |
| deltablue               | 3.66 ms                                                             | 3.30 ms: 1.11x faster                                               |
| sqlglot_transpile       | 1.65 ms                                                             | 1.50 ms: 1.10x faster                                               |
| genshi_xml              | 51.8 ms                                                             | 47.6 ms: 1.09x faster                                               |
| json_loads              | 26.2 us                                                             | 24.1 us: 1.09x faster                                               |
| hexiom                  | 6.48 ms                                                             | 5.98 ms: 1.08x faster                                               |
| xml_etree_parse         | 162 ms                                                              | 150 ms: 1.08x faster                                                |
| richards                | 45.7 ms                                                             | 42.5 ms: 1.08x faster                                               |
| tornado_http            | 96.7 ms                                                             | 90.9 ms: 1.06x faster                                               |
| deepcopy_memo           | 36.4 us                                                             | 34.2 us: 1.06x faster                                               |
| logging_simple          | 6.09 us                                                             | 5.74 us: 1.06x faster                                               |
| pickle_pure_python      | 307 us                                                              | 290 us: 1.06x faster                                                |
| scimark_fft             | 328 ms                                                              | 311 ms: 1.05x faster                                                |
| mdp                     | 2.64 sec                                                            | 2.51 sec: 1.05x faster                                              |
| json                    | 4.86 ms                                                             | 4.63 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                               |
| sqlglot_optimize        | 53.4 ms                                                             | 51.0 ms: 1.05x faster                                               |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                |
| html5lib                | 64.0 ms                                                             | 61.2 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.05x faster                                                |
| coverage                | 101 ms                                                              | 96.7 ms: 1.05x faster                                               |
| meteor_contest          | 106 ms                                                              | 102 ms: 1.04x faster                                                |
| logging_format          | 6.64 us                                                             | 6.36 us: 1.04x faster                                               |
| telco                   | 6.59 ms                                                             | 6.32 ms: 1.04x faster                                               |
| deepcopy                | 339 us                                                              | 326 us: 1.04x faster                                                |
| genshi_text             | 21.8 ms                                                             | 21.0 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.31 ms: 1.04x faster                                               |
| comprehensions          | 22.2 us                                                             | 21.4 us: 1.04x faster                                               |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.04x faster                                               |
| nqueens                 | 84.0 ms                                                             | 81.0 ms: 1.04x faster                                               |
| sqlglot_normalize       | 108 ms                                                              | 105 ms: 1.04x faster                                                |
| bench_thread_pool       | 820 us                                                              | 791 us: 1.04x faster                                                |
| spectral_norm           | 99.5 ms                                                             | 96.1 ms: 1.04x faster                                               |
| float                   | 76.0 ms                                                             | 73.6 ms: 1.03x faster                                               |
| chaos                   | 68.0 ms                                                             | 65.9 ms: 1.03x faster                                               |
| go                      | 138 ms                                                              | 134 ms: 1.03x faster                                                |
| 2to3                    | 257 ms                                                              | 250 ms: 1.03x faster                                                |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                               |
| raytrace                | 292 ms                                                              | 285 ms: 1.03x faster                                                |
| sympy_str               | 291 ms                                                              | 285 ms: 1.02x faster                                                |
| regex_compile           | 137 ms                                                              | 134 ms: 1.02x faster                                                |
| sympy_expand            | 477 ms                                                              | 467 ms: 1.02x faster                                                |
| pprint_pformat          | 1.45 sec                                                            | 1.42 sec: 1.02x faster                                              |
| scimark_sor             | 115 ms                                                              | 112 ms: 1.02x faster                                                |
| async_tree_none         | 525 ms                                                              | 515 ms: 1.02x faster                                                |
| docutils                | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                              |
| pprint_safe_repr        | 701 ms                                                              | 690 ms: 1.02x faster                                                |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                |
| logging_silent          | 98.7 ns                                                             | 97.7 ns: 1.01x faster                                               |
| fannkuch                | 384 ms                                                              | 380 ms: 1.01x faster                                                |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                |
| dulwich_log             | 63.6 ms                                                             | 63.3 ms: 1.01x faster                                               |
| chameleon               | 6.52 ms                                                             | 6.49 ms: 1.00x faster                                               |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.01x slower                                              |
| deepcopy_reduce         | 2.96 us                                                             | 2.99 us: 1.01x slower                                               |
| django_template         | 32.9 ms                                                             | 33.4 ms: 1.02x slower                                               |
| thrift                  | 766 us                                                              | 780 us: 1.02x slower                                                |
| regex_v8                | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                               |
| scimark_lu              | 108 ms                                                              | 111 ms: 1.02x slower                                                |
| unpickle                | 13.2 us                                                             | 13.5 us: 1.02x slower                                               |
| create_gc_cycles        | 1.48 ms                                                             | 1.51 ms: 1.02x slower                                               |
| mako                    | 9.82 ms                                                             | 10.1 ms: 1.03x slower                                               |
| xml_etree_process       | 54.1 ms                                                             | 56.2 ms: 1.04x slower                                               |
| regex_effbot            | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                               |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                                |
| python_startup          | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                               |
| sqlite_synth            | 2.51 us                                                             | 2.63 us: 1.05x slower                                               |
| pickle_dict             | 30.9 us                                                             | 32.6 us: 1.05x slower                                               |
| xml_etree_generate      | 76.5 ms                                                             | 80.9 ms: 1.06x slower                                               |
| pickle_list             | 4.03 us                                                             | 4.35 us: 1.08x slower                                               |
| python_startup_no_site  | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                               |
| pickle                  | 9.79 us                                                             | 10.9 us: 1.11x slower                                               |
| async_generators        | 361 ms                                                              | 408 ms: 1.13x slower                                                |
| gc_traversal            | 3.63 ms                                                             | 4.10 ms: 1.13x slower                                               |
| dask                    | 368 ms                                                              | 507 ms: 1.38x slower                                                |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                        |

Benchmark hidden because not significant (11): unpickle_list, sqlalchemy_imperative, crypto_pyaes, pathlib, async_tree_io, bench_mp_pool, async_tree_cpu_io_mixed, pyflate, djangocms, async_tree_memoization, scimark_monte_carlo
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
