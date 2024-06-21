from typing import Optional, Iterable

import kopf
from kopf._cogs.structs import bodies, dicts, ids, patches

class NoAnnotationsDiffBaseStorage(kopf.AnnotationsDiffBaseStorage):
    def build(
            self,
            *,
            body: bodies.Body,
            extra_fields: Optional[Iterable[dicts.FieldSpec]] = None,
    ) -> bodies.BodyEssence:
        essence = super().build(body=body, extra_fields=extra_fields)
        return essence

    def fetch(
            self,
            *,
            body: bodies.Body,
    ) -> Optional[bodies.BodyEssence]:
        pass

    def store(
            self,
            *,
            body: bodies.Body,
            patch: patches.Patch,
            essence: bodies.BodyEssence,
    ) -> None:
        pass
