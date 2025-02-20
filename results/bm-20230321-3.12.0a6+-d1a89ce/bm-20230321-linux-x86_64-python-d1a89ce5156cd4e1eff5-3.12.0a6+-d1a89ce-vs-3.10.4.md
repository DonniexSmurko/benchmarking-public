
# Results vs. 3.10.4

- fork: python
- ref: d1a89ce5156cd4e1eff5
- machine: linux-x86_64
- commit hash: d1a89ce
- commit date: 2023-03-21
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.35 ms: 1.44x faster                                                  |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.5 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 91.0 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.7 ms: 1.64x faster                                                  |
| float          | 109 ms                                                 | 74.3 ms: 1.47x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.34x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                  |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.42 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.59 ms: 1.40x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 56.0 ms: 1.33x faster                                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.23 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                   |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| unpickle_list        | 4.92 us                                                | 5.05 us: 1.03x slower                                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.88 ms: 1.59x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.56 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.1 ms: 1.45x faster                                                  |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                  |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.7 ms: 2.57x faster                                                  |
| deltablue               | 7.28 ms                                                | 3.17 ms: 2.30x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                   |
| logging_silent          | 176 ns                                                 | 94.8 ns: 1.86x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.82x faster                                                   |
| richards                | 75.2 ms                                                | 43.2 ms: 1.74x faster                                                  |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                   |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.2 ms: 1.64x faster                                                  |
| nbody                   | 144 ms                                                 | 87.7 ms: 1.64x faster                                                  |
| spectral_norm           | 150 ms                                                 | 92.0 ms: 1.63x faster                                                  |
| pyflate                 | 676 ms                                                 | 416 ms: 1.62x faster                                                   |
| chaos                   | 106 ms                                                 | 65.8 ms: 1.60x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                   |
| python_startup          | 14.1 ms                                                | 8.88 ms: 1.59x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 74.9 ms: 1.56x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.17 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                   |
| float                   | 109 ms                                                 | 74.3 ms: 1.47x faster                                                  |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.45x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.35 ms: 1.44x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.62 us: 1.44x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                  |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                  |
| coroutines              | 31.6 ms                                                | 22.2 ms: 1.42x faster                                                  |
| html5lib                | 85.9 ms                                                | 60.5 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                 |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                  |
| tornado_http            | 128 ms                                                 | 91.0 ms: 1.41x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.59 ms: 1.40x faster                                                  |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                  |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                                   |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                 |
| pprint_safe_repr        | 953 ms                                                 | 691 ms: 1.38x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                 |
| async_tree_memoization  | 855 ms                                                 | 624 ms: 1.37x faster                                                   |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                   |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                                   |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                   |
| regex_compile           | 177 ms                                                 | 133 ms: 1.34x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 44.4 ns: 1.34x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 56.0 ms: 1.33x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                  |
| genshi_xml              | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                  |
| fannkuch                | 488 ms                                                 | 368 ms: 1.33x faster                                                   |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                                  |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 735 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.28 ms: 1.27x faster                                                  |
| nqueens                 | 100 ms                                                 | 79.7 ms: 1.26x faster                                                  |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                 |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.7 ms: 1.22x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 788 us: 1.20x faster                                                   |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                  |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                                  |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                  |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                  |
| djangocms               | 36.9 us                                                | 32.5 us: 1.14x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.23 us: 1.12x faster                                                  |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                   |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                   |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.63 sec: 1.04x faster                                                 |
| async_generators        | 426 ms                                                 | 417 ms: 1.02x faster                                                   |
| telco                   | 6.73 ms                                                | 6.60 ms: 1.02x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| unpickle_list           | 4.92 us                                                | 5.05 us: 1.03x slower                                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.42 ms: 1.07x slower                                                  |
| gc_traversal            | 3.53 ms                                                | 3.84 ms: 1.09x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.56 ms: 1.14x slower                                                  |
| dask                    | 436 ms                                                 | 501 ms: 1.15x slower                                                   |
| coverage                | 74.7 ms                                                | 93.4 ms: 1.25x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230321-3.12.0a6+-d1a89ce/bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce.json: comprehensions
