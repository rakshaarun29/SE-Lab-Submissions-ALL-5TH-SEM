# Lab 7: Hypothesis fuzz testing

The handout refers to `processor.py` and `test_processor.py`. This repository uses the equivalent names `self_storage.py` and `test_self_storage.py`.

Run from this directory:

```powershell
python -m pip install hypothesis pytest
python self_storage.py
python -m pytest -q test_self_storage.py
```

The functions reject invalid input with `ValueError`. `duration_average` returns the floor of the arithmetic mean, and payable rent applies 18% tax before subtracting the discount, with a zero floor.
