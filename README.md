# 🌍 Mapeamento das Ações Coletivas de Voluntariado - Santa Maria/RS (2024)

[![License: LA-DataLABIS](https://img.shields.io/badge/License-DataLABIS-blue.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15708548.svg)](https://doi.org/10.5281/zenodo.15708548)

Projeto de mapeamento interativo das iniciativas de voluntariado emergenciais após o desastre socioambiental de 2024 em Santa Maria/RS.

<p align="center">
  <img src="https://raw.githubusercontent.com/labis-ufsm/mapeamento-voluntariado-sm/main/preview-map.png" alt="Preview do Mapa" width="600">
</p>

## 📋 Sobre o Projeto
Desenvolvido pelo **Laboratório de Investigação Sociológica (LABIS/UFSM)** como parte do projeto *"Catástrofes climáticas: dimensões socioculturais do alerta e contenção de riscos"*, financiada pela Pró-Reitoria de Extensão (PRE/UFSM).

**Objetivos**:
- Visualizar geograficamente a rede de solidariedade emergencial
- Documentar iniciativas comunitárias de resposta à crise
- Facilitar a conexão entre voluntários e organizações

## 🛠️ Tecnologias
- **Python 3** + **Jupyter Notebook** (opcional)
- Bibliotecas:
  - `folium` (mapas interativos)
  - `branca` (elementos customizados)

## 🚀 Como Executar
```bash
# 1. Clonar repositório
git clone https://github.com/labis-ufsm/mapeamento-voluntariado-sm.git
cd mapeamento-voluntariado-sm

# 2. Instalar dependências (recomendado: ambiente virtual)
pip install folium branca

# 3. Executar
python mapa_coletivosSM.py
