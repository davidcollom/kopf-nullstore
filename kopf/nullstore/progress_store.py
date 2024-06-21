from typing import Optional, Iterable

import kopf
from kopf._cogs.structs import bodies, dicts, ids, patches

class NullProgressStore(kopf.ProgressStorage):
    def fetch(self, *, key: ids.HandlerId, body: bodies.Body,) -> Optional[kopf.ProgressRecord]:
        return None
    def store(
              self,
              *,
              key: ids.HandlerId,
              record: kopf.ProgressRecord,
              body: bodies.Body,
              patch: patches.Patch) -> None:
        pass
    def purge(self, *, key: ids.HandlerId, body: bodies.Body, patch: patches.Patch,):
        pass
    def touch(self, *, body: bodies.Body, patch: patches.Patch, value: Optional[str],):
        pass
    def clear(self, *, essence: bodies.BodyEssence) -> bodies.BodyEssence:
        essence = super().clear(essence=essence)
        return essence
