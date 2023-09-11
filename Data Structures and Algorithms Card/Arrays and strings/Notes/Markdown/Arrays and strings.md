An array or a string will be part of many problems as input.

Technically, an array can't be resized. A dynamic array, or list, can be. We will refer to dynamic arrays/lists using the word "array".

Strings in Python and Java are immutable while in C++ they are mutable. Mutable means it can be changed. Immutable means it can't be. If you want to change something immutable, you will need to recreate the entire thing.

Sometimes you are dealing with strings with 100,000 characters, so creating new versions just to modify, say for instance, one character is very expensive (O(n) where n is the size of the string).

