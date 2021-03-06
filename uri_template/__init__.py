"""Module to implement something."""

from typing import Optional

from .uritemplate import ExpansionInvalid, ExpansionReserved, URITemplate
from .variable import Variable, VariableInvalid


__all__ = ['URITemplate', 'Variable', 'ExpansionInvalid', 'ExpansionReserved', 'VariableInvalid']


def expand(template: str, **kwargs, default_url: Optional[str] = None) -> Optional[str]:
    try:
        templ = URITemplate(template)
        return templ.expand(**kwargs)
    except Exception:
        return default_url


def partial(template: str, **kwargs) -> Optional[str]:
    try:
        templ = URITemplate(template)
        return str(templ.partial(**kwargs))
    except Exception:
        return None


def validate(template: str) -> bool:
    try:
        URITemplate(template)
        return True
    except Exception:
        return False
