# CSC500 Portfolio

Python coursework portfolio for **CSC500 - Principles of Programming** at CSU Global.

## Overview

This repository contains milestone and assignment work focused on core programming concepts:

- Classes and objects
- Lists and iteration
- User input and menu-driven programs
- Basic modular design across files

## Project Structure

```text
Assignments/
Milestone/
  Module 4/
    ItemToPurchase.py
  Module 6/
    ItemToPurchase.py
    ShoppingCart.py
  Module 8/
    ItemToPurchase.py
    ShoppingCart.py
Discussions/
```

## Featured Milestones

### Module 4 - ItemToPurchase Foundation

- Initial class-based shopping item implementation
- Item name, price, and quantity attributes
- Item cost output flow used as a base for later shopping cart milestones

### Module 6 - ShoppingCart (Steps 4-6)

- `ShoppingCart` class with required attributes and methods
- Menu system with options:
  - `a` Add item
  - `r` Remove item
  - `c` Change item quantity
  - `i` Output item descriptions
  - `o` Output shopping cart
  - `q` Quit
- Output-focused options implemented for cart totals and item descriptions

### Module 8 - Online Shopping Cart (Final)

- Complete `ItemToPurchase` and `ShoppingCart` implementation
- Customer/date prompt flow
- Add, remove, and modify quantity actions
- Cart total and descriptions output

## How to Run

From the repository root:

```powershell
python "Milestone/Module 4/ItemToPurchase.py"
python "Milestone/Module 6/ShoppingCart.py"
python "Milestone/Module 8/ShoppingCart.py"
```

You can also run the `ItemToPurchase.py` scripts directly for Milestone 1 item-cost input/output flow.

## Notes

- Built with Python 3
- Console-based interaction (no external libraries required)
