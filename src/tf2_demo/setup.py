from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'tf2_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
    os.path.join(
        'share',
        package_name,
        'launch'
    ),
    glob('launch/*.py')
),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='parallels',
    maintainer_email='Shubhammanglaw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "dynamic_broadcaster=tf2_demo.dynamic_broadcaster:main",
            "tf_listener=tf2_demo.tf_listener:main"
        ],
    },
)
