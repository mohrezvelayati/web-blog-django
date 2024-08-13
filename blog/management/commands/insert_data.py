from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify

from blog.models import Post, Category, Comment

category_list = [
    "IT",
    "IO",
    "AI"
]


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        # Create a dummy user
        user = User.objects.create_user(
            username=self.fake.user_name(),
            email=self.fake.email(),
            password="mohrez123",
            first_name=self.fake.first_name(),  # Add first name directly to User
            last_name=self.fake.last_name()  # Add last name directly to User
        )

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            title = self.fake.paragraph(nb_sentences=1)
            post = Post.objects.create(
                author=user,
                title=title,
                slug=slugify(title),  # Generate slug from title
                content=self.fake.paragraph(nb_sentences=10),
                status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_date=datetime.now()
            )

            # Add comments to each post
        for _ in range(random.randint(5, 15)):  # Random number of comments per post
            comment = Comment.objects.create(
                author=user,
                post=post,
                message=self.fake.paragraph(nb_sentences=2),
                email=self.fake.email(),
                approved=random.choice([True, False]),
                created_date=self.fake.date_time_this_year()
            )

            # Optionally, add replies to comments
            if random.choice([True, False]):  # Randomly decide if a comment gets a reply
                Comment.objects.create(
                    author=user,
                    post=post,
                    message=self.fake.paragraph(nb_sentences=2),
                    email=self.fake.email(),
                    approved=random.choice([True, False]),
                    created_date=self.fake.date_time_this_year(),
                    reply_to=comment  # Set the parent comment
                )