from typing import List

from discord import Emoji

from discordmenu.embed.base import Box


class Text(Box):
    def __init__(self, value: str):
        super().__init__(self)
        self.value = value

    def to_markdown(self) -> str:
        return self.value


class BoldText(Box):
    def __init__(self, value: str):
        super().__init__(self)
        self._value = Text(value)

    def to_markdown(self) -> str:
        return "**{}**".format(self._value.to_markdown())

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = Text(value)


class LabeledText(Box):
    def __init__(self, name: str, value: str):
        super().__init__(self)
        self._name = BoldText(name)
        self._value = Text(value)

    def to_markdown(self) -> str:
        return "{} {}".format(self._name.to_markdown(), self._value.to_markdown())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = BoldText(name)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = Text(value)


class LinkedText(Box):
    def __init__(self, name: str, link: str):
        super().__init__(self)
        self._name = Text(name)
        self.link = link

    def to_markdown(self) -> str:
        return "[{}]({})".format(self._name.to_markdown(), self.link)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = Text(value)


class HighlightableLinks(Box):
    def __init__(self, links: List[LinkedText], highlighted: int, delimiter=", "):
        super().__init__(self)
        self.delimiter = delimiter
        self.links = links
        self._highlighted = links[highlighted]

    def _get_link_markdown(self, link: LinkedText) -> str:
        return link.to_markdown() if link != self.highlighted else BoldText(link.name.value).to_markdown()

    def to_markdown(self) -> str:
        return self.delimiter.join([self._get_link_markdown(link) for link in self.links])

    @property
    def highlighted(self):
        return self._highlighted

    @highlighted.setter
    def highlighted(self, highlighted):
        if len(self.links) <= highlighted < 0:
            raise Exception("Selected is out of bounds")
        self.highlighted = self.links[highlighted]


class CustomEmoji(Box):
    def __init__(self, emoji: Emoji):
        super().__init__(self)
        self.emoji = emoji

    def to_markdown(self) -> str:
        return "<{}:{}:{}>".format("a" if self.emoji.animated else "", self.emoji.name, self.emoji.id)
