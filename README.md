# Court Data Processing & Search Toolkit

## Overview

Court Data Processing & Search Toolkit is a Python project focused on processing, organising, validating, and searching structured court-case information.

The repository contains exploratory notebooks covering data preparation, scraping, and analysis.

The next development phase aims to transform the existing data-processing work into a reusable application for managing permitted public court-case datasets.

## Business Problem

Court-case information is often distributed across different sources and stored in inconsistent formats.

Common challenges include:

- Inconsistent case identifiers
- Missing or incomplete records
- Duplicate entries
- Different date formats
- Inconsistent field names
- Limited search capabilities
- Time-consuming manual processing

This project aims to simplify the preparation and organisation of court-case records.

## Current Project Status

The repository currently includes:

- Data exploration notebooks
- Data-wrangling notebooks
- Scraping experiments
- A court-case spreadsheet
- Exploratory NLP and clustering notebooks

The standalone data-processing application, database integration, and search interface are planned enhancements.

The proposed development will focus on conventional software engineering and data processing, not AI model development.

## Planned Features

### 1. Data Ingestion

- Import CSV files.
- Import Excel spreadsheets.
- Validate file structures.
- Handle malformed records.
- Support configurable input mappings.

### 2. Data Cleaning

- Standardise column names.
- Normalise date formats.
- Remove duplicate records.
- Identify missing values.
- Validate case identifiers.

### 3. Data Storage

- Store processed records in SQLite.
- Support record updates.
- Maintain processing history.
- Track data import status.

### 4. Search and Filtering

- Search records using keywords.
- Filter by available case metadata.
- Sort search results.
- Export filtered records.

### 5. User Interface

- Display records in a searchable table.
- Show validation summaries.
- Support CSV downloads.
- Provide basic data-processing statistics.

### 6. Testing

- Unit tests for data validation.
- Integration tests for database operations.
- Search functionality tests.
- Automated testing through GitHub Actions.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Core application |
| Pandas | Data cleaning and processing |
| SQLite | Database storage |
| SQLAlchemy | Database operations |
| Streamlit | User interface |
| Pydantic | Input validation |
| Pytest | Automated testing |
| GitHub Actions | Continuous integration |
| Git | Version control |

## Proposed Project Structure

```text
judges/
├── src/
│   └── court_data/
│       ├── __init__.py
│       ├── ingestion.py
│       ├── cleaning.py
│       ├── validation.py
│       ├── database.py
│       ├── search.py
│       └── export.py
├── app/
│   └── streamlit_app.py
├── notebooks/
├── tests/
│   ├── test_ingestion.py
│   ├── test_validation.py
│   ├── test_database.py
│   └── test_search.py
├── examples/
├── README.md
├── ROADMAP.md
├── LICENSE
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.11 or later
- Git
- pip

### Clone the Repository

```bash
git clone https://github.com/mideade247/judges.git
cd judges
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### Install Dependencies

Once the dependency configuration is implemented:

```bash
pip install -e .
```

## Planned Application Usage

The following command illustrates the proposed interface once the Streamlit application is implemented:

```bash
streamlit run app/streamlit_app.py
```

The application will allow users to:

1. Upload a permitted public or synthetic dataset.
2. Validate the dataset.
3. Standardise the records.
4. Store processed information.
5. Search and filter records.
6. Export results.

## Development Roadmap

| Phase | Development Task | Estimated Hours |
|-------|------------------|-----------------|
| 1 | Review existing notebooks and data rights | 4 |
| 2 | Build reusable data ingestion modules | 6 |
| 3 | Implement cleaning and validation | 6 |
| 4 | Integrate SQLite database | 6 |
| 5 | Develop keyword search | 5 |
| 6 | Build Streamlit interface | 5 |
| 7 | Testing and documentation | 5 |
| **Total** | | **37 hours** |

## Testing

Once the test suite is implemented:

```bash
pytest
```

Tests will cover:

- File ingestion
- Invalid input handling
- Data standardisation
- Duplicate detection
- Database operations
- Keyword search
- Export functionality

## Data Privacy and Compliance

The project must use only appropriately licensed public information or synthetic datasets.

Existing datasets and scraping code must be reviewed before public distribution.

Confidential records, restricted personal information, and unauthorised datasets must not be included.

## Development Scope

The planned development focuses on:

- Python software engineering
- Data ingestion
- Data validation
- Database management
- Search functionality
- Automated testing
- Documentation

AI model training, fine-tuning, evaluation, benchmarking, and inference are outside the proposed development scope.

## Future Improvements

- Advanced filtering
- Batch data processing
- Processing history
- Improved search performance
- Data export templates
- Additional validation rules

## License

No licence for now
