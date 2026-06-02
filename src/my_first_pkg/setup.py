from rclpy import publisher
from setuptools import find_packages, setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shubham',
    maintainer_email='shubhammanglaw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = my_first_pkg.publisher_node:main',
'subscriber_node = my_first_pkg.subscriber_node:main',
'distance_publisher = my_first_pkg.distance_publisher:main',
'distance_subscriber = my_first_pkg.distance_subscriber:main',
        ],
    },
)
