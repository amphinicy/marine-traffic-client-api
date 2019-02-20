from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Marine Traffic API',
    version='0.4.0',

    description='Marine Traffic Client Api',
    long_description=readme(),
    long_description_content_type='text/markdown',

    url='https://github.com/arrrlo/marine-traffic-client-api',
    licence='MIT',

    author='Ivan Arar',
    author_email='ivan.arar@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='marine traffic, api, cruise, distance, port, vessel, track, fleet',

    packages=find_packages(),
    install_requires=[
        'click~=6.7',
        'lxml>=4.3.0',
        'ujson>=1.35',
        'requests~=2.20.0'
    ],

    project_urls={
        'Source': 'https://github.com/arrrlo/marine-traffic-client-api',
    },
)
