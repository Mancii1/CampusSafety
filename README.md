# DUT CampusSafety

A comprehensive web-based safety reporting and resource system for the Durban University of Technology.

## Features

- Incident Reporting System
- Safety Resources Directory
- User Management
- Emergency Contacts
- Real-time Status Updates
- Mobile-responsive Design

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/campussafety.git
cd campussafety
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python app.py
```

## Running the Application

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
campussafe/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
├── templates/         # HTML templates
└── instance/         # Instance-specific files (database)
```

## Security Features

- User authentication
- Password hashing
- Form validation
- CSRF protection
- Secure session management

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## Support

For support, please contact:
- Email: support@dut.ac.za
- Phone: 031 373 2000

## Emergency Contacts

- Campus Security: 031 373 2000
- Medical Emergency: 10111
- Crisis Line: 0800 123 456 #   c a m p uss a f e ty
 
 