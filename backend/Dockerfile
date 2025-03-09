# 1. Rasm sifatida Python 3.10 ni ishlatamiz
FROM python:3.10

# 2. Ishchi katalogni belgilaymiz
WORKDIR /app

# 3. Barcha kerakli fayllarni konteynerga nusxalash
COPY requirements.txt .

# 4. Kerakli kutubxonalarni o‘rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Ilova fayllarini nusxalash
COPY . .

# 6. Django uchun statik fayllarni yig‘ish
RUN python manage.py collectstatic --noinput

# 7. Konteyner ishga tushirilganda Django serverini boshlash
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
