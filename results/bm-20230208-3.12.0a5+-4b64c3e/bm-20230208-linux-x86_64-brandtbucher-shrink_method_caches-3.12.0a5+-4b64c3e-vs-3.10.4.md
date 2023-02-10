
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                        |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.8 ms                                                | 61.0 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.8 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.0 ms: 1.48x faster                                                        |
| nbody          | 136 ms                                                 | 93.1 ms: 1.46x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.13x faster                                                        |
| regex_dna      | 214 ms                                                 | 218 ms: 1.02x slower                                                         |
| regex_effbot   | 3.21 ms                                                | 3.52 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 294 us: 1.54x faster                                                         |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.33 ms: 1.45x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                        |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 80.5 ms: 1.16x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| pickle_list          | 4.50 us                                                | 4.13 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                         |
| unpickle             | 14.3 us                                                | 13.7 us: 1.05x faster                                                        |
| pickle_dict          | 28.3 us                                                | 30.4 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.86 ms: 1.57x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.42 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                        |
| mako            | 14.3 ms                                                | 9.90 ms: 1.44x faster                                                        |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.19 ms: 2.31x faster                                                        |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                         |
| logging_silent          | 173 ns                                                 | 95.9 ns: 1.81x faster                                                        |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                         |
| richards                | 71.4 ms                                                | 42.8 ms: 1.67x faster                                                        |
| pyflate                 | 675 ms                                                 | 406 ms: 1.66x faster                                                         |
| raytrace                | 461 ms                                                 | 286 ms: 1.61x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 73.6 ms: 1.60x faster                                                        |
| spectral_norm           | 148 ms                                                 | 93.4 ms: 1.58x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.58x faster                                                        |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.86 ms: 1.57x faster                                                        |
| chaos                   | 104 ms                                                 | 66.4 ms: 1.57x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 294 us: 1.54x faster                                                         |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                         |
| float                   | 108 ms                                                 | 73.0 ms: 1.48x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                        |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                                         |
| nbody                   | 136 ms                                                 | 93.1 ms: 1.46x faster                                                        |
| deepcopy_memo           | 50.0 us                                                | 34.5 us: 1.45x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.33 ms: 1.45x faster                                                        |
| mako                    | 14.3 ms                                                | 9.90 ms: 1.44x faster                                                        |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                        |
| html5lib                | 85.8 ms                                                | 61.0 ms: 1.40x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.42 sec: 1.39x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.74 ms: 1.39x faster                                                        |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.38x faster                                                       |
| logging_format          | 8.92 us                                                | 6.49 us: 1.38x faster                                                        |
| pprint_safe_repr        | 943 ms                                                 | 686 ms: 1.37x faster                                                         |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                         |
| thrift                  | 1.03 ms                                                | 759 us: 1.36x faster                                                         |
| logging_simple          | 8.06 us                                                | 5.95 us: 1.35x faster                                                        |
| tornado_http            | 128 ms                                                 | 94.8 ms: 1.35x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                       |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.5 ns                                                | 44.2 ns: 1.34x faster                                                        |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 645 ms: 1.32x faster                                                         |
| fannkuch                | 477 ms                                                 | 361 ms: 1.32x faster                                                         |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.32x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                        |
| nqueens                 | 99.3 ms                                                | 76.2 ms: 1.30x faster                                                        |
| deepcopy                | 429 us                                                 | 331 us: 1.30x faster                                                         |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                        |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.27 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 749 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.8 ms: 1.26x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                                         |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                       |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                         |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                                         |
| bench_thread_pool       | 943 us                                                 | 791 us: 1.19x faster                                                         |
| sympy_expand            | 537 ms                                                 | 452 ms: 1.19x faster                                                         |
| dulwich_log             | 75.5 ms                                                | 63.6 ms: 1.19x faster                                                        |
| xml_etree_generate      | 93.3 ms                                                | 80.5 ms: 1.16x faster                                                        |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                         |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                        |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.4 ms: 1.14x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| pickle_list             | 4.50 us                                                | 4.13 us: 1.09x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                         |
| mdp                     | 2.82 sec                                               | 2.70 sec: 1.05x faster                                                       |
| unpickle                | 14.3 us                                                | 13.7 us: 1.05x faster                                                        |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                                        |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| generators              | 75.8 ms                                                | 76.9 ms: 1.02x slower                                                        |
| async_generators        | 428 ms                                                 | 435 ms: 1.02x slower                                                         |
| regex_dna               | 214 ms                                                 | 218 ms: 1.02x slower                                                         |
| pickle_dict             | 28.3 us                                                | 30.4 us: 1.07x slower                                                        |
| regex_effbot            | 3.21 ms                                                | 3.52 ms: 1.10x slower                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.42 ms: 1.11x slower                                                        |
| coverage                | 75.3 ms                                                | 101 ms: 1.34x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (3): pickle, unpickle_list, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230208-3.12.0a5+-4b64c3e/bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2