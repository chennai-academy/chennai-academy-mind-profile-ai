#!/usr/bin/env python3
"""
Chennai Academy Mind Profile AI
AI Powered Student Intelligence & Career Guidance Platform

An AI-powered educational intelligence platform that helps students,
parents, counsellors, and educational institutions understand a student's
cognitive profile, learning behavior, personality, aptitude, interests,
and career potential.
https://chennai.academy
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "student_profile": "Student Profile",
        "career_readiness": "Career Readiness",
        "learning_style": "Learning Style",
        "psychometric": "Psychometric",
        "multiple_intelligence": "Multiple Intelligence",
        "stream_readiness": "Stream Readiness",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_recommended_pathways(mi: int, career: int, stream: int) -> dict:
    return {
        "Engineering & Technology": min(100, round(mi * 1.05)),
        "Medicine & Healthcare": min(100, round(career * 1.0)),
        "Business & Management": min(100, round(stream * 1.1)),
        "Arts & Humanities": min(100, round(mi * 0.94)),
    }


def analyze_mind_profile(
    student: str,
    grade_level: str = "Grade-12",
    student_profile: int = 85,
    career_readiness: int = 82,
    learning_style: int = 88,
    psychometric: int = 78,
    multiple_intelligence: int = 90,
    stream_readiness: int = 80,
) -> dict:
    """
    Analyze student mind profile signals for AI-powered career guidance.

    Args:
        student: Student name or profile identifier
        grade_level: Current grade or education level
        student_profile: Student profile score (0-100)
        career_readiness: Career readiness score (0-100)
        learning_style: Learning style score (0-100)
        psychometric: Psychometric assessment score (0-100)
        multiple_intelligence: Multiple intelligence score (0-100)
        stream_readiness: Academic stream readiness score (0-100)

    Returns:
        dict with individual signal scores, overall mind profile index,
        and recommended career pathways
    """
    scores = {
        "student_profile": student_profile,
        "career_readiness": career_readiness,
        "learning_style": learning_style,
        "psychometric": psychometric,
        "multiple_intelligence": multiple_intelligence,
        "stream_readiness": stream_readiness,
    }
    overall_mind_profile_index = round(sum(scores.values()) / 6)

    return {
        "student": student,
        "grade_level": grade_level,
        "student_profile_score": student_profile,
        "career_readiness_score": career_readiness,
        "learning_style_score": learning_style,
        "psychometric_score": psychometric,
        "multiple_intelligence_score": multiple_intelligence,
        "stream_readiness_score": stream_readiness,
        "overall_mind_profile_index": overall_mind_profile_index,
        "priority_action": get_priority_action(scores),
        "recommended_pathways": get_recommended_pathways(multiple_intelligence, career_readiness, stream_readiness),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    student = args[0] if len(args) > 0 else "student-profile"
    grade_level = args[1] if len(args) > 1 else "Grade-12"
    student_profile = int(args[2]) if len(args) > 2 else 85
    career_readiness = int(args[3]) if len(args) > 3 else 82
    learning_style = int(args[4]) if len(args) > 4 else 88
    psychometric = int(args[5]) if len(args) > 5 else 78
    multiple_intelligence = int(args[6]) if len(args) > 6 else 90
    stream_readiness = int(args[7]) if len(args) > 7 else 80

    result = analyze_mind_profile(
        student, grade_level, student_profile, career_readiness,
        learning_style, psychometric, multiple_intelligence, stream_readiness
    )

    print(f"Student: {result['student']}")
    print(f"Grade Level: {result['grade_level']}")
    print("=" * 45)
    print(f"Student Profile Score:         {result['student_profile_score']}/100  [{get_status(result['student_profile_score'])}]")
    print(f"Career Readiness Score:        {result['career_readiness_score']}/100  [{get_status(result['career_readiness_score'])}]")
    print(f"Learning Style Score:          {result['learning_style_score']}/100  [{get_status(result['learning_style_score'])}]")
    print(f"Psychometric Score:            {result['psychometric_score']}/100  [{get_status(result['psychometric_score'])}]")
    print(f"Multiple Intelligence Score:   {result['multiple_intelligence_score']}/100  [{get_status(result['multiple_intelligence_score'])}]")
    print(f"Stream Readiness Score:        {result['stream_readiness_score']}/100  [{get_status(result['stream_readiness_score'])}]")
    print("=" * 45)
    print(f"Overall Mind Profile Index:    {result['overall_mind_profile_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nRecommended Career Pathways:")
    for pathway, score in result['recommended_pathways'].items():
        print(f"  {pathway:<30} {score}/100")


if __name__ == "__main__":
    main()
