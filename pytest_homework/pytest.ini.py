[pytest]
addopts = -ra -q
    --tb=short
    --showlocals
    -r a

markers =
    wizard: marks tests as wizard tests
    fast