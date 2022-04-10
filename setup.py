from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

setup(
    name='readme-helper',
    version='0.0.1',
    description='Helpers for generating README files',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/readme-helper',
    download_url='https://github.com/kenjyco/readme-helper/tarball/v0.0.1',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=requirements,
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: Markup :: Markdown',
        'Topic :: Text Processing :: Markup :: reStructuredText',
        'Topic :: Utilities',
    ],
    keywords=['readme', 'cli', 'command-line', 'markdown', 'reStructuredText', 'jinja', 'template', 'pandoc', 'helper', 'kenjyco']
)
