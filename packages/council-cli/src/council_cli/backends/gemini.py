"""Gemini CLI backend."""

from __future__ import annotations

from council_cli.backends.base import CLIBackend
from council_cli.config import BACKENDS


class GeminiBackend(CLIBackend):
    """Wrapper for Google's Gemini CLI (gemini -p)."""

    name = "gemini"
    command = "gemini"

    def __init__(self, model: str | None = None) -> None:
        spec = BACKENDS["gemini"]
        self.default_model = model or spec.default_model

    def build_args(self, prompt: str, *, model: str | None = None) -> list[str]:
        effective_model = model or self.default_model
        return [
            "gemini",
            "-p", prompt,
            "-m", effective_model,
            "-o", "text",
        ]
