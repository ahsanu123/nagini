from pydantic import BaseModel
from nagini.https.emiten_codes import EmitenCode


class NaginiCliArgsModel(BaseModel):
    credential: str
    emitenCode: EmitenCode
