Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 182 ms                                                                | 181 ms: 1.00x faster                                                |
| chameleon      | 4.73 ms                                                               | 4.61 ms: 1.03x faster                                               |
| html5lib       | 35.8 ms                                                               | 34.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 55.7 ms                                                               | 51.7 ms: 1.08x faster                                               |
| nbody          | 63.8 ms                                                               | 65.2 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 77.7 ms                                                               | 76.3 ms: 1.02x faster                                               |
| regex_dna      | 149 ms                                                                | 151 ms: 1.01x slower                                                |
| regex_effbot   | 2.40 ms                                                               | 2.63 ms: 1.10x slower                                               |
| regex_v8       | 16.8 ms                                                               | 16.5 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 7.69 ms                                                               | 7.67 ms: 1.00x faster                                               |
| json_loads           | 16.4 us                                                               | 16.1 us: 1.02x faster                                               |
| pickle               | 7.14 us                                                               | 7.21 us: 1.01x slower                                               |
| pickle_dict          | 17.6 us                                                               | 17.9 us: 1.02x slower                                               |
| pickle_list          | 2.73 us                                                               | 2.86 us: 1.05x slower                                               |
| pickle_pure_python   | 222 us                                                                | 200 us: 1.11x faster                                                |
| unpickle             | 9.97 us                                                               | 9.68 us: 1.03x faster                                               |
| unpickle_list        | 2.77 us                                                               | 2.64 us: 1.05x faster                                               |
| unpickle_pure_python | 175 us                                                                | 159 us: 1.10x faster                                                |
| xml_etree_parse      | 99.1 ms                                                               | 99.6 ms: 1.01x slower                                               |
| xml_etree_iterparse  | 65.2 ms                                                               | 65.6 ms: 1.01x slower                                               |
| xml_etree_generate   | 48.0 ms                                                               | 48.4 ms: 1.01x slower                                               |
| xml_etree_process    | 34.8 ms                                                               | 35.1 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 9.25 ms                                                               | 9.19 ms: 1.01x faster                                               |
| python_startup_no_site | 7.30 ms                                                               | 7.24 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 15.5 ms                                                               | 15.3 ms: 1.01x faster                                               |
| genshi_xml     | 31.3 ms                                                               | 30.5 ms: 1.03x faster                                               |
| mako           | 8.44 ms                                                               | 8.40 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3                    | 182 ms                                                                | 181 ms: 1.00x faster                                                |
| async_generators        | 197 ms                                                                | 195 ms: 1.01x faster                                                |
| async_tree_none         | 287 ms                                                                | 281 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed | 533 ms                                                                | 528 ms: 1.01x faster                                                |
| async_tree_io           | 702 ms                                                                | 696 ms: 1.01x faster                                                |
| async_tree_memoization  | 346 ms                                                                | 317 ms: 1.09x faster                                                |
| chameleon               | 4.73 ms                                                               | 4.61 ms: 1.03x faster                                               |
| chaos                   | 49.5 ms                                                               | 49.3 ms: 1.00x faster                                               |
| bench_thread_pool       | 462 us                                                                | 457 us: 1.01x faster                                                |
| coroutines              | 17.4 ms                                                               | 17.8 ms: 1.02x slower                                               |
| deepcopy                | 237 us                                                                | 222 us: 1.07x faster                                                |
| deepcopy_reduce         | 2.04 us                                                               | 1.90 us: 1.07x faster                                               |
| deepcopy_memo           | 28.7 us                                                               | 26.2 us: 1.10x faster                                               |
| deltablue               | 2.83 ms                                                               | 2.82 ms: 1.00x faster                                               |
| dulwich_log             | 29.4 ms                                                               | 29.1 ms: 1.01x faster                                               |
| fannkuch                | 261 ms                                                                | 262 ms: 1.00x slower                                                |
| float                   | 55.7 ms                                                               | 51.7 ms: 1.08x faster                                               |
| generators              | 27.7 ms                                                               | 28.4 ms: 1.03x slower                                               |
| genshi_text             | 15.5 ms                                                               | 15.3 ms: 1.01x faster                                               |
| genshi_xml              | 31.3 ms                                                               | 30.5 ms: 1.03x faster                                               |
| go                      | 106 ms                                                                | 109 ms: 1.03x slower                                                |
| hexiom                  | 4.71 ms                                                               | 4.73 ms: 1.00x slower                                               |
| html5lib                | 35.8 ms                                                               | 34.7 ms: 1.03x faster                                               |
| json                    | 2.91 ms                                                               | 2.83 ms: 1.03x faster                                               |
| json_dumps              | 7.69 ms                                                               | 7.67 ms: 1.00x faster                                               |
| json_loads              | 16.4 us                                                               | 16.1 us: 1.02x faster                                               |
| logging_format          | 3.74 us                                                               | 3.73 us: 1.00x faster                                               |
| logging_silent          | 65.7 ns                                                               | 67.4 ns: 1.03x slower                                               |
| logging_simple          | 3.44 us                                                               | 3.47 us: 1.01x slower                                               |
| mako                    | 8.44 ms                                                               | 8.40 ms: 1.01x faster                                               |
| mdp                     | 1.53 sec                                                              | 1.54 sec: 1.01x slower                                              |
| meteor_contest          | 77.8 ms                                                               | 73.9 ms: 1.05x faster                                               |
| nbody                   | 63.8 ms                                                               | 65.2 ms: 1.02x slower                                               |
| nqueens                 | 58.7 ms                                                               | 59.5 ms: 1.01x slower                                               |
| pathlib                 | 20.8 ms                                                               | 20.6 ms: 1.01x faster                                               |
| pickle                  | 7.14 us                                                               | 7.21 us: 1.01x slower                                               |
| pickle_dict             | 17.6 us                                                               | 17.9 us: 1.02x slower                                               |
| pickle_list             | 2.73 us                                                               | 2.86 us: 1.05x slower                                               |
| pickle_pure_python      | 222 us                                                                | 200 us: 1.11x faster                                                |
| pprint_safe_repr        | 488 ms                                                                | 467 ms: 1.04x faster                                                |
| pprint_pformat          | 1.00 sec                                                              | 953 ms: 1.05x faster                                                |
| pyflate                 | 318 ms                                                                | 313 ms: 1.02x faster                                                |
| python_startup          | 9.25 ms                                                               | 9.19 ms: 1.01x faster                                               |
| python_startup_no_site  | 7.30 ms                                                               | 7.24 ms: 1.01x faster                                               |
| raytrace                | 208 ms                                                                | 207 ms: 1.00x faster                                                |
| regex_compile           | 77.7 ms                                                               | 76.3 ms: 1.02x faster                                               |
| regex_dna               | 149 ms                                                                | 151 ms: 1.01x slower                                                |
| regex_effbot            | 2.40 ms                                                               | 2.63 ms: 1.10x slower                                               |
| regex_v8                | 16.8 ms                                                               | 16.5 ms: 1.02x faster                                               |
| richards                | 33.3 ms                                                               | 32.7 ms: 1.02x faster                                               |
| scimark_fft             | 199 ms                                                                | 201 ms: 1.01x slower                                                |
| scimark_lu              | 71.8 ms                                                               | 72.2 ms: 1.01x slower                                               |
| scimark_monte_carlo     | 48.9 ms                                                               | 46.9 ms: 1.04x faster                                               |
| scimark_sor             | 77.6 ms                                                               | 83.3 ms: 1.07x slower                                               |
| spectral_norm           | 72.2 ms                                                               | 72.7 ms: 1.01x slower                                               |
| sqlalchemy_declarative  | 61.8 ms                                                               | 62.4 ms: 1.01x slower                                               |
| sqlalchemy_imperative   | 7.29 ms                                                               | 7.22 ms: 1.01x faster                                               |
| sqlglot_parse           | 1.19 ms                                                               | 948 us: 1.25x faster                                                |
| sqlglot_transpile       | 1.35 ms                                                               | 1.11 ms: 1.21x faster                                               |
| sqlglot_optimize        | 31.4 ms                                                               | 31.3 ms: 1.00x faster                                               |
| sqlglot_normalize       | 169 ms                                                                | 171 ms: 1.01x slower                                                |
| sqlite_synth            | 1.35 us                                                               | 1.29 us: 1.04x faster                                               |
| sympy_expand            | 243 ms                                                                | 242 ms: 1.00x faster                                                |
| sympy_integrate         | 11.6 ms                                                               | 11.5 ms: 1.01x faster                                               |
| sympy_sum               | 82.4 ms                                                               | 85.5 ms: 1.04x slower                                               |
| telco                   | 3.42 ms                                                               | 3.39 ms: 1.01x faster                                               |
| thrift                  | 435 us                                                                | 429 us: 1.01x faster                                                |
| unpack_sequence         | 32.2 ns                                                               | 33.1 ns: 1.03x slower                                               |
| unpickle                | 9.97 us                                                               | 9.68 us: 1.03x faster                                               |
| unpickle_list           | 2.77 us                                                               | 2.64 us: 1.05x faster                                               |
| unpickle_pure_python    | 175 us                                                                | 159 us: 1.10x faster                                                |
| xml_etree_parse         | 99.1 ms                                                               | 99.6 ms: 1.01x slower                                               |
| xml_etree_iterparse     | 65.2 ms                                                               | 65.6 ms: 1.01x slower                                               |
| xml_etree_generate      | 48.0 ms                                                               | 48.4 ms: 1.01x slower                                               |
| xml_etree_process       | 34.8 ms                                                               | 35.1 ms: 1.01x slower                                               |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (14): aiohttp, bench_mp_pool, crypto_pyaes, django_template, docutils, flaskblogging, gunicorn, mypy, pidigits, pycparser, pylint, scimark_sparse_mat_mult, sympy_str, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-python-deaf509e8fc6e0363bd6-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage