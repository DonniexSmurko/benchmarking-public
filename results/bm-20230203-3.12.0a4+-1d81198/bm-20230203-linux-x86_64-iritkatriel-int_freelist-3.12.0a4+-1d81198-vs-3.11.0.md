
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1d81198
- commit date: 2023-02-03
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.28 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 60.0 ms: 1.05x faster                                               |
| tornado_http   | 96.6 ms                                                | 93.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 191 ms: 1.05x faster                                                |
| float          | 76.3 ms                                                | 73.2 ms: 1.04x faster                                               |
| nbody          | 95.0 ms                                                | 95.8 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                               |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.51 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.43 ms: 1.34x faster                                               |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.08x faster                                                |
| pickle_pure_python   | 304 us                                                 | 286 us: 1.06x faster                                                |
| unpickle             | 13.3 us                                                | 12.9 us: 1.02x faster                                               |
| xml_etree_process    | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| pickle_dict          | 31.4 us                                                | 31.3 us: 1.00x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 103 ms: 1.00x slower                                                |
| pickle_list          | 4.17 us                                                | 4.23 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.4 ms: 1.01x slower                                               |
| unpickle_list        | 4.95 us                                                | 5.05 us: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.93 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.47 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.3 ms: 1.10x faster                                               |
| genshi_text     | 22.1 ms                                                | 20.3 ms: 1.09x faster                                               |
| mako            | 9.85 ms                                                | 9.60 ms: 1.03x faster                                               |
| django_template | 32.5 ms                                                | 32.3 ms: 1.00x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.43 ms: 1.34x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                               |
| nqueens                 | 85.0 ms                                                | 75.7 ms: 1.12x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.3 ms: 1.10x faster                                               |
| richards                | 46.2 ms                                                | 42.0 ms: 1.10x faster                                               |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.02 ms: 1.10x faster                                               |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.08x faster                                                |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                |
| chaos                   | 68.6 ms                                                | 63.7 ms: 1.08x faster                                               |
| coroutines              | 26.1 ms                                                | 24.3 ms: 1.07x faster                                               |
| logging_silent          | 98.5 ns                                                | 91.9 ns: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| scimark_fft             | 329 ms                                                 | 308 ms: 1.07x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.07x faster                                               |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                               |
| pickle_pure_python      | 304 us                                                 | 286 us: 1.06x faster                                                |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| logging_simple          | 6.06 us                                                | 5.73 us: 1.06x faster                                               |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.05x faster                                                |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                                |
| html5lib                | 63.2 ms                                                | 60.0 ms: 1.05x faster                                               |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                              |
| logging_format          | 6.62 us                                                | 6.32 us: 1.05x faster                                               |
| pidigits                | 199 ms                                                 | 191 ms: 1.05x faster                                                |
| float                   | 76.3 ms                                                | 73.2 ms: 1.04x faster                                               |
| coverage                | 101 ms                                                 | 96.4 ms: 1.04x faster                                               |
| telco                   | 6.62 ms                                                | 6.37 ms: 1.04x faster                                               |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                |
| json                    | 4.95 ms                                                | 4.76 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| bench_thread_pool       | 810 us                                                 | 782 us: 1.04x faster                                                |
| pycparser               | 1.17 sec                                               | 1.13 sec: 1.03x faster                                              |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                |
| sqlglot_optimize        | 53.0 ms                                                | 51.4 ms: 1.03x faster                                               |
| tornado_http            | 96.6 ms                                                | 93.7 ms: 1.03x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 671 ms: 1.03x faster                                                |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                               |
| mako                    | 9.85 ms                                                | 9.60 ms: 1.03x faster                                               |
| unpickle                | 13.3 us                                                | 12.9 us: 1.02x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 66.8 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                              |
| chameleon               | 6.41 ms                                                | 6.28 ms: 1.02x faster                                               |
| spectral_norm           | 99.9 ms                                                | 98.2 ms: 1.02x faster                                               |
| async_generators        | 359 ms                                                 | 354 ms: 1.02x faster                                                |
| async_tree_none         | 529 ms                                                 | 522 ms: 1.01x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                |
| xml_etree_process       | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                |
| thrift                  | 752 us                                                 | 747 us: 1.01x faster                                                |
| django_template         | 32.5 ms                                                | 32.3 ms: 1.00x faster                                               |
| pickle_dict             | 31.4 us                                                | 31.3 us: 1.00x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 103 ms: 1.00x slower                                                |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                               |
| nbody                   | 95.0 ms                                                | 95.8 ms: 1.01x slower                                               |
| pickle_list             | 4.17 us                                                | 4.23 us: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.01x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 77.4 ms: 1.01x slower                                               |
| unpickle_list           | 4.95 us                                                | 5.05 us: 1.02x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.54 us: 1.02x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                               |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                |
| crypto_pyaes            | 73.9 ms                                                | 76.0 ms: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 647 ms: 1.03x slower                                                |
| regex_effbot            | 3.36 ms                                                | 3.51 ms: 1.05x slower                                               |
| python_startup          | 8.36 ms                                                | 8.93 ms: 1.07x slower                                               |
| generators              | 72.2 ms                                                | 77.1 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.47 ms: 1.08x slower                                               |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (7): raytrace, deepcopy_reduce, pyflate, bench_mp_pool, async_tree_cpu_io_mixed, scimark_lu, unpack_sequence
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-1d81198/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal