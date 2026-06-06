from abc import ABC, abstractmethod


class BaseAIService(ABC):

    @abstractmethod
    def initialize(self):
        """Initialize AI model"""
        pass

    @abstractmethod
    def analyze(self, frame):
        """Analyze current frame"""
        pass

    @abstractmethod
    def health(self):
        """Return service health"""
        pass

    @abstractmethod
    def shutdown(self):
        """Release resources"""
        pass