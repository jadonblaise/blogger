# 📝 Django Blog Application
This is a simple Django blog project that demonstrates how to build a basic blogging platform with blogs, authors, and entries.
The app provides:

- A home page

- A list of blogs

- A detailed view of each blog with its entries

- An author detail view with entries by that author

## 🚀 Features
- Home page → Simple welcome message.

- Blog list → Displays all blogs.

- Blog detail → Shows a single blog with its tagline and entries.

- Author detail → Shows an author with their email and entries.

## ⚙️ Installation & Setup
- Clone the repository
  - git clone https://github.com/jadonblaise/blogger.git
  - cd blogger
- Create and activate a virtual environment
  - python -m venv venv
  - source venv/bin/activate   # macOS/Linux
  - venv\Scripts\activate      # Windows
- Install dependencies
  - pip install -r requirements.txt
- Apply migrations
  - python manage.py makemigrations
  - python manage.py migrate
- Run the development server
  - python manage.py runserver <br> <br>
Open the app in your browser
