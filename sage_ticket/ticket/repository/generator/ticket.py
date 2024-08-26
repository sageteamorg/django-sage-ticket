import functools
import os
import random
from typing import Any, List

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from mimesis import Person, Text
from mimesis.locales import Locale
from tqdm import tqdm

from sage_ticket.ticket.helper import (
    ExtenstionsEnum,
    SeverityEnum,
    StatusEnum,
    TicketStateEnum,
)
from sage_ticket.ticket.models import Attachment, Comment, Department, Issue

User = get_user_model()


class TicketDataGenerator:
    def __init__(self):
        self.person = Person(Locale.EN)
        self.text = Text(Locale.EN)

    def create_users(self, total):
        objs = [
            User(
                username=f"{self.person.username()}{i}",
                email=self.person.email(domains=["sageteam.org", "radin.com"]),
                password=self.person.password(length=12, hashed=True),
            )
            for i in tqdm(range(total))
        ]
        users = User.objects.bulk_create(objs, batch_size=1000)
        return users

    def create_department(self, total):
        objs = [
            Department(
                description=self.text.text(quantity=5),
                title=self.text.title(),
            )
            for _ in range(total)
        ]
        Departments = Department.objects.bulk_create(objs)
        return Departments

    def create_comment(self, total, users, issues):
        objs = [
            Comment(
                user=random.choice(users),
                issue=random.choice(issues),
                message=self.text.text(quantity=3),
                title=self.text.title(),
                status=random.choice(StatusEnum.choices)[0],
                is_unread=True,
            )
            for i in tqdm(range(total))
        ]
        comments = Comment.objects.bulk_create(objs)
        return comments

    def create_issue(self, total, users, department):
        objs = [
            Issue(
                raised_by=random.choice(users),
                message=self.text.text(quantity=3),
                department=random.choice(department),
                subject=self.text.title(),
                state=random.choice(TicketStateEnum.choices)[0],
                severity=random.choice(SeverityEnum.choices)[0],
            )
            for i in tqdm(range(total))
        ]
        issues = Issue.objects.bulk_create(objs)
        return issues

    def create_attachment(self, total, issues):
        filesh = self.get_random_f()
        objs = [
            Attachment(
                issue=random.choice(issues),
                name=self.text.text(quantity=1),
                file=SimpleUploadedFile(
                    name=random.choice(filesh)[0], content=random.choice(filesh)[1]
                ),
                extenstions=random.choice(ExtenstionsEnum.choices)[0],
            )
            for i in tqdm(range(total))
        ]
        attachments = Attachment.objects.bulk_create(objs)
        return attachments

    def get_random_f(self):
        demo_pic_dir_path = os.path.join(
            settings.BASE_DIR,
            "media",
            "demo",
        )
        videos = []

        for root, dirs, files in os.walk(demo_pic_dir_path, topdown=False):
            for name in files:
                pic_path = os.path.join(root, name)
                with open(pic_path, mode="rb") as demo_pic:
                    picture = demo_pic.read()
                data = (pic_path, picture)
                videos.append(data)
        return videos

    def add_2_m_m(self, objs: List[Any], target_feild: str, item_per_obj: int, item):
        attr = getattr(item, target_feild)
        try:
            items_to_add = list(map(lambda: random.choice(objs), range(item_per_obj)))
        except IndexError as exc:
            print(exc)
            raise IndexError(" objs are empty")

        attr.add(*items_to_add)

    def join_members(self, department, members, total):
        joiner = functools.partial(self.add_2_m_m, members, "member", total)
        result = list(tqdm(map(joiner, department)))
        print(result)
        return department
