from django.core.management.base import BaseCommand
from ...models import Component, Category
from faker import Faker
from decimal import Decimal
import random


class Command(BaseCommand):
    help = "Generate 50 test components with semi-realistic data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        manufacturers = [
            "Texas Instruments", "STMicroelectronics", "NXP", "Infineon",
            "Analog Devices", "Maxim Integrated", "Murata", "Samsung"
        ]
        package_types = ["DIP-8", "SOIC-14", "QFN-32", "TO-220", "SOT-23", "BGA", "TSSOP", "LGA"]

        # Create or get a test category
        category, created = Category.objects.get_or_create(name="Дисплеї")

        if created:
            self.stdout.write(self.style.SUCCESS(f"Створено категорію: {category.name}"))

        for i in range(50):
            name = f"{random.choice(['LM', 'NE', 'AD', 'MC', 'TL'])}{random.randint(100, 999)}"
            manufacturer = random.choice(manufacturers)
            package_type = random.choice(package_types)

            voltage = round(random.uniform(1.8, 48), 2)
            current = round(random.uniform(0.01, 5.0), 3)
            power = round(voltage * float(current), 2)

            description = fake.sentence(nb_words=15)

            component = Component.objects.create(
                name=name,
                manufacturer=manufacturer,
                category=category,
                package_type=package_type,
                operating_voltage=Decimal(voltage),
                operating_current=Decimal(current),
                power=Decimal(power),
                description=description
            )

            self.stdout.write(self.style.SUCCESS(f"Створено: {component}"))

        self.stdout.write(self.style.SUCCESS("Успішно створено 50 тестових компонентів."))
