
## Special characters

```
. Matches any single character except newline
^ Matches the start of the string
$ Matches the end of the string
* Matches 0 or more repetitions of the preceding element
+ Matches 1 or more repetitions of the preceding element
? Matches 0 or 1 repetition of the preceding element
{m,n} Matches between m and n repetitions of the preceding element
[abc] Matches any single character a, b, or c
| Acts as a logical OR
\d: Any digit, equivalent to [0-9]
\w: Any word character (letter, digit, underscore), equivalent to [a-zA-Z0-9_]
\s: Any whitespace character (space, tab, newline, etc.)
\D: Not a digit
\W: Not a word character
\S: Not whitespace character

\b: Matches a word boundary. This is a zero-width assertion that matches only the position between a word character and a non-word character.
\B: Matches where there is not a word boundary.
\A: Matches only at the start of the string.
\Z: Matches only at the end of the string or just before a newline at the end.
\z: Matches only at the end of the string.
\G: Matches the point where the last match finished.

\\: Matches a literal backslash (\).
\.: Matches a literal dot.
\*: Matches a literal asterisk.
\+: Matches a literal plus sign.
\?: Matches a literal question mark.
\|: Matches a literal pipe (used for logical OR in regex).
\{ and \}: Match literal curly braces.
\( and \): Match literal parentheses.
\[ and \]: Match literal square brackets.
\^: Matches a literal caret.
\$: Matches a literal dollar sign.
```

Escapes: \ is used to escape special characters.

## The re module

The re module provides a suite of functions that make it possible to search a string for a match:

re.search(): Scans through a string, looking for any location where the regex pattern produces a match.
re.match(): Determines if the regex matches at the beginning of the string.
re.findall(): Finds all substrings where the regex matches, and returns them as a list.
re.finditer(): Similar to re.findall(), but returns an iterator yielding match objects.
re.sub(): Replaces the matches with a string or the result of a function.

## Examples

```python
import re

# Using re.search()
match = re.search(r'\d+', 'The recipe calls for 10 strawberries and 1 banana')
if match:
    print('Found number:', match.group())  # Output: Found number: 10

# Using re.findall()
numbers = re.findall(r'\d+', 'There are 3 apples, 20 bananas, and 15 peaches')
print(numbers)  # Output: ['3', '20', '15']

# Using re.sub()
text = "He's a very very good boy."
replaced_text = re.sub(r'\bvery\b', 'extremely', text)
print(replaced_text)  # Output: He's an extremely extremely good boy.
```


# Reference

https://poe.com/chat/2xq4orcgmzhujjmhd7f
