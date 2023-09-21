from setuptools import setup, find_packages

setup(
    name = 'instacrawler',
    version = '1.0.3',
    description = "The fastest way to check someone's instagram feed/story.",
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author = 'gibiee',
    author_email = 'gibiee@naver.com',
    url = 'https://github.com/gibiee/instacrawler',
    download_url = '',
    packages = find_packages(exclude=[]),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['pillow', 'beautifulsoup4', 'selenium', 'requests'],
    
    python_requires ='>=3.7',
    license = 'MIT',
    keywords = ['instacrawler', 'instagram', 'crawler', 'crawling', 'instagram-crawler', 'instagram-crawling'],
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)