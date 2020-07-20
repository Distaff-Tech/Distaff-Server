# Generated by Django 3.0.8 on 2020-07-20 12:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('social_id', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('login_type', models.CharField(choices=[('i', 'i'), ('f', 'f'), ('g', 'g'), ('e', 'e')], max_length=50)),
                ('address', models.CharField(default='', max_length=255)),
                ('fullname', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(default='M', max_length=6)),
                ('image', models.CharField(default='', max_length=255)),
                ('about_me', models.CharField(default='', max_length=200)),
                ('stripe_id', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('onoffnotification', models.IntegerField(default=1)),
                ('total_follower', models.IntegerField(default=0)),
                ('total_following', models.IntegerField(default=0)),
                ('role', models.IntegerField(default=0)),
                ('adminCardId', models.CharField(default='', max_length=255)),
                ('post_count', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField()),
                ('deviceId', models.CharField(default='', max_length=255)),
                ('deviceType', models.CharField(default='a', max_length=1)),
                ('user_name', models.CharField(max_length=20)),
                ('lastUpdated', models.DateTimeField(blank=True, null=True)),
                ('cartNo', models.IntegerField(default=0)),
                ('has_bank_account', models.IntegerField(default=0)),
                ('is_pro_created', models.BooleanField(default=False)),
                ('is_email_sent', models.IntegerField(default=-1)),
                ('is_email_verified', models.IntegerField(default=-1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'auth_user',
                'verbose_name_plural': 'auth_users',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.CharField(default='', max_length=255)),
                ('createTime', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'appversion',
                'verbose_name_plural': 'appversion',
                'db_table': 'appversion',
            },
        ),
        migrations.CreateModel(
            name='ClothStyle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('style_name', models.CharField(default='', max_length=59)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'clothstyle',
                'verbose_name_plural': 'clothstyles',
                'db_table': 'clothstyle',
            },
        ),
        migrations.CreateModel(
            name='ClothStyleColour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('colour', models.CharField(default='', max_length=59)),
                ('colour_code', models.CharField(default='', max_length=59)),
                ('status', models.BooleanField(default=True)),
                ('image', models.CharField(default='', max_length=255)),
                ('cloth_style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyle')),
            ],
            options={
                'verbose_name': 'clothstylecolour',
                'verbose_name_plural': 'clothstylescolours',
                'db_table': 'clothstylecolour',
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('colour', models.CharField(default='', max_length=59)),
                ('colour_code', models.CharField(default='', max_length=59)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'colour',
                'verbose_name_plural': 'colours',
                'db_table': 'colour',
            },
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fabric', models.CharField(default='', max_length=59)),
                ('status', models.BooleanField(default=True)),
                ('image', models.CharField(default='', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('created_time', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'fabric',
                'verbose_name_plural': 'fabrics',
                'db_table': 'fabric',
            },
        ),
        migrations.CreateModel(
            name='FabricColour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('colour', models.CharField(default='', max_length=59)),
                ('colour_code', models.CharField(default='', max_length=59)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'fabriccolour',
                'verbose_name_plural': 'fabriccolours',
                'db_table': 'fabriccolour',
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pattern', models.CharField(default='', max_length=59)),
                ('image', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'pattern',
                'verbose_name_plural': 'patterns',
                'db_table': 'pattern',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('post_type', models.CharField(default='', max_length=255)),
                ('post_description', models.TextField(default='')),
                ('total_likes', models.IntegerField(default=0)),
                ('total_comments', models.IntegerField(default=0)),
                ('post_status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='ReachUs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('subject', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
                ('phone', models.CharField(max_length=255, null=True)),
                ('created_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'reachus',
                'verbose_name_plural': 'reachus',
                'db_table': 'reachus',
            },
        ),
        migrations.CreateModel(
            name='Sew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sew_name', models.CharField(default='', max_length=59)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'sew',
                'verbose_name_plural': 'sews',
                'db_table': 'sew',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('shape', models.CharField(default='', max_length=59)),
                ('image', models.CharField(default='', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'shape',
                'verbose_name_plural': 'shapes',
                'db_table': 'shape',
            },
        ),
        migrations.CreateModel(
            name='ShapeColour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('colour', models.CharField(default='', max_length=59)),
                ('image', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'shapecolour',
                'verbose_name_plural': 'shapecolours',
                'db_table': 'shapecolour',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(default='', max_length=59)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
                'db_table': 'size',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerifyLog',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('codeUsed', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'verifylog',
                'verbose_name_plural': 'verifylogs',
                'db_table': 'verifylog',
            },
        ),
        migrations.CreateModel(
            name='ReportPost',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField()),
                ('reason', models.TextField(blank=True, choices=[('Unauthorized sale', 'Unauthorized sale'), ('Inappropriate content', 'Inappropriate content'), ('Threatening or Violent', 'Threatening or Violent'), ('Others', 'Others')], null=True)),
                ('status', models.IntegerField(default=0)),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'reportpost',
                'verbose_name_plural': 'reportposts',
                'db_table': 'reportpost',
            },
        ),
        migrations.CreateModel(
            name='RelPostSize',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('size', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Size')),
            ],
            options={
                'verbose_name': 'relpostsize',
                'verbose_name_plural': 'relpostsize',
                'db_table': 'relpostsize',
            },
        ),
        migrations.CreateModel(
            name='RelPostShapeColour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('shape_colour', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.ShapeColour')),
            ],
            options={
                'verbose_name': 'relpostshapecolour',
                'verbose_name_plural': 'relpostshapecolours',
                'db_table': 'relpostshapecolour',
            },
        ),
        migrations.CreateModel(
            name='RelPostShape',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('shape', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Shape')),
            ],
            options={
                'verbose_name': 'relpostshape',
                'verbose_name_plural': 'relpostshapes',
                'db_table': 'relpostshape',
            },
        ),
        migrations.CreateModel(
            name='RelPostSew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('sew', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Sew')),
            ],
            options={
                'verbose_name': 'relpostsew',
                'verbose_name_plural': 'relpostsews',
                'db_table': 'relpostsew',
            },
        ),
        migrations.CreateModel(
            name='RelPostPattern',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pattern', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Pattern')),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
            ],
            options={
                'verbose_name': 'relpostpattern',
                'verbose_name_plural': 'relpostpatterns',
                'db_table': 'relpostpattern',
            },
        ),
        migrations.CreateModel(
            name='RelPostFabric',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fabric', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Fabric')),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
            ],
            options={
                'verbose_name': 'relpostfabric',
                'verbose_name_plural': 'relpostfabrics',
                'db_table': 'relpostfabric',
            },
        ),
        migrations.CreateModel(
            name='RelPostClothStyleColour',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cloth_style_colour', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyleColour')),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
            ],
            options={
                'verbose_name': 'relpostclothstylecolour',
                'verbose_name_plural': 'relpostclothstylecolours',
                'db_table': 'relpostclothstylecolour',
            },
        ),
        migrations.CreateModel(
            name='RelPostClothStyle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cloth_style', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyle')),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
            ],
            options={
                'verbose_name': 'relpostclothstyle',
                'verbose_name_plural': 'relpostclothstyles',
                'db_table': 'relpostclothstyle',
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField()),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'postlike',
                'verbose_name_plural': 'postlikes',
                'db_table': 'postlike',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_images', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField()),
                ('colour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Colour')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
            ],
            options={
                'verbose_name': 'postimage',
                'verbose_name_plural': 'postimages',
                'db_table': 'postimage',
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField()),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'postcomment',
                'verbose_name_plural': 'postcomments',
                'db_table': 'postcomment',
            },
        ),
        migrations.CreateModel(
            name='OrderTrn',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('order_status', models.CharField(choices=[(1, 1), (2, 2), (0, 0), (-1, -1), (-2, -2)], max_length=255)),
                ('transaction_id', models.CharField(default='', max_length=255)),
                ('transaction_time', models.DateTimeField()),
                ('refund_transaction_id', models.CharField(default='', max_length=255)),
                ('refund_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Addresses')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'orderdetail',
                'verbose_name_plural': 'orderdetails',
                'db_table': 'orderdetail',
            },
        ),
        migrations.CreateModel(
            name='OrderPost',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_status', models.CharField(blank=True, choices=[(1, 1), (2, 2), (0, 0), (-1, -1), (-2, -2)], max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('buyer_status', models.CharField(default=0, max_length=255)),
                ('seller_status', models.CharField(default=0, max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('created_time', models.DateTimeField()),
                ('order', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.OrderTrn')),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('post_images', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.PostImage')),
                ('size', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Size')),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'orderpost',
                'verbose_name_plural': 'orderposts',
                'db_table': 'orderpost',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('notification_time', models.DateTimeField()),
                ('message', models.TextField(default='')),
                ('order_id', models.IntegerField(default=0)),
                ('is_read', models.BooleanField(default=False)),
                ('tag', models.CharField(blank=True, max_length=150)),
                ('title', models.CharField(default='', max_length=255)),
                ('table_id', models.CharField(blank=True, max_length=150)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(default='')),
                ('is_read', models.BooleanField(default=False)),
                ('sender_status', models.BooleanField(default=True)),
                ('receiver_status', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField()),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='ForgetPasswordLog',
            fields=[
                ('id', models.CharField(max_length=191, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=191)),
                ('createdTime', models.DateTimeField()),
                ('codeUsed', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'forgetpasswordlog',
            },
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField()),
                ('follow_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('follow_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'follow_user',
                'verbose_name_plural': 'follow_users',
                'db_table': 'follow_user',
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField()),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'favourite',
                'verbose_name_plural': 'favourites',
                'db_table': 'favourite',
            },
        ),
        migrations.CreateModel(
            name='FabricColourImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('image', models.CharField(max_length=255)),
                ('fabric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Fabric')),
                ('fabriccolour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.FabricColour')),
            ],
            options={
                'verbose_name': 'fabriccolourimage',
                'verbose_name_plural': 'fabriccolourimages',
                'db_table': 'fabriccolourimage',
            },
        ),
        migrations.CreateModel(
            name='DuePayment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('payment_status', models.IntegerField(default=0)),
                ('transaction_id', models.CharField(default='', max_length=255)),
                ('transaction_time', models.DateTimeField(blank=True, null=True)),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'duepayment',
                'verbose_name_plural': 'duepayments',
                'db_table': 'duepayment',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('subject', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contactus',
                'verbose_name_plural': 'contactus',
                'db_table': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='ClothStylePatternColourImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('cloth_style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyle')),
                ('colour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyleColour')),
                ('pattern', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.Pattern')),
            ],
            options={
                'verbose_name': 'clothstylepatterncolourimage',
                'verbose_name_plural': 'clothstylepatterncolourimages',
                'db_table': 'clothstylepatterncolourimage',
            },
        ),
        migrations.CreateModel(
            name='ClothStyleColourImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('image', models.CharField(max_length=255)),
                ('cloth_style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyle')),
                ('colour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.ClothStyleColour')),
            ],
            options={
                'verbose_name': 'clothstylecolour',
                'verbose_name_plural': 'clothstylescolours',
                'db_table': 'clothstylecolourimage',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('created_time', models.DateTimeField()),
                ('post', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Post')),
                ('post_images', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.PostImage')),
                ('size', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='apis.Size')),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Account_name', models.CharField(default='', max_length=255)),
                ('Type', models.CharField(default='', max_length=255)),
                ('routing_number', models.CharField(default='', max_length=255)),
                ('acc_number', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'bankdetail',
                'verbose_name_plural': 'bankdetails',
                'db_table': 'bankdetail',
            },
        ),
    ]
