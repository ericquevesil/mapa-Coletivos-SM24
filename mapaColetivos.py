# © 2024 Laboratório de Investigação Sociológica (LABIS/UFSM).
# Licenciado sob a Licença Aberta - DataLABIS v1.0 (2025).

# ============= IMPORTAÇÃO DE BIBLIOTECAS COMPLEMENTARES =================================================
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

# ============= CONFIGURAÇÃO DOS MARCADORES =============================================================
### Coordenadas dos coletivos mapeados e suas respectivas descrições
pontos = [
    # Cozinha Solidária - Marrom (#4E342E)
    {
        "nome": "Cozinha Popular da Comunidade Estação dos Ventos",
        "coordenadas": [-29.6878303, -53.7810022],
        "descricao": "Cozinha Popular da Comunidade E.V.\nAtrás da Creche Estação dos Ventos, Luiz Castagna, Travessa Girassol, 123 – Km 3, Santa Maria, RS",
        "categoria": "cozinha",
        "cor": "brown",
        "icone": "cutlery"
    },
    {
        "nome": "Deus é Amor",
        "coordenadas": [-29.6959701, -53.8351955],
        "descricao": "Cozinha Deus é Amor\nRua G, 1045 – Vila Lídia, Santa Maria, RS\nContato: Flávia Machado: (55) 99166-0622",
        "categoria": "cozinha",
        "cor": "brown",
        "icone": "cutlery"
    },
    {
        "nome": "Amor em Ação",
        "coordenadas": [-29.6758032, -53.8333319],
        "descricao": "Cozinha Amor em Ação\nRua Praia dos Ingleses, 45 – Vila Brenner, Santa Maria, RS\nContato: Pamela: (55) 99182-9548",
        "categoria": "cozinha",
        "cor": "brown",
        "icone": "cutlery"
    },
    {
        "nome": "Associação Espírita Francisco Spinelli",
        "coordenadas": [-29.6819283, -53.8617361],
        "descricao": "Cozinha Ass. Espírita Francisco Spinelli\nRua Auta de Souza, 10 - Nova Santa Marta, Santa Maria, RS\nContato: Elson Busatto: (55) 99159-4623",
        "categoria": "cozinha",
        "cor": "brown",
        "icone": "cutlery"
    },
    {
        "nome": "Mulheres Rosas de Março (Cozinha)",
        "coordenadas": [-29.7264208, -53.8140584],
        "descricao": "Cozinha Mulheres Rosas de Março\nRua 7 de Março – Lorenzi, Santa Maria, RS\nContato: Elizângela de Deus: (55) 99151-1540",
        "categoria": "cozinha",
        "cor": "brown",
        "icone": "cutlery"
    },

    # Associação - Amarelo (#F9A825)
    {
        "nome": "Marias Bonitas - Fazendo história",
        "coordenadas": [-29.7143164, -53.8265761],
        "descricao": "Associação Marias Bonitas\nRua Nova, 100 – Urlândia, Santa Maria, RS\nContato: Elisiane Pahim: (55) 99988-4959",
        "categoria": "associacao",
        "cor": "orange",
        "icone": "users"
    },
    {
        "nome": "Mulheres Rosas de Março (Associação)",
        "coordenadas": [-29.7264219, -53.8140436],
        "descricao": "Associação Mulheres Rosas de Março\nRua 7 de Março – Lorenzi, Santa Maria, RS\nContato: Elizângela de Deus: (55) 99151-1540",
        "categoria": "associacao",
        "cor": "orange",
        "icone": "users"
    },
    {
        "nome": "Centro de Desenvolvimento Comunitário Estação dos Ventos",
        "coordenadas": [-29.6880711, -53.780717],
        "descricao": "Associação Estação dos Ventos\nLuiz Castagna, Travessa Girassol, 123 – Km 3, Santa Maria, RS\nContato: Fabiana Machado: (55) 99217-3707",
        "categoria": "associacao",
        "cor": "orange",
        "icone": "users"
    },
    {
        "nome": "Associação Casa de Assis",
        "coordenadas": [-29.6867575, -53.7991792],
        "descricao": "Associação Casa de Assis\nRua Manoel Gomes Carneiro, 388 – Centro, Santa Maria, RS\nContato: Dona Neiva: (55) 99978-7260",
        "categoria": "associacao",
        "cor": "orange",
        "icone": "users"
    },

    # Instituição Religiosa - Roxo (#880E4F)
    {
        "nome": "Comunidade Santa Terezinha",
        "coordenadas": [-29.7258964, -53.8081479],
        "descricao": "Comunidade Santa Terezinha\nRua Olga Pacianello, 315 – Lorenzi, Santa Maria, RS\nContato: Mari: (45) 98113-0020",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "church"
    },
    {
        "nome": "Ilé Àṣẹ Iyá Omin Orun - Casa de Osun",
        "coordenadas": [-29.6854128, -53.7861647],
        "descricao": "Ilé Àṣẹ Iyá Omin Orun - Casa de Osun\nRua João Brunhauser, 112 – Pres. João Goulart, Santa Maria, RS\nContato: Mãe Silvia: (55) 99138-1717",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "star"
    },
    {
        "nome": "Igreja Batista Ágape",
        "coordenadas": [-29.7077181, -53.8661353],
        "descricao": "Igreja Batista Ágape\nBR-158 (Faixa de Rosário), 2255 – Parque Pinheiro Machado, Santa Maria, RS\nContato: Diego: (54) 99669-4833",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "church"
    },
    {
        "nome": "Igreja Batista Betel",
        "coordenadas": [-29.6742619, -53.826569],
        "descricao": "Igreja Batista Betel\nAv. Borges de Medeiros, 1175 – Salgado Filho, Santa Maria, RS\nContato: Diego: (54) 99669-4833",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "church"
    },
    {
        "nome": "Igreja Templo do Poder de Deus",
        "coordenadas": [-29.7517656, -53.7890168],
        "descricao": "Igreja Templo do Poder de Deus\nRua Augusto Kunz, 150 – Passo das Tropas, Santa Maria, RS",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "church"
    },
    {
        "nome": "Templo de Umbanda Xangô e Exu Caveira",
        "coordenadas": [-29.6799206, -53.8292641],
        "descricao": "Templo de Umbanda Xangô e Exu Caveira\nRua 20 de Janeiro, 391 – Divina Providência, Santa Maria, RS\nContato: Fabrício de Cassenote: (55) 99148-1732",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "star"
    },
    {
        "nome": "Reino de Axé Oyá Nique e Oxalá",
        "coordenadas": [-29.6913361, -53.8623986],
        "descricao": "Reino de Axé Oyá Nique e Oxalá\nRua Benjamin D'Ávila Prado, 11 – Juscelino Kubitschek, Santa Maria, RS\nContato: Sabrina: (55) 98413-1680",
        "categoria": "religiosa",
        "cor": "purple",
        "icone": "star"
    },

    # ONG - Vermelho escuro (#A52714)
    {
        "nome": "ONG Mãos Unidas Pelo Cipriano",
        "coordenadas": [-29.6978052, -53.8675936],
        "descricao": "ONG Mãos Unidas Pelo Cipriano\nRua Niterói, 500 – Parque Pinheiro Machado, Santa Maria, RS\nContato: Anderson Melgares: (55) 98419-9742",
        "categoria": "ong",
        "cor": "darkred",
        "icone": "heart"
    },

    # CTG - Verde escuro (#097138)
    {
        "nome": "CTG Sentinela da Querência",
        "coordenadas": [-29.7029807, -53.7215761],
        "descricao": "CTG Sentinela da Querência\nRua Silvino Jacob Zimmermann, 115 – Camobi, Santa Maria, RS\nContato: Ronaldo Lock: (55) 99145-8529",
        "categoria": "ctg",
        "cor": "darkgreen",
        "icone": "flag"
    },
    {
        "nome": "CTG Passo dos Ferreiros",
        "coordenadas": [-29.7037774, -53.876117],
        "descricao": "CTG Passo dos Ferreiros\nRua Milton Mendonça de Souza, 500 – Tancredo Neves, Santa Maria, RS\nContato: Tiago: (55) 99126-6823",
        "categoria": "ctg",
        "cor": "darkgreen",
        "icone": "flag"
    },

    # Projeto Social - Vermelho (#FF5252)
    {
        "nome": "Projeto Esperança/Cooesperança",
        "coordenadas": [-29.7033798, -53.8075996],
        "descricao": "Projeto Esperança\nRua Ver. Bolsson, 1 – Nossa Sra. Medianeira, Santa Maria, RS\nContato: Tiago: (55) 99126-6823",
        "categoria": "associacao",
        "cor": "orange",
        "icone": "users"
    }
]
# =======================================================================================================

