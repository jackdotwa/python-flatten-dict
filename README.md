# python-flatten-dict

Light-weight utility to flatten a nested json-like dictionary in python. For example:

```json
{"a": [0, 1],
 "b": {"c": 2},
 "d": [3, {"e": 4}]}
```
becomes

```json
{"a.0": 0,
 "a.1": 1,
 "b.c": 2,
 "d.0": 3,
 "d.1.e": 4
}
```
