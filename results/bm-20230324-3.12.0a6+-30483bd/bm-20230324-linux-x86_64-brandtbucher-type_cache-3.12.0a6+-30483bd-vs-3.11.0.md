
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 30483bd
- commit date: 2023-03-24
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 253 ms: 1.02x faster                                               |
| docutils       | 2.59 sec                                                            | 2.55 sec: 1.01x faster                                             |
| html5lib       | 64.0 ms                                                             | 61.4 ms: 1.04x faster                                              |
| tornado_http   | 96.7 ms                                                             | 92.2 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                               | 1.02x faster                                                       |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.6 ms: 1.10x faster                                              |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                               |
| float          | 76.0 ms                                                             | 73.6 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                               | 1.06x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                               |
| regex_v8       | 22.0 ms                                                             | 22.5 ms: 1.02x slower                                              |
| regex_dna      | 196 ms                                                              | 208 ms: 1.06x slower                                               |
| regex_effbot   | 3.32 ms                                                             | 3.53 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                               | 1.03x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.86 ms: 1.27x faster                                              |
| unpickle_pure_python | 228 us                                                              | 204 us: 1.12x faster                                               |
| json_loads           | 26.2 us                                                             | 24.0 us: 1.09x faster                                              |
| xml_etree_parse      | 162 ms                                                              | 151 ms: 1.07x faster                                               |
| pickle_pure_python   | 307 us                                                              | 290 us: 1.06x faster                                               |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.03x faster                                               |
| pickle_list          | 4.03 us                                                             | 4.10 us: 1.02x slower                                              |
| unpickle_list        | 4.96 us                                                             | 5.12 us: 1.03x slower                                              |
| xml_etree_process    | 54.1 ms                                                             | 56.4 ms: 1.04x slower                                              |
| pickle_dict          | 30.9 us                                                             | 32.3 us: 1.04x slower                                              |
| pickle               | 9.79 us                                                             | 10.3 us: 1.05x slower                                              |
| xml_etree_generate   | 76.5 ms                                                             | 81.4 ms: 1.06x slower                                              |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.85 ms: 1.04x slower                                              |
| python_startup_no_site | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                              |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 48.2 ms: 1.07x faster                                              |
| mako            | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                              |
| django_template | 32.9 ms                                                             | 33.5 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.4 ms: 2.50x faster                                              |
| asyncio_tcp             | 888 ms                                                              | 510 ms: 1.74x faster                                               |
| json_dumps              | 12.5 ms                                                             | 9.86 ms: 1.27x faster                                              |
| mypy2                   | 422 ms                                                              | 336 ms: 1.25x faster                                               |
| coroutines              | 26.3 ms                                                             | 22.9 ms: 1.15x faster                                              |
| unpickle_pure_python    | 228 us                                                              | 204 us: 1.12x faster                                               |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.03 ms: 1.11x faster                                              |
| deltablue               | 3.66 ms                                                             | 3.31 ms: 1.10x faster                                              |
| nbody                   | 96.7 ms                                                             | 87.6 ms: 1.10x faster                                              |
| unpack_sequence         | 49.5 ns                                                             | 45.2 ns: 1.09x faster                                              |
| scimark_fft             | 328 ms                                                              | 300 ms: 1.09x faster                                               |
| json_loads              | 26.2 us                                                             | 24.0 us: 1.09x faster                                              |
| spectral_norm           | 99.5 ms                                                             | 91.5 ms: 1.09x faster                                              |
| genshi_xml              | 51.8 ms                                                             | 48.2 ms: 1.07x faster                                              |
| xml_etree_parse         | 162 ms                                                              | 151 ms: 1.07x faster                                               |
| scimark_sor             | 115 ms                                                              | 108 ms: 1.06x faster                                               |
| richards                | 45.7 ms                                                             | 43.0 ms: 1.06x faster                                              |
| deepcopy_memo           | 36.4 us                                                             | 34.2 us: 1.06x faster                                              |
| hexiom                  | 6.48 ms                                                             | 6.10 ms: 1.06x faster                                              |
| pickle_pure_python      | 307 us                                                              | 290 us: 1.06x faster                                               |
| tornado_http            | 96.7 ms                                                             | 92.2 ms: 1.05x faster                                              |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                               |
| json                    | 4.86 ms                                                             | 4.65 ms: 1.04x faster                                              |
| html5lib                | 64.0 ms                                                             | 61.4 ms: 1.04x faster                                              |
| nqueens                 | 84.0 ms                                                             | 80.9 ms: 1.04x faster                                              |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.03x faster                                               |
| sqlglot_optimize        | 53.4 ms                                                             | 51.7 ms: 1.03x faster                                              |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                              |
| float                   | 76.0 ms                                                             | 73.6 ms: 1.03x faster                                              |
| bench_thread_pool       | 820 us                                                              | 798 us: 1.03x faster                                               |
| deepcopy                | 339 us                                                              | 330 us: 1.03x faster                                               |
| sympy_expand            | 477 ms                                                              | 465 ms: 1.03x faster                                               |
| logging_simple          | 6.09 us                                                             | 5.94 us: 1.02x faster                                              |
| logging_silent          | 98.7 ns                                                             | 96.6 ns: 1.02x faster                                              |
| sympy_str               | 291 ms                                                              | 285 ms: 1.02x faster                                               |
| sqlglot_normalize       | 108 ms                                                              | 106 ms: 1.02x faster                                               |
| telco                   | 6.59 ms                                                             | 6.46 ms: 1.02x faster                                              |
| scimark_lu              | 108 ms                                                              | 106 ms: 1.02x faster                                               |
| pprint_pformat          | 1.45 sec                                                            | 1.43 sec: 1.02x faster                                             |
| 2to3                    | 257 ms                                                              | 253 ms: 1.02x faster                                               |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                               |
| logging_format          | 6.64 us                                                             | 6.54 us: 1.02x faster                                              |
| docutils                | 2.59 sec                                                            | 2.55 sec: 1.01x faster                                             |
| chaos                   | 68.0 ms                                                             | 67.0 ms: 1.01x faster                                              |
| pprint_safe_repr        | 701 ms                                                              | 692 ms: 1.01x faster                                               |
| pathlib                 | 18.2 ms                                                             | 18.0 ms: 1.01x faster                                              |
| create_gc_cycles        | 1.48 ms                                                             | 1.46 ms: 1.01x faster                                              |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.96 us                                                             | 2.94 us: 1.01x faster                                              |
| fannkuch                | 384 ms                                                              | 381 ms: 1.01x faster                                               |
| sympy_sum               | 167 ms                                                              | 167 ms: 1.00x faster                                               |
| crypto_pyaes            | 73.8 ms                                                             | 74.1 ms: 1.00x slower                                              |
| dulwich_log             | 63.6 ms                                                             | 64.1 ms: 1.01x slower                                              |
| pyflate                 | 414 ms                                                              | 418 ms: 1.01x slower                                               |
| async_tree_none         | 525 ms                                                              | 531 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                              | 745 ms: 1.01x slower                                               |
| mako                    | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                              |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.02x slower                                             |
| django_template         | 32.9 ms                                                             | 33.5 ms: 1.02x slower                                              |
| pickle_list             | 4.03 us                                                             | 4.10 us: 1.02x slower                                              |
| async_tree_io           | 1.28 sec                                                            | 1.31 sec: 1.02x slower                                             |
| regex_v8                | 22.0 ms                                                             | 22.5 ms: 1.02x slower                                              |
| mdp                     | 2.64 sec                                                            | 2.71 sec: 1.03x slower                                             |
| unpickle_list           | 4.96 us                                                             | 5.12 us: 1.03x slower                                              |
| sqlite_synth            | 2.51 us                                                             | 2.60 us: 1.03x slower                                              |
| python_startup          | 8.49 ms                                                             | 8.85 ms: 1.04x slower                                              |
| xml_etree_process       | 54.1 ms                                                             | 56.4 ms: 1.04x slower                                              |
| pickle_dict             | 30.9 us                                                             | 32.3 us: 1.04x slower                                              |
| thrift                  | 766 us                                                              | 805 us: 1.05x slower                                               |
| pickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                              |
| gc_traversal            | 3.63 ms                                                             | 3.83 ms: 1.06x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                             | 1.75 ms: 1.06x slower                                              |
| regex_dna               | 196 ms                                                              | 208 ms: 1.06x slower                                               |
| xml_etree_generate      | 76.5 ms                                                             | 81.4 ms: 1.06x slower                                              |
| regex_effbot            | 3.32 ms                                                             | 3.53 ms: 1.06x slower                                              |
| sqlglot_parse           | 1.36 ms                                                             | 1.45 ms: 1.06x slower                                              |
| async_tree_memoization  | 621 ms                                                              | 670 ms: 1.08x slower                                               |
| comprehensions          | 22.2 us                                                             | 24.3 us: 1.09x slower                                              |
| python_startup_no_site  | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                              |
| async_generators        | 361 ms                                                              | 416 ms: 1.15x slower                                               |
| dask                    | 368 ms                                                              | 516 ms: 1.40x slower                                               |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                       |

Benchmark hidden because not significant (7): raytrace, scimark_monte_carlo, genshi_text, bench_mp_pool, go, chameleon, unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative