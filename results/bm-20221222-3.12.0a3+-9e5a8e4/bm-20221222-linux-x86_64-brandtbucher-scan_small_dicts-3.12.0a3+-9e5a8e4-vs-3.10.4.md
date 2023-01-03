Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 255 ms: 1.31x faster                                                     |
| chameleon      | 8.86 ms                                                | 6.52 ms: 1.36x faster                                                    |
| docutils       | 3.18 sec                                               | 2.65 sec: 1.20x faster                                                   |
| html5lib       | 85.8 ms                                                | 60.4 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                  | 1.32x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.2 ms: 1.49x faster                                                    |
| nbody          | 136 ms                                                 | 96.6 ms: 1.41x faster                                                    |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 131 ms: 1.33x faster                                                     |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                     |
| regex_effbot   | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                    |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.43x faster                                                    |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                    |
| pickle_dict          | 28.3 us                                                | 30.4 us: 1.07x slower                                                    |
| pickle_list          | 4.50 us                                                | 4.09 us: 1.10x faster                                                    |
| pickle_pure_python   | 453 us                                                 | 285 us: 1.59x faster                                                     |
| unpickle             | 14.3 us                                                | 13.8 us: 1.04x faster                                                    |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                                    |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                     |
| xml_etree_generate   | 93.3 ms                                                | 76.3 ms: 1.22x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.55 ms: 1.63x faster                                                    |
| python_startup_no_site | 5.76 ms                                                | 6.13 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.0 ms: 1.45x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                    |
| genshi_xml      | 63.6 ms                                                | 47.1 ms: 1.35x faster                                                    |
| mako            | 14.3 ms                                                | 9.37 ms: 1.52x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 255 ms: 1.31x faster                                                     |
| async_generators        | 428 ms                                                 | 352 ms: 1.22x faster                                                     |
| async_tree_none         | 713 ms                                                 | 541 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 769 ms: 1.23x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 683 ms: 1.25x faster                                                     |
| chameleon               | 8.86 ms                                                | 6.52 ms: 1.36x faster                                                    |
| chaos                   | 104 ms                                                 | 67.0 ms: 1.55x faster                                                    |
| bench_thread_pool       | 943 us                                                 | 780 us: 1.21x faster                                                     |
| coroutines              | 31.7 ms                                                | 24.9 ms: 1.27x faster                                                    |
| coverage                | 75.3 ms                                                | 104 ms: 1.38x slower                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.8 ms: 1.55x faster                                                    |
| deepcopy                | 429 us                                                 | 329 us: 1.30x faster                                                     |
| deepcopy_reduce         | 3.75 us                                                | 2.91 us: 1.29x faster                                                    |
| deepcopy_memo           | 50.0 us                                                | 33.2 us: 1.51x faster                                                    |
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                                    |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.45x faster                                                    |
| docutils                | 3.18 sec                                               | 2.65 sec: 1.20x faster                                                   |
| dulwich_log             | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                    |
| fannkuch                | 477 ms                                                 | 371 ms: 1.29x faster                                                     |
| float                   | 108 ms                                                 | 72.2 ms: 1.49x faster                                                    |
| generators              | 75.8 ms                                                | 76.8 ms: 1.01x slower                                                    |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                    |
| genshi_xml              | 63.6 ms                                                | 47.1 ms: 1.35x faster                                                    |
| go                      | 226 ms                                                 | 141 ms: 1.61x faster                                                     |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.57x faster                                                    |
| html5lib                | 85.8 ms                                                | 60.4 ms: 1.42x faster                                                    |
| json                    | 5.35 ms                                                | 5.17 ms: 1.03x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.43x faster                                                    |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                    |
| logging_format          | 8.92 us                                                | 6.28 us: 1.42x faster                                                    |
| logging_silent          | 173 ns                                                 | 90.9 ns: 1.91x faster                                                    |
| logging_simple          | 8.06 us                                                | 5.68 us: 1.42x faster                                                    |
| mako                    | 14.3 ms                                                | 9.37 ms: 1.52x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.73 sec: 1.04x faster                                                   |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                     |
| mypy                    | 1.01 sec                                               | 808 ms: 1.26x faster                                                     |
| nbody                   | 136 ms                                                 | 96.6 ms: 1.41x faster                                                    |
| nqueens                 | 99.3 ms                                                | 78.7 ms: 1.26x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                                    |
| pickle_dict             | 28.3 us                                                | 30.4 us: 1.07x slower                                                    |
| pickle_list             | 4.50 us                                                | 4.09 us: 1.10x faster                                                    |
| pickle_pure_python      | 453 us                                                 | 285 us: 1.59x faster                                                     |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| pprint_safe_repr        | 943 ms                                                 | 665 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                   |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.31x faster                                                   |
| pyflate                 | 675 ms                                                 | 399 ms: 1.69x faster                                                     |
| python_startup          | 13.9 ms                                                | 8.55 ms: 1.63x faster                                                    |
| python_startup_no_site  | 5.76 ms                                                | 6.13 ms: 1.06x slower                                                    |
| raytrace                | 461 ms                                                 | 278 ms: 1.66x faster                                                     |
| regex_compile           | 174 ms                                                 | 131 ms: 1.33x faster                                                     |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                     |
| regex_effbot            | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                    |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                    |
| richards                | 71.4 ms                                                | 45.6 ms: 1.56x faster                                                    |
| scimark_fft             | 414 ms                                                 | 312 ms: 1.33x faster                                                     |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 67.8 ms: 1.54x faster                                                    |
| scimark_sor             | 193 ms                                                 | 104 ms: 1.86x faster                                                     |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.20 ms: 1.30x faster                                                    |
| spectral_norm           | 148 ms                                                 | 97.1 ms: 1.53x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                    |
| sqlglot_transpile       | 2.42 ms                                                | 1.73 ms: 1.39x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                                    |
| sympy_expand            | 537 ms                                                 | 456 ms: 1.18x faster                                                     |
| sympy_integrate         | 23.9 ms                                                | 20.5 ms: 1.16x faster                                                    |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                     |
| sympy_str               | 324 ms                                                 | 285 ms: 1.14x faster                                                     |
| telco                   | 6.68 ms                                                | 6.31 ms: 1.06x faster                                                    |
| thrift                  | 1.03 ms                                                | 763 us: 1.35x faster                                                     |
| unpack_sequence         | 59.5 ns                                                | 42.6 ns: 1.39x faster                                                    |
| unpickle                | 14.3 us                                                | 13.8 us: 1.04x faster                                                    |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                                    |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                     |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                     |
| xml_etree_generate      | 93.3 ms                                                | 76.3 ms: 1.22x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-9e5a8e4/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4.json: djangocms