#!/usr/bin/env python3
import boto3
ec2 = boto3.resource('ec2')

# Obtenemos las instancias
#instances = ec2.instances.all()
instances = ec2.instances.filter(Filters=[{'Name': 'subnet-id', 'Values': [subnet-1234567890abcdefg]}])
# Iteramos sobre ellas
for instance in instances:
    # Obtenemos los tags de cada instancia
    tags = instance.tags
    # Y revisamos si contiene el tag Environment
    if not any(tag['Key'] == 'Environment' for tag in tags):
        # Si no cumplen el tag se muestra la instancia a eliminar
        print('Eliminando instancia:', instance)
        # Los tags
        print('Con etiquetas:')
        print(tags)
        # Y se termina la instancia
        instance.terminate()
print('Se eliminaron las intancias que no cumplían con los requisitos de etiquetado')