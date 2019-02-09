#Intro
This is a repo for sample design patterns and programming idioms.

## Design Patterns
A **design pattern** is a way to manipulate object oriented classes in such a way that reduces code redundancy and simplifies class usage.

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