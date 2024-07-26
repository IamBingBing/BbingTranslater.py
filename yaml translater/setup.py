from setuptools import setup, find_packages

setup(
    name='B.bingTranslater',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tk>= 0.0.0',
        'pyyaml>= 0.0.0',
        
        'requests>= 0.0.0',
        'pip >= 0.0.0'
    ],
    entry_points={
        'console_scripts': ''
    },
    author='lee jongwon',
    author_email='03lonnie@naver.com',
    description='translate yaml value eng to kor ',
    url='https://github.com/iambingbing',  # 프로젝트 URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: do not sell this program then do whatever you want with it',
    ]
)