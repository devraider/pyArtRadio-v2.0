from abc import ABC, abstractmethod
from model.song import Song


class DiscoverStrategy(ABC):
    """
    Base class for radio discovery strategies.

    This class provides the interface and common functionality for different
    strategies to discover radio stations.
    Subclasses should implement the specific discovery mechanisms.
    """
    @abstractmethod
    def discover(self) -> Song:
        raise NotImplementedError("Subclasses must implement the discover method")

