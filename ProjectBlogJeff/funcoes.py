import os
import secrets
from ProjectBlogJeff import app
from PIL import Image

def tratamento_img(imagem):
    cdg = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_completo = nome + cdg + extensao
    caminho_final = os.path.join(app.root_path, 'static/fotos_perfil', nome_completo)
    tamanho = (300,300)
    imagem_tratada = Image.open(imagem)
    imagem_tratada.thumbnail(tamanho)
    imagem_tratada.save(caminho_final)
    return nome_completo

def validar_cursos(formulario):
    lista = []
    for curso in formulario:
        if 'curso_' in curso.name:
            if curso.data:
                lista.append(curso.label.text)
    return ';'.join(lista)

def cursos_lista(cursos):
    lista = []
    cursos = cursos.split(';')
    for curso in cursos:
        lista.append(curso)
    return lista


