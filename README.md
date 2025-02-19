# Marvel API Data Fetcher

This project fetches all Marvel character names and the quantity of comics in which they appear from the Marvel API and saves result to a CSV file.

## 📂 Project Structure

```
project_root/
│── .env                 # Environment variables
│── config.py            # Configuration file
│── utils.py             # Utility functions
│── marvel_api.py        # Marvel API interaction logic
│── main.py              # Main script to fetch data
│── tests/               # Unit tests
│   ├── __init__.py      # Makes tests a package
│   ├── test_marvel_api.py # Unit tests for API functions
│── marvel_characters.csv # Output file (generated after running main.py)
```

## 🛠️ Setup & Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/marvel-api-fetcher.git
   cd marvel-api-fetcher
   ```

2. **Create a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Marvel API keys in `.env` file:
     ```sh
     MARVEL_PUBLIC_KEY=your_public_key
     MARVEL_PRIVATE_KEY=your_private_key
     ```

## 🚀 Running the Project

To fetch Marvel characters and save them to a CSV file, run:
```sh
python main.py
```
The results will be stored in `marvel_characters.csv`.

## 🧪 Running Tests

To run the unit tests:
```sh
python -m unittest discover tests
```
