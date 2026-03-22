# SociaLink

A full-stack social media web application built with Vue.js and Django REST Framework.

🔗 **Live Demo:** [socia-link-beryl.vercel.app](https://socia-link-beryl.vercel.app)

## Features

- User registration and authentication with JWT
- Social feed with posts, likes, and comments
- Image attachments on posts
- Friend request system with suggestions
- Direct messaging / chat
- Notifications
- Hashtag trending
- User search
- Profile editing

## Tech Stack

**Frontend**
- Vue 3
- Vite
- Tailwind CSS
- Pinia (state management)
- Vue Router
- Axios

**Backend**
- Django 4.2
- Django REST Framework
- Simple JWT authentication
- PostgreSQL
- Whitenoise
- Gunicorn

## Deployment

- Frontend deployed on Vercel
- Backend deployed on Render
- PostgreSQL database hosted on Render

## Local Development

**Backend**
```bash
cd SociaLink_backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend**
```bash
cd SociaLink_frontend
npm install
npm run dev
```

## Known Limitations

- **Avatar uploads** — media files are stored on Render's ephemeral filesystem and will not persist between deploys. A future improvement would integrate Cloudinary or AWS S3 for persistent media storage.
- **Trends & People You May Know** — these features require periodic background scripts to populate data. A production implementation would use a task scheduler such as Celery with Redis, or Render's paid cron job feature.
- **Friend count** — the displayed friend count is calculated from the live database relationship and may appear inconsistent with legacy test data created during development.

## Author

Jacob Bailly — [LinkedIn](https://www.linkedin.com/in/jacob-bailly-22a31919a) | [GitHub](https://github.com/JacobBailly123)
```

