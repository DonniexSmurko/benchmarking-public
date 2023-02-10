
# Results vs. 3.10.4

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.26x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 257 ms: 1.29x faster                                   |
| chameleon      | 8.86 ms                                                | 6.49 ms: 1.37x faster                                  |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                 |
| html5lib       | 85.8 ms                                                | 64.0 ms: 1.34x faster                                  |
| tornado_http   | 128 ms                                                 | 96.1 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 136 ms                                                 | 93.0 ms: 1.47x faster                                  |
| float          | 108 ms                                                 | 76.6 ms: 1.41x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 138 ms: 1.26x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| regex_dna      | 214 ms                                                 | 192 ms: 1.11x faster                                   |
| regex_effbot   | 3.21 ms                                                | 3.39 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 305 us: 1.49x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.38x faster                                  |
| unpickle_pure_python | 297 us                                                 | 228 us: 1.30x faster                                   |
| xml_etree_generate   | 93.3 ms                                                | 76.5 ms: 1.22x faster                                  |
| json_loads           | 28.9 us                                                | 26.2 us: 1.10x faster                                  |
| pickle_list          | 4.50 us                                                | 4.16 us: 1.08x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.5 ms: 1.08x faster                                  |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                  |
| xml_etree_iterparse  | 110 ms                                                 | 104 ms: 1.06x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.03x faster                                   |
| pickle               | 10.1 us                                                | 10.00 us: 1.01x faster                                 |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                  |
| pickle_dict          | 28.3 us                                                | 31.4 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.47 ms: 1.65x faster                                  |
| python_startup_no_site | 5.76 ms                                                | 5.97 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.83 ms: 1.45x faster                                  |
| django_template | 46.3 ms                                                | 32.7 ms: 1.41x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.7 ms: 1.41x faster                                  |
| genshi_xml      | 63.6 ms                                                | 51.5 ms: 1.23x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.68 ms: 2.01x faster                                  |
| logging_silent          | 173 ns                                                 | 99.8 ns: 1.74x faster                                  |
| scimark_sor             | 193 ms                                                 | 115 ms: 1.68x faster                                   |
| python_startup          | 13.9 ms                                                | 8.47 ms: 1.65x faster                                  |
| pyflate                 | 675 ms                                                 | 417 ms: 1.62x faster                                   |
| go                      | 226 ms                                                 | 141 ms: 1.60x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.59x faster                                  |
| raytrace                | 461 ms                                                 | 291 ms: 1.59x faster                                   |
| richards                | 71.4 ms                                                | 45.6 ms: 1.56x faster                                  |
| scimark_monte_carlo     | 105 ms                                                 | 67.7 ms: 1.55x faster                                  |
| chaos                   | 104 ms                                                 | 68.2 ms: 1.53x faster                                  |
| spectral_norm           | 148 ms                                                 | 98.4 ms: 1.50x faster                                  |
| pickle_pure_python      | 453 us                                                 | 305 us: 1.49x faster                                   |
| hexiom                  | 9.42 ms                                                | 6.36 ms: 1.48x faster                                  |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.38 ms: 1.48x faster                                  |
| nbody                   | 136 ms                                                 | 93.0 ms: 1.47x faster                                  |
| mako                    | 14.3 ms                                                | 9.83 ms: 1.45x faster                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.67 ms: 1.45x faster                                  |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.41x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.7 ms: 1.41x faster                                  |
| float                   | 108 ms                                                 | 76.6 ms: 1.41x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.38x faster                                  |
| logging_format          | 8.92 us                                                | 6.49 us: 1.37x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                 |
| chameleon               | 8.86 ms                                                | 6.49 ms: 1.37x faster                                  |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                 |
| pprint_pformat          | 1.97 sec                                               | 1.45 sec: 1.36x faster                                 |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 628 ms: 1.36x faster                                   |
| deepcopy_memo           | 50.0 us                                                | 36.8 us: 1.36x faster                                  |
| pprint_safe_repr        | 943 ms                                                 | 697 ms: 1.35x faster                                   |
| logging_simple          | 8.06 us                                                | 5.97 us: 1.35x faster                                  |
| html5lib                | 85.8 ms                                                | 64.0 ms: 1.34x faster                                  |
| thrift                  | 1.03 ms                                                | 770 us: 1.34x faster                                   |
| tornado_http            | 128 ms                                                 | 96.1 ms: 1.34x faster                                  |
| unpickle_pure_python    | 297 us                                                 | 228 us: 1.30x faster                                   |
| 2to3                    | 332 ms                                                 | 257 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 740 ms: 1.28x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.05 ms: 1.28x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.13 ms: 1.27x faster                                  |
| scimark_fft             | 414 ms                                                 | 327 ms: 1.26x faster                                   |
| regex_compile           | 174 ms                                                 | 138 ms: 1.26x faster                                   |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                 |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.24x faster                                   |
| coroutines              | 31.7 ms                                                | 25.6 ms: 1.24x faster                                  |
| deepcopy                | 429 us                                                 | 348 us: 1.24x faster                                   |
| deepcopy_reduce         | 3.75 us                                                | 3.04 us: 1.23x faster                                  |
| genshi_xml              | 63.6 ms                                                | 51.5 ms: 1.23x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 53.3 ms: 1.23x faster                                  |
| xml_etree_generate      | 93.3 ms                                                | 76.5 ms: 1.22x faster                                  |
| unpack_sequence         | 59.5 ns                                                | 48.8 ns: 1.22x faster                                  |
| fannkuch                | 477 ms                                                 | 392 ms: 1.22x faster                                   |
| async_generators        | 428 ms                                                 | 357 ms: 1.20x faster                                   |
| nqueens                 | 99.3 ms                                                | 83.1 ms: 1.20x faster                                  |
| flaskblogging           | 8.38 ms                                                | 7.02 ms: 1.19x faster                                  |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.63 ms: 1.18x faster                                  |
| dulwich_log             | 75.5 ms                                                | 63.7 ms: 1.18x faster                                  |
| sqlite_synth            | 2.90 us                                                | 2.46 us: 1.18x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.17x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| bench_thread_pool       | 943 us                                                 | 812 us: 1.16x faster                                   |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.2 ms: 1.16x faster                                  |
| sympy_integrate         | 23.9 ms                                                | 20.8 ms: 1.15x faster                                  |
| sympy_expand            | 537 ms                                                 | 468 ms: 1.15x faster                                   |
| sympy_str               | 324 ms                                                 | 288 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| regex_dna               | 214 ms                                                 | 192 ms: 1.11x faster                                   |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                   |
| json_loads              | 28.9 us                                                | 26.2 us: 1.10x faster                                  |
| pylint                  | 519 ms                                                 | 475 ms: 1.09x faster                                   |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                   |
| json                    | 5.35 ms                                                | 4.92 ms: 1.09x faster                                  |
| pickle_list             | 4.50 us                                                | 4.16 us: 1.08x faster                                  |
| json_dumps              | 13.5 ms                                                | 12.5 ms: 1.08x faster                                  |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                  |
| xml_etree_iterparse     | 110 ms                                                 | 104 ms: 1.06x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.03x faster                                   |
| generators              | 75.8 ms                                                | 74.1 ms: 1.02x faster                                  |
| mdp                     | 2.82 sec                                               | 2.77 sec: 1.02x faster                                 |
| telco                   | 6.68 ms                                                | 6.59 ms: 1.01x faster                                  |
| pickle                  | 10.1 us                                                | 10.00 us: 1.01x faster                                 |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| python_startup_no_site  | 5.76 ms                                                | 5.97 ms: 1.04x slower                                  |
| regex_effbot            | 3.21 ms                                                | 3.39 ms: 1.06x slower                                  |
| pickle_dict             | 28.3 us                                                | 31.4 us: 1.11x slower                                  |
| coverage                | 75.3 ms                                                | 103 ms: 1.37x slower                                   |
| Geometric mean          | (ref)                                                  | 1.26x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.11.2-878ead1/bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2