
# Results vs. 3.11.0

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: 19b61a7
- commit date: 2023-02-23
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                 |
| chameleon      | 6.38 ms                                                | 6.48 ms: 1.02x slower                                                |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                               |
| html5lib       | 64.8 ms                                                | 62.4 ms: 1.04x faster                                                |
| tornado_http   | 96.5 ms                                                | 95.3 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.5 ms: 1.05x faster                                                |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                 |
| nbody          | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.27 ms: 1.06x faster                                                |
| regex_compile  | 136 ms                                                 | 133 ms: 1.02x faster                                                 |
| regex_v8       | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                |
| regex_dna      | 203 ms                                                 | 210 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.34 ms: 1.32x faster                                                |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                                 |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                                |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                 |
| pickle_list          | 4.14 us                                                | 3.92 us: 1.06x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 98.5 ms: 1.06x faster                                                |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                                 |
| pickle_dict          | 31.2 us                                                | 30.1 us: 1.04x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.91 us: 1.02x faster                                                |
| pickle               | 9.90 us                                                | 9.95 us: 1.00x slower                                                |
| xml_etree_process    | 53.7 ms                                                | 55.8 ms: 1.04x slower                                                |
| xml_etree_generate   | 75.9 ms                                                | 81.5 ms: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                |
| python_startup_no_site | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.1 ms: 1.07x faster                                                |
| mako            | 9.83 ms                                                | 9.93 ms: 1.01x slower                                                |
| django_template | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.5 ms: 2.41x faster                                                |
| asyncio_tcp             | 883 ms                                                 | 505 ms: 1.75x faster                                                 |
| json_dumps              | 12.4 ms                                                | 9.34 ms: 1.32x faster                                                |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                 |
| coroutines              | 26.2 ms                                                | 22.3 ms: 1.17x faster                                                |
| deltablue               | 3.66 ms                                                | 3.24 ms: 1.13x faster                                                |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                                 |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                 |
| json                    | 4.87 ms                                                | 4.55 ms: 1.07x faster                                                |
| genshi_xml              | 51.4 ms                                                | 48.1 ms: 1.07x faster                                                |
| richards                | 46.1 ms                                                | 43.4 ms: 1.06x faster                                                |
| unpack_sequence         | 44.5 ns                                                | 41.9 ns: 1.06x faster                                                |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                               |
| regex_effbot            | 3.46 ms                                                | 3.27 ms: 1.06x faster                                                |
| pickle_list             | 4.14 us                                                | 3.92 us: 1.06x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 98.5 ms: 1.06x faster                                                |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.05x faster                                                 |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                                 |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                 |
| float                   | 76.8 ms                                                | 73.5 ms: 1.05x faster                                                |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                 |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                |
| html5lib                | 64.8 ms                                                | 62.4 ms: 1.04x faster                                                |
| mdp                     | 2.63 sec                                               | 2.53 sec: 1.04x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                               |
| pickle_dict             | 31.2 us                                                | 30.1 us: 1.04x faster                                                |
| coverage                | 99.3 ms                                                | 95.9 ms: 1.03x faster                                                |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                 |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                 |
| sqlglot_optimize        | 52.7 ms                                                | 51.2 ms: 1.03x faster                                                |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                                 |
| bench_thread_pool       | 817 us                                                 | 794 us: 1.03x faster                                                 |
| logging_silent          | 98.0 ns                                                | 95.4 ns: 1.03x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 66.2 ms: 1.03x faster                                                |
| crypto_pyaes            | 75.7 ms                                                | 73.8 ms: 1.03x faster                                                |
| nqueens                 | 83.8 ms                                                | 81.6 ms: 1.03x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                 |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.02x faster                                                |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                 |
| spectral_norm           | 98.1 ms                                                | 95.9 ms: 1.02x faster                                                |
| regex_compile           | 136 ms                                                 | 133 ms: 1.02x faster                                                 |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                                 |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.02x faster                                                |
| pyflate                 | 419 ms                                                 | 411 ms: 1.02x faster                                                 |
| hexiom                  | 6.34 ms                                                | 6.22 ms: 1.02x faster                                                |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.51 ms: 1.02x faster                                                |
| unpickle_list           | 4.99 us                                                | 4.91 us: 1.02x faster                                                |
| logging_simple          | 6.02 us                                                | 5.93 us: 1.01x faster                                                |
| sympy_str               | 291 ms                                                 | 287 ms: 1.01x faster                                                 |
| tornado_http            | 96.5 ms                                                | 95.3 ms: 1.01x faster                                                |
| dulwich_log             | 64.0 ms                                                | 63.3 ms: 1.01x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                 |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                                 |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                               |
| regex_v8                | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                |
| pickle                  | 9.90 us                                                | 9.95 us: 1.00x slower                                                |
| logging_format          | 6.48 us                                                | 6.51 us: 1.01x slower                                                |
| mako                    | 9.83 ms                                                | 9.93 ms: 1.01x slower                                                |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                                 |
| chameleon               | 6.38 ms                                                | 6.48 ms: 1.02x slower                                                |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                 |
| deepcopy_reduce         | 3.02 us                                                | 3.08 us: 1.02x slower                                                |
| thrift                  | 760 us                                                 | 779 us: 1.03x slower                                                 |
| regex_dna               | 203 ms                                                 | 210 ms: 1.04x slower                                                 |
| django_template         | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                |
| xml_etree_process       | 53.7 ms                                                | 55.8 ms: 1.04x slower                                                |
| nbody                   | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                                |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.06x slower                                                |
| async_tree_memoization  | 624 ms                                                 | 662 ms: 1.06x slower                                                 |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                |
| gc_traversal            | 3.82 ms                                                | 4.07 ms: 1.07x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 81.5 ms: 1.07x slower                                                |
| python_startup_no_site  | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                |
| async_generators        | 356 ms                                                 | 411 ms: 1.16x slower                                                 |
| dask                    | 365 ms                                                 | 509 ms: 1.39x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (11): async_tree_none, deepcopy_memo, chaos, deepcopy, genshi_text, telco, djangocms, bench_mp_pool, async_tree_cpu_io_mixed, sqlalchemy_imperative, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint