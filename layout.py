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
                            'width': '35%',
                            'minWidth': '280px',
                            'maxWidth': '400px',
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
                            'width': '65%',
                            'minWidth': '600px',
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
                                    'alignItems': 'flex-start',  # Alinha os itens ao topo
                                    'justifyContent': 'space-between'
                                },
                                children=[
                                    # Gráfico
                                    dcc.Graph(id='vetor-grafico', style={'flex': '2'}),

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
                                            html.H4("Descrição do gráfico", style={'marginBottom': '10px'}),
                                            html.P(
                                                "O vetor em azul representa o equilibrio entre as dimensões onde as coordenadas desse vetor é (10,10,10), isso significa que o estado teria o valor máximo do trilema nas três dimnesões.",
                                                style={'marginBottom': '5px'}
                                            ),
                                            html.P(
                                                "Os vetores da cor preto representam as projeções do vetor ideal da cor azul em cima de cada eixo. Os pontos de cada vetor ideal são ligados entre si através de uma figura, que é uma representação do equilibrio entre as dimensões.",
                                                style={'marginBottom': '5px'}
                                            ),
                                            html.P(
                                                "Os pontos de cada vetor ideal são ligados entre si através de uma figura, que é uma representação do equilibrio entre as dimensões.",
                                                style={'marginBottom': '5px'}
                                            ),
                                            html.P(
                                                "O vetor da cor vermelho representa a situação em cada dimensão do estado selecionado, onde cada coordenada do vetor vai indicar qual dimensão esta sendo priorizada.",
                                                style={'marginBottom': '5px'}
                                            ),
                                            html.P(
                                                "Os vetores da cor amarela representam as projeções do vetor vermelho em cima de cada eixo. Os pontos de cada vetor são ligados entre si através da figura vermelha, que é uma representação da condição atual do estado em relação as dimensões.",
                                                style={'marginBottom': '5px'}
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
                    #'padding': '5px 0',  # Espaçamento vertical
                    'backgroundColor': '#f8f9fa',  # Cor de fundo opcional para destaque
                    'borderRadius': '10px',
                    

                },
                children=[
                    # Título principal
                    html.H4(
                        "Visualização Animada do Movimento dos Vetores",
                        style={
                            'color': 'gray',
                            'fontFamily': 'Helvetica',
                            'fontSize': '24px',
                            'textAlign': 'left',
                            'margin': '0 auto',
                            'maxWidth': '90%',
                            'marginTop': '30px',
                        }
                    ),

                    # Container principal com texto e imagem
                    html.Div(
                        style={
                            'width': '88%',
                            'margin': '20px auto',
                            'display': 'flex',
                            'flexDirection': 'row',
                            'alignItems': 'flex-start',
                            'justifyContent': 'space-between',
                            'backgroundColor': '#f8f9fa',
                            'padding': '5px',
                            'borderRadius': '12px',
                            #'gap': '0px',
                            #'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'
                        },
                        children=[
                            # Texto explicativo à esquerda
                            html.Div(
                                style={
                                    'width': '35%',
                                    'textAlign': 'left',
                                    'padding': '5px',
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'justifyContent': 'center',
                                    'alignItems': 'flex-start',
                                    'fontFamily': 'Helvetica',
                                    'color': '#001219'
                                },
                                children=[
                                    html.P(
                                        "Nesta seção é possível observar, através de GIFs, o movimento dos vetores de cada estado, permitindo visualizar para qual dimensão o estado está priorizando.",
                                        style={'marginBottom': '12px'}
                                    ),
                                    html.P(
                                        "Observe que existe uma caixa de seleção acima do GIF ao lado. A partir dessa caixa, é possível selecionar um estado e observar o GIF correspondente."
                                    ),
                                ]
                            ),

                            # Dropdown + GIF à direita
                            html.Div(
                                style={
                                    'width': '65%',
                                    'minWidth': '300px',
                                    'display': 'flex',
                                    'flexDirection': 'column',
                                    'alignItems': 'center',
                                    'justifyContent': 'center',
                                },
                                children=[
                                    dcc.Dropdown(
                                        id='gif-dropdown',
                                        options=[{'label': est, 'value': est} for est in estado],
                                        value=estado[0],
                                        clearable=False,
                                        style={
                                            'width': '55%',
                                            'fontSize': '16px',
                                            'marginBottom': '20px',
                                            'fontFamily': 'Helvetica',
                                            'textAlign': 'center',
                                            'alignItems': 'left',
                                        }
                                    ),
                                    html.Img(
                                        id='gif-image',
                                        src='',  # Atualizado via callback
                                        style={
                                            'width': '100%',
                                            'maxWidth': '520px',
                                            'borderRadius': '8px',
                                            'border': '1px solid #ccc'
                                        }
                                    )
                                ]
                            ),
                        ]
                    ),
                ]
            )

                    

        ]
    )
