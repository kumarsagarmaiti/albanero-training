# Similar to NuGet.org & Npmjs.org, Python also has its own official third-party software repository. The Python Package Index (PyPI) is a repository of software that hosts an extensive collection of Python packages, development frameworks, tools, and libraries.

# PyPI packages allow developers to share and reuse code rather than having to reinvent the wheel. As PyPI grew, the need for a package manager became so apparent that Python eventually created its own standard package manager: pip.
# Pip is built-in to Python, and can install packages from many different sources. But PyPI.org is the primary and default package source used.

# Pip is Python’s package manager, providing essential core features for installing and maintaining Python packages and their dependencies. While many Python developers use Pip as a Dependency Manager, it was never intended to be used as one. Pip will not flag dependency conflicts. As a result, it will happily install multiple versions of a dependency into your project, which will likely result in errors.

# One way to avoid dependency conflicts is to use an alternative Python package manager, like conda, poetry or ActiveState’s State Tool. While all three perform dependency resolution (unlike pip), only the State Tool is capable of resolving dependency conflicts, eliminating dependency hell. The easiest way to install the State Tool is to install Python 3.9 from ActiveState.
