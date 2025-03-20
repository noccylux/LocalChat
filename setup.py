from setuptools import setup


setup(
    # ...其他配置...
    entry_points={
        'console_scripts': [
            'localchat=localchat.cli:main',
        ],
    },
)