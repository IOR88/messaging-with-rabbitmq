from os import path

import setuptools


def _get_version():
    filename = path.join('src', 'mwr', '__init__.py')
    glb = {}
    with open(filename) as fp:
        for line in fp:
            if '__version__' in line:
                exec(line, glb)
                return glb['__version__']
    raise RuntimeError('cannot find version')


setuptools.setup(
    name='mwr',
    version=_get_version(),
    description='Messaging with Rabbitmq',
    long_description=open('README.md').read(),
    author='Igor Miazek',
    author_email='igor_miazek@protonmail.com',
    url=None,
    download_url=None,
    license='MIT',
    namespace_packages=[],
    package_dir={'': 'src'},
    packages=[
        'mwr',
        'chat',
        'chat.migrations'

    ],
    include_package_data=True,
    install_requires=[
        'Django==2.2.7',
        'djangorestframework==3.10.3',
        'psycopg2-binary==2.8.5',
        'celery==4.4.2',
        'SQLAlchemy==1.3.16'
    ],
    entry_points='''
        [console_scripts]
        mwr-manage = manage:main
    '''
)
