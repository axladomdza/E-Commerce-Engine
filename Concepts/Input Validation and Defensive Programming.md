# Input Validation and Defensive Programming

## The Main Idea

When a program receives data from a user, another program, or a file, it should not assume that the data is valid. The program should check the data before using it.

This practice is called **input validation** or **data validation**.

In the e-commerce program, the user types a product number. That number is data coming from outside the program. Before using it to look up a product, the program should confirm that the number is an actual product ID in the inventory dictionary.

```python
if order_num in inv:
    user_prod = inv[order_num]
```

The condition asks a direct question:

> Does this exact product ID exist in the inventory?

Only after the answer is yes does the program perform the dictionary lookup.

## Why `len()` Is Not the Same as Key Validation

This check:

```python
if 1 <= order_num <= len(inv):
```

checks whether the number falls inside a numerical range. It does not check whether that number is actually a key.

With this inventory, both approaches currently behave the same:

```python
inv = {
    1: {...},
    2: {...},
    3: {...},
    4: {...}
}
```

The keys are consecutive, start at `1`, and there are four products. Therefore, the valid keys happen to be the same as the range from `1` to `len(inv)`.

However, the dictionary length describes how many entries exist. It does not describe which keys exist.

### Example: A Missing Product ID

Suppose product `2` is removed:

```python
inv = {
    1: {...},
    3: {...},
    4: {...}
}
```

Now `len(inv)` is `3`.

The range check would accept `2`, even though key `2` is missing. It would reject `4`, even though key `4` exists.

The membership check remains accurate because it examines the actual keys:

```python
if order_num in inv:
    ...
```

### Example: Product IDs Are Not Positions

Suppose product IDs are assigned as `101`, `205`, and `900`:

```python
inv = {
    101: {...},
    205: {...},
    900: {...}
}
```

There are three products, but the valid product numbers are not `1`, `2`, and `3`. A length-based range cannot represent these IDs. Membership validation can:

```python
if order_num in inv:
    ...
```

## Dictionary Iteration and Membership

A dictionary stores key-value relationships:

```python
inventory = {
    1: {
        "model": "Iphone 15 Pro Max",
        "stock": 550
    }
}
```

The outer dictionary has:

- Key: `1`, the product ID
- Value: another dictionary containing product information

The expression `order_num in inv` checks the outer dictionary's keys. It does not search inside the product information. That is exactly what is needed because the user is entering an outer product ID.

After the ID is confirmed, this lookup gets the value associated with it:

```python
user_prod = inv[order_num]
```

Then the inner dictionary can be accessed using its own keys:

```python
user_prod["model"]
user_prod["storage"]
user_prod["price"]
user_prod["stock"]
```

The two lookups operate at different levels:

```text
inv[order_num]       -> product information dictionary
user_prod["model"]  -> model value inside that dictionary
```

## Defensive Programming

**Defensive programming** is the broader engineering approach of writing code that protects itself from invalid, unexpected, or unusual data.

Input validation is one defensive programming technique. Other examples include:

- Checking that a quantity is a positive integer
- Checking that requested quantity does not exceed stock
- Checking that a dictionary key exists before using it
- Checking that a string is not empty when a name is required
- Checking that a choice belongs to the available menu options

The goal is not to assume that the user will always do exactly what the program expects.

## Guard Conditions and Guard Clauses

An `if` statement that protects an operation is often called a **guard condition**:

```python
if order_num in inv:
    user_prod = inv[order_num]
else:
    print("Please input a valid product number.")
```

It guards the dictionary lookup from an invalid key.

When a function exits early after invalid input, the check may also be called a **guard clause**:

```python
if order_num not in inv:
    print("Please input a valid product number.")
    continue
```

The exact name depends on the shape of the code, but the underlying idea is the same: verify a condition before proceeding.

## Validation Versus Exception Handling

Validation and exception handling are related, but they are not identical.

### Validation

Validation checks whether an operation should be attempted:

```python
if order_num in inv:
    user_prod = inv[order_num]
```

This prevents a known invalid case before it causes a problem.

### Exception Handling

Exception handling responds when an operation raises an error:

```python
try:
    user_prod = inv[order_num]
except KeyError:
    print("Please input a valid product number.")
```

For ordinary user input, explicit validation is often easier to read because the expected condition is visible before the lookup. Exception handling is useful when a failure is less predictable or when attempting the operation directly is the clearest approach.

In short:

- Validation: prevent an expected invalid operation
- Exception handling: respond when an operation fails

## Fail-Fast Behavior

Rejecting invalid input as soon as it is discovered is called **fail-fast behavior**.

For the product selection flow, fail-fast behavior means:

1. Convert the input into the expected type.
2. Check whether the product ID exists.
3. Stop that attempt and ask again if it does not exist.
4. Look up the product only after validation succeeds.

Failing fast makes errors easier to locate and prevents invalid data from moving deeper into the program.

## Preconditions and Postconditions

A **precondition** is something that must be true before an operation begins.

Before looking up a product, the precondition is:

```text
order_num must be a key in inv
```

A **postcondition** is something that should be true after an operation finishes. After successfully placing an order, possible postconditions include:

```text
the order was added to the queue
stock decreased by the requested quantity
the customer was added to the customer set
```

Thinking in preconditions and postconditions helps break a feature into clear responsibilities.

## The Most Important Distinction

The range check is based on an assumption:

```text
Product IDs are always consecutive integers from 1 through the number of products.
```

The membership check is based on the data itself:

```text
The product is valid if its ID is actually present in the inventory.
```

When validating identifiers, prefer checking the source of truth. In this program, the inventory dictionary is the source of truth for which product IDs exist.

## Review Questions

1. What does `len(inv)` tell you, and what does it not tell you?
2. What does `order_num in inv` check?
3. What error can occur if `inv[order_num]` is used with a missing key?
4. Why is a product ID different from a product's position in a list?
5. Which checks should happen before placing an order?
