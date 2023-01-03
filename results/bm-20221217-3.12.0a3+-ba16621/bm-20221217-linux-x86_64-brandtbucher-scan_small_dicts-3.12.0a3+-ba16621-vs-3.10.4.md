Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                     |
| chameleon      | 8.86 ms                                                | 6.26 ms: 1.42x faster                                                    |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                   |
| html5lib       | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.0 ms: 1.50x faster                                                    |
| nbody          | 136 ms                                                 | 94.1 ms: 1.45x faster                                                    |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.33x faster                                                     |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                     |
| regex_effbot   | 3.21 ms                                                | 3.50 ms: 1.09x slower                                                    |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                    |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                    |
| pickle               | 10.1 us                                                | 10.1 us: 1.00x faster                                                    |
| pickle_dict          | 28.3 us                                                | 30.9 us: 1.09x slower                                                    |
| pickle_list          | 4.50 us                                                | 4.10 us: 1.10x faster                                                    |
| pickle_pure_python   | 453 us                                                 | 281 us: 1.61x faster                                                     |
| unpickle             | 14.3 us                                                | 13.0 us: 1.09x faster                                                    |
| unpickle_list        | 4.99 us                                                | 5.09 us: 1.02x slower                                                    |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                 | 107 ms: 1.04x faster                                                     |
| xml_etree_generate   | 93.3 ms                                                | 76.2 ms: 1.22x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.51 ms: 1.64x faster                                                    |
| python_startup_no_site | 5.76 ms                                                | 6.09 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                    |
| genshi_xml      | 63.6 ms                                                | 46.9 ms: 1.36x faster                                                    |
| mako            | 14.3 ms                                                | 9.42 ms: 1.51x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                     |
| async_generators        | 428 ms                                                 | 348 ms: 1.23x faster                                                     |
| async_tree_none         | 713 ms                                                 | 533 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 629 ms: 1.36x faster                                                     |
| chameleon               | 8.86 ms                                                | 6.26 ms: 1.42x faster                                                    |
| chaos                   | 104 ms                                                 | 67.3 ms: 1.55x faster                                                    |
| bench_thread_pool       | 943 us                                                 | 777 us: 1.21x faster                                                     |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                                    |
| coverage                | 75.3 ms                                                | 101 ms: 1.34x slower                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.5 ms: 1.56x faster                                                    |
| deepcopy                | 429 us                                                 | 323 us: 1.33x faster                                                     |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                                    |
| deepcopy_memo           | 50.0 us                                                | 33.2 us: 1.51x faster                                                    |
| deltablue               | 7.39 ms                                                | 3.22 ms: 2.29x faster                                                    |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                    |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                   |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                                    |
| fannkuch                | 477 ms                                                 | 377 ms: 1.27x faster                                                     |
| float                   | 108 ms                                                 | 72.0 ms: 1.50x faster                                                    |
| generators              | 75.8 ms                                                | 77.0 ms: 1.02x slower                                                    |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                    |
| genshi_xml              | 63.6 ms                                                | 46.9 ms: 1.36x faster                                                    |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                     |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                                    |
| html5lib                | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                    |
| json                    | 5.35 ms                                                | 4.81 ms: 1.11x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                    |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                    |
| logging_format          | 8.92 us                                                | 6.26 us: 1.42x faster                                                    |
| logging_silent          | 173 ns                                                 | 91.9 ns: 1.88x faster                                                    |
| logging_simple          | 8.06 us                                                | 5.72 us: 1.41x faster                                                    |
| mako                    | 14.3 ms                                                | 9.42 ms: 1.51x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                   |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                     |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                     |
| nbody                   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                    |
| nqueens                 | 99.3 ms                                                | 77.4 ms: 1.28x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.15x faster                                                    |
| pickle                  | 10.1 us                                                | 10.1 us: 1.00x faster                                                    |
| pickle_dict             | 28.3 us                                                | 30.9 us: 1.09x slower                                                    |
| pickle_list             | 4.50 us                                                | 4.10 us: 1.10x faster                                                    |
| pickle_pure_python      | 453 us                                                 | 281 us: 1.61x faster                                                     |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                     |
| pprint_safe_repr        | 943 ms                                                 | 669 ms: 1.41x faster                                                     |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.45x faster                                                   |
| pycparser               | 1.51 sec                                               | 1.08 sec: 1.40x faster                                                   |
| pyflate                 | 675 ms                                                 | 407 ms: 1.66x faster                                                     |
| python_startup          | 13.9 ms                                                | 8.51 ms: 1.64x faster                                                    |
| python_startup_no_site  | 5.76 ms                                                | 6.09 ms: 1.06x slower                                                    |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                     |
| regex_compile           | 174 ms                                                 | 130 ms: 1.33x faster                                                     |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                     |
| regex_effbot            | 3.21 ms                                                | 3.50 ms: 1.09x slower                                                    |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                                    |
| richards                | 71.4 ms                                                | 42.0 ms: 1.70x faster                                                    |
| scimark_fft             | 414 ms                                                 | 310 ms: 1.33x faster                                                     |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.51x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 66.0 ms: 1.59x faster                                                    |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.84x faster                                                     |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.01 ms: 1.37x faster                                                    |
| spectral_norm           | 148 ms                                                 | 95.1 ms: 1.56x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                    |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 50.3 ms: 1.30x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                                    |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.18x faster                                                     |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                    |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                     |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                     |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                                    |
| thrift                  | 1.03 ms                                                | 754 us: 1.37x faster                                                     |
| unpack_sequence         | 59.5 ns                                                | 42.1 ns: 1.41x faster                                                    |
| unpickle                | 14.3 us                                                | 13.0 us: 1.09x faster                                                    |
| unpickle_list           | 4.99 us                                                | 5.09 us: 1.02x slower                                                    |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                     |
| xml_etree_iterparse     | 110 ms                                                 | 107 ms: 1.04x faster                                                     |
| xml_etree_generate      | 93.3 ms                                                | 76.2 ms: 1.22x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221217-3.12.0a3+-ba16621/bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621.json: djangocms