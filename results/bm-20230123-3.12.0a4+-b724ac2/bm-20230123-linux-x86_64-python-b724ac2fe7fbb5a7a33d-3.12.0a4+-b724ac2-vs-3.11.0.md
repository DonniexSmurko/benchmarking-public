
# Results vs. 3.11.0

- fork: python
- ref: b724ac2fe7fbb5a7a33d
- machine: linux-x86_64
- commit hash: b724ac2
- commit date: 2023-01-23
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                   |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| html5lib       | 63.2 ms                                                | 60.3 ms: 1.05x faster                                                  |
| tornado_http   | 96.6 ms                                                | 93.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.6 ms: 1.05x faster                                                  |
| nbody          | 95.0 ms                                                | 93.8 ms: 1.01x faster                                                  |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                                   |
| regex_effbot   | 3.36 ms                                                | 3.44 ms: 1.02x slower                                                  |
| regex_v8       | 22.3 ms                                                | 21.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.38 ms: 1.35x faster                                                  |
| json_loads           | 26.2 us                                                | 24.3 us: 1.08x faster                                                  |
| pickle               | 9.79 us                                                | 10.3 us: 1.06x slower                                                  |
| pickle_dict          | 31.4 us                                                | 32.2 us: 1.02x slower                                                  |
| pickle_list          | 4.17 us                                                | 4.26 us: 1.02x slower                                                  |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                                   |
| unpickle_list        | 4.95 us                                                | 5.08 us: 1.03x slower                                                  |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.04x slower                                                   |
| xml_etree_generate   | 76.2 ms                                                | 79.1 ms: 1.04x slower                                                  |
| xml_etree_process    | 53.8 ms                                                | 54.4 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.9 ms: 1.01x slower                                                  |
| genshi_xml      | 52.1 ms                                                | 46.8 ms: 1.11x faster                                                  |
| mako            | 9.85 ms                                                | 9.66 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 994 us: 1.05x faster                                                   |
| async_generators        | 359 ms                                                 | 351 ms: 1.02x faster                                                   |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                 |
| async_tree_memoization  | 625 ms                                                 | 666 ms: 1.07x slower                                                   |
| chaos                   | 68.6 ms                                                | 63.6 ms: 1.08x faster                                                  |
| bench_thread_pool       | 810 us                                                 | 774 us: 1.05x faster                                                   |
| coroutines              | 26.1 ms                                                | 25.6 ms: 1.02x faster                                                  |
| coverage                | 101 ms                                                 | 97.3 ms: 1.03x faster                                                  |
| crypto_pyaes            | 73.9 ms                                                | 73.3 ms: 1.01x faster                                                  |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                                   |
| deepcopy_memo           | 36.4 us                                                | 34.6 us: 1.05x faster                                                  |
| deltablue               | 3.64 ms                                                | 3.23 ms: 1.13x faster                                                  |
| django_template         | 32.5 ms                                                | 32.9 ms: 1.01x slower                                                  |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| float                   | 76.3 ms                                                | 72.6 ms: 1.05x faster                                                  |
| generators              | 72.2 ms                                                | 74.7 ms: 1.04x slower                                                  |
| genshi_xml              | 52.1 ms                                                | 46.8 ms: 1.11x faster                                                  |
| go                      | 143 ms                                                 | 136 ms: 1.06x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                  |
| hexiom                  | 6.35 ms                                                | 5.95 ms: 1.07x faster                                                  |
| html5lib                | 63.2 ms                                                | 60.3 ms: 1.05x faster                                                  |
| json                    | 4.95 ms                                                | 4.60 ms: 1.07x faster                                                  |
| json_dumps              | 12.7 ms                                                | 9.38 ms: 1.35x faster                                                  |
| json_loads              | 26.2 us                                                | 24.3 us: 1.08x faster                                                  |
| logging_format          | 6.62 us                                                | 6.34 us: 1.04x faster                                                  |
| logging_silent          | 98.5 ns                                                | 93.3 ns: 1.06x faster                                                  |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                                  |
| mako                    | 9.85 ms                                                | 9.66 ms: 1.02x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.43 sec: 1.08x faster                                                 |
| mypy                    | 669 ms                                                 | 810 ms: 1.21x slower                                                   |
| nbody                   | 95.0 ms                                                | 93.8 ms: 1.01x faster                                                  |
| nqueens                 | 85.0 ms                                                | 76.2 ms: 1.12x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                  |
| pickle                  | 9.79 us                                                | 10.3 us: 1.06x slower                                                  |
| pickle_dict             | 31.4 us                                                | 32.2 us: 1.02x slower                                                  |
| pickle_list             | 4.17 us                                                | 4.26 us: 1.02x slower                                                  |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                                   |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.02x faster                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.07x faster                                                 |
| pyflate                 | 417 ms                                                 | 400 ms: 1.04x faster                                                   |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                                  |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                                   |
| regex_effbot            | 3.36 ms                                                | 3.44 ms: 1.02x slower                                                  |
| regex_v8                | 22.3 ms                                                | 21.0 ms: 1.06x faster                                                  |
| richards                | 46.2 ms                                                | 42.9 ms: 1.08x faster                                                  |
| scimark_fft             | 329 ms                                                 | 306 ms: 1.07x faster                                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 65.2 ms: 1.05x faster                                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.06 ms: 1.09x faster                                                  |
| spectral_norm           | 99.9 ms                                                | 97.7 ms: 1.02x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 51.3 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.03x slower                                                  |
| sympy_expand            | 472 ms                                                 | 456 ms: 1.04x faster                                                   |
| sympy_integrate         | 20.9 ms                                                | 20.2 ms: 1.03x faster                                                  |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                   |
| sympy_str               | 287 ms                                                 | 281 ms: 1.02x faster                                                   |
| telco                   | 6.62 ms                                                | 6.38 ms: 1.04x faster                                                  |
| thrift                  | 752 us                                                 | 746 us: 1.01x faster                                                   |
| tornado_http            | 96.6 ms                                                | 93.7 ms: 1.03x faster                                                  |
| unpack_sequence         | 43.4 ns                                                | 41.6 ns: 1.04x faster                                                  |
| unpickle_list           | 4.95 us                                                | 5.08 us: 1.03x slower                                                  |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.01x faster                                                   |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.04x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 79.1 ms: 1.04x slower                                                  |
| xml_etree_process       | 53.8 ms                                                | 54.4 ms: 1.01x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, chameleon, bench_mp_pool, deepcopy_reduce, genshi_text, meteor_contest, scimark_lu, unpickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230123-3.12.0a4+-b724ac2/bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal