# Project: E-Commerce Engine (Terminal Application)

An interactive, terminal-based E-Commerce Engine for Apple designed to track product inventory, manage incoming orders, and keep a registry of unique customers using fundamental Python data structures.

## Tutoring Mode Guidelines (Strictly Project-Scoped)
- **Role**: Act as a straightforward, brutally honest code instructor.
- **Workflow**: Do not give complete answers or code solutions directly. Provide insights, identify problems, and suggest the critical first steps so the user learns concepts and builds the project on their own.

## Core Architectural Design

- **Inventory**: Managed via a Python `dict` of `dict`s mapping product IDs (e.g., `"PROD001"`) to attributes (model, storage, price, stock).
- **Order Queue**: Managed using a Python `list` to queue incoming orders chronologically.
- **Customer Tracking**: Managed using a Python `set` of strings to track unique customer names.
- **User Actions**: Structured via standalone functions.

---

## Progress Tracker & Backlog

### Phase 1: Foundations & Setup
- [x] Create initial `ecom_main_script.py` structure.
- [ ] Establish correct data structures and fix inventory schema inconsistencies (e.g., missing stock keys for PROD003/PROD004).

### Phase 2: Core Engine Operations
- [ ] Implement **View Inventory** function (displaying products, specifications, pricing, and stock in a readable format).
- [ ] Implement **Place Order** function:
  - Prompt user for customer name and add it to unique customer set.
  - Prompt user for product ID and quantity.
  - Validate stock availability.
  - Add order details to the order queue.
  - Deduct stock upon successful placement.
- [ ] Implement **Process Next Order** (FIFO queue processing, popping from the queue and marking as fulfilled).

### Phase 3: Interactive Main Loop
- [ ] Wrap application entry point in a continuous loop so users can perform multiple actions without restarting the script.
- [ ] Add graceful exit option.

---

## Engineering Conventions & Notes
1. **No External Libraries**: Stick strictly to standard Python library and basic built-in types (lists, dicts, sets, tuples).
2. **Input Validation**: Check that input choices are valid numbers/strings to prevent script crashes.
