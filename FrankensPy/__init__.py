"""
This package depends on other subpackages. This will facilitate to impot.
"""
from __future__ import absolute_import



from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
