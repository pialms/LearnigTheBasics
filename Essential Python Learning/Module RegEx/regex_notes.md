## what is re.compile:

To Search a pattern, we have to create a pattern object. Which is achived by re.compile. We have to fed the string pattern in a raw format - into the re.compile()

To ignore case sensetivity use re.IGNORECASE as a flag

## What is `.finditer()`:

Use to find all non-overlaping matches of a regular expression pattern within a string.

- It returns an iterator of match objects
  - which provides more detailed information about each match,
  - Such as its start and end Position
- It is a fantastic solution for
  - `pattern.search(strObject)` which return match details but only of the first occurance. &
  - `pattern.findall(strObject)` which returns a list of repeated pattern

## MetaCharacters or Wild Card Charcter (Need to be escaped):

- The MetaCharacters mentioned in the above string example, has its own basic functionality in the python environment.
- They are use to do some pre defined task.
- If not supressed while searching for such character they will start to do there pre defined task.
- To supress them we have to use \ . Put \ before the metacharacter and they will not perform their pre-defined task.
- **Put \ before some normal charcter and they will perform some speacial task**

## Example of some Wild Card

. =Any Charcter Except New Line <br>
\d =Digit (0-9) <br>
\D = Not a Digit <br>
\w =word Charcter (a-z, A-Z, 0-9, \_) <br>
\W =Not a Word Character <br>
\s =Whitespace (space, tab, newline) <br>
\S =Not Whitespace<br>
\b =Word Boundary

- consider `\bcat\b` in regex
- Matches: "cat" in "The cat sat"
- Does not Matches: "cat" in the "catalogue

\B =Not a Word Boundary <br><br>
^ = Begining of a string<br>
$ = End of a string <br>

| Syntax | Description                        |
| :----: | :--------------------------------- |
|  [ ]   | Matches Characters in brackets     |
|  [^ ]  | Matches Characters NOT in brackets |
|   \|   | Either Or                          |
|  ( )   | Group                              |

---

---

> **Quantifiers:**

| Syntax | Description                         |
| :----: | :---------------------------------- |
|   \*   | 0 or More                           |
|   +    | 1 or More                           |
|   ?    | 0 or One                            |
|  {3}   | Exact Number                        |
| {3,4}  | Range of Numbers (Minimum, Maximum) |

---

---

> **Sample Regexs**

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


## What is re.sub()
```python
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3, urls)
```

`re.sub()` is a function in Python's built-in `re` (regular expression) module used to replace occurrences of a particular pattern within a string. It is widely used for text manipulation, data cleaning, and replacing specific text patterns with new content. 

In the above Code it execute the works as follow:
- goes into the urls Varriable,
- Search for the main Pattern,
- Then Replace the main pattern with the Given pattern
- And Returns whole String with replaced item within it.