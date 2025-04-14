from dash import dcc, html
import data as dt

estado = dt.capturar_estado()
ano = dt.capturar_ano()

def create_layout(app):
    return html.Div(
        style={
            'height': '100%',
            'width': '100%',
            'margin': '0',
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'backgroundColor': '#edf6f9',#EDF6F9
        },
        children=[
            # Cabeçalho
            html.Div(
                style={
                    'width': '100%',
                    'backgroundColor': '#b8dedc',#0677BB
                    'padding': '5px',
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                },
                children=[
                    # Imagem com link
                    html.Img(
                        src=app.get_asset_url("logo-sistema.png"),  # Substitua pela URL da imagem
                        style={
                            'width': '50px',  # Ajuste conforme necessário
                            'height': '50px',  # Mantém proporção
                            'marginLeft': '20px'  # Espaço à direita
                        }
                    ),
                    html.Div(
                        style={
                            'flexGrow': 1,  # Ocupa o máximo de espaço disponível
                            'display': 'flex',
                            'justifyContent': 'left',  # Centraliza o título
                        },
                        children=[
                            html.H1(
                                " SISTEMA VETORIAL TRIDIMENSIONAL DA TRANSIÇÃO ENERGÉTICA JUSTA ",
                                style={
                                    'color': '#EDF6F9',
                                    'fontFamily': 'Helvetica',
                                    'fontSize': '20px',
                                    'textAlign': 'center',
                                }
                            )
                        ]
                    ),
                    html.A(
                        href="https://lecos.ufc.br/pt/pagina-de-introducao/m",  # URL do site de destino
                        target="_blank",  # Abre em uma nova aba
                        children=[
                            html.Img(
                                src=app.get_asset_url("logo-lecos.png"),  # Substitua pela URL da imagem
                                style={
                                    'width': '80px',  # Ajuste conforme necessário
                                    'height': '70px',  # Mantém proporção
                                    'marginRight': '50px',  # Espaço à direita
                                    #'border': '1px solid #ccc'
                                }
                            )
                        ]
                    ),
                ]
            ),

            # Conteúdo principal
            html.Div(
                style={
                    'display': 'flex',
                    'flexWrap': 'wrap',
                    'width': '100%',
                    'justifyContent': 'center',
                    'padding': '10px',
                },
                children=[
                    # Filtros
                    html.Div(
                        style={
                            'width': '30%',
                            'minWidth': '280px',
                            'maxWidth': '300px',
                            'backgroundColor': '#ffffff',
                            'color': 'black',
                            'padding': '10px',
                            'borderRadius': '8px',
                        },
                        children=[
                            #html.H2("Filtros", style={'fontSize': '18px', 'marginBottom': '10px','fontFamily': 'Helvetica'}),
                            dcc.Dropdown(
                                id='estado-dropdown',
                                options=[{'label': est, 'value': est} for est in estado],
                                value=estado[0],
                                clearable=False,
                                style={'width': '100%', 'fontSize': '16px', 'fontFamily': 'Helvetica'}
                            ),
                            dcc.Dropdown(
                                id='ano-dropdown',
                                options=[{'label': a, 'value': a} for a in ano],
                                value=ano[0],
                                clearable=False,
                                style={'width': '100%', 'fontSize': '16px', 'marginTop': '10px','fontFamily': 'Helvetica'}
                            ),
                            html.Div(style={'height': '10px'}),  # Espaçamento
                            html.Div(
                                id='angulos-div',
                                style={'padding': '10px', 'color': 'gray','fontFamily': 'Helvetica'},
                                children=[
                                    html.H3("Ângulos de Inclinação"),
                                    html.Hr(),
                                    html.P("Comparação entre eixos e vetor ideal"),
                                    html.P(id='angulo-ideal-x'),
                                    html.P(id='angulo-ideal-y'),
                                    html.P(id='angulo-ideal-z'),
                                    html.Hr(),
                                    html.P("Comparação com vetor genérico"),
                                    html.P(id='angulo-generico-x'),
                                    html.P(id='angulo-generico-y'),
                                    html.P(id='angulo-generico-z'),
                                    html.Hr(),
                                    html.P(id='angulo-generico-ideal',),
                                    html.Hr(),
                                    html.P("Comparação das dimensões entre si"),
                                    html.P(id='angulo-ambiental-seguranca'),
                                    html.P(id='angulo-ambiental-equidade'),
                                    html.P(id='angulo-seguranca-equidade'),
                                ]
                            )
                        ],
                    ),
                    # Área de gráficos
                    html.Div(
                        style={
                            'width': '70%',
                            'minWidth': '300px',
                            'backgroundColor': '#f8f9fa',  # Fundo claro
                            'color': 'black',
                            'padding': '15px',
                            'borderRadius': '8px',
                            'marginLeft': '10px',
                            'fontFamily': 'Helvetica'
                        },
                        children=[
                            html.Div(
                                style={
                                    'display': 'flex',
                                    'flexDirection': 'row',
                                    'alignItems': 'center',  # Alinha os itens ao topo
                                    'justifyContent': 'space-between'
                                },
                                children=[
                                    # Gráfico
                                    dcc.Graph(id='vetor-grafico', style={'flex': '0.5'}),

                                    # Descrição do gráfico
                                    html.Div(
                                        style={
                                            'flex': '1',  # Ocupa menos espaço que o gráfico
                                            'textAlign': 'left',
                                            'padding': '10px',
                                            'display': 'flex',
                                            'flexDirection': 'column',
                                            'alignItems': 'flex-start',  # Mantém os textos no topo
                                            'justifyContent': 'flex-start',  # Preenchendo de cima para baixo
                                            'height': '100%'  # Garante preenchimento dinâmico
                                        },
                                        children=[
                                            html.Img(
                                                id='gif-image',
                                                src='',  # Atualizado via callback
                                                style={
                                                    'width': '100%',
                                                    'maxWidth': '900px',
                                                    'borderRadius': '8px',
                                                    #'border': '1px solid #ccc'
                                                }
                                            ),
                                            
                                        ]
                                    )
                                ]
                            ),
                        ]
                    )

                ]
            ),
            # **Nova Div abaixo do gráfico para o GIF + Dropdown de seleção**
           html.Div(
                style={
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '10px',
                    'padding': '30px 20px',
                    'fontFamily': 'Helvetica',
                    'color': '#001219'
                },
                children=[
                    html.Div(
                        style={
                            'display': 'flex',
                            'flexDirection': 'row',
                            'justifyContent': 'space-between',
                            'alignItems': 'flex-start',
                            'flexWrap': 'wrap',
                            'gap': '30px',
                            'maxWidth': '1000px',
                            'margin': '0 auto',
                            'padding': '20px',
                            'backgroundColor': '#ffffff',
                            'borderRadius': '12px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.05)',
                        },
                        children=[
                            # Texto à esquerda
                            html.Div(
                                style={
                                    'flex': '1',
                                    'minWidth': '280px',
                                    'maxWidth': '450px',
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'gap': '10px',
                                    'textAlign': 'left',
                                },
                                children=[
                                    html.H4("Descrição do gráfico", style={'marginBottom': '8px'}),
                                    html.P("O vetor em azul representa o equilíbrio entre as dimensões onde as coordenadas desse vetor são (10,10,10). Isso significa que o estado teria o valor máximo do trilema nas três dimensões."),
                                    html.P("Os vetores na cor preta representam as projeções do vetor ideal (azul) em cada eixo. Os pontos desses vetores são ligados entre si formando uma figura — representação do equilíbrio entre as dimensões."),
                                    html.P("O vetor vermelho representa a situação atual do estado em cada dimensão. Suas coordenadas indicam qual dimensão está sendo priorizada."),
                                    html.P("As projeções do vetor vermelho em cada eixo são representadas por vetores amarelos. Os pontos finais desses vetores formam uma figura vermelha que simboliza a condição atual do estado."),
                                ]
                            ),
                            # Texto à direita
                            html.Div(
                                style={
                                    'flex': '1',
                                    'minWidth': '280px',
                                    'maxWidth': '450px',
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'gap': '10px',
                                    'textAlign': 'left',
                                },
                                children=[
                                    html.H4("Movimento Animado do Sistema", style={'marginBottom': '8px'}),
                                    html.P("Através de GIF's é possível observar o movimento dos vetores de cada estado, permitindo visualizar para qual dimensão o estado está priorizando."),
                                    html.P("Observe que é possível selecionar qual o estado você quer visualizar o movimento selecionando o estado no filtro lateral."),
                                ]
                            ),
                        ]
                    )
                ]
            )
        ]
    )
