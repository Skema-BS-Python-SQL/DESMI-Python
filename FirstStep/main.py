def foo(x):
  if x == 0:
    bar()
    baz()
  else:
    qux(x)
    foo(x - 1)