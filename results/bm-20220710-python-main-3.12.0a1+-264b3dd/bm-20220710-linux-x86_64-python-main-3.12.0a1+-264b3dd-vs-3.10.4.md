| Benchmark               | bm-20220323-linux-amd64-python-main-3.10.4-9d38120 | bm-20220710-linux-amd64-python-main-3.12.0a1+-264b3dd |
|-------------------------|:--------------------------------------------------:|:-----------------------------------------------------:|
| 2to3                    | 332 ms                                             | 249 ms: 1.33x faster                                  |
| chameleon               | 8.76 ms                                            | 6.30 ms: 1.39x faster                                 |
| chaos                   | 107 ms                                             | 65.0 ms: 1.64x faster                                 |
| crypto_pyaes            | 116 ms                                             | 74.3 ms: 1.57x faster                                 |
| deltablue               | 7.32 ms                                            | 3.24 ms: 2.26x faster                                 |
| django_template         | 45.7 ms                                            | 31.5 ms: 1.45x faster                                 |
| dulwich_log             | 75.2 ms                                            | 61.2 ms: 1.23x faster                                 |
| fannkuch                | 483 ms                                             | 378 ms: 1.28x faster                                  |
| float                   | 107 ms                                             | 72.4 ms: 1.48x faster                                 |
| go                      | 227 ms                                             | 130 ms: 1.74x faster                                  |
| hexiom                  | 9.29 ms                                            | 5.92 ms: 1.57x faster                                 |
| html5lib                | 85.1 ms                                            | 62.6 ms: 1.36x faster                                 |
| json                    | 5.55 ms                                            | 4.69 ms: 1.18x faster                                 |
| json_dumps              | 13.2 ms                                            | 11.8 ms: 1.11x faster                                 |
| json_loads              | 31.1 us                                            | 24.2 us: 1.28x faster                                 |
| logging_format          | 8.78 us                                            | 6.35 us: 1.38x faster                                 |
| logging_silent          | 168 ns                                             | 92.5 ns: 1.81x faster                                 |
| logging_simple          | 8.07 us                                            | 5.67 us: 1.42x faster                                 |
| mako                    | 14.7 ms                                            | 9.45 ms: 1.56x faster                                 |
| meteor_contest          | 114 ms                                             | 101 ms: 1.13x faster                                  |
| nbody                   | 135 ms                                             | 90.5 ms: 1.49x faster                                 |
| nqueens                 | 98.4 ms                                            | 80.8 ms: 1.22x faster                                 |
| pathlib                 | 20.1 ms                                            | 18.0 ms: 1.12x faster                                 |
| pickle                  | 10.2 us                                            | 10.5 us: 1.02x slower                                 |
| pickle_dict             | 27.2 us                                            | 31.6 us: 1.16x slower                                 |
| pickle_list             | 4.40 us                                            | 4.12 us: 1.07x faster                                 |
| pickle_pure_python      | 449 us                                             | 286 us: 1.57x faster                                  |
| pidigits                | 190 ms                                             | 193 ms: 1.01x slower                                  |
| pycparser               | 1.52 sec                                           | 1.06 sec: 1.43x faster                                |
| pyflate                 | 664 ms                                             | 398 ms: 1.67x faster                                  |
| python_startup          | 9.21 ms                                            | 8.16 ms: 1.13x faster                                 |
| python_startup_no_site  | 5.97 ms                                            | 6.01 ms: 1.01x slower                                 |
| raytrace                | 463 ms                                             | 286 ms: 1.62x faster                                  |
| regex_compile           | 178 ms                                             | 126 ms: 1.42x faster                                  |
| regex_dna               | 214 ms                                             | 207 ms: 1.04x faster                                  |
| regex_effbot            | 3.24 ms                                            | 3.54 ms: 1.09x slower                                 |
| regex_v8                | 25.7 ms                                            | 22.1 ms: 1.16x faster                                 |
| richards                | 68.9 ms                                            | 45.0 ms: 1.53x faster                                 |
| scimark_fft             | 419 ms                                             | 313 ms: 1.34x faster                                  |
| scimark_lu              | 160 ms                                             | 104 ms: 1.54x faster                                  |
| scimark_monte_carlo     | 107 ms                                             | 64.6 ms: 1.66x faster                                 |
| scimark_sor             | 196 ms                                             | 111 ms: 1.77x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                            | 4.18 ms: 1.30x faster                                 |
| spectral_norm           | 144 ms                                             | 97.7 ms: 1.47x faster                                 |
| sqlite_synth            | 2.92 us                                            | 2.62 us: 1.12x faster                                 |
| sympy_expand            | 538 ms                                             | 450 ms: 1.19x faster                                  |
| sympy_integrate         | 24.1 ms                                            | 20.1 ms: 1.20x faster                                 |
| sympy_str               | 325 ms                                             | 279 ms: 1.17x faster                                  |
| sympy_sum               | 184 ms                                             | 158 ms: 1.16x faster                                  |
| telco                   | 6.60 ms                                            | 6.51 ms: 1.01x faster                                 |
| thrift                  | 1.01 ms                                            | 720 us: 1.41x faster                                  |
| tornado_http            | 127 ms                                             | 91.3 ms: 1.39x faster                                 |
| unpack_sequence         | 56.1 ns                                            | 46.4 ns: 1.21x faster                                 |
| unpickle                | 14.4 us                                            | 13.1 us: 1.09x faster                                 |
| unpickle_list           | 4.90 us                                            | 5.04 us: 1.03x slower                                 |
| unpickle_pure_python    | 298 us                                             | 201 us: 1.48x faster                                  |
| xml_etree_generate      | 92.4 ms                                            | 75.9 ms: 1.22x faster                                 |
| xml_etree_iterparse     | 110 ms                                             | 104 ms: 1.06x faster                                  |
| xml_etree_parse         | 162 ms                                             | 156 ms: 1.04x faster                                  |
| xml_etree_process       | 72.6 ms                                            | 53.3 ms: 1.36x faster                                 |
| Geometric mean          | (ref)                                              | 1.30x faster                                          |
Ignored benchmarks (3) of /home/mdboom/Work/builds/self-hosted-runner-playground/results/bm-20220323-python-main-3.10.4-9d38120/bm-20220323-linux-amd64-python-main-3.10.4-9d38120.json: genshi_text, genshi_xml, pylint