# Day 16 Report – Advanced Launch & Parameter Validation

**Date:** 2026-06-08  
**Status:** ✅ Completed

## Objective

Learn ROS 2 runtime parameter validation using parameter callbacks and implement safety checks that prevent invalid configuration values from being applied to a running node.

---

# Concepts Learned

## 1. Parameter Validation Callback

ROS 2 provides:

```python
self.add_on_set_parameters_callback(
    self.validate_parameters
)
```

This callback executes before parameter updates are applied.

Benefits:

- Accept valid updates
- Reject invalid updates
- Return useful error messages
- Keep node configuration safe

---

## 2. SetParametersResult

Imported:

```python
from rcl_interfaces.msg import SetParametersResult
```

Used to tell ROS whether a parameter update should be accepted.

### Reject Update

```python
result.successful = False
result.reason = "error message"
```

### Accept Update

```python
result.successful = True
result.reason = ""
```

---

## 3. Multiple Parameter Updates

The callback receives:

```python
parameters
```

which is a list.

Reason:

ROS can update multiple parameters in a single request.

Example:

```text
max_linear_speed = 2.0
max_angular_speed = 3.0
```

The callback must validate all proposed updates before accepting them.

---

## 4. Defensive Programming

Instead of trusting users to always enter valid values:

```text
Validate first
Apply second
```

This prevents invalid robot configurations.

---

# Implementation

Created:

```text
velocity_limiter_v3.py
```

Added validation callback registration:

```python
self.add_on_set_parameters_callback(
    self.validate_parameters
)
```

Validation rules:

### max_linear_speed

```text
0 < value <= 5.0
```

### max_angular_speed

```text
0 < value <= 10.0
```

Invalid values are rejected before they are applied.

---

# Final Validation Function

```python
def validate_parameters(self, parameters):
    for parameter in parameters:

        if parameter.name == "max_linear_speed":
            if not (0 < parameter.value <= 5.0):
                result = SetParametersResult()
                result.successful = False
                result.reason = "max_linear_speed must be > 0 and <= 5.0"
                self.get_logger().warn(result.reason)
                return result

        elif parameter.name == "max_angular_speed":
            if not (0 < parameter.value <= 10.0):
                result = SetParametersResult()
                result.successful = False
                result.reason = "max_angular_speed must be > 0 and <= 10.0"
                self.get_logger().warn(result.reason)
                return result

    result = SetParametersResult()
    result.successful = True
    result.reason = ""

    self.get_logger().info(
        f"Parameter {parameter.name} validated successfully"
    )

    return result
```

---

# Testing Performed

## Test 1 – Reject Negative Value

Command:

```bash
ros2 param set /velocity_limiter max_linear_speed -1.0
```

Output:

```text
Setting parameter failed: max_linear_speed must be > 0 and <= 5.0
```

Result: ✅ PASS

---

## Test 2 – Reject Oversized Value

Command:

```bash
ros2 param set /velocity_limiter max_linear_speed 6.0
```

Output:

```text
Setting parameter failed: max_linear_speed must be > 0 and <= 5.0
```

Result: ✅ PASS

---

## Test 3 – Accept Valid Value

Command:

```bash
ros2 param set /velocity_limiter max_linear_speed 2.0
```

Output:

```text
Set parameter successful
```

Result: ✅ PASS

---

## Test 4 – Verify Previous Value Is Preserved

Commands:

```bash
ros2 param set /velocity_limiter max_linear_speed 2.0
ros2 param set /velocity_limiter max_linear_speed 6.0
ros2 param get /velocity_limiter max_linear_speed
```

Output:

```text
Set parameter successful
Setting parameter failed: max_linear_speed must be > 0 and <= 5.0
Double value is: 2.0
```

Result: ✅ PASS

Observation:

Rejected updates do not overwrite the previous valid value.

---

# Debugging & Mistakes

## Mistake 1

Returned success inside the loop.

Incorrect:

```python
for parameter in parameters:
    return success
```

Problem:

Only the first parameter would be checked.

Fix:

Move the success return outside the loop.

---

## Mistake 2

Used:

```bash
ros2 param set /velocity_limiter max_linear_speed -1
```

ROS rejected it before validation.

Error:

```text
Wrong parameter type, expected DOUBLE got INTEGER
```

Fix:

```bash
ros2 param set /velocity_limiter max_linear_speed -1.0
```

---

## Mistake 3

Initially thought validation should happen inside:

```python
velocity_callback()
```

Realization:

Validation must happen before ROS applies parameter changes.

Correct solution:

```python
add_on_set_parameters_callback()
```

---

# Key Learnings

1. ROS parameters can be validated before they are applied.
2. Parameter callbacks receive a list because multiple parameters may be updated together.
3. Invalid updates should be rejected immediately.
4. Previous valid values remain unchanged after failed updates.
5. Defensive programming improves robot reliability and safety.
6. Validation callbacks are event-driven and executed automatically by ROS.

---

# Confidence Rating

| Topic | Confidence |
|---------|---------|
| Parameter Files | 9/10 |
| Runtime Parameters | 9/10 |
| Parameter Callbacks | 8/10 |
| Validation Logic | 8/10 |
| Launch Concepts | 7/10 |

**Overall Confidence: 8.2/10**

---

# Reflection

This day focused more on software engineering and system safety than ROS commands.

The most important lesson was understanding how ROS validates parameter changes before applying them and how defensive programming prevents a running robot from entering an invalid state.

I learned not only how to use parameters but also how to protect them through validation callbacks and maintain a safe configuration throughout runtime.