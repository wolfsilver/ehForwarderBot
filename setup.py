import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise Exception("Python 3.6 or higher is required. Your version is %s." % sys.version)

long_description = open('README.rst', encoding="utf-8").read()

__version__ = ""
exec(open('ehforwarderbot/__version__.py').read())


tests_require = ["pytest", "mypy"]


setup(
    name='ehforwarderbot',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=__version__,
    description='An extensible message tunneling chat bot framework.',
    long_description=long_description,
    author='Eana Hufwe',
    author_email='ilove@1a23.com',
    url='https://efb.1a23.studio',
    license='AGPLv3+',
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    keywords=['EFB', 'EH Forwarder Bot', 'Chat tunneling', 'IM', 'messaging'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Typing :: Typed"
    ],
    install_requires=[
        "ruamel.yaml",
        "bullet",
        "cjkwrap",
        "typing_extensions"
    ],
    tests_require=tests_require,
    extras_require={
        'telemetry': ['1a23-telemetry'],
        'trace': ['hanging-threads'],
        'tests': tests_require
    },
    entry_points={
        "console_scripts": [
            'ehforwarderbot = ehforwarderbot.__main__:main',
            'efb-wizard = ehforwarderbot.wizard:main'
        ]
    },
    project_urls={
        "Documentation": "https://ehForwarderBot.readthedocs.io",
        "Telegram Chat": "https://t.me/EFBSupport",
        "Gitter Chat": "https://gitter.im/blueset/ehForwarderBot"
    }
)
