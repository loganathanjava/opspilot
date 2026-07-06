from abc import ABC, abstractmethod


class Page(ABC):
    """
    Base class for every page in OpsPilot.
    """

    id: str = ""
    title: str = ""
    icon: str = ""

    @abstractmethod
    def render(self):
        """
        Render the page.
        """
        raise NotImplementedError