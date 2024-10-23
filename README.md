# Expense Sharing Application

This is a backend service for a daily expenses sharing application that allows users to add expenses and split them using different methods.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- User Management: Create and manage users with email, name, and mobile number.
- Expense Management: Add and manage expenses with various split methods:
  - Equal split
  - Exact amount split
  - Percentage-based split
- Balance Sheet: Generate individual and overall expenses.
- Downloadable balance sheets in CSV format.
- User authentication and authorization.

## Requirements
- Python 3.6+
- Django 3.x+
- Django REST Framework
- PostgreSQL or SQLite (for local development)
  
## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rajshekhar5/Daily-Expenses-Sharing-Application.git
   cd expense-sharing
