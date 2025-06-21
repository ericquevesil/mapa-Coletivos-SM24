# © 2024 Laboratório de Investigação Sociológica (LABIS/UFSM).
# Licenciado sob a Licença Aberta - DataLABIS v1.0 (2025).


# ============= MAPEAMENTO DAS AÇÕES COLETIVAS DE TRABALHO VOLUNTÁRIO NO CONTEXTO DO DESASTRE SOCIOAMBIENTAL EM SANTA MARIA/RS (2024) ========================================


# ============= IMPORTAÇÃO DE BIBLIOTECAS COMPLEMENTARES # =================================================
import folium
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
# =======================================================================================================



# ============= CONFIGURAÇÃO DO MAPA BASE ===============================================================
mapa = folium.Map(
    location=[-29.6833, -53.8000], # Define o ponto central do mapa
    zoom_start=13, # Zoom inicial para visualização
    control_scale=True  # Mostra escala em km/m
)
# =======================================================================================================



# ============= CONFIGURAÇÃO DOS MARCADORES  ===============================================================================================
### Coordenadas dos coletivos mapeados e suas respectivas descrições
pontos = [
    {
        "nome": "Igreja Batista Betel",
        "coordenadas": [-29.6742619, -53.826569],
        "descricao": "Igreja Batista Betel\nAv. Borges de Medeiros, 1175 – Salgado Filho, Santa Maria, RS\nContato: Diego: (54) 99669-4833"
    },
    {
        "nome": "Igreja Templo do Poder de Deus",
        "coordenadas": [-29.7517656, -53.7890168],
        "descricao": "Igreja Templo do Poder de Deus\nRua Augusto Kunz, 150 – Passo das Tropas, Santa Maria, RS"
    },
    {
        "nome": "Templo de Umbanda Xangô e Exu Caveira",
        "coordenadas": [-29.6799206, -53.8292641],
        "descricao": "Templo de Umbanda Xangô e Exu Caveira\nRua 20 de Janeiro, 391 – Divina Providência, Santa Maria, RS\nContato: Fabrício de Cassenote: (55) 99148-1732"
    },
    {
        "nome": "Reino de Axé Oyá Nique e Oxalá",
        "coordenadas": [-29.6913361, -53.8623986],
        "descricao": "Reino de Axé Oyá Nique e Oxalá\nRua Benjamin D’Ávila Prado, 11 – Juscelino Kubitschek, Santa Maria, RS\nContato: Sabrina: (55) 98413-1680"
    },
    {
        "nome": "ONG Mãos Unidas Pelo Cipriano",
        "coordenadas": [-29.6978133, -53.8675947],
        "descricao": "ONG Mãos Unidas Pelo Cipriano\nRua Niterói, 500 – Parque Pinheiro Machado, Santa Maria, RS\nContato: Anderson Melgares: (55) 98419-9742"
    },
    {
        "nome": "CTG Sentinela da Querência",
        "coordenadas": [-29.7029807, -53.7215761],
        "descricao": "CTG Sentinela da Querência\nRua Silvino Jacob Zimmermann, 115 – Camobi, Santa Maria, RS\nContato: Ronaldo Lock: (55) 99145-8529"
    },
    {
        "nome": "CTG Passo dos Ferreiros",
        "coordenadas": [-29.7037774, -53.876117],
        "descricao": "CTG Passo dos Ferreiros\nRua Milton Mendonça de Souza, 500 – Tancredo Neves, Santa Maria, RS\nContato: Tiago: (55) 99126-6823"
    },
    {
        "nome": "Projeto Esperança/Cooesperança",
        "coordenadas": [-29.7033798, -53.8075996],
        "descricao": "Projeto Esperança\nRua Ver. Bolsson, 1 – Nossa Sra. Medianeira, Santa Maria, RS\nContato: Tiago: (55) 99126-6823"
    },
    {
        "nome": "Cozinha Popular da Comunidade Estação dos Ventos",
        "coordenadas": [-29.6878303, -53.7810022],
        "descricao": "Cozinha Popular da Comunidade E.V.\nAtrás da Creche Estação dos Ventos, Luiz Castagna, Travessa Girassol, 123 – Km 3, Santa Maria, RS"
    },
    {
        "nome": "Deus é Amor",
        "coordenadas": [-29.6959701, -53.8351955],
        "descricao": "Cozinha Deus é Amor\nRua G, 1045 – Vila Lídia, Santa Maria, RS\nContato: Flávia Machado: (55) 99166-0622"
    },
    {
        "nome": "Amor em Ação",
        "coordenadas": [-29.6758032, -53.8333319],
        "descricao": "Cozinha Amor em Ação\nRua Praia dos Ingleses, 45 – Vila Brenner, Santa Maria, RS\nContato: Pamela: (55) 99182-9548"
    },
    {
        "nome": "Associação Espírita Francisco Spinelli",
        "coordenadas": [-29.6819283, -53.8617361],
        "descricao": "Cozinha Ass. Espírita Francisco Spinelli\nRua Auta de Souza, 10 - Nova Santa Marta, Santa Maria, RS\nContato: Elson Busatto: (55) 99159-4623"
    },
    {
        "nome": "Mulheres Rosas de Março",
        "coordenadas": [-29.7263889, -53.8138889],
        "descricao": "Cozinha Mulheres Rosas de Março\nRua 7 de Março – Lorenzi, Santa Maria, RS\nContato: Elizângela de Deus: (55) 99151-1540"
    },
    {
        "nome": "Marias Bonitas - Fazendo história",
        "coordenadas": [-29.7143164, -53.8265761],
        "descricao": "Associação Marias Bonitas\nRua Nova, 100 – Urlândia, Santa Maria, RS\nContato: Elisiane Pahim: (55) 99988-4959"
    },
    {
        "nome": "Centro de Desenvolvimento Comunitário Estação dos Ventos",
        "coordenadas": [-29.6880711, -53.780717],
        "descricao": "Associação Estação dos Ventos\nLuiz Castagna, Travessa Girassol, 123 – Km 3, Santa Maria, RS\nContato: Fabiana Machado: (55) 99217-3707"
    },
    {
        "nome": "Associação Casa de Assis",
        "coordenadas": [-29.6867575, -53.7991792],
        "descricao": "Associação Casa de Assis\nRua Manoel Gomes Carneiro, 388 – Centro, Santa Maria, RS\nContato: Dona Neiva: (55) 99978-7260"
    },
    {
        "nome": "Comunidade Santa Terezinha",
        "coordenadas": [-29.7267222, -53.8079444],
        "descricao": "Comunidade Santa Terezinha\nRua Olga Pacianello, 315 – Lorenzi, Santa Maria, RS\nContato: Mari: (45) 98113-0020"
    },
    {
        "nome": "Ilé Àṣẹ Iyá Omin Orun - Casa de Osun",
        "coordenadas": [-29.6854128, -53.7861647],
        "descricao": "Ilé Àṣẹ Iyá Omin Orun - Casa de Osun\nRua João Brunhauser, 112 – Pres. João Goulart, Santa Maria, RS\nContato: Mãe Silvia: (55) 99138-1717"
    },
    {
        "nome": "Igreja Batista Ágape",
        "coordenadas": [-29.7076944, -53.8661667],  # Convertido de DMS para decimal
        "descricao": "Igreja Batista Ágape\nBR-158 (Faixa de Rosário), 2255 – Parque Pinheiro Machado, Santa Maria, RS\nContato: Diego: (54) 99669-4833"
    }
]
# =======================================================================================================



