import kopf

from .diff_base_storage import NoAnnotationsDiffBaseStorage
from .progress_store import NullProgressStore

kopf.nullstore = {}

# Optionally, attach your classes to the kopf namespace if you want to make them accessible via kopf directly.
kopf.NullProgressStore = NullProgressStore
kopf.NoAnnotationsDiffBaseStorage = NoAnnotationsDiffBaseStorage
