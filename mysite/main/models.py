from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название жанра'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Composer(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='ФИО композитора'
    )
    biography = models.TextField(
        blank=True,
        verbose_name='Биография'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Композитор'
        verbose_name_plural = 'Композиторы'


class Hall(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название зала'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    capacity = models.PositiveIntegerField(
        verbose_name='Количество мест'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Collective(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название коллектива'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to='collectives/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллективы'


class Artist(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='ФИО артиста'
    )
    biography = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    collective = models.ForeignKey(
        Collective,
        on_delete=models.PROTECT,
        related_name='artists',
        verbose_name='Коллектив'
    )
    photo = models.ImageField(
        upload_to='artists/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'


class Work(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название произведения'
    )
    composer = models.ForeignKey(
        Composer,
        on_delete=models.PROTECT,
        related_name='works',
        verbose_name='Композитор'
    )
    duration = models.PositiveIntegerField(
        verbose_name='Длительность в минутах'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Concert(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название концерта'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    date = models.DateTimeField(
        verbose_name='Дата и время'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость билета'
    )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.PROTECT,
        related_name='concerts',
        verbose_name='Зал'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='concerts',
        verbose_name='Жанр'
    )
    collective = models.ForeignKey(
        Collective,
        on_delete=models.PROTECT,
        related_name='concerts',
        verbose_name='Коллектив'
    )
    poster = models.ImageField(
        upload_to='posters/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Афиша'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'


class Ticket(models.Model):
    concert = models.ForeignKey(
        Concert,
        on_delete=models.PROTECT,
        related_name='tickets',
        verbose_name='Концерт'
    )
    seat = models.PositiveIntegerField(
        verbose_name='Номер места'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость'
    )
    is_sold = models.BooleanField(
        default=False,
        verbose_name='Продан'
    )

    def __str__(self):
        return f'{self.concert} — место {self.seat}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        constraints = [
            models.UniqueConstraint(
                fields=['concert', 'seat'],
                name='unique_concert_seat'
            )
        ]