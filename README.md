# Game2D_Alien
Projeto realizado em aula durante a disciplina AQS

## Testes automatizados

Instale as dependências de teste e execute os testes a partir desta pasta:

```powershell
python -m pip install pytest pytest-mock pytest-html coverage
python -m pytest -v
```

Os testes também demonstram um stub para a nave usada pelo projétil e um mock
para verificar a chamada de colisão entre os grupos de sprites.

Para gerar um relatório HTML dos testes:

```powershell
python -m pytest --html=relatorio.html
```

Para medir a cobertura do código:

```powershell
python -m coverage run --source=src -m pytest
python -m coverage report
```

Os relatórios (`relatorio.html`, `htmlcov/` e `.coverage`) são locais e não devem
ser enviados ao repositório.
