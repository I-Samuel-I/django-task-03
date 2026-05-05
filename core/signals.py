import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Pedido

logger = logging.getLogger('globaldocs')


@receiver(post_save, sender=Pedido)
def notificar_criacao_pedido(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Pedido criado: {instance.titulo} por {instance.usuario.email}")
