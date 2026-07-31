from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chennai-academy-mind-profile-ai",
    version="1.0.0",
    author="Chennai.Academy",
    author_email="info@chennai.academy",
    description="AI Powered Student Intelligence & Career Guidance Platform — Chennai Academy Mind Profile AI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://chennai.academy",
    project_urls={
        "Homepage": "https://chennai.academy",
        "GitHub": "https://github.com/chennai-academy/chennai-academy-mind-profile-ai",
        "Documentation": "https://chennai-academy-mind-profile-ai.readthedocs.io",
        "PyPI": "https://pypi.org/project/chennai-academy-mind-profile-ai",
    },
    py_modules=["mind_profile"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "mind-profile-ai",
        "student-intelligence",
        "career-guidance",
        "psychometric-assessment",
        "multiple-intelligence",
        "learning-style",
        "stream-selection",
        "chennai-academy",
    ],
    entry_points={
        "console_scripts": [
            "mind-profile-ai=mind_profile:main",
        ],
    },
)
