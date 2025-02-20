
# Results vs. 3.10.4

- fork: python
- ref: 281a3f18cc2afac0fa92
- machine: darwin-arm64
- commit hash: 281a3f1
- commit date: 2022-10-09
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.61 ms: 1.26x faster                                                 |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| html5lib       | 44.2 ms                                                | 36.6 ms: 1.21x faster                                                 |
| tornado_http   | 91.5 ms                                                | 69.4 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.3 ms: 1.45x faster                                                 |
| float          | 72.4 ms                                                | 56.1 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.5 ms: 1.26x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.3 ms: 1.08x faster                                                 |
| regex_dna      | 162 ms                                                 | 151 ms: 1.07x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.68 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.17 ms: 1.36x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 208 us: 1.36x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.25x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 90.0 ms: 1.18x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 47.1 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 64.6 ms: 1.12x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.54 us: 1.06x faster                                                 |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| unpickle             | 9.89 us                                                | 9.78 us: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.56 us: 1.03x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.91 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.38 ms: 1.27x faster                                                 |
| python_startup_no_site | 8.88 ms                                                | 7.41 ms: 1.20x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.11 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.7 ms: 1.25x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.1 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.3 ms: 1.20x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.74 ms: 1.88x faster                                                 |
| logging_silent          | 119 ns                                                 | 65.9 ns: 1.81x faster                                                 |
| richards                | 51.4 ms                                                | 33.5 ms: 1.54x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 51.8 ms: 1.51x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 325 ms: 1.51x faster                                                  |
| raytrace                | 325 ms                                                 | 219 ms: 1.49x faster                                                  |
| scimark_lu              | 109 ms                                                 | 73.9 ms: 1.48x faster                                                 |
| nbody                   | 93.3 ms                                                | 64.3 ms: 1.45x faster                                                 |
| async_tree_none         | 400 ms                                                 | 287 ms: 1.39x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.38x faster                                                  |
| go                      | 165 ms                                                 | 120 ms: 1.38x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.17 ms: 1.36x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 208 us: 1.36x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.36x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.34x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 54.6 ms: 1.33x faster                                                 |
| thrift                  | 580 us                                                 | 438 us: 1.33x faster                                                  |
| chaos                   | 66.7 ms                                                | 50.4 ms: 1.32x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 72.5 ms: 1.32x faster                                                 |
| tornado_http            | 91.5 ms                                                | 69.4 ms: 1.32x faster                                                 |
| pycparser               | 916 ms                                                 | 706 ms: 1.30x faster                                                  |
| mako                    | 10.5 ms                                                | 8.11 ms: 1.29x faster                                                 |
| float                   | 72.4 ms                                                | 56.1 ms: 1.29x faster                                                 |
| pyflate                 | 453 ms                                                 | 352 ms: 1.29x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.28x faster                                                 |
| python_startup          | 11.9 ms                                                | 9.38 ms: 1.27x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.66 us: 1.26x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.3 ms: 1.26x faster                                                 |
| regex_compile           | 96.4 ms                                                | 76.5 ms: 1.26x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.61 ms: 1.26x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.25x faster                                                  |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.25x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 486 ms: 1.25x faster                                                  |
| scimark_sor             | 126 ms                                                 | 101 ms: 1.25x faster                                                  |
| logging_format          | 4.97 us                                                | 4.00 us: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.78 ms: 1.24x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 992 ms: 1.24x faster                                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.16 ms: 1.24x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.1 ms: 1.23x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 61.0 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 545 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                                |
| bench_thread_pool       | 546 us                                                 | 452 us: 1.21x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.6 ms: 1.21x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.3 ms: 1.20x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.41 ms: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.7 ms: 1.20x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 90.0 ms: 1.18x faster                                                 |
| fannkuch                | 317 ms                                                 | 269 ms: 1.18x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 29.2 us: 1.18x faster                                                 |
| deepcopy                | 281 us                                                 | 239 us: 1.17x faster                                                  |
| async_generators        | 234 ms                                                 | 199 ms: 1.17x faster                                                  |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.16x faster                                                  |
| pylint                  | 307 ms                                                 | 265 ms: 1.16x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.06 us: 1.15x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 47.1 ms: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.6 ms: 1.14x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 173 ms: 1.14x faster                                                  |
| nqueens                 | 68.2 ms                                                | 60.3 ms: 1.13x faster                                                 |
| generators              | 32.7 ms                                                | 29.0 ms: 1.13x faster                                                 |
| sympy_expand            | 275 ms                                                 | 246 ms: 1.12x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 64.6 ms: 1.12x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 33.5 ns: 1.12x faster                                                 |
| sympy_str               | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| telco                   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.52 sec: 1.09x faster                                                |
| sympy_sum               | 93.6 ms                                                | 86.0 ms: 1.09x faster                                                 |
| 2to3                    | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| json                    | 3.08 ms                                                | 2.84 ms: 1.08x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.3 ms: 1.08x faster                                                 |
| regex_dna               | 162 ms                                                 | 151 ms: 1.07x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.0 ms: 1.06x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.54 us: 1.06x faster                                                 |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 76.2 ms: 1.02x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.45 us: 1.02x faster                                                 |
| unpickle                | 9.89 us                                                | 9.78 us: 1.01x faster                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.56 us: 1.03x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.91 us: 1.04x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 41.4 ms: 1.04x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.68 ms: 1.09x slower                                                 |
| coverage                | 42.0 ms                                                | 53.4 ms: 1.27x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221009-3.12.0a0-281a3f1/bm-20221009-darwin-arm64-python-281a3f18cc2afac0fa92-3.12.0a0-281a3f1.json: mypy
