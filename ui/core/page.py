from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(slots=True)
class Page(ABC):
    """
    Base class for every page in OpsPilot.
    """

    id: str
    title: str
    icon: str
    description: str = ""
    category: str = "General"
    order: int = 0
    permissions: list[str] = field(default_factory=list)

    @abstractmethod
    def render(self) -> None:
        """
        Render the page.
        """
        raise NotImplementedError