# ROADMAP.md — Internship-Worthy MVP Progression

## Status
**Current Level:** 1 — Function Contracts, Type Safety & Defensive Code

---

## Level 1: Function Contracts, Type Safety & Defensive Code

- [ ] Add type hints to all functions (`place_order`, `show_inventory`, `main`)
- [ ] Fix inconsistent return values — `'None', 'None'` → `None, None`; handle implicit `None` on 'n' path
- [ ] Remove redundant `customers` list; `unique_customers` set is the single source of truth
- [ ] Fix `unique_customers = set(customers)` → `unique_customers = set()`
- [ ] Add stock == 0 validation before order placement
- [ ] Add graceful exit option (menu choice 3) wired to `running = False`
- [ ] Add module-level guard: `if __name__ == "__main__":`
- [ ] Defensive input validation — handle edge cases (empty input, negative numbers)

---

## Level 2: File Persistence & Data Serialization
- [ ] TBD

## Level 3: OOP & Modularity
- [ ] TBD

## Level 4: Relational Databases & SQL
- [ ] TBD

## Level 5: Clean Interfaces & Automated Testing
- [ ] TBD

---

## Technical Debt (discovered during work)
- `customers` list is dead code — parallel structure to `unique_customers` set, never used independently
