from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ros2_advanced'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*'),
        ),
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*'),
        ),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shubham',
    maintainer_email='Shubhammanglaw@gmail.com',
    description='Advanced ROS 2 learning package',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'validation_node = ros2_advanced.nodes.parameters.validation_node:main',
            'descriptor_node = ros2_advanced.nodes.parameters.descriptor_node:main',
        ],
    },
)
