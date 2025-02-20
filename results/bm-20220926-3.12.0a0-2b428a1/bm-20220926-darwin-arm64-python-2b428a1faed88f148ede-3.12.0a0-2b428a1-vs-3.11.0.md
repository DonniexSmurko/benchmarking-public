
# Results vs. 3.11.0

- fork: python
- ref: 2b428a1faed88f148ede
- machine: darwin-arm64
- commit hash: 2b428a1
- commit date: 2022-09-26
- overall geometric mean: 1.01x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.67 ms: 1.02x slower                                                 |
| docutils       | 1.47 sec                                               | 1.47 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.8 ms: 1.01x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 56.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| regex_v8       | 16.2 ms                                                | 16.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.09 ms: 1.27x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.6 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 65.2 ms: 1.06x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.54 us: 1.04x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 47.6 ms: 1.03x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 35.0 ms: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 205 us: 1.03x slower                                                  |
| pickle               | 7.17 us                                                | 7.55 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.15 ms: 1.30x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.08 ms: 1.27x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.16 ms: 1.04x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.2 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.6 ms: 1.35x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.15 ms: 1.30x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.08 ms: 1.27x faster                                                 |
| json_dumps              | 7.72 ms                                                | 6.09 ms: 1.27x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.83 ms: 1.13x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.6 ms: 1.10x faster                                                 |
| coverage                | 58.6 ms                                                | 53.7 ms: 1.09x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.22 ms: 1.09x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 65.2 ms: 1.06x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 41.2 ms: 1.05x faster                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.00 ms: 1.04x faster                                                 |
| mako                    | 8.49 ms                                                | 8.16 ms: 1.04x faster                                                 |
| bench_thread_pool       | 473 us                                                 | 455 us: 1.04x faster                                                  |
| unpickle_list           | 2.63 us                                                | 2.54 us: 1.04x faster                                                 |
| dulwich_log             | 29.9 ms                                                | 29.1 ms: 1.03x faster                                                 |
| logging_silent          | 68.0 ns                                                | 66.2 ns: 1.03x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 47.6 ms: 1.03x faster                                                 |
| pylint                  | 271 ms                                                 | 264 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 61.3 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| mdp                     | 1.54 sec                                               | 1.52 sec: 1.01x faster                                                |
| telco                   | 3.39 ms                                                | 3.36 ms: 1.01x faster                                                 |
| nbody                   | 65.5 ms                                                | 64.8 ms: 1.01x faster                                                 |
| xml_etree_process       | 35.2 ms                                                | 35.0 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 532 ms: 1.00x faster                                                  |
| scimark_fft             | 199 ms                                                 | 199 ms: 1.00x faster                                                  |
| crypto_pyaes            | 51.7 ms                                                | 51.8 ms: 1.00x slower                                                 |
| docutils                | 1.47 sec                                               | 1.47 sec: 1.00x slower                                                |
| scimark_lu              | 72.1 ms                                                | 72.3 ms: 1.00x slower                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| regex_v8                | 16.2 ms                                                | 16.3 ms: 1.01x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.83 ms: 1.01x slower                                                 |
| sympy_str               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.2 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                 |
| json                    | 2.77 ms                                                | 2.81 ms: 1.01x slower                                                 |
| unpack_sequence         | 33.6 ns                                                | 34.1 ns: 1.02x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| thrift                  | 433 us                                                 | 442 us: 1.02x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.67 ms: 1.02x slower                                                 |
| sympy_expand            | 243 ms                                                 | 248 ms: 1.02x slower                                                  |
| pycparser               | 697 ms                                                 | 713 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.9 ms: 1.02x slower                                                 |
| async_generators        | 195 ms                                                 | 200 ms: 1.03x slower                                                  |
| chaos                   | 49.5 ms                                                | 50.9 ms: 1.03x slower                                                 |
| pickle_pure_python      | 199 us                                                 | 205 us: 1.03x slower                                                  |
| richards                | 32.2 ms                                                | 33.2 ms: 1.03x slower                                                 |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| raytrace                | 207 ms                                                 | 214 ms: 1.03x slower                                                  |
| fannkuch                | 261 ms                                                 | 270 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| hexiom                  | 4.73 ms                                                | 4.92 ms: 1.04x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| async_tree_io           | 706 ms                                                 | 736 ms: 1.04x slower                                                  |
| sqlglot_parse           | 957 us                                                 | 1000 us: 1.04x slower                                                 |
| logging_format          | 3.78 us                                                | 3.95 us: 1.05x slower                                                 |
| logging_simple          | 3.50 us                                                | 3.67 us: 1.05x slower                                                 |
| pickle                  | 7.17 us                                                | 7.55 us: 1.05x slower                                                 |
| pprint_pformat          | 950 ms                                                 | 1.00 sec: 1.06x slower                                                |
| meteor_contest          | 73.8 ms                                                | 78.2 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 495 ms: 1.07x slower                                                  |
| float                   | 53.0 ms                                                | 56.5 ms: 1.07x slower                                                 |
| deepcopy                | 224 us                                                 | 241 us: 1.08x slower                                                  |
| go                      | 109 ms                                                 | 118 ms: 1.08x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.08 us: 1.09x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.7 us: 1.09x slower                                                 |
| coroutines              | 17.7 ms                                                | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 311 ms                                                 | 351 ms: 1.13x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 383 ms: 1.14x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.46 us: 1.15x slower                                                 |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 54.3 ms: 1.17x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 102 ms: 1.22x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (8): tornado_http, nqueens, sympy_sum, async_tree_none, regex_dna, regex_effbot, spectral_norm, unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220926-3.12.0a0-2b428a1/bm-20220926-darwin-arm64-python-2b428a1faed88f148ede-3.12.0a0-2b428a1.json: mypy
