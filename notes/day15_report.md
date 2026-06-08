# Day 15 Report — Configuration Profiles & YAML Deployment

## Objective
Move robot configuration out of source code and into reusable YAML configuration profiles.

## Package
my_first_pkg

## Work Completed

### Created Configuration Profiles

#### indoor.yaml
```yaml
/**:
  ros__parameters:
    max_linear_speed: 0.2
    max_angular_speed: 0.5
```

#### outdoor.yaml
```yaml
/**:
  ros__parameters:
    max_linear_speed: 1.0
    max_angular_speed: 2.0
```

#### testing.yaml
```yaml
/**:
  ros__parameters:
    max_linear_speed: 0.1
    max_angular_speed: 0.2
```
### setup.py Changes

Added YAML installation support:

```python
from glob import glob

('share/' + package_name + '/config',
 glob('config/*.yaml'))
```

## Validation

### Indoor Profile

Command:
```bash
ros2 run my_first_pkg velocity_limiter --ros-args --params-file config/indoor.yaml
```

Results:
- max_linear_speed = 0.2
- max_angular_speed = 0.5

### Testing Profile

Results:
- max_linear_speed = 0.1
- max_angular_speed = 0.2

### Parameter Dump

```yaml
/velocity_limiter:
  ros__parameters:
    max_angular_speed: 0.2
    max_linear_speed: 0.1
    start_type_description_service: true
    use_sim_time: false
```

## Key Learnings

- ROS 2 parameters can be stored in YAML files.
- One codebase can support multiple robot configurations.
- Configuration should be separated from software logic.
- setup.py must install configuration files for deployment.
- ros2 param dump validates active runtime parameters.

## Reflection

1. YAML files allow parameter changes without editing source code.
2. Multiple robots can be supported using separate configuration profiles.
3. Separating configuration from software improves maintainability and scalability.
4. Hardcoded values make deployments difficult and increase maintenance effort.

## Outcome

Built a deployable robot configuration system using YAML parameter profiles and verified runtime parameter loading through ROS 2 tools.