# ============= ADICIONAR MARCADORES AO MAPA ======================================================
for ponto in pontos:
    folium.Marker(
        location=ponto["coordenadas"],
        popup=ponto["descricao"],
        icon=folium.Icon(
            color=ponto["cor"],
            icon=ponto["icone"],
            prefix="fa"
        ),
        tooltip=ponto["nome"]
    ).add_to(mapa)
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
    <h4 style="margin-top:0; text-align:center">LEGENDA</h4>
    <div style="margin-bottom:5px">
        <i class="fa fa-cutlery" style="color:brown; margin-left:3px"></i>
        <span style="margin-left:8px">Cozinha Solidária</span>
    </div>
    <div style="margin-bottom:5px">
        <i class="fa fa-users" style="color:orange; margin-left:3px"></i>
        <span style="margin-left:8px">Associação</span>
    </div>
    <div style="margin-bottom:5px">
        <i class="fa fa-church" style="color:purple; margin-left:3px"></i>
        <span style="margin-left:8px">Instituição Religiosa</span>
    </div>
    <div style="margin-bottom:5px">
        <i class="fa fa-heart" style="color:darkred; margin-left:3px"></i>
        <span style="margin-left:8px">ONG</span>
    </div>
    <div style="margin-bottom:5px">
        <i class="fa fa-flag" style="color:darkgreen; margin-left:3px"></i>
        <span style="margin-left:8px">CTG</span>
    </div>
    <div style="margin-bottom:5px">
        <p style="margin-bottom:0; font-size:10px">DOI 10.5281/zenodo.15708548</p>
        <p style="margin-bottom:0; font-size:10px">DataLABIS © 2025</p>
    </div>
</div>
{% endmacro %}
'''

macro = MacroElement()
macro._template = Template(legend_html)
mapa.get_root().add_child(macro)
# =================================================================================

# ============= VISUALIZAÇÃO FINAL ================================================
mapa.save("mapa_coletivosSM.html") # Salva em HTML
mapa # Exibe o mapa final
