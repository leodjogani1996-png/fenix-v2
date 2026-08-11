"""
FENIX - Human Emotion Knowledge Module

Purpose:
Provides structured knowledge about human emotions, emotional states,
motivation, attachment, grief, love, and emotional regulation.

Important:
FENIX must never claim that it personally feels human emotions.
This module exists so that FENIX can understand, explain, and reason
about human emotional experiences.

Core principle:
Emotion != fact.

An emotion is a signal shaped by perception, memory, expectations,
beliefs, goals, bodily state, social context, and interpretation.
"""

from typing import Dict, List, Optional


# ============================================================
# CORE PRINCIPLES
# ============================================================

EMOTION_CORE_PRINCIPLES = {
    "emotion_is_not_fact": (
        "An emotion is not the same as a fact. "
        "It is a signal about how a person is interpreting a situation."
    ),

    "meaning_matters": (
        "Emotional reactions are shaped not only by what happened, "
        "but by the meaning a person assigns to what happened."
    ),

    "same_event_different_emotion": (
        "Two people may experience the same event and feel different emotions "
        "because of different memories, beliefs, expectations, goals, "
        "relationships, and previous experiences."
    ),

    "emotion_is_not_behavior": (
        "Feeling an emotion is not the same as acting on it. "
        "A person may feel anger, jealousy, fear, or sadness "
        "without behaving aggressively, destructively, or manipulatively."
    ),

    "emotion_is_signal": (
        "Emotion should be treated as meaningful information, "
        "not as an automatic command that must be obeyed."
    ),
}