# ============= ADICIONAR MARCADORES AO MAPA ======================================================
### Identificando a localização das ações coletivas de voluntariado  ======
for ponto in pontos:
    folium.Marker(
        location=ponto["coordenadas"],
        popup=ponto["descricao"],
        icon=folium.Icon( # Configuração do ícone do marcador
            color="green", # Cor azul para indicar eventos de inundação
            icon="exclamation-triangle",  # Ícone de triângulo de exameção (padrão FontAwesome)
            prefix="fa" # Prefixo indicando que estamos usando ícones FontAwesome
                    ),
).add_to(mapa) # Adiciona o marcador criado ao objeto mapa previamente definido
# =======================================================================================================



# ============= ADICIONA UMA LEGENDA =================================================
legend_html = '''
{% macro html(this, kwargs) %}
<div style="
    position: fixed;
    bottom: 50px;
    left: 50px;
    width: 250px;
    height: auto;
    z-index: 9999;
    background-color: white;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0,0,0,0.2);
    font-family: Arial, sans-serif;
    font-size: 12px;
">
    <h4 style="margin-top:0; text-align:center">DESCRIÇÃO</h4>
    <div style="margin-bottom:5px">
    </div>
    <div style="margin-bottom:5px">
        <i class="fa fa-exclamation-triangle" style="color:green; margin-left:3px"></i>
        <span style="margin-left:8px">Coletivos mapeados</span>
    </div>
    <div style="margin-bottom:5px">
    <p style="margin-bottom:0; font-size:10px">DOI 10.5281/zenodo.15708548</p>
    <p style="margin-bottom:0; font-size:10px">DataLABIS © 2025 </p>
</div>
{% endmacro %}
'''

macro = MacroElement()
macro._template = Template(legend_html)
mapa.get_root().add_child(macro)
# =================================================================================



# ============= VISUALIZAÇÃO FINAL ===============================================================================================================
mapa.save("mapa_coletivosSM.html") # Salva em HTML
mapa # Exibe o mapa final