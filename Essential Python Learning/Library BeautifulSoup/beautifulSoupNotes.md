# What is Beautiful Soup
Beautiful Soup is a powerful Python library designed for parsing HTML and XML documents, making it easy to extract data for web scraping. It creates a parse tree from page source code, allowing users to navigate, search, and modify data using Pythonic idioms.

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

**To Install Beautiful Soup** Run this: `pip install beautifulsoup4`

# `BeautifulSoup()` Constructor
To get the desired information, or to manipulate the html file we have feed the file into the `BeautifulSoup()` method.

The `BeautifulSoup()` constructor is the primary function used to parse HTML and XML documents in the Beautiful Soup Python library. 

It converts raw markup into a complex tree of Python objects that allows for easy navigation, searching, and modification of the document structure.

## Key Methods and Features of the Resulting Object
The object returned by `BeautifulSoup()` is a BeautifulSoup object, which behaves much like a Tag object for most purposes. You can use its methods to interact with the document


- `.find()`: Finds the first matching tag that meets specific criteria (e.g., tag name, class, ID).
- `.find_all()`: Finds all matching tags and returns them as a ResultSet (a list of Tag objects).
- `.select()`: Allows searching for elements using CSS selectors, offering a powerful alternative to find_all().
- `.get_text()`: Extracts all the text content from within a tag, removing the HTML markup.
- `.prettify()`: Formats the HTML with proper indentation for improved readability during debugging.
- `.title.string`: Accesses specific parts of the parse tree directly, such as the text within the `<title>` tag.
- `.find_all(text='string')` : Find all the matching text and return them as a ResultSet.
- `.parent` : This attribute retruns the immediate parent of a tag or **string**

# Extracting an attribute value:

In `Beautiful Soup`, we can get the value of a tag's attribute primarily by 
- treating the tag object like a dictionary or by using the .get() method. 
- The .get() method is generally preferred as it prevents a KeyError if the attribute does not exist. 


## Method 1: Dictionary-style Access (Square Brackets)
We can access attributes using square brackets [ ] with the attribute name as a string key. This works well if we are certain the attribute exists.

```python
from bs4 import BeautifulSoup

html_doc = '<a href="https://www.google.com" id="link1">Google</a>'
soup = BeautifulSoup(html_doc, 'html.parser')

a_tag = soup.find('a')

# Accessing the 'href' attribute
href_value = a_tag['href']
print(f"The href value is: {href_value}")

# Accessing the 'id' attribute
id_value = a_tag['id']
print(f"The id value is: {id_value}")

```

**Caution:** If the attribute we try to access with [] does not exist, it will raise a `KeyError`.

## Method 2: The `.get()` Method (Recommended)
The `.get()` method is safer because it returns None (or a default value we specify) if the attribute is missing, instead of raising an error.

```python
from bs4 import BeautifulSoup

html_doc = '<a href="https://www.google.com">Google</a>'
soup = BeautifulSoup(html_doc, 'html.parser')

a_tag = soup.find('a')

# Using .get() for 'href'
href_value = a_tag.get('href')
print(f"The href value is: {href_value}")

# Using .get() for a non-existent 'class' attribute (returns None)
class_value = a_tag.get('class')
print(f"The class value is: {class_value}")

# Using .get() with a default value
title_value = a_tag.get('title', 'No title found')
print(f"The title value is: {title_value}")

```
## Accessing All Attributes
We can view all attributes of a tag as a dictionary using the `.attrs` property.

```python
from bs4 import BeautifulSoup

html_doc = '<div id="main" class="container">Content</div>'
soup = BeautifulSoup(html_doc, 'html.parser')

div_tag = soup.find('div')

# Get the dictionary of all attributes
all_attributes = div_tag.attrs
print(f"All attributes: {all_attributes}")
# Output: {'id': 'main', 'class': ['container']}

```

Note that for multi-valued attributes like class, the value is returned as a list.

- To get multiple tags we have to use [ ] => `.find_all(['p', 'div'])`

# Extract Class name from tag:

In Beautiful Soup, we can get the class names of an element by treating the Tag object like a dictionary and accessing the `'class'` attribute. This returns a list of all class names associated with that element.

## Accessing the Class Names
We can access the `class` attribute of a tag using dictionary notation: `tag['class']`. 

```python
from bs4 import BeautifulSoup

html_doc = """
<div class="class1 class2 class3">
    <span class="inner-class">Some text</span>
</div>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Find the div tag
div_tag = soup.find('div')

# Get the value of the 'class' attribute
classes = div_tag['class']

print(f"The classes are: {classes}")
# Output: The classes are: ['class1', 'class2', 'class3']

# Accessing a single class name (e.g., the first one)
first_class = classes[0]
print(f"The first class is: {first_class}")
# Output: The first class is: class1

```
## Finding Elements by Class
To find elements that have a specific class, we should use the `class_` parameter in methods like `find()` or `find_all()` (since class is a reserved keyword in Python).

```python
first_element = soup.find(class_="class1")
# You can then get its class names
if first_element:
    print(first_element['class'])
```
```python
all_elements = soup.find_all(class_="class1")
for element in all_elements:
    print(element['class'])
```

## Using CSS selectors (the `select()` method):
For a more powerful way to find elements by class, we can use the `select()` method with CSS selector syntax (a dot `.` followed by the class name).

```python
# Select all elements with the class 'class2'
elements_by_selector = soup.select(".class2")
for element in elements_by_selector:
    print(element['class'])
```

# Navigating the HTML Tree:

Navigating the HTML tree in Beautiful Soup 4 (BS4) can be done through two main approaches: 
- **direct object attributes** for common movements and 
- **search methods** for more specific 


## Direct Navigation (Relationships)
These attributes allow us to move relative to a specific Tag object. 

- `tag.contents`: Access a tag's direct children as a list, including NavigableString objects (like whitespace and text).
- `tag.children`: Iterate over a tag's direct children as a generator (useful for large documents or loops).
- `tag.descendants`: Iterate over all children nested within a tag, recursively (direct and indirect).
- `tag.parent`: Access the immediate parent tag of an element. We can chain .parent.parent to move up multiple levels.
- `tag.parents`: Iterate over all ancestor elements (parents, grandparents, etc.) up to the top of the document.
- `tag.next_sibling / tag.previous_sibling`: Access the next or previous element at the same hierarchical level (sibling).
- `tag.next_siblings / tag.previous_siblings`: Iterate over all following or preceding siblings.
### `tag.string / tag.strings / tag.stripped_strings`:
- `tag.string` gets the text content if a tag has only one child that is a string.
- `tag.strings` iterates over all strings within the tag, including whitespace.
- `tag.stripped_strings` iterates over strings with leading/trailing whitespace removed and entirely whitespace-only strings ignored.