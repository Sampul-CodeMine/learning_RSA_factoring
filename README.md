# Learning RSA Factoring

<center>A repository for educational purposes. Learning to get the factors to a number and checking for the factors that are co-prime</center>

---

## How it Works

This is a simple project for educational purposes.
It is does not deal with fast program algorithms as per complexities and
executions, but it teaches how multiple factors for a number is computed
and also to check if multiple pairs are co-prime

The program operates from 2 modes:

- If from the CLI a filepath is specified with the program name during execution, it reads from the file a line at a time and try to generate factors for the numbers

- If no filename is specified, it generates a random number and solves for the multiple factors and the co-primes.

- Raises: If the program freezes, and the CTRL + Z or CTRL + C keys are pressed, a KeyboardInterrupt error is generated.

> The example below shows the execution of the program specifying the path to the file that should be read from.
>
> Each line is read from the file until the `EOF` (End of File) is reached.
>

```bash
nerdie@PC $ time python main.py tests/test00

Generated Number: 7:
The list of factor(s):
[(7, 1)]
7 has prime multiple factors: [(7, 1)]

Generated Number: 9:
The list of factor(s):
[(3, 3)]
9 has prime multiple factors: [(3, 3)]

Generated Number: 12:
The list of factor(s):
[(6, 2), (4, 3), (3, 4), (2, 6)]
12 has no multiple factors that are both prime.

Generated Number: 34:
The list of factor(s):
[(17, 2), (2, 17)]
34 has prime multiple factors: (17, 2)

Generated Number: 45:
The list of factor(s):
[(15, 3), (9, 5), (5, 9), (3, 15)]
45 has no multiple factors that are both prime.

Generated Number: 49:
The list of factor(s):
[(7, 7)]
49 has prime multiple factors: [(7, 7)]

Generated Number: 99:
The list of factor(s):
[(33, 3), (11, 9), (9, 11), (3, 33)]
99 has no multiple factors that are both prime.

Generated Number: 331:
The list of factor(s):
[(331, 1)]
331 has prime multiple factors: [(331, 1)]

Generated Number: 479:
The list of factor(s):
[(479, 1)]
479 has prime multiple factors: [(479, 1)]

Generated Number: 617:
The list of factor(s):
[(617, 1)]
617 has prime multiple factors: [(617, 1)]

Generated Number: 623:
The list of factor(s):
[(89, 7), (7, 89)]
623 has prime multiple factors: (89, 7)

Generated Number: 852:
The list of factor(s):
[(426, 2), (284, 3), (213, 4), (142, 6), (71, 12), (12, 71), (6, 142), (4, 213), (3, 284), (2, 426)]
852 has no multiple factors that are both prime.

Generated Number: 4958:
The list of factor(s):
[(2479, 2), (134, 37), (74, 67), (67, 74), (37, 134), (2, 2479)]
4958 has no multiple factors that are both prime.

Generated Number: 5427:
The list of factor(s):
[(1809, 3), (603, 9), (201, 27), (81, 67), (67, 81), (27, 201), (9, 603), (3, 1809)]
5427 has no multiple factors that are both prime.

Generated Number: 6531:
The list of factor(s):
[(2177, 3), (933, 7), (311, 21), (21, 311), (7, 933), (3, 2177)]
6531 has no multiple factors that are both prime.


real    0m32.104s
user    0m0.031s
sys     0m0.093s
```

> If a wrong file is specified, the application raises an exception
>

```bash
nerdie@PC $ time python main.py tests/tes
[Errno 2] No such file or directory: 'tests/tes'

real    0m0.377s
user    0m0.015s
sys     0m0.078s
```

> If an invalid datatype or character was found within the file that is not integer, a `ValueError` or `TypeError` is raised
>

`tests/test00 # the file to read from`

```md
7
9
12
"56"
34
45
```

```bash
nerdie@PC $ time python main.py tests/test00

Generated Number: 7:
The list of factor(s):
[(7, 1)]
7 has prime multiple factors: [(7, 1)]

Generated Number: 9:
The list of factor(s):
[(3, 3)]
9 has prime multiple factors: [(3, 3)]

Generated Number: 12:
The list of factor(s):
[(6, 2), (4, 3), (3, 4), (2, 6)]
12 has no multiple factors that are both prime.

invalid literal for int() with base 10: '"56"'

real    0m0.394s
user    0m0.000s
sys     0m0.125s
```

> If during the program execution, the `CTRL + C` or `CTRL + Z` key was pressed, a `KeyboardInterrupt` exception is raised
>

```bash
nerdie@PC $ time python main.py tests/test00

Generated Number: 7:
The list of factor(s):
[(7, 1)]
7 has prime multiple factors: [(7, 1)]

Generated Number: 9:
The list of factor(s):
[(3, 3)]
9 has prime multiple factors: [(3, 3)]

Generated Number: 12:
The list of factor(s):
[(6, 2), (4, 3), (3, 4), (2, 6)]
12 has no multiple factors that are both prime.

Generated Number: 34:
The list of factor(s):
[(17, 2), (2, 17)]
34 has prime multiple factors: (17, 2)

Generated Number: 45:
The list of factor(s):
[(15, 3), (9, 5), (5, 9), (3, 15)]
45 has no multiple factors that are both prime.

Generated Number: 49:
The list of factor(s):
[(7, 7)]
49 has prime multiple factors: [(7, 7)]

Generated Number: 99:
The list of factor(s):
[(33, 3), (11, 9), (9, 11), (3, 33)]
99 has no multiple factors that are both prime.

Generated Number: 331:
The list of factor(s):
[(331, 1)]
331 has prime multiple factors: [(331, 1)]

Generated Number: 479:
The list of factor(s):
[(479, 1)]
479 has prime multiple factors: [(479, 1)]

Generated Number: 617:
The list of factor(s):
[(617, 1)]
617 has prime multiple factors: [(617, 1)]

Generated Number: 623:
The list of factor(s):
[(89, 7), (7, 89)]
623 has prime multiple factors: (89, 7)

Program was interrupted.


real    0m0.609s
user    0m0.015s
sys     0m0.093s
```

> If no filename is specified from the `CLI`, the program generates a random number and executes it.
>

```bash
nerdie@PC $ time python main.py

Generated Number: 154:
The list of factor(s):
[(77, 2), (22, 7), (14, 11), (11, 14), (7, 22), (2, 77)]
154 has no multiple factors that are both prime.


real    0m0.457s
user    0m0.031s
sys     0m0.125s
```

> As stated earlier, it is just for educational purposes, time complexities, execution time, were not factors considered.
>
> The program is opened to corrections, adjustments and refactoring.
>
---
<a href="http://sampulcodemine.hashnode.dev/" target="_blank">Ehigboria Dukeson O</a> | <a target="_blank" href="https://www.linkedin.com/in/dukeson-ehigboria">LinkedIn</a> | <a target="_blank" href="https://twitter.com/Sampul_CodeMine">Twitter</a>
