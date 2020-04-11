from distutils.core import setup

setup(
    name='deeply',
    packages=['deeply'],
    version='1.0',
    license='MIT',
    description='Deeply allow you to make your dataclasses more functional',
    author='Alex Dudko',
    author_email='duke@simfik.ru',
    url='https://github.com/SimfikDuke/deeply',
    download_url='https://github.com/SimfikDuke/deeply/archive/v_1.tar.gz',
    keywords=['web', 'dataclass', 'dict', 'api', 'easy', 'json'],
    install_requires=[
        'dacite',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
