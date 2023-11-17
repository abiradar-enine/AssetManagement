# AssetManagement 

## Getting Started

1. Create migrations and migrate
- `python manage.py migrate`

2. Load fixtures from `asset_management/fixtures/`

- `python manage.py loaddata asset_management/fixtures/asset_group.json`
- `python manage.py loaddata asset_management/fixtures/asset.json`
- `python manage.py loaddata asset_management/fixtures/asset_allocation.json`


3. Run server
- `python manage.py runserver`
