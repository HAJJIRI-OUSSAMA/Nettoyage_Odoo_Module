# Nettoyage Project

This project is an Odoo module for managing cleaning services (prestations de nettoyage), including clients, employees, and statistics.

## Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- (Optional) [Git](https://git-scm.com/) if you want to clone the repository

## How to Run

1. **Clone or Download the Project**

   ```
   git clone <your-repo-url>
   cd NetoyageProject
   ```

2. **Start the Services**

   In the project root directory, run:

   ```
   docker-compose up -d
   ```

   This will start:

   - PostgreSQL database
   - Odoo 17 server (with your custom module)
   - pgAdmin (for database management, accessible at [http://localhost:5050](http://localhost:5050))

3. **Access Odoo**

   Open your browser and go to [http://localhost:8069](http://localhost:8069)

   - Create a new Odoo database if prompted.
   - Go to **Apps** and update the app list (click "Update Apps List" in debug mode).
   - Search for **Nettoyage Module** and install it.

## Usage

- **Prestations**: Manage cleaning services, assign employees, track status and duration.
- **Clients**: Manage clients, their contact info, and see related prestations.
- **Statistics**: View prestation statistics and analysis.
- **Security**: User and Manager roles control access to features.

## Development

- Custom modules are in the `addons` directory.
- To add or update modules, place them in `addons` and restart Odoo.

## Stopping the Project

To stop all services:

```
docker-compose down
```

## Troubleshooting

- If you change Python or Odoo code, restart the Odoo container:

  ```
  docker-compose restart odoo
  ```

- For database issues, use pgAdmin at [http://localhost:5050](http://localhost:5050) (login: admin@admin.com / admin).

---

**Enjoy managing your cleaning services with Odoo!**
