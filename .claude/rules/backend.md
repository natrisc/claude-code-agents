# Backend Rules

- Validate all inputs at system boundaries.
- Keep handlers, controllers, and routes thin.
- Put business rules in services, modules, or domain logic.
- Keep persistence behind repositories or clear data-access boundaries.
- Treat external systems as adapters or integrations.
- Add tests for branching logic, bug fixes, and new behavior.
- Document migrations, contract changes, and backward compatibility concerns.