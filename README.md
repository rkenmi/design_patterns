## About

This is a repo for sample design patterns and programming idioms.

## Design Patterns
Design patterns are higher level than libraries. Design patterns tell us how to structure classes and objects to solve certain problems and it is our job to adapt those designs to fit our particular application.

> Good OO designs are reusable, extensible, and maintainable

Design patterns are based off of one simple principle:
> *take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don't*

### Composition vs. Inheritance
Favor composition over inheritance. It lets you *change behavior at runtime* as long as the object you're composing with implements the correct behavior interface.

## Programming Idioms
A **programming idiom** is the *usual* way to accomplish a task with a particular language.

For example, in C:

```
for (int i = 0; i < sizeof(arr); i++)
```

is the idiom for executing some loop over an array.

In PHP, you can do the equivalent:

```
for ($i = 1; $i <= sizeof($arr); $i++)
```

but it is discouraged to write a for-loop in this way in PHP, so this is not considered an idiom.

An idiom for this in PHP would instead be:

```
foreach ($arr as $value)
```

Likewise, in Python:

```
for value in arr:
```