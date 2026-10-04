"""Testes da criação de site pela distribuição."""

#: Objects per portal type with the example content (``setup_content=True``).
EXAMPLE_CONTENT: dict[str, int] = {
    "Document": 15,
    "Image": 5,
    "News Item": 1,
    "Plone Site": 1,
}

#: Objects per portal type with only the base content (``setup_content=False``).
BASE_CONTENT: dict[str, int] = {
    "Document": 2,
    "Image": 3,
    "Plone Site": 1,
}
