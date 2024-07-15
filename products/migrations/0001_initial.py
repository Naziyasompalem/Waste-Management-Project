# Generated by Django 5.0.6 on 2024-07-15 09:38

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('StartDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField(blank=True)),
                ('Price', models.CharField(max_length=10)),
                ('Image', models.ImageField(blank=True, upload_to='products/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('PointsRequired', models.PositiveIntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.CharField(blank=True, max_length=20)),
                ('CompanyAddress', models.CharField(blank=True, max_length=255)),
                ('TaxIdentificationNumber', models.CharField(blank=True, max_length=50)),
                ('PickupAddress', models.CharField(blank=True, max_length=255)),
                ('BankAccountName', models.CharField(blank=True, max_length=255)),
                ('BankName', models.CharField(blank=True, max_length=255)),
                ('AccountNumber', models.CharField(blank=True, max_length=50)),
                ('Description', models.TextField(blank=True)),
                ('Website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=255)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Phone', models.CharField(blank=True, max_length=20)),
                ('AddressLine1', models.CharField(max_length=255)),
                ('AddressLine2', models.CharField(blank=True, max_length=255)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('PostalCode', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=100)),
                ('ShippingInstructions', models.TextField(blank=True)),
                ('ShippingMethod', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Address', models.CharField(blank=True, max_length=255)),
                ('Phone', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(blank=True, related_name='customer_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customer_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.CharField(blank=True, max_length=20)),
                ('CompanyAddress', models.CharField(blank=True, max_length=255)),
                ('TaxIdentificationNumber', models.CharField(blank=True, max_length=50)),
                ('PickupAddress', models.CharField(blank=True, max_length=255)),
                ('BankAccountName', models.CharField(blank=True, max_length=255)),
                ('BankName', models.CharField(blank=True, max_length=255)),
                ('AccountNumber', models.CharField(blank=True, max_length=50)),
                ('Description', models.TextField(blank=True)),
                ('Website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=255)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Phone', models.CharField(blank=True, max_length=20)),
                ('AddressLine1', models.CharField(max_length=255)),
                ('AddressLine2', models.CharField(blank=True, max_length=255)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('PostalCode', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=100)),
                ('ShippingInstructions', models.TextField(blank=True)),
                ('ShippingMethod', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Address', models.CharField(blank=True, max_length=255)),
                ('Phone', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(blank=True, related_name='customer_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customer_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.PositiveIntegerField()),
                ('Cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('Cuisine', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'managed': True,
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_name='newuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='newuser_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryStatus', models.CharField(choices=[('Pending', 'Pending'), ('On the way', 'On the way'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('DeliveryFee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DeliveryPerson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.customer')),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentMethod', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Cash on Delivery', 'Cash on Delivery')], max_length=20)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EarnedDate', models.DateTimeField(blank=True, null=True)),
                ('Cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
                ('Reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.reward')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
