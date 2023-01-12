
# Results vs. 3.11.0

- fork: faster_cpython
- ref: nogil
- machine: linux-x86_64
- commit hash: 258cab1
- commit date: 2022-12-21
- overall geometric mean: 1.26x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 382 ms: 1.48x slower                                         |
| chameleon      | 6.41 ms                                                | 8.19 ms: 1.28x slower                                        |
| docutils       | 2.60 sec                                               | 5.22 sec: 2.01x slower                                       |
| html5lib       | 63.2 ms                                                | 82.2 ms: 1.30x slower                                        |
| tornado_http   | 96.6 ms                                                | 124 ms: 1.28x slower                                         |
| Geometric mean | (ref)                                                  | 1.45x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 76.3 ms                                                | 104 ms: 1.37x slower                                         |
| nbody          | 95.0 ms                                                | 170 ms: 1.79x slower                                         |
| pidigits       | 199 ms                                                 | 186 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                  | 1.32x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 186 ms: 1.37x slower                                         |
| regex_dna      | 203 ms                                                 | 221 ms: 1.09x slower                                         |
| regex_effbot   | 3.36 ms                                                | 3.30 ms: 1.02x faster                                        |
| regex_v8       | 22.3 ms                                                | 24.4 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                  | 1.13x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 13.4 ms: 1.06x slower                                        |
| json_loads           | 26.2 us                                                | 32.4 us: 1.24x slower                                        |
| pickle               | 9.79 us                                                | 9.95 us: 1.02x slower                                        |
| pickle_dict          | 31.4 us                                                | 26.5 us: 1.18x faster                                        |
| pickle_list          | 4.17 us                                                | 4.23 us: 1.01x slower                                        |
| pickle_pure_python   | 304 us                                                 | 339 us: 1.12x slower                                         |
| unpickle             | 13.3 us                                                | 18.7 us: 1.41x slower                                        |
| unpickle_list        | 4.95 us                                                | 5.78 us: 1.17x slower                                        |
| unpickle_pure_python | 225 us                                                 | 263 us: 1.17x slower                                         |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                         |
| xml_etree_iterparse  | 103 ms                                                 | 95.8 ms: 1.07x faster                                        |
| xml_etree_generate   | 76.2 ms                                                | 88.8 ms: 1.17x slower                                        |
| xml_etree_process    | 53.8 ms                                                | 72.0 ms: 1.34x slower                                        |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 9.42 ms: 1.13x slower                                        |
| python_startup_no_site | 5.96 ms                                                | 5.92 ms: 1.01x faster                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 42.2 ms: 1.30x slower                                        |
| genshi_text     | 22.1 ms                                                | 52.4 ms: 2.37x slower                                        |
| genshi_xml      | 52.1 ms                                                | 74.0 ms: 1.42x slower                                        |
| mako            | 9.85 ms                                                | 16.4 ms: 1.66x slower                                        |
| Geometric mean  | (ref)                                                  | 1.64x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 382 ms: 1.48x slower                                         |
| aiohttp                 | 1.05 ms                                                | 1.44 ms: 1.37x slower                                        |
| async_generators        | 359 ms                                                 | 623 ms: 1.73x slower                                         |
| async_tree_none         | 529 ms                                                 | 371 ms: 1.43x faster                                         |
| async_tree_cpu_io_mixed | 752 ms                                                 | 616 ms: 1.22x faster                                         |
| async_tree_io           | 1.31 sec                                               | 827 ms: 1.58x faster                                         |
| async_tree_memoization  | 625 ms                                                 | 457 ms: 1.37x faster                                         |
| chameleon               | 6.41 ms                                                | 8.19 ms: 1.28x slower                                        |
| chaos                   | 68.6 ms                                                | 101 ms: 1.48x slower                                         |
| bench_mp_pool           | 24.0 ms                                                | 23.9 ms: 1.01x faster                                        |
| bench_thread_pool       | 810 us                                                 | 1.18 ms: 1.46x slower                                        |
| coroutines              | 26.1 ms                                                | 72.4 ms: 2.78x slower                                        |
| coverage                | 101 ms                                                 | 533 ms: 5.31x slower                                         |
| crypto_pyaes            | 73.9 ms                                                | 121 ms: 1.64x slower                                         |
| deepcopy                | 344 us                                                 | 394 us: 1.14x slower                                         |
| deepcopy_reduce         | 2.97 us                                                | 3.65 us: 1.23x slower                                        |
| deepcopy_memo           | 36.4 us                                                | 40.0 us: 1.10x slower                                        |
| deltablue               | 3.64 ms                                                | 5.41 ms: 1.49x slower                                        |
| django_template         | 32.5 ms                                                | 42.2 ms: 1.30x slower                                        |
| docutils                | 2.60 sec                                               | 5.22 sec: 2.01x slower                                       |
| dulwich_log             | 63.9 ms                                                | 77.8 ms: 1.22x slower                                        |
| fannkuch                | 388 ms                                                 | 491 ms: 1.26x slower                                         |
| flaskblogging           | 7.08 ms                                                | 12.2 ms: 1.72x slower                                        |
| float                   | 76.3 ms                                                | 104 ms: 1.37x slower                                         |
| generators              | 72.2 ms                                                | 81.3 ms: 1.13x slower                                        |
| genshi_text             | 22.1 ms                                                | 52.4 ms: 2.37x slower                                        |
| genshi_xml              | 52.1 ms                                                | 74.0 ms: 1.42x slower                                        |
| go                      | 143 ms                                                 | 159 ms: 1.11x slower                                         |
| gunicorn                | 1.12 ms                                                | 1.52 ms: 1.36x slower                                        |
| hexiom                  | 6.35 ms                                                | 7.69 ms: 1.21x slower                                        |
| html5lib                | 63.2 ms                                                | 82.2 ms: 1.30x slower                                        |
| json                    | 4.95 ms                                                | 5.44 ms: 1.10x slower                                        |
| json_dumps              | 12.7 ms                                                | 13.4 ms: 1.06x slower                                        |
| json_loads              | 26.2 us                                                | 32.4 us: 1.24x slower                                        |
| logging_format          | 6.62 us                                                | 7.50 us: 1.13x slower                                        |
| logging_silent          | 98.5 ns                                                | 96.4 ns: 1.02x faster                                        |
| logging_simple          | 6.06 us                                                | 6.85 us: 1.13x slower                                        |
| mako                    | 9.85 ms                                                | 16.4 ms: 1.66x slower                                        |
| mdp                     | 2.62 sec                                               | 3.04 sec: 1.16x slower                                       |
| meteor_contest          | 105 ms                                                 | 129 ms: 1.23x slower                                         |
| mypy                    | 669 ms                                                 | 1.13 sec: 1.69x slower                                       |
| nbody                   | 95.0 ms                                                | 170 ms: 1.79x slower                                         |
| nqueens                 | 85.0 ms                                                | 110 ms: 1.29x slower                                         |
| pathlib                 | 18.2 ms                                                | 20.4 ms: 1.12x slower                                        |
| pickle                  | 9.79 us                                                | 9.95 us: 1.02x slower                                        |
| pickle_dict             | 31.4 us                                                | 26.5 us: 1.18x faster                                        |
| pickle_list             | 4.17 us                                                | 4.23 us: 1.01x slower                                        |
| pickle_pure_python      | 304 us                                                 | 339 us: 1.12x slower                                         |
| pidigits                | 199 ms                                                 | 186 ms: 1.07x faster                                         |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                       |
| pycparser               | 1.17 sec                                               | 1.33 sec: 1.13x slower                                       |
| pyflate                 | 417 ms                                                 | 638 ms: 1.53x slower                                         |
| pylint                  | 463 ms                                                 | 633 ms: 1.37x slower                                         |
| python_startup          | 8.36 ms                                                | 9.42 ms: 1.13x slower                                        |
| python_startup_no_site  | 5.96 ms                                                | 5.92 ms: 1.01x faster                                        |
| raytrace                | 290 ms                                                 | 413 ms: 1.42x slower                                         |
| regex_compile           | 136 ms                                                 | 186 ms: 1.37x slower                                         |
| regex_dna               | 203 ms                                                 | 221 ms: 1.09x slower                                         |
| regex_effbot            | 3.36 ms                                                | 3.30 ms: 1.02x faster                                        |
| regex_v8                | 22.3 ms                                                | 24.4 ms: 1.09x slower                                        |
| richards                | 46.2 ms                                                | 39.1 ms: 1.18x faster                                        |
| scimark_fft             | 329 ms                                                 | 429 ms: 1.30x slower                                         |
| scimark_lu              | 107 ms                                                 | 151 ms: 1.40x slower                                         |
| scimark_monte_carlo     | 68.3 ms                                                | 102 ms: 1.49x slower                                         |
| scimark_sor             | 115 ms                                                 | 147 ms: 1.28x slower                                         |
| scimark_sparse_mat_mult | 4.40 ms                                                | 6.10 ms: 1.39x slower                                        |
| spectral_norm           | 99.9 ms                                                | 142 ms: 1.42x slower                                         |
| sqlglot_parse           | 1.37 ms                                                | 2.22 ms: 1.62x slower                                        |
| sqlglot_transpile       | 1.66 ms                                                | 2.58 ms: 1.56x slower                                        |
| sqlglot_optimize        | 53.0 ms                                                | 69.5 ms: 1.31x slower                                        |
| sqlglot_normalize       | 108 ms                                                 | 145 ms: 1.34x slower                                         |
| sqlite_synth            | 2.49 us                                                | 3.31 us: 1.33x slower                                        |
| sympy_expand            | 472 ms                                                 | 538 ms: 1.14x slower                                         |
| sympy_integrate         | 20.9 ms                                                | 25.3 ms: 1.21x slower                                        |
| sympy_sum               | 166 ms                                                 | 211 ms: 1.27x slower                                         |
| sympy_str               | 287 ms                                                 | 333 ms: 1.16x slower                                         |
| telco                   | 6.62 ms                                                | 7.24 ms: 1.09x slower                                        |
| thrift                  | 752 us                                                 | 988 us: 1.31x slower                                         |
| tornado_http            | 96.6 ms                                                | 124 ms: 1.28x slower                                         |
| unpack_sequence         | 43.4 ns                                                | 52.6 ns: 1.21x slower                                        |
| unpickle                | 13.3 us                                                | 18.7 us: 1.41x slower                                        |
| unpickle_list           | 4.95 us                                                | 5.78 us: 1.17x slower                                        |
| unpickle_pure_python    | 225 us                                                 | 263 us: 1.17x slower                                         |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                         |
| xml_etree_iterparse     | 103 ms                                                 | 95.8 ms: 1.07x faster                                        |
| xml_etree_generate      | 76.2 ms                                                | 88.8 ms: 1.17x slower                                        |
| xml_etree_process       | 53.8 ms                                                | 72.0 ms: 1.34x slower                                        |
| Geometric mean          | (ref)                                                  | 1.26x slower                                                 |
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.9.10-258cab1/bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json: djangocms