from typing import Protocol


# rust trait like in python
#
# this feel weird, static tool is not give me fail compile or waring message
# about "not implemented method inside class"
class SamplerTrait(Protocol):
    def sample(self) -> float: ...


class DriverTrait(Protocol):
    def set_value(self): ...


class Max31865Sampler(SamplerTrait, DriverTrait):
    def sample(self) -> float:
        return 1.0


class PT100Sampler(SamplerTrait, DriverTrait):
    def sample(self) -> float:
        return 1.0

    def set_value(self):
        print("somethink")
